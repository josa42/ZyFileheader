#!/usr/bin/env python
# -*- coding:utf-8 -*-
#*********************************************************#
# @@ScriptName: zy_file_header.py
# @@Author: zhenyu<fjctlzy@gmail.com>
# @@Create Date: 2012-11-26 20:27:03
# @@Modify Date: 2012-12-04 14:30:58
# @@Function:
#*********************************************************#
import sublime_plugin
import os
import datetime
import re

from zy_config import ZyConfig


class ZyAddHeaderOnCreatedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        zy_config = ZyConfig.get_singleton()
        if zy_config.get('add_on_created') == False:
            return
        else:
            self.view.run_command('zy_file_new_header')


class ZyFileNewHeaderCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        zy_config = ZyConfig.get_singleton()
        file_header_format = zy_config.get('file_header_format')
        """replace @@author and @@email with the user definied value"""
        author = zy_config.get('author')
        email = zy_config.get('email')
        file_header_format = file_header_format.replace('@@author', author)
        file_header_format = file_header_format.replace('@@email', email)

        """
            when file exists already, we need to use original create time
            using os.stat, otherwise using current time instead
        """
        if not self.view.file_name():
            create_time = datetime.datetime.now().strftime(zy_config.get('time_format'))
        else:
            file_stat = os.stat(self.view.file_name())
            st_ctime = file_stat[9]
            create_time = datetime.datetime.fromtimestamp(st_ctime).strftime(zy_config.get('time_format'))
        if file_header_format.find('@@Create Date') >= 0:
            file_header_format = file_header_format.replace('@@Create Date:', '@@Create Date: ' + create_time)

        self.view.insert(edit, 0, file_header_format)


class ZyAddCmdHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        zy_config = ZyConfig.get_singleton()
        if zy_config.get('add_on_created') == False:
            return

        file_name = self.view.file_name()
        if file_name.endswith('.py'):
            cmd_header = zy_config.get('python')
        elif file_name.endswith('.sh'):
            cmd_header = zy_config.get('shell')

        cmd_headers = cmd_header.split('\n')
        exists = False
        for line_no in xrange(0, 5):
            line = self.view.substr(self.view.line(line_no))
            for cmd_line in cmd_headers:
                if line.find(cmd_line) >= 0:
                    exists = True
                    break

        if not exists:
            self.view.insert(edit, 0, cmd_header + '\n')


class ZyAddFileFooterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        default_footer = os.linesep
        """add a line to the end of the line"""
        last_line = self.view.substr(self.view.line(self.view.size()))
        if len(last_line) > 0:
            self.view.insert(edit, self.view.size(), default_footer)


class ZyFileModifiedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        modified_date_region = self.view.find('@@Modify Date', 0)
        if modified_date_region:
            line = self.view.line(modified_date_region)
            now = datetime.datetime.now().strftime(ZyConfig.get_singleton().get('time_format'))
            self.view.replace(edit,
                              line,
                              '# @@Modify Date: ' + now)

        file_name_region = self.view.find('@@ScriptName', 0)
        if file_name_region:
            line = self.view.line(file_name_region)
            self.view.replace(edit,
                              line,
                              '# @@ScriptName: ' + os.path.basename(self.view.file_name()))


class ZyAddFileHeaderManually(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('zy_file_new_header')
        self.view.run_command('zy_file_modified')
        self.view.run_command('zy_add_cmd_header')


class ZyAddFileAndCmdHeader(sublime_plugin.EventListener):
    def on_new(self, view):
        view.run_command('zy_add_header_on_created')

    def on_pre_save(self, view):
        zy_config = ZyConfig.get_singleton()
        ignore_files = zy_config.get('ignore_files')
        current_file = os.path.basename(view.file_name())
        for f in ignore_files:
            pattern = re.compile(f)
            if pattern.match(current_file):
                return

        view.run_command('zy_file_modified')
        view.run_command('zy_add_cmd_header')
        view.run_command('zy_add_file_footer')

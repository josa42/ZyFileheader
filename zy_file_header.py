#!/usr/bin/env python
import sublime_plugin
import os
import sublime
import datetime
import re


class ZyFileNewHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings('Preferences.sublime-settings')
        file_header_format = s.get('file_header_format')
        """replace @@author and @@email with the user definied value"""
        author = s.get('author')
        email = s.get('email')
        file_header_format = file_header_format.replace('@@author', author)
        file_header_format = file_header_format.replace('@@email', email)

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if file_header_format.find('@@Create Date') >= 0:
            file_header_format = file_header_format.replace('@@Create Date:', '@@Create Date: ' + now)

        self.view.insert(edit, 0, file_header_format)


class ZyAddCmdHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings('Preferences.sublime-settings')
        file_name = self.view.file_name()
        if file_name.endswith('.py'):
            cmd_header = s.get('python')
        elif file_name.endswith('.sh'):
            cmd_header = s.get('shell')

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
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
        view.run_command('zy_file_new_header')

    def on_pre_save(self, view):
        s = sublime.load_settings('Preferences.sublime-settings')
        ignore_files = s.get('ignore_files')
        current_file = os.path.basename(view.file_name())
        for f in ignore_files:
            pattern = re.compile(f)
            if pattern.match(current_file):
                return

        view.run_command('zy_file_modified')
        view.run_command('zy_add_cmd_header')
        view.run_command('zy_add_file_footer')

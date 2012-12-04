#!/usr/bin/env python
# -*- coding:utf-8 -*-
#*********************************************************#
# @@ScriptName: zy_config.py
# @@Author: zhenyu<fjctlzy@gmail.com>
# @@Create Date: 2012-12-04 12:53:05
# @@Modify Date: 2012-12-04 14:36:07
# @@Function:
#*********************************************************#
import sublime


class ZyConfig:

    config = None

    @classmethod
    def get_singleton(self):
        self.load_settings()

        return self.config

    @classmethod
    def load_settings(self):
        s = sublime.load_settings('Preferences.sublime-settings')
        self.config = s.get('zy_file_header')
        if not self.config:
            raise Exception("zy_file_header is not configured.")

        print self.config
        """set default time_format"""
        if not self.config.get('time_format'):
            self.config['time_format'] = '%Y-%m-%d %H:%M:%S'

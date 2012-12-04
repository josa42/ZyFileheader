# Description

ZyFileheader is a plugin of Sublime Text2 which helps to add file header like 

      {
         #!/usr/bin/env python
         # -*- coding:utf-8 -*-
         #*********************************************************#
         # @@ScriptName: a.py
         # @@Author: Your name here<Your email here>
         # @@Create Date: 2012-11-25 22:24:14
         # @@Modify Date: 2012-11-25 22:24:34
         # @@Function:
         #*********************************************************#
      }

to your new created file, and you could define the header for yourself. Currently the plugin support python and shell, which is my mostly used.

# Installation

* The easiest way to install ZyFileheader is via the excellent Package Control Plugin
    * **NOTE** at the time of writing this, it's not in the default Package Control channel. Please add it via
        1. Open up the command palette
        2. Select "Package Control: Add Repository"
        3. Type https://github.com/fjctlzy/ZyFileheader
    1. See the [Package Control Installation Instructions](http://wbond.net/sublime_packages/package_control/installation)
    2. Once package control has been installed, bring up the command palette (cmd+shift+P or ctrl+shift+P)
    3. Type Install and select "Package Control: Install Package"
    4. Select PlatformSettings from the list. Package Control will keep it automatically updated for you
* If you don't want to use package control, you can manually install it
    1. Go to your packages directory and type:
    2.    git clone https://github.com/fjctlzy/ZyFileheader

# Usage

You could put settings below in your Perferences.sublime-settings by click "Perferences"=>"Settings - User": 

    "zy_file_header" : {
        "add_on_created": true,
        "file_header_format": "#*********************************************************#\n# @@ScriptName: \n# @@Author: @@author<@@email>\n# @@Create Date:\n# @@Modify Date: \n# @@Function:\n#*********************************************************#",
        "file_header_format.php": "/*********************************************************#\n# @@ScriptName: \n# @@Author: @@author<@@email>\n# @@Create Date:\n# @@Modify Date: \n# @@Function:\n#*********************************************************/",
        "file_header_format.c": "/*********************************************************#\n# @@ScriptName: \n# @@Author: @@author<@@email>\n# @@Create Date:\n# @@Modify Date: \n# @@Function:\n#*********************************************************/",
        "python": "#!/usr/bin/env python\n# -*- coding:utf-8 -*-",
        "shell": "#!/usr/bin/env bash",
        "author": "your name here",
        "email": "your email here",
        "time_format": "%Y-%m-%d %H:%M:%S",
        "ignore_files":
        [
            ".*.sublime.*",
            "README",
            ".*.sublime-settings",
            "zy_file_header.py"
        ]
    }

# Features
* Modify Date will change each time you save(CTRL+S) the file
* ScriptName will change each time you save as(CTRL+SHIFT+S) the file
* CTRL + 1 could add defined header to your current file which has no header
* Custom time format, using Python datetime format, please refer to https://github.com/fjctlzy/ZyFileheader/blob/master/time_format.md
* CTRL + 1 will use file ctime as @@Create Date for existed file
* You could set add_on_created to false so that when file is created, the header won't be added automatically(set this to be false if you want to use multiple header formats functions now)
* Multiple header formats such as(but add_on_created should be set to false now):

        "zy_file_header"{
            "file_header_format.c":"xxxxxxx"
            "file_header_format.php": "/**/"
            "file_header_format.py": "#######"
        }
    
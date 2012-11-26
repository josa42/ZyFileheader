ZyFileheader is a plugin of Sublime Text2 which helps to add file header like 

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#*********************************************************#
# @@ScriptName: a.py
# @@Author: Your name here<Your email here>
# @@Create Date: 2012-11-25 22:24:14
# @@Modify Date: 2012-11-25 22:24:34
# @@Function:
#*********************************************************#

to your new created file, and you could define the header for yourself. Currently the plugin support python and shell, which is my mostly used. 

You could put settings below in your Perferences.sublime-settings by click "Perferences"=>"Settings - User": 

{
"ignore_files": ["zy_file_header.py", "default.sublime-settings", "Preferences.sublime-settings"], 
"file_header_format": "#*********************************************************#\n# @@ScriptName: \n# @@Author: @@author<@@email>\n# @@Create Date:\n# @@Modify Date: \n# @@Function:\n#*********************************************************#",
"python": "#!/usr/bin/env python\n# -*- coding:utf-8 -*-",
"shell" : "#!/usr/bin/env bash",
"author" : "Your name here", 
"email" : "Your email here"
}
#!/usr/bin/python

import os, sys

current_name = "php-script-plugin-template"
new_name = sys.argv[1]

#update the directory names in the various files subfolders
os.rename("pkg/files/plugins/scripts/" + current_name, "pkg/files/plugins/scripts/" + new_name)
os.rename("pkg/files-posix/plugins/scripts/" + current_name, "pkg/files-posix/plugins/scripts/" + new_name)
os.rename("pkg/files-win/plugins/scripts/" + current_name, "pkg/files-win/plugins/scripts/" + new_name)

#!/usr/bin/python

import os, sys

current_name = "php-script-plugin-template"
new_name = sys.argv[1]

#update the directory names in the various files subfolders
os.rename("pkg/files/plugins/scripts/" + current_name, "pkg/files/plugins/scripts/" + new_name)
os.rename("pkg/files-posix/plugins/scripts/" + current_name, "pkg/files-posix/plugins/scripts/" + new_name)
os.rename("pkg/files-win/plugins/scripts/" + current_name, "pkg/files-win/plugins/scripts/" + new_name)

#rename the xml file in pkg & update contents
old_xml = open("pkg/" + current_name + ".xml", 'r')
new_xml = open("pkg/" + new_name + ".xml", 'w')

for line in old_xml:
    new_xml.write(line.replace(current_name, new_name))

old_xml.close()
new_xml.close()




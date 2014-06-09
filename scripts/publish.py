#!/usr/bin/env python
import os
import shutil

ver = open("VERSION","r").readline()
is_win = os.name == 'nt'

name="chib_note_v%s.pdf" % ver
source="./build/chib_note.pdf"

if is_win:
    target_www = "H:/www/%s" %name
else:
    target_www = "/afs/cern.ch/user/a/amazurov/www/%s" % name

target_local="./build/%s" % name

shutil.copyfile(source, target_local)
print("File '%s' copied to '%s'" % (source, target_local))
shutil.copyfile(source, target_www)
print("File '%s' copied to '%s'" % (source, target_www))
print("Url: http://cern.ch/amazurov/%s" % name)
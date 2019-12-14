#!/bin/usr/python
import re
file=open("filename.txt","r")
read=file.read()
reg=re.findall("text to find",read)
print(reg)
file.close()

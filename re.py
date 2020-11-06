import sys
import re
arg=sys.argv[1]
print arg
fin=re.search("^.*(?=.{8,})((?=.*[!@#$%^&*()\-_=+{};:,<.>]){1})(?=.*\d)((?=.*[a-z]){1})((?=.*[A-Z]){1}).*$",arg)
if fin:
  print("Strong Pwd")
else:
  print("week pwd")

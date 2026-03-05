str="error in the log"
#to find the error

import re

if re.match(r"^error",str):
    print("error found")
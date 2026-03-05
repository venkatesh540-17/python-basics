num="123445"
import re

if re.fullmatch(r"\d+",num):
    print("full match")
else:
    print("not match")

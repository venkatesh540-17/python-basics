str1="cat"
str2="act"

l1=list(str2)
print(l1)
if len(str1)!=len(str2):
    print("not eligible")
else:

   for i in str1:
      if i in l1:
        l1.remove(i)

      else:
        print("not anagram")
        break

   else:
    print("yes")

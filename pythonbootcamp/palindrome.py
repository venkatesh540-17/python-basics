text = "malayalam"
is_palindrome = True

for i in range(0,len(text)//2):
    if  text[i]!=text[len(text)-1-i]:
        is_palindrome=False
        break
print(is_palindrome)
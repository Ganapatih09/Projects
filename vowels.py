letter_count=0
vcount=0
str=str(input("enter the string="))
str=str.lower()
for i in range(0, len(str)):
    if str[i]>='a' and str[i]<='z':
        letter_count=letter_count+1
        if str[i] in("a","e","i","o","u"):
            vcount=vcount+1

print('no of letters is:',letter_count)
print('numbers of vowels count is:',vcount)
print('total number of characters in the input string is:',len(str))
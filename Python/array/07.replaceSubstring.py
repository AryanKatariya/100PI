def replaceSubstring(s,str1,str2):
    string=s.replace(str1,str2)
    return string

string=input("Enter String :\n")
str1=input("Enter substring which has to be replaced :\n")
str2=input("Enter substring with which str1 has to be replaced :\n")
print("String after replacement")
print(replaceSubstring(string,str1,str2))
def onlyAlpha(string):
    ans = ''
    for i in String1:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            ans+=i
    return ans
            
String1 = "#Justice!For@Chutki123"
ans = onlyAlpha(String1)
print('Alphabets in string are :' + ans)
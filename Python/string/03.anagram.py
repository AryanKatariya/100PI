def anagram(s1,s2):
    String1 = sorted(s1.lower())
    String2 = sorted(s2.lower())


    if String1 == String2:
        print('Strings are anagram')
    else:
        print('Strings are not anagram')

String1 = "Listen"
String2 = "Silent"

anagram(String1,String2)
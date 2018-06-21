def uniqueChars(s):
    d={}
    for each in s:
        if each in d:
            return False
        else:
            d[each]=1
    return True

s='Kartik'

assert uniqueChars(s)==True

#searching in dict is O(1)
#time complexity - worst time - O(n)
#o(62) -- after this it will have duplicate characters
#space complexity - worst time - o(26+26+10)
#dictionary, list - dynamic allocation

def stringPermutation(s1,s2):
    d={}
    if len(s1)!=len(s2):
        return False
    for each in s1:
        if each in d:
            d[each]+=1
        else:
            d[each]=1
    for each in s2:
        if each in d and d[each]>0:
            d[each]-=1
        else:
            return False

    return True

print(stringPermutation('111','11'))

#space - o(n)
#time complexity -o(n)


'pales', 'pale'

if abs(len(s1)-len(s2))>1:
    return False
else:
    greaterString= s1 if len(s1)>=len(s2) else s2
    smallerString=s2 if len(s1)>=len(s2) else s1
    d={}
    for each in greaterString:
        if each in d:
            d[each]+=1
        else:
            d[each]=1
    for each in smallerString:
        if each in d:
            d[each]-=1
        else:
            d[each]=1


class subject():
    count=0
    def __init__(self,name):
        self.name=name
    def __get


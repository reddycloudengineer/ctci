# 1.1 Is unique
def isunique(s):
    if len(s)>128:
        return False
    al=[-1]*128
    for i in range(0,len(s)):
        c=ord[s[i]]-97
        if c>0:
            return False
        al[c]=1
    return True

#1.2 check permutation

def permutation(s,t):
    if len(s)!=len(t):
        return False
    c=[0]*26
    for i in range(0,len(s)):
        ts=ord(s[i])-97
        c[ts]=c[ts]+1

    for i in range(0,len(t)):
        ts=ord(t[i])-97
        c[ts]=c[ts]-1
        if c[ts]<0:
            return False

    return True

#urlify 1.3

def replaceSpaces(s):
    s=list(s)
    for i in range(0,len(s)):
        if s[i]==' ':
            s[i]='%20'
    return ''.join(s)


#1.4 palindrome


def charDict(s):
    d={}
    for each in s:
        if each not in d and each!=' ':
            d[each]=1
        else:
            d[each]+=1
    return d

def oddCount(d):
    ocount=0
    for each in d:
        if each%2!=0:
            ocount+=1
    if ocount>1:
        return False

    return True


def permutationisPalindrome(s):
    countOdd=0
    a=[0]*26
    for each in s:
        t=ord(each)-97
        a[t]+=1
        if a[t]%2!=0:
            countOdd+=1
        else:
            countOdd-=1
    return countOdd>1

def oneAway(s,t):
    if len(s)==len(t):
        return oneReplaceAway(s,t)
    elif abs(len(s)-len(t))==1:
        if len(s)>len(t):
            return oneEditAway(t,s)
        return oneEditAway(s,t)
    return False

def oneEditAway(short,long):
    si=0
    li=0
    while(si<len(short) and li<len(long)):
        if short[si]!=long[li]:
            if si!=li:
                return False
            li+=1
        else:
            li+=1
            si+=1
    return True

def oneReplaceAway(s1,s2):
    found=False
    for i in range(0,len(s1)):
        if s1[i]!=s2[i]:
            found=True
            if found:
                return False
    return True

def stringCompression(s):
    r=[]
    while(s):
        c=s[0]
        if not r:
            r.append([c,1])
        else:
            if r[-1][0]==c:
                r[-1][1]+=1
            else:
                r.append([c,1])
        s=s[1:]
    s=[]
    for each in r:
        s.append(each[0]+str(each[1]))

    print(''.join(s))


stringCompression('aabcccccaaa')

def stringRotation(s1,s2):
    t=''
    for i in range(0,len(s1)):
        t=s1[i:]+s1[:i]
        if t==s2:
            return True
    return False

print(stringRotation('waterBottle','rBottlewate'))


























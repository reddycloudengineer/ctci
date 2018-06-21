S = "a1b2"
l=[]
def letterCasePermutation(s,l):
    if s=='':
        return l

    c=s[0]
    t=[c]
    # print(s,l,c)
    if c.islower():
        t.append(c.upper())
    m=[]
    if not l:
        m=t
    else:
        for each in t:
            for leach in l:
                m.append(leach+each)
    # print(m)
    return letterCasePermutation(s[1:],m)

# print(letterCasePermutation(S,l))
#
# S='3z4'
# l=[]
# print(letterCasePermutation(S,l))
# S='12345'
# l=[]
# print(letterCasePermutation(S,l))
# S=''
# l=[]
# print(letterCasePermutation(S,l))


def isPalindrome(s):
    # fromLast=len(s)-1
    # fromBeg=0
    # tLast=[]
    # tBeg=[]
    # while(fromLast>=0):
    #     if s[fromBeg].isalnum():
    #         tBeg.append(s[fromBeg].lower())
    #     if s[fromLast].isalnum():
    #         tLast.append(s[fromLast].lower())
    #     fromBeg=fromBeg+1
    #     fromLast=fromLast-1
    #
    # return ''.join(tLast)==''.join(tBeg)

    t=[]
    l=0
    for each in s:
        if each.isalnum():
            t.append(each.lower())
            l+=1

    v=True
    beg=0
    last=l-1

    while(last>=beg):

        if t[beg]!=t[last]:
            return False
        last=last-1
        beg=beg+1
    return True

# print(isPalindrome('A man, a plan, a canal: Panama'))
# print(isPalindrome('race a car'))
# print(isPalindrome(''))

def validPalindrome(s):
    beg=0
    last=len(s)-1
    v=True
    while(last>=beg):

        if s[last]!=s[beg]:
            last=last-2
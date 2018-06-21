import datetime
import math
def findPrimes(n):
    d={}
    i=2
    while(i<n):
        if i not in d:
            k=2
            while(k*i<n):
                d[k*i]=False
                k=k+1
        i=i+1
    print(n-2-len(d))



def findPrimesModfied(n):
    pass
    #do it using i*i
    # you need to go through the array to count the true values
    # since you have didn't go all over the array

# 2,3,5,7,9 /2
# 2,3,5,7

print(findPrimes(1000000))


def secondMaxNumber(l):
    fMax=-math.inf
    sMax=-math.inf
    tMax=-math.inf

    for each in l:
        if each>fMax:
            tMax=sMax
            sMax=fMax
            fMax=each
        elif each>sMax and each<fMax:
            tMax=sMax
            sMax=each
        elif each>tMax and each<sMax:
            tMax=each

    if tMax!=-math.inf:
        return tMax

    if sMax!=-math.inf or fMax!=-math.inf:
        return fMax


    print(fMax,sMax,tMax)




# secondMaxNumber([1,2,3,4,5,6,7,8,9,10])
# secondMaxNumber([2,2,3,1])
# secondMaxNumber([1,2,1])
# secondMaxNumber([1,1,1])
# secondMaxNumber([1,2])
# secondMaxNumber([3,2,1])


def kdiffArrays(nums,k):
    c=0
    if k>=0:
        d={}
        ind=0
        for each in nums:
            if each in d:
                d[each]=d[each]+1
            else:
                d[each]=1
            ind+=1
        c=0
        t=[]
        for each in d:
            if k==0:
                if d[each]>1:
                    c=c+1
            elif k+each in d:
                c=c+1
    print(c)
    return c

# kdiffArrays([1,1,1,1,3,3,3],0)
# kdiffArrays([1,2,3,4,5],1)
# kdiffArrays([3, 1, 4, 1, 5],2)
# kdiffArrays([1, 3, 1, 5, 4],0)
# kdiffArrays([1,3,1,4,5],0)

def shiftingLetters(S,shifts):
    l=[]
    # for each in S:
    #     l.append(ord(each)-96)
    # print(l)
    # t=[]
    c=0
    i=len(shifts)-1
    j=len(shifts)-1
    while(i>=0):

        c = c + shifts[i]
        t=ord(S[j])-96
        t=t+c
        t=t%26
        print('before ',c,S[j],t)
        if t==0:
            t='z'
        else:
            t=chr(t+96)
        l.append(t)
        i-=1
        j-=1
    # print(l)
    return ''.join(l[::-1])
    # for i in range(0,len(shifts)):
    #     t=shifts[i]
    #     for j in range(i+1,len(shifts)):
    #         t=t+shifts[j]
    #     c.append(t)
    # print(c)
    #
    # for i in range(0,len(shifts)):
    #     l[i]=l[i]+c[i]
    #     l[i]=chr(l[i]%26+96)
    #
    # return ''.join(l)




# print(shiftingLetters('abc',[3,5,9]))


def maxDistToClosest(seats):
    i=0
    m=-99999999
    t=-99999999
    while(i<len(seats)):
        if seats[i]==1:
            t=1
        elif t>=0:
            t=t+1
        if t>m:
            m=t
        i=i+1
    if m==t:
        return m-1
    return int(m/2)

# print(maxDistToClosest([1,0,0,0,1,0,1]))
# print(maxDistToClosest([1,0,0,0]))


def solution(K, L, A):
    memo=[[[None for k in range(0,2)] for j in range(0,K+1)] for i in range(0,len(A))]
    return solHelper(K,L,A,memo,True,0)


def solHelper(k, L, A, memo, isEmpty, index):
    if k == 0:
        return 0
    elif index>=len(A):
        if isEmpty:
            return 0
        return -21441717

    elif memo[index][k][isEmpty]:
        print('inside memo ','index ', index, 'k', k, 'isEmpty ', isEmpty, memo[index][k][isEmpty])
        return memo[index][k][isEmpty]
    else:
        memo[index][k][isEmpty] = max(0,solHelper(k, L, A, memo, isEmpty, index + 1))
        if isEmpty:
            memo[index][k][isEmpty] = max(memo[index][k][isEmpty],-A[index] + solHelper(k, L, A, memo, False, index + L))
        else:
            memo[index][k][isEmpty] = max(memo[index][k][isEmpty],A[index] + solHelper(k - 1, L, A, memo, True, index + 1))
    print('index ',index,'k',k,'isEmpty ',isEmpty,memo[index][k][isEmpty])
    return memo[index][k][isEmpty]

# print(solution(2,2,[1,10,20,1,10,8]))
# print(solution(2,2,[1]))


def backspaceCompare(S,T):
    s = []
    for each in S:
        if each == '#' and s:
            s.pop()
        elif each!='#':
            s.append(each)
        # print(s)
    t = []
    print('T ', T)
    for each in T:
        print('each ', each)
        if each == '#' and t:
            t.pop()
        elif each!='#':
            t.append(each)
        print('t', t)

    return ''.join(t)==''.join(s)

# S = "ab#c"
# T = "ad#c"
#
# print(backspaceCompare(S,T))
#
# S = "ab##"
# T = "c#d#"
# print(backspaceCompare(S,T))
#
# S = "a##c"
# T = "#a#c"
# print(backspaceCompare(S,T))
#
# S = "a#c"
# T = "b"
# print(backspaceCompare(S,T))

# S="y#fo##f"
# T="y#f#o##f"
# print(backspaceCompare(S,T))

# S="a##c"
# T="#a#c"
# print(backspaceCompare(S,T))


def isNStraightHand(hand, W):
    if W*3>len(hand):
        return False

    d={}
    temp=0
    for each in hand:
        if each in d:
            d[each]=d[each]+1
        else:
            d[each]=1
    for each in d:
        t=each
        c=0
        while(t<each+3):
            if (t in d) and d[t]>0:
                c=c+1
            else:
                break
            t=t+1
        if c==3:
            temp=temp +1
            t=each
            while(t<each+3):
                d[t]=d[t]-1
                t=t+1
    print('d ',d,'temp ',temp)
    if temp>=W:
        return True
    return False




# hand = [1,2,3,6,2,3,4,7,8]
# W = 3
#
# print(isNStraightHand(hand,W))
# hand = [1,2,3,4,5]
# W = 4
# print(isNStraightHand(hand,W))


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next




def creatingNodes(l):
    head=None
    currentNode=head
    for each in l:
        if not head:
            head=Node(each)
            currentNode=head
        else:
            currentNode.next=Node(each)
            currentNode=currentNode.next

    return head

def findNodeLen(head):
    currentNode=head
    l=0
    while(currentNode):
        l=l+1
        currentNode=currentNode.next
    return l

# 1,2,3,3,2,1 , k=6
#
# 1, [2,3,3,2,1] k =4 , True
# 2, [3,3,2,1] k=2 , True
# 3, [3,2,1] - [3 ] True
# base k=0: sl[0]
# base k=1 : sl[1]

#[1,2,3,2,1]
#k=5 , 1,[2,3,2,1]
#k=3, 2,[3,2,1]
#k=1, 3, [2,1]

def findPalindrome(head,k):
    if not head:
        return (head, True)
    if k==0:
        return (head,True)
    elif k==1:
        return (head.next,True)
    currentNode=head
    res=findPalindrome(head.next,k-2)
    print('currentNode ',currentNode.data,'resultNode data',res[0].data)
    if currentNode.data!=res[0].data:
        return (res[0].next,False)
    return (res[0].next,res[1])


def nodePalindromeHelper(head):
    pass



l=[1,2,3,3,2,1]
head=creatingNodes(l)
# print(findPalindrome(head,findNodeLen(head)))


def palinList(l):
    if len(l)<=1:
        print('It will be always since it doesnt have length greater 1')
    print('result will be',palinListHelper(l,0,len(l)))

def palinListHelper(l,ind,k):
    if k==0:
        return (l,ind,True)
    elif k==1:
        return (l,ind+1,True)

    currentElement=l[ind]
    res=palinListHelper(l,ind+1,k-2)
    print('ind ',ind,'current element ', currentElement,'result ','result element ',l[res[1]],'result index ',res[1],'k value ',k)
    if currentElement!=l[res[1]]:
        print('inside if',(l,res[1]+1,False))
        return (l,res[1]+1,False)
    return (l,res[1]+1,res[2])

# l=[1,2,3,3,1,1]
# palinList(l)
#
# l=[1]
# palinList(l)
#
# l=[]
# palinList(l)
# l=[1,1,1]
# palinList(l)
#
# l=[1,2]
# palinList(l)

class TreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


def makeTreeNodes(l):
    if not l:
        return None
    mid=int(len(l)/2)
    head=TreeNode(l[mid])
    head.left=makeTreeNodes(l[0:mid])
    head.right=makeTreeNodes(l[mid+1:])
    return head




def mergeTrees(nodeA,nodeB):
    if not nodeA and not nodeB:
        return None
    t=0
    if nodeA:
        t=t+nodeA.data
    if nodeB:
        t=t+nodeB.data
    head=TreeNode(t)
    leftA=None
    rightA=None
    leftB=None
    rightB=None

    if nodeA and nodeA.left:
        leftA=nodeA.left
    if nodeB and nodeB.left:
        leftB=nodeB.left
    if nodeA and nodeA.right:
        rightA=nodeA.right
    if nodeB and nodeB.right:
        rightB=nodeB.right

    head.right=mergeTrees(rightA,rightB)
    head.left=mergeTrees(leftA,leftB)

    return head





def printNodes(root):
    if not root:
        return ''

    s=str(root.data)


    if not root.left and root.right:
        s = s + '(' + printNodes(root.left) + ')' + '(' + printNodes(root.right) + ')'
    else:
        if root.left:
            s= s + '(' + printNodes(root.left) + ')'

        if root.right:
            s=s+'(' + printNodes(root.right) + ')'

    return s


nodeA=makeTreeNodes([1,2])
nodeB=makeTreeNodes([1,2,3,4,5,6,7])

# mergedNode=mergeTrees(nodeA,nodeB)
# print(mergedNode.data)

print(printNodes(nodeA))

M=[[1,1,1],
 [1,0,1],
 [1,1,1]]
def imageSmoother(M):
    l=len(M)
    w=len(M[0])
    o=[]

    for i in range(0,l):
        o.append([0]*w)
        for j in range(0,w):
            c=0
            s=0
            for x in [i,i+1,i-1]:
                for y in [j,j+1,j-1]:
                    if x>=0 and x<l and y>=0 and y<w:
                        s=s+M[x][y]
                        c=c+1
            o[i][j]=int(s/c)
    print(o)

# imageSmoother(M)


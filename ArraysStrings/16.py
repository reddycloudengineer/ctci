#16.1

def numSwapper(a,b):
    a=a^b
    print('a ',a)
    b=a^b
    print('b ',b)
    a=a^b
    print('a ',a)

    print(a,b)

# numSwapper(5,6)

def factorialZeros(n):

    i=5
    count=0
    while(n/i>0):
        count=count+int(n/i)
        i=i*5
    print(count)

# factorialZeros(26)

#16.6 smallest difference

a=[1,3,15,11,7,2]
b=[23,127,235,19,8,7]



def smallDiff(a,b):
    a=sorted(a)
    b=sorted(b)

    i1=0
    i2=0
    diff=65000
    while(i1<len(a) and i2<len(b)):
        t1=a[i1]
        t2=b[i2]
        if t1<=t2:
            if t2-t1<diff:
                diff=t2-t1
            i1=i1+1
        else:
            if t1-t2<diff:
                diff=t1-t2
            i2=i2+1
    print(diff)
    return diff

# smallDiff(a,b)

years=[[12,15],[20,90],[10,98],[1,72],[10,98],[23,82],[13,98],[90,98],[83,99],[75,94]]

def numMax(years):
    yearD=[]
    mx=0
    for year in years:
        start,end=year
        if end>mx:
            mx=end

    yearList=[0]*(mx+1)

    for year in years:
        start,end=year
        yearList[start]=yearList[start]+1
        yearList[end]=yearList[end]-1
    for i in range(1,len(yearList)):

        yearList[i]=yearList[i-1]+yearList[i]

    m=0
    for each in yearList:
        if each>m:
            m=each
    print('max value ',m)
    return m

# numMax(years)

def divingBoard(k,short,long,lengths):
    if k<=0:
        return None
    else:
        total=0
        return divingBoardHelper(k,total,short,long,lengths)

def divingBoardHelper(k,total,short,long,lengths):
    if k==0:
        if total not in lengths:
            lengths.append(total)
            return
    elif k<0:
        return
    else:
        divingBoardHelper(k-1,total+short,short,long,lengths)
        divingBoardHelper(k-1,total+long,short,long,lengths)

lengths=[]
divingBoard(5,1,2,lengths)

# print(lengths)


def divingBoardMemo(k,short,long,lengths,memo):
    if k<=0:
        return None
    else:
        divingBoardMemoHelper(5,0,1,2,lengths,memo)

def divingBoardMemoHelper(k,total,short,long,lengths,memo):
    if k<0:
        return
    elif k==0:
        if total not in lengths:
            lengths.append(total)

    elif (k,total) in memo:
        print('inside memo ',(k,total))

    else:
        memo[(k-1,total+short)]=total+short
        memo[(k-1,total+long)]=total+long
        divingBoardMemoHelper(k+1,total-short,short,long,lengths,memo)
        divingBoardMemoHelper(k+1,total-long,short,long,lengths,memo)

lengths=[]
memo={}
# divingBoardMemo(5,1,2,lengths,memo)
#
# print('lengths ',lengths,'memo ',memo)

s=[1,2,4,7,10,11,7,12,6,7,16,18,19]

def subSort(s):
    positionFromFirst=0
    postionFromLast=len(s)-1
    mini=s[len(s)-1]
    maxi=s[0]
    t=0
    for i in range(1,len(s)-1):
        if s[i]>=t:
            t=s[i]
        else:
            maxi=i
    print(maxi,s[maxi])

    t=None
    for i in range(len(s)-1,0,-1):
        if not t:
            t=s[i]
        elif s[i]<=t:
            t=s[i]
        else:
            mini=i
    print(mini,s[mini])

    mint=s[mini]
    maxt=s[mini]
    for i in range(mini+1,maxi+1):
        if s[i]>maxt:
            maxt=s[i]

        if s[i]<mint:
            mint=s[i]

    print('max t',maxt,'min t',mint)

    minindex=0
    for i in range(0,len(s)):
        if s[i]<mint and s[i+1]>mint:
            minindex=i+1
            break

    maxindex=0
    for i in range(len(s)-1,1,-1):
        if s[i]>maxt and s[i-1]<maxt:
            maxindex=i-1
            break

    print('minindex', minindex,'maxindex',maxindex)

# subSort(s)


s=[2,-8,3,-2,4,-10]

def contiguousSequence(s):
    i=0
    mx=-650000
    while(i<len(s)):

        for j in range(i+1,len(s)+1):
            t=s[i:j]
            print(t)
            if sum(t)>mx and sum(t)>0:
                mx=sum(t)
                print(mx)
            elif sum(t)<0:
                break
        i=j
    print('max value',mx)

# contiguousSequence(s)


sizes=[[0,2,1,0],
       [0,1,0,1],
       [1,1,0,1],
       [0,1,0,1]]

visited=[]
def pondSizes(sizes,visited):

    for row in range(0,len(sizes)):
        for col in range(0,len(sizes[0])):
            if  sizes[row][col]==0 and (row,col) not in visited:
                print(pondSizesHelper(sizes,row,col,visited))

def pondSizesHelper(sizes,row,col,visited):
    ways=0
    if row<0 or row>len(sizes)-1 or col<0 or col>len(sizes[0])-1 or sizes[row][col]!=0:
        return 0
    elif sizes[row][col]==0:
        return 1
    else:
         rc=[(row+1,col),(row-1,col),(row,col+1),(row,col-1),(row+1,col+1),(row-1,col+1),(row+1,col-1),(row-1,col-1)]
         for each in rc:
             a,b=each
             visited.append(each)
             ways=ways+pondSizesHelper(sizes,a,b,visited)

    print(visited)
    return ways

# pondSizes(sizes,visited)


input=8733

class trieNode(object):
    def __init__(self,data,children={}):
        self.data=data
        self.children=children
    def addChldren(self,val):
        self.children[val.data]=val



rootNode=trieNode('*')

tNode=trieNode('t')
rNode=trieNode('r')
eNode=trieNode('e')
e1Node=trieNode('e')
endNode=trieNode('*')

rootNode.addChldren(tNode)
tNode.addChldren(rNode)
rNode.addChldren(eNode)
eNode.addChldren(e1Node)
endNode.addChldren(endNode)

uNode=trieNode('u')
sNode=trieNode('s')
e2Node=trieNode('e')
dNode=trieNode('d')

rootNode.addChldren(uNode)
uNode.addChldren(sNode)
sNode.addChldren(e2Node)
e2Node.addChldren(dNode)
dNode.addChldren(endNode)

d={1:[],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v']
   ,9:['w','x','y','z'],0:[]}

s='8733'

# nodes={}
# stack=[rootNode]
# while(s):
#
#     t=int(s[0])
#     st=[]
#     for each in d[t]:
#         for n in stack:
#             if each in n.children:
#                 print(each)
#                 st.append()

    #
    # s=s[1:]


a=[4,1,2,1,1,2]
b=[3,6,3,3]

def sumSwap(a,b):
    sa=sum(a)
    sb=sum(b)

    for each in b:
        ta=int((sa-sb)/2)+each
        if ta in a:
            print('a',ta,'b',each)
            break

# sumSwap(a,b)


a=[1,1,1,2,2,2,4,4,3,3,3,3]

def pairSum(a,targetSum):
    d={}
    for each in a:
        if each not in d:
            d[each]=1
        else:
            d[each]+=1
    for each in d:
        b=targetSum-a
        if b in d:
            if a==b:
                pass
            else:
                pass


class dNode(object):
    def __init__(self,key,val,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

headNode=None
def lruCache():
    d={72:'Food',13:'Key chain',45:'Blanket',27:'Book'}
    dn={}
    for each in d:

        if not headNode:
            headNode=dNode(each,d[each])
            currentNode=headNode
            dn[each]=currentNode
        else:
            temp=dNode(each,d[each])
            currentNode.next=temp
            temp.prev=currentNode
            currentNode=temp
            dn[each]=currentNode
            


















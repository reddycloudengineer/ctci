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


nodeA=makeTreeNodes([1,2,3,4,5,6,7])

def convertBST(root):
    a=0
    b=0
    t=[]
    if root:
        t.append(root)

    if root.left:
        t.append(root.left)

    if root.right:
        t.append(root.right)

    d={}
    for i in t:
        m=0
        for j in t:
            if i!=j and j.data>i.data:
                m=j.data+m
            d[i]=m +i.data

    for each in d:
        each.data=d[each]

def printNodes(root):
    c=0
    if not root:
        return 0

    if root.left:
        c=c+root.left.data
    c=c+printNodes(root.left)+printNodes(root.right)
    return c



c=0
print(printNodes(nodeA))


def levelOrderPrint(root,height,l):

    if not root:
        return

def heightBinaryTree(root):
    if not root:
        return 0
    return 1+max(heightBinaryTree(root.left),heightBinaryTree(root.right))

def minDepth(root):
    h=0
    q=[root]
    c=1
    while(q):
        t=[]
        currentNode=q.pop()
        while(currentNode):



            if currentNode.left:
                if currentNode.left.left == None and currentNode.left.right == None:
                    print('current Node value', currentNode.left.data)
                    return c
                t.append(currentNode.left)
            if currentNode.right:
                t.append(currentNode.right)

            if not q:
                currentNode=None
            else:
                currentNode=q.pop()
        c=c+1
        q=t


nums1=[4,1,2]
nums2=[1,3,4,2]

def findNextMin(nums1,nums2):
    t=nums1[0]



def findNextMinVal(minVal,nums1):
    t=9999999999
    for each in nums1:
        if t>=minVal and t>each:
            t=each
    return t



findNextMin(nums1,nums2)




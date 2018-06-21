#4.1 Route between nodes

a=[1,2,3,4,5,6,7,8,9]

class Node(object):

    def __init__(self,data,left=None,right=None,level=0):
        self.data=data
        self.left=left
        self.right=right
        self.level=level

class createBST(object):

    def createBST(self,a):
        if not a:
            return None
        else:
            self.createBSTHelper(a,0,len(a)-1)

    def createBSTHelper(self,a,start,end):
        if end>start:
            return None
        mid=int((start+end)/2)
        currentNode=Node(a[mid])
        currentNode.left=self.createBSTHelper(a,start,mid-1)
        currentNode.right=self.createBSTHelper(a,mid+1,end)
        return currentNode
    def createBSTHelperV2(self,a,h):
        if not a:
            # print('a is',a)
            return None
        mid=int(len(a)/2)
        currentNode=Node(a[mid])
        currentNode.level=h
        print('currentLevel ',h)
        # print('a[0:mid]',a[0:mid],'a[mid:]',a[mid+1:])

        left=self.createBSTHelperV2(a[0:(mid)],h+1)
        if not left:
            currentNode.left=None
        else:
            currentNode.left=left

        right=self.createBSTHelperV2(a[mid+1:],h+1)
        if not right:
            currentNode.right=None
        else:
            currentNode.right=right

        return currentNode


cbst=createBST()
h=0
rootNode=cbst.createBSTHelperV2(a,h)
print(rootNode)

#print all the nodes

nodeStack=[rootNode]

while(nodeStack):
    currentNode=nodeStack.pop(0)
    print('currentNode',currentNode.data)
    if currentNode.right:
        nodeStack.append(currentNode.right)
        print('currentNode right',currentNode.right.data,'level right',currentNode.right.level)
    else:
        print('currentNode right is None')
    if currentNode.left:
        nodeStack.append(currentNode.left)
        print('currentNode left',currentNode.left.data,'level left',currentNode.left.level)
    else:
        print('currentNode left is None')


#4.3List of Depths

def listDepths(root,linkList):
    if not root:
        return
    ind=root.level
    if len(linkList)<=ind:
        linkList.insert(ind,[])
    linkList[ind].append(root.data)
    listDepths(root.left,linkList)
    listDepths(root.right,linkList)

linkList=[]
listDepths(rootNode,linkList)
print('link list',linkList)

#4.4 checkbalanced

def checkBalanced(rootNode):
    if not rootNode:
        return True

    h=abs(getHeight(rootNode.left)-getHeight(rootNode.right))
    if h>2:
        return False
    return checkBalanced(rootNode.left) and checkBalanced(rootNode.right)

def getHeight(node):
    if node==None:
        return -1
    return max(getHeight(node.left),getHeight(node.right))+1

#4.5ValidateBST

def validateBST(rootNode):
    return validateBSTHelper(rootNode,0,10000)

def validateBSTHelper(rootNode,minval,maxval):

    if not rootNode:
        True

    if rootNode.data>=minval and rootNode.data<=maxval:
        return True
    else:
        return False

    return validateBSTHelper(rootNode.left,minval,rootNode.data+1) and validateBSTHelper(rootNode,rootNode.data+1,maxval)

print(validateBST(rootNode))


#4.8 FirstCommonAncestor

def searchNode(rootNode,val,path):
    if not rootNode:
        return
    if rootNode.data==val:
        return path.append(val)


    left=searchNode(rootNode.left,val,path)
    right=searchNode(rootNode.right,val,path)
    # if rootNode.left:
    #     print('rootNode.left ',rootNode.left.data,'left',left)
    # if rootNode.right:
    #     print('rootNode.right ',rootNode.right.data,'right ',right)

    if left:
        print('left ',left,rootNode.data)
        path.append(rootNode.left.data)
    if right:
        print('right ',right,rootNode.data)
        path.append(rootNode.right.data)
    # path.append(searchNode(rootNode.left,val,path))
    # path.append(searchNode(rootNode.right,val,path))
    return path

path=[]
searchNode(rootNode,6,path)
print(path)

















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


# nodeA=makeTreeNodes([1,2,3,4,5,6,7])
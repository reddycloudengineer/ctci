

#3rd level
leaf_7 = (7, None, None)
leaf_1 = (1, None, None)
#2nd level
node_3 = (3, leaf_7, None)
node_2 = (2, None, leaf_1)
root = (1, node_3, node_2)

# def serialize_tree(tree):
#     return '13700020100'
# assert serialize_tree(root) == '13700020100'
# def serialize_tree(leaf_7):
#     return '700'
#
#

def recNode(root):
    l=[]
    if root==None:
        print('0',end='')
        return '0'
    else:
        l.append(root[0])
        print(root[0],end='')
        l.extend(recNode(root[1]))
        l.extend(recNode(root[2]))
    return l

print(recNode(root))




#13700020100
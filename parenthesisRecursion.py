#input --> 1
#output --> ()
#2 --()(), (())

def paranthesis(n):
    paranAll=[]
    if n==1:
        return ['()']
    else:
        paranAll=paranthesis(n-1)
        #(,)



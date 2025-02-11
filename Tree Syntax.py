#### Trees #####################################
#### Binary Tree is a one in which each node has one or two child

class binaryTree(object):
     def _init_(self,value):
         self.value=value
         self.leftBranch=None
         self.rightBranch=None
         self.parent=None
     def setLeftBranch(self,node):
         self.leftBranch=node
     def setRightBranch(self,node):
         self.rightBranch=node
     def setParent(self,parent):
         self.Parent=parent
     def getValue(self):
         return self.value
     def getLeftBranch(self):
         return self.leftBranch
     def getRightBranch(self):
         return self.rightBranch
     def getParent(self):
         return self.Parent
     def _str_(self):
         return self.value
   
n5=binaryTree(5)
n2=binaryTree(2)
n1=binaryTree(1)                                                                               
n4=binaryTree(4)          
n8=binaryTree(8)
n6=binaryTree(6)
n7=binaryTree(7)
n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRigthBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)

####################################################################################
######## Searching a tree #########################################################
###1. Depth first search
#### 2. Breadth first search

################## Depth first Search ##############################################
###### DFS uses the notion of stacks###############################################
def DFSBinary(root,fcn): #####fcn is a function that returns true or false
    stack=[root]
    while len(stack)>0:
        if(fcn(stack[0])):
            return True
        else:
            temp=stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0,temp.getRightBranch)
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch)
    return False
    
#####################################################################################
################## Breadth First Search ###########################################
####################### BFS uses the notion of Queue #############################
 
def BFSBinary(root,fcn): #####fcn is a function that returns true or false
    queue=[root]
    while len(queue)>0:
        if(fcn(queue[0])):
            return True
        else:
            temp=queue.pop(0)
            if temp.getRightBranch():
                queue.append(temp.getRightBranch)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch)
    return False                                                                                       

#######################################################################################

##########################################################################################
#### id we have to trace the path back in a tree ##########################################

def DFSBinaryPath(root,fcn): #####fcn is a function that returns true or false
    stack=[root]
    while len(stack)>0:
        if(fcn(stack[0])):
            return TracePath(stack[0])
        else:
            temp=stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0,temp.getRightBranch)
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch)
    return False

def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node]+TracePath(node.getParent())
   
#######################################################################################
######### Ordered Search in a Ordered Tree ############################################

def DFSBinaryOrdered(root,fcn,ItFcn): #####fcn is a function that returns true or false
    stack=[root]
    while len(stack)>0:
        if(fcn(stack[0])):
            return True
        elif ItFcn(stack[0]):  ############# IfFcn is a function which compare the value and give the result
            temp=stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0,temp.getRightBranch)
        else:
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch)
    return False                                     

##############################################################################################
                                                                    
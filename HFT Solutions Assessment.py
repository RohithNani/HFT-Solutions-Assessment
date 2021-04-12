
import copy

class Node():

    def  __init__(self,price,shares):
        self.price = price
        self.shares = shares
        self.parent = None
        self.left = None
        self.right = None

class MinHeap:
    
    def __init__(self):
        self.root = None
        
        
    def positionFinder(self,root):
        
        queue = list()
        queue.append(root)
        
        while(True):
            
            node = queue.pop(0)
            
            if node.left is not None and node.right is not None:
                queue.append(node.left)
                queue.append(node.right) 
            else:
                return node;
        
    
    def upHeapify(self,node):
        
        if node.parent is None:
            return
        
        if node.parent.price>node.price:
            price = node.parent.price
            shares = node.parent.shares
            node.parent.price = node.price
            node.parent.shares = node.shares
            node.price = price
            node.shares = shares
            self.upHeapify(node.parent)
        
        
        
    def add(self,price,shares):
        
        temp = Node(price,shares)
        
        if self.root is None:
            self.root = temp
            #print(f"Added price : {price} and shares : {shares}")
            return
        
        node = self.positionFinder(self.root)
        
        if node.left is None:
            node.left = temp
            node.left.parent = node
            node = node.left
        else:
            node.right = temp
            node.right.parent = node
            node = node.right
        
        self.upHeapify(node)
        #print(f"Added price : {price} and shares : {shares}")
    
    def lastNode(self,node):
        
        queue = list()
        queue.append(node)
        
        while True:
            
            node = queue.pop(0)
            
            if(len(queue)==0 and node.left is None):
                return node
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    
    def downHeapify(self,node):
        
        if node is None or node.left is None:
            return
        if node.right is None:
            if node.left.price<node.price:
                price = node.left.price
                shares = node.left.shares
                node.left.price = node.price
                node.left.shares = node.shares
                node.price = price
                node.shares = shares
            return
        
        if node.left.price<node.right.price:
            if node.left.price<node.price:
                price = node.left.price
                shares = node.left.shares
                node.left.price = node.price
                node.left.shares = node.shares
                node.price = price
                node.shares = shares
                self.downHeapify(node.left)
        else:
            if node.right.price<node.price:
                price = node.right.price
                shares = node.right.shares
                node.right.price = node.price
                node.right.shares = node.shares
                node.price = price
                node.shares = shares
                self.downHeapify(node.right)
                
    
    def pop(self):
        
        if self.root is None:
            return
        
        if self.root.left is None and self.root.right is None:
            root = self.root
            self.root = None
            return root
        
        node = self.lastNode(self.root)
        
        price = self.root.price
        shares = self.root.shares
        self.root.price = node.price
        self.root.shares = node.shares
        node.price = price
        node.shares = shares
        
        if node.parent.left is node:
            node.parent.left = None
        else:
            node.parent.right = None
            
        self.downHeapify(self.root)
        
        return node
        
    
    def peek(self):
        return self.root
        
    
    def levelOrder(self,root):
        queue = list()
        queue.append(root)
        queue.append(None)
        flag=0
        
        while(True):
            #print(queue)
            node = queue.pop(0)
            
            if node is None:
                if flag==1:
                    break
                flag=1
                queue.append(None)
                print("")
                continue
            
            flag=0
            
            print(f"price = {node.price} shares = {node.shares}",end=" ")
            queue.append(node.left)
            queue.append(node.right)
            
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(f"price = {root.price} shares = {root.shares}")
        self.inorder(root.right)
    
    def show(self):
        self.levelOrder(self.root)
        
class MaxHeap:
    
    def __init__(self):
        self.root = None
        
        
    def positionFinder(self,root):
        
        queue = list()
        queue.append(root)
        
        while(True):
            
            node = queue.pop(0)
            
            if node.left is not None and node.right is not None:
                queue.append(node.left)
                queue.append(node.right) 
            else:
                return node;
        
    
    def upHeapify(self,node):
        
        if node.parent is None:
            return
        
        if node.parent.price<node.price:
            price = node.parent.price
            shares = node.parent.shares
            node.parent.price = node.price
            node.parent.shares = node.shares
            node.price = price
            node.shares = shares
            self.upHeapify(node.parent)
        
        
        
    def add(self,price,shares):
        
        temp = Node(price,shares)
        
        if self.root is None:
            self.root = temp
            #print(f"Added price : {price} and shares : {shares}")
            return
        
        node = self.positionFinder(self.root)
        
        if node.left is None:
            node.left = temp
            node.left.parent = node
            node = node.left
        else:
            node.right = temp
            node.right.parent = node
            node = node.right
        
        self.upHeapify(node)
        #print(f"Added price : {price} and shares : {shares}")
    
    def lastNode(self,node):
        
        queue = list()
        queue.append(node)
        
        while True:
            
            node = queue.pop(0)
            
            if(len(queue)==0 and node.left is None):
                return node
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    
    def downHeapify(self,node):
        
        if node is None or node.left is None:
            return
        if node.right is None:
            if node.left.price>node.price:
                price = node.left.price
                shares = node.left.shares
                node.left.price = node.price
                node.left.shares = node.shares
                node.price = price
                node.shares = shares
            return
            
        if node.left.price>node.right.price:
            if node.left.price>node.price:
                price = node.left.price
                shares = node.left.shares
                node.left.price = node.price
                node.left.shares = node.shares
                node.price = price
                node.shares = shares
                self.downHeapify(node.left)
        else:
            if node.right.price>node.price:
                price = node.right.price
                shares = node.right.shares
                node.right.price = node.price
                node.right.shares = node.shares
                node.price = price
                node.shares = shares
                self.downHeapify(node.right)
                
    
    def pop(self):
        
        if self.root is None:
            return
        
        if self.root.left is None and self.root.right is None:
            root = self.root
            self.root = None
            return root
        
        node = self.lastNode(self.root)
        
        price = self.root.price
        shares = self.root.shares
        self.root.price = node.price
        self.root.shares = node.shares
        node.price = price
        node.shares = shares
        
        if node.parent.left is node:
            node.parent.left = None
        else:
            node.parent.right = None
            
        self.downHeapify(self.root)
        
        return node
        
    
    def peek(self):
        return self.root
        
    
    def levelOrder(self,root):
        queue = list()
        queue.append(root)
        queue.append(None)
        flag=0
        
        while(True):
            #print(queue)
            node = queue.pop(0)
            
            if node is None:
                if flag==1:
                    break
                flag=1
                queue.append(None)
                print("")
                continue
            
            flag=0
            
            print(f"price = {node.price} shares = {node.shares}",end=" ")
            queue.append(node.left)
            queue.append(node.right)
            
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(f"price = {root.price} shares = {root.shares}")
        self.inorder(root.right)
    
    def show(self):
        self.levelOrder(self.root)



buy = MinHeap()
sell = MaxHeap()

buy.add(11.38, 400)
buy.add(11.39, 1600)
buy.add(11.40, 1205)
buy.add(11.41, 1400)
buy.add(11.42, 900)
buy.add(11.43, 900)

sell.add(11.36,2700)
sell.add(11.35,1100)
sell.add(11.34,1100)
sell.add(11.33,1600)
sell.add(11.32,700)
sell.add(11.31,700)

def show(buy, sell):
    count=0
    print("----------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t BUY")
    print("\t\t\t\t\t\tPrice\tShares")
    while buy.peek() is not None:
        #buy.show()
        temp = buy.pop()
        print("\t\t\t\t\t\t",temp.price,"\t",temp.shares)
        count+=1
        if(count==5):
            break
    count=0
    print("----------------------------------------------------------------------")
    print("\tSELL")
    print("Price\tShares")
    while sell.peek() is not None:
        temp = sell.pop()
        print(temp.price,"\t",temp.shares)
        count+=1
        if(count==5):
            break
    print("----------------------------------------------------------------------")
    

def marketBuy():
    
    shares = int(input("\n\nEnter no of shares you want to buy : "))
    
    while True:
        node = buy.peek()
        shares = shares - node.shares
        
        if shares>0:
            buy.pop()
        elif shares==0:
            buy.pop()
            break
        else:
            node.shares=-shares
            break
        
def marketSell():
    
    shares = int(input("\n\nEnter no of shares you want to Sell : "))
    
    while True:
        node = sell.peek()
        shares = shares - node.shares
        
        if shares>0:
            sell.pop()
        elif shares==0:
            sell.pop()
            break
        else:
            node.shares=-shares
            break

def marketOrder():
    while True:
        
        dupBuy = copy.deepcopy(buy)
        dupSell = copy.deepcopy(sell)
        
        show(dupBuy,dupSell)
        
        print("\n\n\t\t\t\tMARKET ORDER\n\nEnter \n 1. buy\n 2. sell\n 3. Exit\n Enter Your Choice : ", end=" ")
        n = int(input())
        
        if n==1:
            marketBuy()
        elif n==2:
            marketSell()
        else:
            break;

def limitBuy():
    
    shares = int(input("\n\nEnter no of shares you want to buy : "))
    limit = float(input("\n\nEnter limit of share price : "))
    
    while True:
        node = buy.peek()
        if(node.price<=limit):
            shares = shares - node.shares
            
            if shares>0:
                buy.pop()
            elif shares==0:
                buy.pop()
                break
            else:
                node.shares=-shares
                break
        else:
            break;
            
def limitSell():
    
    shares = int(input("\n\nEnter no of shares you want to Sell : "))
    limit = float(input("\n\nEnter limit of share price : "))
    
    while True:
        node = sell.peek()
        if(node.price>=limit):
            shares = shares - node.shares
            
            if shares>0:
                sell.pop()
            elif shares==0:
                sell.pop()
                break
            else:
                node.shares=-shares
                break

def LimitOrder():
    while True:
        
        dupBuy = copy.deepcopy(buy)
        dupSell = copy.deepcopy(sell)
        
        show(dupBuy,dupSell)
        
        print("\n\n\t\t\t\tLIMIT ORDER\n\nEnter \n 1. buy\n 2. sell\n 3. Exit\n Enter Your Choice : ", end=" ")
        n = int(input())
        
        if n==1:
            limitBuy()
        elif n==2:
            limitSell()
        else:
            break;

while True:
    
    print("\n\n\t\t\t\tMAIN PAGE\n\nEnter \n 1. Market Order\n 2. Limit Order\n 3. Exit\n Enter Your Choice : ", end=" ")
    n = int(input())
     
    if n==1:
        marketOrder()
    elif n==2:
        LimitOrder()
    else:
        print("\t\t\t\tSee You Again....")
        break

        
        


        
    
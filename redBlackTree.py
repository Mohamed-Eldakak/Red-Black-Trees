from pickle import TRUE


class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

        #  red = 1
        #  black = 0

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
##############################PART 1 START##############################
#Searching
    def search(self,node,key):
        if node == self.TNULL or key==node.item:
            return node
        if key < node.item:
            return self.search(node.left,key)
        return self.search(node.right,key)
    def searchTree(self, k):
            return self.search(self.root, k)
#Insertion
    def fix_insert(self, z):
        while z.parent.color == 1:  # red
            if z.parent == z.parent.parent.left:
                u = z.parent.parent.right
                if u.color == 1:  # red
                    u.color = 0  # black
                    z.parent.color = 0  # black
                    z.parent.parent.color = 1  # red
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 0  # black
                    z.parent.parent.color = 1  # red
                    self.right_rotate(z.parent.parent)

            else:
                u = z.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.left_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

#Getting Height
    def getHeight(self,z):
        if z.left and z.right:
            return 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        elif z.left:
            return 1 + self.getHeight(z.left)
        elif z.right:
            return 1 + self.getHeight(z.right)
        else:
            return 0
    def height(self):
        if self.root != self.TNULL:
            return self.getHeight(self.root)
        else:
            return 0
#Getting size
    def getSize(self,z):
        if z.left and z.right:
            return 1 + self.getSize(z.left)+self.getSize(z.right)
        elif z.left:
            return 1 + self.getSize(z.left)
        elif z.right:
            return 1 + self.getSize(z.right)
        else:
            return 0
    def size(self):
        if self.root != self.TNULL:
            return self.getSize(self.root)
        else:
            return 0
##############################PART 1 END##############################
##############################PART 2 Start##############################
#Loading
def load(src,rbt):
    f=open(src,"r")
    a=f.read().split("\n")
    f.close()
    for line in a:
        rbt.insert(line.upper())
#printing dictionary size
def printDecSize(rbt):
    print(rbt.size())
#Insert Word
def insertWord(word,rbt):
    a=rbt.searchTree(word)
    if a == rbt.TNULL:
        rbt.insert(word)
    else:
        print("ERROR!!!,Word already exists\n")
#LookUp
def lookUp(word,rbt):
    a=rbt.searchTree(word)
    if a == rbt.TNULL:
        print("NO\n")
    else:
        print("YES\n")
#MENU
def menu(rbt):
    load("F:\EN-US-Dictionary.txt",rbt)
    print("\t\t Red Black Tree\n")
    print("1-Insert a word\n2-Print tree size\n3-Print tree height\n4-Look Up a word")
    resume=True
    while resume:
        x=int(input("Enter an option\n"))
        if x==1:
            word=input("Enter a word\n")
            insertWord(word.upper(),rbt)
        elif x==2:
            printDecSize(rbt)
        elif x==3:
            print(rbt.height())
        elif x==4:
            word=input("Enter a word\n")
            lookUp(word.upper(),rbt)
        response=input("Do you want another operation\nIf yes press y else do anything\n")
        if response == 'y':
             resume=True
        else:
            resume=False
if __name__ == '__main__':
    rbt = RedBlackTree()
    menu(rbt)
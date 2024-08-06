from node import Node

class MyLl:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        iHead = self.head
        while iHead.get_next() is not None:
            iHead = iHead.get_next()
        newNode = Node(data)
        iHead.set_next(newNode)

    def reverse(self):
        if self.head is None :
            return 'Nothing to reverse in an empty list'
        if self.head.get_next() is None:
            return self.head
        current_node = self.head
        next_node = self.head.get_next()
        while next_node is not None:
            temp = next_node.get_next()
            next_node.set_next(current_node)
            current_node = next_node
            next_node = temp
        self.head.set_next(None)
        self.head = current_node
        
        
    def sort_insert(self, data):
        iHead = self.head
        newNode = Node(data)
        if iHead is None:
            self.head = newNode
        else:
            current = self.head
            next_node = current.get_next()
            if data < current.get_data():
                newNode.set_next(current)
                self.head = newNode
                return 
            while next_node is not None:
                if next_node.get_data() < data:
                    current = next_node
                    next_node = current.get_next()
                elif next_node.get_data() >= data:
                    newNode.set_next(next_node)
                    current.set_next(newNode)
                    return
            current.set_next(newNode)


    def delete_node(self, nodeDataToDelete):
        if self.head is None:
            print("Nothing to delete in an empty list")
            return
        else:
            if self.head.get_data() == nodeDataToDelete:
                self.head = self.head.get_next()
                return
            iHead = self.head
            while iHead.get_next().get_data() != nodeDataToDelete:
                iHead = iHead.get_next()
            if iHead.get_next().get_next() is None:
                iHead.set_next(None)
            else:
                iHead.set_next(iHead.get_next().get_next())
            return

    def add_node_after(self, priorNodeData, newNodeData):
        if self.head is None:
            print("No such node found !")
            return
        
        iHead = self.head
        while iHead.get_data() != priorNodeData:
            iHead = iHead.get_next()
        
        if iHead is None:
            print("No such node found !")
        else:
            if iHead.get_next() is None:
                iHead.set_next(Node(newNodeData))
            else:
                iHeadNext = iHead.get_next()
                newNode = Node(newNodeData)
                newNode.set_next(iHeadNext)
                iHead.set_next(newNode)
            print("Inserted ", newNodeData," after ", iHead.get_data())
            return

    def __str__(self):
        result = ""
        iHead = self.head
        while iHead is not None:
            result=result+'->'+str(iHead.get_data())
            iHead=iHead.get_next()
        return result           

mylinkedList = MyLl()
# mylinkedList.add_node(5)
# mylinkedList.add_node(6)
# mylinkedList.add_node(76)
# mylinkedList.add_node(68)
# mylinkedList.add_node(9)
print(mylinkedList)
# mylinkedList.add_node_after(76,100)
# print(mylinkedList)
# mylinkedList.add_node_after(9,10)
# print(mylinkedList)
# mylinkedList.delete_node(68)
# print(mylinkedList)
# mylinkedList.delete_node(5)
# print(mylinkedList)
# print("Reversak")
# mylinkedList.reverse()
# print(mylinkedList)
mylinkedList.sort_insert(11)
mylinkedList.sort_insert(99)
mylinkedList.sort_insert(29)
mylinkedList.sort_insert(2)
mylinkedList.sort_insert(222)
print(mylinkedList)


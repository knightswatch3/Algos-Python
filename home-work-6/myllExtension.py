from myll import MyLl
from node import Node
class MyLlExtension:
    def __init__(self, list1: MyLl, list2: MyLl):
        self.list1 = list1
        self.list2 = list2 
    
    def mergeCommon(self):
        ilist1Head = self.list1.head
        ilist2Head = self.list2.head
        resultList : MyLl = None
        iresultList = None

        while ilist1Head is not None and ilist2Head is not None:
            if ilist1Head.get_data() <= ilist2Head.get_data():
                if resultList is None:
                    resultList = Node(ilist1Head.get_data())
                    iresultList = resultList
                else:
                    iresultList.set_next(Node(ilist1Head.get_data()))
                    iresultList = iresultList.get_next()
                ilist1Head = ilist1Head.get_next()
            elif ilist1Head.get_data() > ilist2Head.get_data():
                if resultList is None:
                    resultList = Node(ilist2Head.get_data())
                    iresultList = resultList
                else:
                    iresultList.set_next(Node(ilist2Head.get_data()))
                    iresultList = iresultList.get_next()
                ilist2Head = ilist2Head.get_next()
        
        while ilist1Head is not None:
            iresultList.set_next(Node(ilist1Head.get_data()))
            ilist1Head = ilist1Head.get_next()
            iresultList = iresultList.get_next()
    
        while ilist2Head is not None:
            iresultList.set_next(Node(ilist2Head.get_data()))
            ilist2Head = ilist2Head.get_next()
            iresultList = iresultList.get_next()
        return resultList.__str__()

    def findCommon(self):
        buffer = {}
        ilist1Head = self.list1.head
        ilist2Head = self.list2.head

        while ilist1Head is not None:
            if ilist1Head.get_data() in buffer.keys():
                value = buffer[ilist1Head.get_data()]
                newValue = value+1
                buffer.update(ilist1Head.get_data(), newValue)
            else:
                buffer[ilist1Head.get_data()]= 1
            ilist1Head = ilist1Head.get_next()
        while ilist2Head is not None:
            if ilist2Head.get_data() in buffer.keys():
                value = buffer[ilist2Head.get_data()]
                newValue = value-1
                buffer[ilist2Head.get_data()] = newValue
            else:
                buffer[ilist2Head.get_data()]= 1
            ilist2Head = ilist2Head.get_next()
        common = [element for element in buffer.keys() if buffer[element] == 0]
        return common



mylinkedList1 = MyLl()
mylinkedList1.add_node(15)
mylinkedList1.add_node(26)
mylinkedList1.add_node(37)
mylinkedList1.add_node(48)
mylinkedList1.add_node(59)

mylinkedList2 = MyLl()
mylinkedList2.add_node(25)
mylinkedList2.add_node(33)
mylinkedList2.add_node(68)
mylinkedList2.add_node(87)
mylinkedList2.add_node(90)

comparator = MyLlExtension(mylinkedList2,mylinkedList1)
# print(comparator.findCommon())
print(comparator.mergeCommon())
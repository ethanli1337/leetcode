class Node:
    def __init__(self, value=0):
        self.value=value
        self.next=None

def to_linked(lst):
    dummy=Node()
    pointer=dummy
    for num in lst:
        pointer.next=Node(num)
        pointer=pointer.next 
    return dummy.next 


def print_ll(node):
    while node:
        print(node.value,end=' -> ')
        node = node.next 
    print('None')

def to_list(node):
    lst=[]
    while node:
        lst.append(node.val)
        node=node.next 
    return lst
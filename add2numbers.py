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
        lst.append(node.value)
        node=node.next 
    return lst

list1=[2,4,3]
list2=[5,6,4]

l1=to_linked(list1)
print_ll(l1)
l2=to_linked(list2)
print_ll(l2)

print(to_list(l1))
print(to_list(l2))

def add_two(l1,l2):
    dummy=Node()
    pointer=dummy
    carry=0 

    while l1 or l2 or carry: 
        val1=l1.value if l1 else 0
        val2=l2.value if l2 else 0 

        total=val1+val2+carry 
        carry=total//10 

        pointer.next=Node(total%10) 
        pointer=pointer.next

        l1=l1.next 
        l2=l2.next 

    return dummy.next

result=add_two(l1,l2)
print_ll(result)
print("List: ", to_list(result))

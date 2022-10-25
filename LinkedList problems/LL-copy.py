# Linked list functions. Solves variety of interview questions

class Node:
    
    def __init__(self, v, n = None):
        self.v = v
        self.n = n
        self.r = None

    @staticmethod
    def print(msg, head):
        print(msg)
        while (head != None):
            if head.r != None:
                print(head.v, head.r.v)
            else:
                print(head.v, "None")
            head = head.n

    @staticmethod
    def copy(head):
        if (head == None):
            return None
        
        new_head = Node(head.v)
        curr_n = new_head
        next_old = head.n
        while next_old:
            node_n = Node(next_old.v)
            curr_n.n = node_n
            next_old = next_old.n
            curr_n = curr_n.n
        return new_head

    @staticmethod
    def excopy(head):
        if head == None:
            return None

        mapping = {}
        new_head = Node(head.v)
        mapping[head] = new_head

        next_old = head.n
        curr = new_head
        while next_old:
            new_node = Node(next_old.v)
            mapping[next_old] = new_node
            curr.n = new_node
            next_old = next_old.n
            curr = curr.n
        
        curr = head
        curr_n = new_head
        while curr != None:
            curr_n.r = mapping[curr.r]      
            curr = curr.n
            curr_n = curr_n.n  

        return new_head

    @staticmethod
    def Nth(n, head):
        if head == None:
            raise BaseException("list does not exist")
        if n == 0:
            return head
        count = 1
        curr = head.n
        while count < n and curr != None :
            count = count + 1
            curr = curr.n
        if curr != None:
            return curr
        raise BaseException("not enough elements: ", count-1, n)

    @staticmethod
    def reverse(head):
        if head == None:
            return None
        prev = None
        curr = head
        while curr != None:
            nxt = curr.n
            curr.n = prev
            prev = curr
            curr = nxt
        return prev

    @staticmethod
    def count(head):
        if head == None:
            return 0
        count = 0
        while head != None:
            count = count+1
            head = head.n
        return count

    @staticmethod
    def is_palindrome(head):
        if head == None:
            return True
        
        count = Node.count(head)
        if count % 2 == 0: # even number of elements
            middle_last = count // 2
            middle_head = middle_head + 1
            middle_elem = None
        else:   # odd number of elements
            middle_last = count // 2
            middle_head = middle_head + 2
            middle_elem = Node.Nth(middle_head + 1)
        


n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
 
n0.n = n1
n0.r = n2

n1.n = n2
n1.r = n0

n2.n = n3
n2.r = n1

n3.n = n4
n3.r = n5

n4.n = n5
n4.r = n4

n5.r = n4

print(Node.Nth(0, n0).v)
print(Node.Nth(1, n0).v)
print(Node.Nth(3, n0).v)
print(Node.Nth(5, n0).v)
# print(Node.Nth(6, n0).v)
# print(Node.Nth(7, n0).v)


Node.print("orig list", n0)
# new_list = list_copy(n0)
# list_traverse("after copy", n0)
# list_traverse("new list", new_list)

new_list = Node.excopy(n0)
Node.print("ex copy", new_list)
print("count new list: ", Node.count(new_list))

Node.print("reverse n0", Node.reverse(Node.copy(n0)))
Node.print("orig list", n0)
Node.print("reverse n5", Node.reverse(Node.copy(n5)))
Node.print("reverse n4", Node.reverse(Node.copy(n4)))
# There is a single linked list with additional pointer to a random node from the same list (or None):
# Let's use the following syntax for the node: [value, next: pointer to #, random: pointer to #]. 
# for example, [1, #2, #4] means that the node with value 1, next is the node #2, random points to node #4
# Copy such list. Test list:

# [1, #2, #3] // random points to #3
# [2, #3, None] // random points no None
# [3, #4, #3] // random points to itself
# [4, None, #2] // random points to #2

# Problem: create a deepcopy function for such list. Estimate the time and memory complexity of the solution

class Node:

    def __init__(self, v, n = None, r = None):
        self.val = v
        self.next = n
        self.rnd = r


    # CPU: O(n), Mem: O(n) solution
    def deepCopy(self):
        map = {}
        map[None] = None # this allows me to get rid of conditions on .next and .rnd

        curr = self
        while curr is not None:
            map[curr] = Node(curr.val)
            curr = curr.next

        curr = self
        while curr is not None:
            map[curr].next = map[curr.next] # if curr.next else None # note that it's needed when map doesn't have None mapping
            map[curr].rnd = map[curr.rnd] # if curr.rnd else None # note that it's needed when map doesn't have None mapping
            curr = curr.next

        return map[self]

    
    def print(self):
        curr = self
        while curr is not None:
            print(
                curr.val, 
                curr.next.val if curr.next else None, 
                curr.rnd.val if curr.rnd else None
            )
            curr = curr.next



root = Node(1, Node(2, Node(3, Node(4))))   # 1 -> 2 -> 3 -> 4

# random linking: 1->3, 2->None, 3->3, 4->2
root.rnd = root.next.next                   # 1st -> 3rd
root.next.rnd = None                        # 2nd -> None
root.next.next.rnd = root.next.next         # 3rd -> self (3rd)
root.next.next.next.rnd = root.next         # 4th -> 2nd

root.print()
print('--- Next output should be line to line the same as prev ---')

root.deepCopy().print()

import collections

def question1(s, t):

    if len(t) > len(s) or len(t) == 0:
        return False

    # collections.defaultdict adds a not found entry to the dict
    string_table = collections.defaultdict(int)
    for char in s:
      string_table[char] += 1

    substring_table = collections.defaultdict(int)
    for char in t:
      substring_table[char] += 1

    for key, value in substring_table.iteritems():
        if not key in string_table or string_table[key] < substring_table[key]:
            return False

    return True


assert question1('udacity', 'ad') == True
assert question1('udacity', 'od') == False
assert question1('udacity', 'yt') == True

print('Tests passed for question1')


def question2(string):
    length = len(string)
    table = [[None for i in range(0, length)] for j in range(0, length)]
    longest_pal = ""


    # Length-1 (trivial) substrings like b, a, n, a, n, a, s
    for i in range(0, length):
        for j in range(i, i+1):
            table[i][j] = True
            longest_pal = return_longest(longest_pal, string[i:j+1])


    # Length-2 (special) substrings like ba, an, na, an, na, as
    for i in range(0, length-1):
        for j in range(i+1, i+2):
            if string[i] == string[j]:
                table[i][j] = True
                longest_pal = return_longest(longest_pal, string[i:j+1])
            else:
                table[i][j] = False


    # Length-3 to Length-N
    for l in range(3, length+1):
        for i in range(0, length-l+1):
            for j in range(i+l-1, i+l):
                if table[i+1][j-1] and string[i] == string[j]:
                    table[i][j] = True
                    longest_pal = return_longest(longest_pal, string[i:j+1])
                else:
                    table[i][j] = False


    return longest_pal


def return_longest(longest_pal, new_pal):
    if len(new_pal) > len(longest_pal):
        return new_pal
    else:
        return longest_pal


assert question2('aa') == 'aa'
assert question2('aaa') == 'aaa'
assert question2('aba') == 'aba'
assert question2('aaaa') == 'aaaa'
assert question2('abba') == 'abba'
assert question2('abcdedcba') == 'abcdedcba'
assert question2('abcdeedcba') == 'abcdeedcba'
assert question2('bananas') == 'anana'
print('Tests passed for question2')

import collections

# Union-Find

parent = dict()
rank = dict()

def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def question3(graph):
    for vertex in graph.keys():
        make_set(vertex)

    minimum_spanning_tree = set()

    edges = get_edges(graph)
    edges.sort()
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            minimum_spanning_tree.add(edge)

    adj = collections.defaultdict(list)
    for weight, vertex1, vertex2 in minimum_spanning_tree:
        adj[vertex1].append((vertex2, weight))
        adj[vertex2].append((vertex1, weight))
    return adj


# Utility function to convert adjacency lists to edge list (dictionary input)
def get_edges(adj):
    edge_list = []
    for vertex, edges in adj.iteritems():
        for edge in edges:
            if vertex < edge[0]:
                edge_list.append((edge[1], vertex, edge[0]))
    return edge_list

graph1 = {
    'A': [('B', 1), ('C', 5), ('D', 3)],
    'B': [('A', 1), ('C', 4), ('D', 2)],
    'C': [('B', 4), ('D', 1)],
    'D': [('A', 3), ('B', 2), ('C', 1)],
}
minimum_spanning_tree1 = {
    'A': [('B', 1)],
    'B': [('A', 1), ('D', 2)],
    'C': [('D', 1)],
    'D': [('C', 1), ('B', 2)]
}

graph2 = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 4)],
    'C': [('A', 5), ('B', 4)]
}

minimum_spanning_tree2 = {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 4)],
    'C': [('B', 4)]
}


graph3 = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 2)],
    'C': [('A', 3), ('B', 4), ('D', 3), ('E', 2), ('F', 6), ('G', 3)],
    'D': [('B', 2), ('C', 3), ('E', 1)],
    'E': [('C', 2), ('D', 1), ('G', 2)],
    'F': [('C', 6), ('G', 4)],
    'G': [('C', 3), ('E', 2), ('F', 4)]
}


minimum_spanning_tree3 = {
    'A': [('B', 2)],
    'B': [('A', 2), ('D', 2)],
    'C': [('E', 2)],
    'D': [('E', 1), ('B', 2)],
    'E': [('D', 1), ('C', 2), ('G', 2)],
    'F': [('G', 4)],
    'G': [('E', 2), ('F', 4)]
}

assert question3(graph1) == minimum_spanning_tree1
assert question3(graph2) == minimum_spanning_tree2
assert question3(graph3) == minimum_spanning_tree3
print('Tests passed for question3')



### Question 4


# A recursive python program to find LCA of two nodes
# n1 and n2

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

    return root.data


def question4(matrix, root, n1, n2):
    bst = BST(root)
    for node in matrix[root]:
        bst.insert(node)

    # insert all elements in row, starting from the last
    for row in reversed(range(len(matrix))):
        for node in matrix[row]:
            bst.insert(node)


    return lca(bst.root, n1, n2)

assert question4([[0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 2) == 1

assert question4([[0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]],
                  3,
                  1,
                  4) == 3

assert question4([[0, 1, 1],
                  [0, 0, 0],
                  [0, 0, 0]],
                  0,
                  1,
                  2) == 1
print('Tests passed for question4')



### Question 5

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if self.head:
            self.length = 1
        else:
            self.length = 0

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
        self.length += 1

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        while current.next and position >= 2:
            current = current.next
            position = position - 1
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        new_element.next = self.get_position(position + 1)
        self.get_position(position - 1).next = new_element
        self.length += 1


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if (current.value == value):
            self.head = current.next
            self.length -= 1
        while current.value != value and current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return
            else:
                current = current.next

def question5(ll, m):
    return ll.get_position(ll.length - m)

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# assert ll.length == 3

assert question5(ll, 0) == e3
assert question5(ll, 1) == e2
assert question5(ll, 2) == e1


ll.insert(e4,3)
assert question5(ll, 1) == e4
assert question5(ll, 0) == e3
assert question5(ll, 2) == e2
print('Tests passed for question5')

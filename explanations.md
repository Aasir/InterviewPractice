## Technical Interview Practice


### Question 1
Given two strings `s` and `t`, determine whether some anagram of `t` is a substring of `s`. For example: if `s = "udacity"` and `t = "ad"`, then the function returns `True`. Your function definition should look like: `question1(s, t)` and return a boolean `True` or `False`.

#### Answer:

In order for `t` to be a substring of `s`, it must be true that all characters (including duplicates) in `t` are contained in `s`. In order to count the number of characters in `s`, then, we should use two hash tables to compare the components of two strings.

Assume that cases are ignored.

Edge case 1: the substring `t` is longer than `s`. This is definitely false.
Edge case 2: the substring `t` is an empty string. Let's assume this is false.
Test case: `t = ad`, `s = Udacity`.

The time complexity of this solution is O(s) because t is smaller than s, and at the worst case s must be traversed completely. The space complexity is O(1) because there are 26 letters in the Englis alphabet.


## Question 2
Given a string `a`, find the longest palindromic substring contained in `a`. Your function definition should look like `question2(a)`, and return a string.


## Longest Palindromic Substring

How to find `anana` in `bananas`?

### Intuitive Solution

#### 1. Write it out

Intuitive, we can just get all substrings in `bananas`:

`b`, `ba`, `ban`, `bana`, `banan`, `banana`, `bananas`,   
`a`, `an`, `ana` (&#10003;), `anan`, `anana` (&#10003;), `ananas`,  
`n`, `na`, `nan` (&#10003;), `nana`, `nanas`,   
`a`, `an`, `ana` (&#10003;), `anas`,    
`n`, `na`, `nas` (&#10003;),    
`a`, `as`,    
`s`  

#### 2. It's complex!

What's the space complexity here? For `bananas` (7 characters), we have to start from each character and get the substrings from there. Starting from `b` we hit each of the 6 letters after that: `ba`, `ban`, `bana`, `banan`, `banana`, `bananas`; then `a`: `an`, `ana`, `anan`, `anana`, `ananas` (5 remaining letters); next, `n`: `na`, `nan`, `nana`, `nanas` (4). There seems to be a pattern here!

Say we have a string of length `n`. Starting from the first letter we hit the second to the last letter, that is, for a total of (n - 1) times. Next, we start from the second character and hit the third to the last letter, that is, for a total of (n - 2) times, so on and so forth, all the way up to starting at the last (nth) letter. Well, we have nothing to hit so it's only one. Let's add them up! (n - 1) + (n - 2) + (n - 3) + ... + 1 = ?

If you haven't taken discrete math, adding consecutive integers can be calculated by

```
(number of things to add) * (first thing to add + last thing to add) / 2
```
, that is,

```
(n - 1) * ((n - 1) + 1) / 2 = (n - 1) * n / 2
= (n^2 - n) / 2
```

Say there are n^2 of these substrings. So the complexity must be O(n^2)...

NOT SO FAST! Although it's easy for us to spot a palindrome, but the computer? It'd have to actually check each character in the substring:

```
// pseudocode
isPalindrome(substring) {
  foreach character in substring {
    // ugh I don't wanna write the actual code right now
  }
}
```

Laziness aside, you see that for each string, we must check all of it's characters regardless. For each substring of length `m`, we must operate on each of its `m` characters. So for any substring, the time complexity is O(m).

So it's O(length(substring)) for 1 substring, and for n^2 substrings of length of at most (n - 1)? Simply, it's `n^2 * n = n^3`.

### Dynamic Programming Solution

The spirit of dynamic programming is accumulating results from previous computation and using the accumulation to do the next step.

What does storing previous results mean here? Well, if we already know that a substring like `an` is not a palindrome, adding a letter on each side doesn't make it one (`bana`), but if it is (e.g., `a`), adding the same letter around would (`nan`). Let's make a table: for `bananas`:

|b| | | | | | |
|:-|:-|:-|:-|:-|:-|:-|
| |**a**| | | | | |
| | |**n**| | | | |
| | | |**a**| | | |
| | | | |**n**| | |
| | | | | |**a**| |
| | | | | | |**s**|

where the diagonal are one-letter substrings that we consider (trivial) palindromes. Now that we have length-1 palindromes, we can use the definition of a palindrome to build length-2 palindromes. For a length-2 substring to be a palindrome, such as `aa`, the two adjacent letters must be the same.

|b| | | | | | |
|:-|:-|:-|:-|:-|:-|:-|
|ba|**a**| | | | | |
| |an|**n**| | | | |
| | |na|**a**| | | |
| | | |an|**n**| | |
| | | | |na|**a**| |
| | | | | |as|**s**|

Then length-3 substrings. From 3 on, we arrive at a general formula to determine if a substring is a palindrome:

Adding the same letter to each side of a palindrome makes the new substring a palindrome.

|**b**| | | | | | |
|:-|:-|:-|:-|:-|:-|:-|
|ba|**a**| | | | | |
|ban|an|**n**| | | | |
| |**ana**|na|**a**| | | |
| | |**nan**|an|**n**| | |
| | | |**ana**|na|**a**| |
| | | | |nas|as|**s**|

For example, for `ban`, although `a` is a palindrome, the side letters `b != a`, so `ban` is not a palindrome. You can visualize this process as
1. looking up to the northeast cell `a` and see if it's a palindrome
1. look up the diagonal cells up `b` and right `n` and see if they equal.

Moving on to length-4:

|**b**| | | | | | |
|:-|:-|:-|:-|:-|:-|:-|
|ba|**a**| | | | | |
|ban|an|**n**| | | | |
|bana|**ana**|na|**a**| | | |
| |anan|**nan**|an|**n**| | |
| | |nana|**ana**|na|**a**| |
| | | |anas|nas|as|**s**|

Length-5:

|**b**| | | | | | |
|:-|:-|:-|:-|:-|:-|:-|
|ba|**a**| | | | | |
|ban|an|**n**| | | | |
|bana|**ana**|na|**a**| | | |
|banan|anan|**nan**|an|**n**| | |
| |**anana**|nana|**ana**|na|**a**| |
| | |nanas|anas|nas|as|**s**|

Length-6:

|**b**| | | | | | |
|:-|:-|:-|:-|:-|:-|:-|
|ba|**a**| | | | | |
|ban|an|**n**| | | | |
|bana|**ana**|na|**a**| | | |
|banan|anan|**nan**|an|**n**| | |
|banana|**anana**|nana|**ana**|na|**a**| |
| |ananas|nanas|anas|nas|as|**s**|

Length-7:

|**b**| | | | | | |
|:-|:-|:-|:-|:-|:-|:-|
|ba|**a**| | | | | |
|ban|an|**n**| | | | |
|bana|**ana**|na|**a**| | | |
|banan|anan|**nan**|an|**n**| | |
|banana|**anana**|nana|**ana**|na|**a**| |
|bananas|ananas|nanas|anas|nas|as|**s**|

For each substring, you no longer check each of its characters. Instead, you look up the previous result (O(1)) and the extra one letter on each side (O(1)), so although there are still O(n^2) substrings to consider, you only have to do O(1) on each. The result is a O(n^2) operation overall, a considerable improvement from O(n^3).


# Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],  
 'B': [('A', 2), ('C', 5)],  
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should be question3(G)

![Alt text](https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    A -> C [label=4, dir=none];
    B -> C [label=3, dir=none];
    C -> D [label=2, dir=none];
    A -> D [label=4, dir=none];
    C -> F [label=2, dir=none];
    B -> G [label=3, dir=none];
    G -> F [label=3, dir=none];
    G -> C [label=4, dir=none];
  }
)


# Answer 3

## 1. Kruskal's Algorithm

Kruskal's finds the next shortest *edge* that doesn't create a cycle.

#### Step 1. Start with the shortest edge

Could be either C-D (2) or C-F (2). Let's pick C-F (2).

![Alt text](https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    C -> F [label=2, dir=none];
  }
)

#### Step 2. Pick the next smallest edge without creating a cycle

Definitely C-D (2).

![Alt text](https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    C -> D [label=2, dir=none];
    C -> F [label=2, dir=none];
  }
)

#### Step 3. Then the next smallest edge without creating a cycle

Could be B-C (3), B-G (3), or G-F (3). Say B-G (3).

![Alt text](https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    C -> D [label=2, dir=none];
    C -> F [label=2, dir=none];
    B -> G [label=3, dir=none];
  }
)

#### Step 4.

Could be B-C (3) or G-F (3). Let's pick B-C (3).

![Alt text](https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    C -> D [label=2, dir=none];
    C -> F [label=2, dir=none];
    B -> C [label=3, dir=none];
    B -> G [label=3, dir=none];
  }
)

#### Step 5.

We can't pick G-F (3) because it'll create a cycle (B-C-G-F). Let's choose among G-C (4), A-D (4), and A-C (4)...BUT wait, G-C would create a cycle G-C-B-G, so let's do A-D (4).

![Alt text](https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    A -> D [label=4, dir=none]
    C -> D [label=2, dir=none];
    C -> F [label=2, dir=none];
    B -> C [label=3, dir=none];
    B -> G [label=3, dir=none];
  }
)


#### Step 6. Done!

Now that we have all 5 (V-1 = 6-1) edges  covered, we are done.

### Kruskal MST in Pseudocode

KRUSKAL(G):
    A = ∅
    foreach v ∈ G.V:
        MAKE-SET(v)
    foreach (u, v) in G.E ordered by weight(u, v), increasing:
        if FIND-SET(u) ≠ FIND-SET(v):
            A = A ∪ {(u, v)}
            UNION(u, v)
    return A

### Kruskal's Complexity

1. Sort the edges by weight at O(E log E) time, E being the number of edges in the graph.
1. Remove an edge with minimum weight at O(1) time (since they're already sorted, just remove the end elements).
1. We need to make sure that this lightest edge doesn't form a cycle in the MST. In order to do that, we use an algorithm to detect cycle: Union and Find, which uses disjoint-set data structure to keep track of which vertices are in which components.
1. We need to perform O(V) operations, as in each iteration we connect a vertex to the spanning tree, two 'find' operations and possibly one union for each edge.
1. Even a simple disjoint-set data structure such as disjoint-set forests with union by rank can perform O(V) operations in O(V log V) time. Thus the total time is O(E log E) = O(E log V).


### Kruskal MST in Python

# Question 4
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],  
           [0, 0, 0, 0, 0],  
           [0, 0, 0, 0, 0],  
           [1, 0, 0, 0, 1],  
           [0, 0, 0, 0, 0]],  
          3,  
          1,  
          4)
and the answer would be 3.

Because we can assume the input is a Binary Search Tree, the time complexity of above solution is O(h) where h is height of tree.


# Question 5
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

```python
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
```

# Answer 5

We can simply calculate the length of the linked list and access the (length - reverse_index)th element, with a time complexity of O(n).

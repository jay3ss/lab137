Title: Building a Linked Stack: Part 2
Author: Jay Ess
Date: 2019-06-12 12:01
Tags: data structure, stack, Python
Status: published


*This is the second article in a multi-part series on the
[stack data structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)).
This series defines what a stack is and what it does, then implements a
link-based stack*

[Earlier]({filename}/articles/building_a_linked_stack_part_3.md), we talked
about what a stack is, what a linked stack is, and then we wrote an interface
for a stack. In this article, we'll start implementing a *singly*-linked stack
starting with implementing a node and then implementing the `is_empty` and `push`
methods using the stack interface that we made.

## A Singly-Linked Stack

Recall that a stack is a data structure that holds data in
<abbr title="Last In First Out">LIFO</abbr> order. When new data is added to
the stack it is added to the top and when data is removed it is removed from
the top. We can also check how many entries are in the stack, check if it's
empty, and get a copy of the top entry too. This is, abstractly, what a stack
is. But, what is a *singly*-linked stack?

A singly-linked stack holds its data as chain of nodes. Each node in the chain
holds the data and a reference to the next node in the chain such as shown in
the figure below (recycled from the previous post). We need this reference to
the next node because it can be anywhere in memory.

<div class="row">
    <div class="col-sm-12">
        <div class="thumbnail">
            <img src="{static}/img/singly-linked-list.svg"
                 class="img-responsive align-center"
                 alt="A link of nodes"
                 title="A link of nodes">
            <div class="caption text-center">
                A link of nodes. Image courtesy of
                <a href="https://commons.wikimedia.org/wiki/File:Singly-linked-list.svg">Lasindi</a>
            </div>
        </div>
    </div>
</div>

### Using the Stack Interface

In the previous article we created an interface for a stack. Now is the time to
use it. The way that we're going to use it is by making our `LinkedStack` class
a sublcass of the `StackInterface` class. By subclassing the `StackInterface`
class, we are forced to live up to the specs that we laid out earlier.

    :::python
    class LinkedStack(StackInterface):
        """Defines a link-based stack"""

And that's it! Now we just have to override the methods declared as abstract
methods in the `StackInterface` class.

### A Node

Previously, we learned that a node is something that holds data and a reference
to the next node. Now, let's see how we can define a node. If you're using
Python 3.7+, then you can use the `dataclasses` module, otherwise, we're going
to define a node using a vanilla Python class.

Since a node holds *data* and a reference to the *next* node, our node class
will have `data` and `next` attributes and we'll implement a dunder method to
make our lives easier.

    :::python
    # node.py
    class Node:
        """A node in a chain"""

        def __init__(self, next=None, data=None):
            self.next = next
            self.data = data

        def __repr__(self):
            return repr(self.data)

The default values of the attributes inherently make sense. If we instantiate a
`node` object without specifying any data or the next node, then those should
be `None`. Next, we'll start connecting multiple nodes together to make the
underlying chain for our linked stack.

### The Top Node

Recall that the chain underlying the linked stack is made up of a series of
nodes, each one pointing to the next. Every chain has a starting point, and in
the linked stack that starting point is called the top node. It serves as a
way to find the other nodes in the stack.

The top node has two possible states:

1. Empty (`None` is how this will be expressed)
2. Occupied and will hold a node

When we instantiate the linked stack it will be empty so the top node will be
`None`. When an entry is pushed onto the stack it gets added to the front and,
therefore, the top will hold the most recently added entry.

When an entry is popped from the stack the that entry comes from the top which
is the top node. As you can see, most of the action is happening at the top of
the chain.

Our `__init__` method ends up being

    :::python
    def __init__(self):
        self.top = None

### The is_empty Method

According to our specifications laid out in the previous post, we need to
implement a method that determines if the stack is empty or not. An easy way to
do that is to check if the top node is `None`

    :::python
    def is_empty(self):
        """Determines if the stack is empty"""
        return self.top is None

### The Push Method

We just found out that the `push` method puts the data at the start of the
chain. How can we implement this? It's actually pretty straightforward, but we
do have to stick to the specification which says that we must accept an entry
parameter and return `True` if the entry was successfully added and return
`False` otherwise. Here's a pseudocode version of what we're going to do

1. Create a new node that we're going to add to the stack (we'll call this
`node`)
2. Check if the stack is empty
    1. If the stack is empty, set the top node to be the node that we just
    created
    2. Otherwise, set `node.next` to the top node
3. Increase the number of items in the stack
4. Return `True`

Here's the Python code

    :::python
    def push(self, entry):
        """Adds a new entry to the top of the stack"""
        node = Node(data=entry)
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node

        return True

## Conclusion

In this article, we learned about nodes and the top node and we also
implemented the `is_empty` and `push` methods. In the next article we'll finish
implementing our `LinkedStack` class by implementing the pop and peek methods.

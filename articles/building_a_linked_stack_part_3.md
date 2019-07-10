Title: Building a Linked Stack: Part 3
Author: Jay Ess
Date: 2019-06-12 12:02
Tags: data structure, stack, Python
Status: published


*This is the third article in a multi-part series on the
[stack data structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)).
This series defines what a stack is and what it does, then implements a
link-based stack*

[Earlier]({filename}/articles/building_a_linked_stack_part_2.md), we learned
about nodes and the top node and we also implemented the `is_empty` and `push`
methods. In the next article we'll finish implementing our `LinkedStack` class
by implementing the pop and peek methods.

## What We Have So Far

So far, we've implemented the `is_empty` and `push` methods. Before we get
going it's a good idea to take a step back and see the big picture. Let's take
a look at what we have at the moment

    :::python
    class LinkedStack(StackInterface):
        """Defines a link-based stack"""
        def __init__(self):
            self.top = None

        def is_empty(self):
            """Determines if the stack is empty"""
            return self.top is None

        def push(self, entry):
            """Adds a new entry to the top of the stack"""
            node = Node(data=entry)
            if self.is_empty():
                self.top = node
            else:
                node.next = self.top
                self.top = node

            return True

### The Pop Method

Now, we're going to implement the `pop` method. The specifications from
[the first article]({filename}/articles/building_a_linked_stack_part_1.md)
show that we need to obey the following behavior

1. `(new Stack()).pop() = False`
2. `(a_stack.push(item)).pop() = True`

This means that if we try to pop an item off of a stack, then `pop` should
return `False` if the stack is empty and `True` otherwise. Pretty
straightforward.

To get this behavior, we should first check if the stack is empty and
immediately return `False` if it is.

    :::python
    def pop(self):
        """Removes the top of the stack"""
        if self.is_empty():
            return False

If the stack *isn't* empty, then we need to remove the first item. A way that
we can do that is to advance the reference to the top node and then return
`True`.

    :::python
    self.top = self.top.next
    return True

Putting this together results in

    :::python
    def pop(self):
        """Removes the top of the stack"""
        if self.is_empty():
            return False

        self.top = self.top.next
        return True

Personally, I'm ok with having more than one `return` in a function. However,
I'm a firm believer in making sure that one's code tells an easy-to-follow
story (just think of the person that has to read your code next is a homicidal
maniac who is triggered by unclear code) and I think that we can tell the `pop`
story a little better.

    :::python
    def pop(self):
        """Removes the top of the stack"""
        can_pop = not self.is_empty()
        if can_pop:
            # Advance the top of the stack to the next node
            self.top = self.top.next

        return can_pop

I believe that the above will give me a slightly longer life.

### The Peek Method

Now, we're going to implement the `peek` method. The specifications from
[the first article]({filename}/articles/building_a_linked_stack_part_1.md)
show that we need to obey the following behavior

1. `(new Stack()).peek() = error`
2. `(a_stack.push(item)).peek() = item`

This means that if we try to peek at an item of a stack, then `peek` should
raise an error if the stack is empty and return the item (without modifying the
stack!) otherwise. Pretty straightforward, but it will require us to create our
own exception.

The [documentation](https://docs.python.org/3/library/exceptions.html#Exception)
states that when creating user-define exceptions we should derive from the
`Exception` class, so that's what we're going to do. We're going to go with a
meaningful name, otherwise we may not live very long.

    :::python
    # exception.py
    class EmptyException(Exception):
        """Exception that's raised when a data structure is empty"""

That's it! Notice how we didn't have to import any modules. Now, let's start
working on `peek`. Just like `pop`, we need to see if the stack is empty, and
if it is, raise an `EmptyException`.

    :::python
    def peek(self):
        """Returns the top of the stack"""
        if self.top is None:
            raise EmptyException("Stack is empty")

        return self.top.data

Notice how we're returning the item with `self.top.data` instead of using
`self.top`. The first bit returns the item while the second returns the node,
which is *not* what we want to do.

### Some Python Bits

Since we're using Python, there's something that we can do to make *using* our
code a little easier. We can implement the
[`__repr__` dunder method](https://docs.python.org/3.7/reference/datamodel.html#object.__repr__).
which will

> compute the “official” string representation of an object.

This is nice to have when using the
<abbr title="Read-Eval-Print Loop">REPL</abbr>, which we'll be using later.

    :::python
    def __repr__(self):
        nodes = []
        curr = self.top
        while curr:
            nodes.append(repr(curr))
            curr = curr.next

        return '[' + ', '.join(nodes) + ']'


### Putting it All Together

Our complete implementation of the linked stack is as follows

    :::python
    # interface.py
    import abc


    class StackInterface(abc.ABC):
        """An abstract base class that defines a stack"""
        @abc.abstractmethod
        def is_empty(self):
            """Determines if the stack is empty"""

        @abc.abstractmethod
        def peek(self):
            """Returns the top of the stack"""

        @abc.abstractmethod
        def pop(self):
            """Removes the top of the stack"""

        @abc.abstractmethod
        def push(self, entry):
            """Adds data to the top of the stack"""

        @abc.abstractmethod
        def push(self, entry):
            """Adds a new entry to the top of the stack"""


    # stack.py
    from exception import EmptyException
    from interface import StackInterface
    from node import Node


    class LinkedStack(StackInterface):
        """Defines a link-based stack"""
        def __init__(self):
            self.top = None

        def is_empty(self):
            """Determines if the stack is empty"""
            return self.top is None

        def peek(self):
            """Returns the top of the stack"""
            if self.is_empty():
                raise EmptyException("Stack is empty")

            return self.top.data

        def pop(self):
            """Removes the top of the stack"""
            can_pop = not self.is_empty()
            if can_pop:
                # Advance the top of the stack to the next node
                self.top = self.top.next

            return can_pop

        def push(self, entry):
            """Adds a new entry to the top of the stack"""
            node = Node(data=entry)
            if not self.top:
                self.top = node
            else:
                node.next = self.top
                self.top = node

            return True

        def __repr__(self):
            nodes = []
            curr = self.top
            while curr:
                nodes.append(repr(curr))
                curr = curr.next

            return '[' + ', '.join(nodes) + ']'


    # node.py
    class Node:
        """A node in a chain"""

        def __init__(self, next=None, data=None):
            self.next = next
            self.data = data

        def __repr__(self):
            return repr(self.data)


    # exception.py
    class EmptyException(Exception):
        """Exception that's raised when a data structure is empty"""

## Using the Stack

Let's play around with the stack a little using the REPL (I prefer IPython). We
can make sure we've met our specifications. As a recap, here they are

1. `(new Stack()).isEmpty() = True`
2. `(new Stack()).pop() = False`
3. `(new Stack()).peek() = error`
4. `(a_stack.push(item)).isEmpty() = False`
5. `(a_stack.push(item)).peek() = item`
6. `(a_stack.push(item)).pop() = True`

So, now let's fire up that REPL and test out our shiny stack.

```python
In [1]: stack = LinkedStack()

In [2]: stack.is_empty()
Out[2]: True

In [3]: stack.pop()
Out[3]: False

In [4]: stack.peek()

---------------------------------------------------------------------------
EmptyException                            Traceback (most recent call last)
<ipython-input-7-1e84c3c721a3> in <module>
----> 1 stack.peek()

<ipython-input-4-6a54ea098db0> in peek(self)
     11         """Returns the top of the stack"""
     12         if self.top is None:
---> 13             raise EmptyException("Stack is empty")
     14
     15         return self.top.data

EmptyException: Stack is empty

In [5]: stack.pop()
Out[5]: False

In [6]: stack.push(1)
Out[6]: True

In [7]: stack.is_empty()
Out[7]: False

In [7]: stack.push(2)
Out[7]: True

In [8]: stack.peek()
Out[8]: 2

In [9]: stack.pop()
Out[9]: True

In [10]: stack.peek()
Out[1]: 1
```

We can see that our stack implements the specifications and works quite nicely.
Although this may not be the best (e.g., most efficient) implementation, it
does implement the specifications and in a manner that is clear and tells a
nice story (i.e., we won't get killed with this code, hopefully).

## Conclusion

In this article, we learned about nodes and the top node and we also
implemented the `is_empty` and `push` methods. In the next article we'll finish
implementing our `LinkedStack` class by implementing the pop and peek methods.

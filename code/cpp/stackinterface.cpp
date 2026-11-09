#ifndef STACK_INTERFACE_H
#define STACK_INTERFACE_H

template<class T>
class StackInterface
{
public:
    virtual ~StackInterface() {}

    /* Checks if the stack is empty
    @return True if the stack is empty, false otherwise */
    virtual bool isEmpty() const = 0;

    /* Returns the top of the stack
    @precondition The stack isn't empty
    @return The entry at the top of the stack */
    virtual T peek() = const 0;

    /* Removes the entry from the top of the stack
    @postcondition The entry at the top of stack will be removed, if possible
    @return True if removal was successful, false otherwise */
    virtual bool pop() = 0;

    /* Adds an entry to the top of the stack
    @postcondition The entry will be added to the top of stack, if possible
    @return True if addition was successful, false otherwise */
    virtual bool push() = 0;
};

#endif // STACK_INTERFACE_H

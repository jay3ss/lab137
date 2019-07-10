Title: C++: Simple Structs Usage
Author: Jay Ess
Date: 2019-06-19 12:00
Tags: C++, struct, beginner
Status: published

Similar to arrays, structs allow you to hold a group of data. structs allow
you to group together related members that would be awkwardly expressed as
multiple arrays (e.g., the x- and y-coordinates of a pixel or the name,
address, and telephone number of a person) into one convenient unit.

Not only do structs group data, they're also easy to define and use.

## Declaring a Struct

The example below shows the semantics of declaring a struct. Just replace
whatever is inside of the `<...>` with the appropriate text.

    :::cpp
    struct <tag>
    {
        <data-type> <member-name>;
        // more declarations...
    };  // notice the semicolon

For example

- `<tag>`: is the name of the struct, so `Student`
- `<data-type>`: is the data type of the member (variable), so `int`
- `<member-name>`: is the name of the member (variable), so `id`

Put it all together (plus some additional members) and we have

    :::cpp
    struct Student
    {
        int id;             // Student's ID number
        std::string name;   // Student's name
        float gpa;          // Student's GPA
        int gradeLevel;     // Students current grade level (e.g., 11)
    };

Notice how I left the tag (`Student`) capitalized? I like to do that so when
I'm reading my code I can easily spot the declaration of a struct. This
`Student` struct is basically a new data type and we can use it as such.

## Defining a Struct Variable

It's no different defining a variable of type `Student` than it is of `int`
or `double`. For example,

    :::cpp
    Student student;

We just declared a variable named `student` with the type of `Student`. Simple!

### Initialization Lists

You can also use an initialization list to when defining a struct.

    :::cpp
    Student student = {5678, "A. Student", 4.0, 12};

You don't have to provide an initializer for each member of the struct, but you
can't skip any either. That means that if you skip initializing one member then
you must leave all of the members that follow it uninitialized as well.

    :::cpp
    Student stu1 = {6789, "Billy"}; // works
    Student stu2 = {6789, 4.0, 12}; // does not work, skipped "name"

## Using a Struct

We use the dot (`.`) operator to set and access the members of a struct like
below

    :::cpp
    Student johnny;
    johnny.id = 1234;
    johnny.name = "Johnny B. Goode";
    johnny.gpa = 1.1;
    johnny.gradeLevel = 7;

    // Student johnny = {1234, "Johnny B. Goode", 1.1, 7} // also works

    std::cout << "ID:\t\t" << johnny.id << "\n"
              << "Name:\t\t" << johnny.name << "\n"
              << "GPA:\t\t" << johnny.gpa << "\n"
              << "Grade Level:\t" << johnny.gradeLevel << "\n";

After we compile and run this, the output will be

```
ID:		        1234
Name:		    Johnny B. Goode
GPA:		    1.1
Grade Level:	7
```

This may seem like a lot of work, but its usefulness becomes immediately clear
when we have multiple students.

## Array of Structs

Instead of having to declare multiple arrays (or vectors) or variables we can
declare an array (or vector) of type `Student` and use a loop to set or access
the members of each element of the array (or vector). For example

    :::cpp
    // const int NUMBER_OF_STUDENTS = <pick a number>;
    Student students[NUMBER_OF_STUDENTS];

    // Set the member for each element of the array
    for (int i = 0; i < NUMBER_OF_STUDENTS; i++)
    {
        std::cout << "Enter student ID: ";
        std::cin >> students[i].id;
        std::cin.ignore();

        std::cout << "Enter student name: ";
        std::getline(std::cin, students[i].name);

        std::cout << "Enter student GPA: ";
        std::cin >> students[i].gpa;

        std::cout << "Enter student grade level: ";
        std::cin >> students[i].gradeLevel;

        std::cout << std::endl;
    }

    // Print out the member for each element of the array
    for (int i = 0; i < NUMBER_OF_STUDENTS; i++)
    {
        std::cout << "Student #" << (i + 1) << "\n"
                  << "ID:\t\t" << students[i].id << "\n"
                  << "Name:\t\t" << students[i].name << "\n"
                  << "GPA:\t\t" << students[i].gpa << "\n"
                  << "Grade Level:\t" << students[i].gradeLevel << "\n";

        std::cout << std::endl;
    }

## Pointer to Structs

You define a pointer to a struct in the exact same way that you'd define a
pointer to any other data type

    :::cpp
    Student* student;

Using a pointer to a struct is a *little* bit more involved. If you need to
use a pointer to a struct then you have a couple of options with one of them
being *much* easier and the preferred way.

### Dereferencing

I'm going to start with the awkward notation first. To dereference a pointer
you use the star (`*`) operator just like any other pointer. However, if you
want to access the member of a pointer to a struct you'd *think* that the `*`
operator would be all that's necessary

    :::cpp
    std::cout << *student.name;

The above should print out the string that's at `name`, right? Wrong! You're
actually trying to dereference `student.name` *not* `student`. The `.`
operator has a higher precedence than `*` so you need to use parentheses to
give the `*` higher precedence.

    :::cpp
    std::cout << (*student).name;

**Now** we'll print out the `name`. This is very awkward and can actually be
confusing too. This is why the arrow notation is better.

### Arrow Notation

Instead of using the clumsy dereferencing notation we're going to prefer using
the arrow operator (`->`). As you'll see, it's very similar to the dot notation

    :::cpp
    std::cout << student->name;

This is much easier on the eyes.

## Array Members

Structs can have an array as a member, but you have to take care of how you
define them. Member arrays must have their lengths defined in the definition of
the struct *unless* it's the last member of the struct
<a href="#references">[1]</a>. For example,

    :::cpp
    // Will compile, flexible length member array declared
    // as last member
    struct Testing1
    {
        int number;
        int numbers[];
    };

    // Won't compile, member array length not declared
    struct Testing2
    {
        int numbers[];
        int number;
    }

    // Will compile, member array length declared
    struct Testing3
    {
        int numbers[5];
        int number;
    };

To use an array member, you use it just like any other array

    :::cpp
    Testing3 testing;
    for (int i = 0; i < 5; i++)
    {
        testing.numbers[i] = i;
    }

## Nested Structs

You can also have nested structs (one within another). This is done in the
same manner that you'd define any other member. For example, we can create a
new struct that holds a US address

    :::cpp
    struct Address
    {
        std::string street;
        std::string city;
        int zipcode;
        std::string state;
    };

and now we can update our `Student` struct to include the `Address` struct

    :::cpp
    struct Student
    {
        int id;
        std::string name;
        float gpa;
        int gradeLevel;
        Address address
    };

To access member struct, we use the dot notation twice

    :::cpp
    Student student;
    student.address.street = "123 Fake St.";
    student.address.city = "Springfield";
    student.address.zipcode = 97475;
    student.address.state = "OR";

Or, if we're using a pointer to a struct we use the arrow and dot operators
together

    :::cpp
    Student* student;
    student->address.street = "123 Fake St.";
    student->address.city = "Springfield";
    student->address.zipcode = 97475;
    student->address.state = "OR";

## Conclusion

We've learned what a struct is, what it's used for, and different ways of using
structs. Now, go on and make use of this knowledge to create some great
programs!

## <a name="references"></a>References

1. [Starting out with C++: From Control Structure Through Objects, 8th Edition](https://www.pearson.com/us/higher-education/product/Gaddis-Starting-Out-with-C-from-Control-Structures-to-Objects-8th-Edition/9780133769395.html)
2. [Structures in C++ - Tutorial - Cprogramming.com](https://www.cprogramming.com/tutorial/lesson7.html)

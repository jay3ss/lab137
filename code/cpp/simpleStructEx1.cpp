#include <iostream>
#include <string>
#include <vector>

struct Student
{
    int id;             // Student's ID number
    std::string name;   // Student's name
    float gpa;          // Student's GPA
    int gradeLevel;     // Students current grade level (e.g., 11)
};

int main()
{
    Student johnny;
    johnny.id = 1234;
    johnny.name = "Johnny B. Goode";
    johnny.gpa = 1.1;
    johnny.gradeLevel = 7;

    std::cout << "ID:\t\t" << johnny.id << "\n"
              << "Name:\t\t" << johnny.name << "\n"
              << "GPA:\t\t" << johnny.gpa << "\n"
              << "Grade Level:\t" << johnny.gradeLevel << "\n";

    const int NUMBER_OF_STUDENTS = 5;
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

    Student* stu;

    return 0;
}

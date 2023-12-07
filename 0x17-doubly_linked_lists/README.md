Project Title: 0x17. C - Doubly Linked Lists
Description
This project involves the implementation of doubly linked lists in the C programming language. The provided data structure for this project is a doubly linked list node, defined as follows:

c
Copy code
/**
 * struct dlistint_s - doubly linked list
 * @n: integer
 * @prev: points to the previous node
 * @next: points to the next node
 *
 * Description: doubly linked list node structure
 * 
 */
typedef struct dlistint_s
{
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;
Requirements
General
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files should end with a new line
A README.md file, at the root of the folder of the project is mandatory
Code should follow the Betty style. It will be checked using betty-style.pl and betty-doc.pl
Not allowed to use global variables
No more than 5 functions per file
The only C standard library functions allowed are malloc, free, printf, and exit
Use provided main.c files for testing functions, but don’t push them to the repo
Prototypes of all functions should be included in the header file named lists.h
Don't forget to push your header file
All header files should be include guarded
Project Files
0-print_dlistint.c: Function that prints all the elements of a doubly linked list of integers.
1-dlistint_len.c: Function that returns the number of elements in a doubly linked list of integers

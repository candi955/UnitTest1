# UnitTest1
# This project was completed for my master's course MS549 assignment: Test Driven Development with the University of Advancing Technology. 
# I had the choice to pick a programming language to complete the project with, and chose Python.  

# The following were instructions given:

# To test and handle:
# 1) Pop and Peek from an empty stack (no values are stored on the stack)
# 2) Push to a stack that is full (no space is left in the array)

# Further instructions included:
# 1)Begin by coding a test that initializes and constructs a Stack object. Note, this test will fail because we have not coded the Stack constructor. 
# 2)Create the Stack class and a constructor for the Stack class. Your test from step 1 should now pass.
# 3)Commit the current state of your code to your Versioning Control system with a short description of the progress that has been made.
# 4)Create a test for the Push function of the stack. This test will fail at this point.
# 5)Write the Push function of the Stack class. Your Push function test should now pass.
# 6)Commit the current state of your code to your Versioning Control system.

# I created a class TestStack(), with the functions _unitTestStackEven_() and _unitTestStackFail_() to show a test concerning modulo %2.
# It proved whether a number in a stack could be shown as even or odd utilizing the resulting remainder of a programmed equation. 

# I next created a class NumStack() with the functions _intStack_, _popStack_, and _peekStack_.  These were used to fulfill the rest
# of the requirements of the project, concerning showing and testing aspects of append() (push), pop(), and peek() (had to use iter tools
# to complete the peek() function). 

# There is no user-input required in this program, as the user is just guided through the process via reading the program print explanations
# and the following results of the various tests of assignment requirements.  

# All of the classes are assigned variables in the final program function of main(), and then all other class functions are implemented 
# utilizing the assigned class variables. 

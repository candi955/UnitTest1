# MS549 assignment: Test Driven Development
# Github repository can be found at: https://github.com/candi955/UnitTest1

# References:

# for Unit Test: https://www.jetbrains.com/pycharm/guide/tips/run-single-test/
# for peek: https://www.jetbrains.com/pycharm/guide/tips/run-single-test/
# https://stackoverflow.com/questions/46801747/peek-stack-in-python-3
# reference for peek() performance on data structure utilizing iter tools (couldn't get .peek() to work)
# https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator
# for stacks and queues, push and pop:
# https://www.geeksforgeeks.org/using-list-stack-queues-python/
# https://dbader.org/blog/stacks-in-python
# for pop() performance on data structure and from empty list: https://dbader.org/blog/stacks-in-python
# for sets and frozensets: https://www.python-course.eu/sets_frozensets.php
# for modulo: https://www.java67.com/2014/11/modulo-or-remainder-operator-in-java.html
# https://medium.com/programminginpython-com/python-program-to-find-whether-an-integer-is-even-or-odd-number-a028da555922
# for exception code: https://stackoverflow.com/questions/41596810/how-to-print-an-exception-in-python-3

# 1/9/2020 @ 16:32pm - I have begun to practice how the concept of peek works, as
# I believe I understand the concepts of push (in python appears to be append() function) and
# pop (appears in python is pop() function)
# 1/9/2020 @ 20:30pm - I took several hours of broken breaks in between coding for family matters, but in between successfully
# created a Github repository called UnitTest on my candi955 Github repository page (https://github.com/candi955/UnitTest)
# which I have at this time set to Public, and have pushed two commits from Pycharm to the repository.  I have also
# double checked that version control is working in Git under the Pycharm VCS menu.  At this time my success and fail
# Unit tests under the class TestStack(), functions unitTestStackEven() and unitTestStackFail() appear to be functioning
# properly (when the program equation result is an even number, a message displays stating the test was successful, and
# when the result is odd, a message displays stating the test is unsuccessful).
# I placed a reference in the code under both TestStack() class functions showing the how I came up with the idea for
# the equation I utilized.  I also placed the reference in the formerly mentioned project references above these notes.
# I have begun to create the actual stack under class NumStack(), which I plan to create an array to demonstrate the
# concepts of push, pop, and peek on the First In Last Out (FILO) stack in array format.
# 1/10/2020 @ 19:30pm - I checked on the assignment to ensure I was following the instructions.  It stated to ensure that
# the following was tested and handled properly:
# 1) Pop and Peek from an empty stack (no values are stored on the stack)
# 2) Push to a stack that is full (no space is left in the array)
# In order to accomplish this, I began following the reference https://dbader.org/blog/stacks-in-python to create a new
# class NumStack() and function _intStack_ to show an empty data structure, and then show the concept of push utilizing append().
# It appears I might perform some of the steps out of order, but I am attempting to complete all steps per my best
# understanding of their functions as I learn.
# 1/10/2020 @ 19:54pm - I have completed the class NumStack() and function _intStack_ to show an empty data structure, and then
# show the concept of push utilizing append(). Next I plan on displaying how to pop the numbers from the data structure and then
# the failed function of popping from an empty data structure.  I am first going to attempt displaying this concept, and plan to
# attempt peek later after learning how to pop the numbers in the stack.
# I also am making another commit on Git to my Github repository.
# 1/11/2020 @ 18:54pm - I have begun programming again, and this time, due to having trouble running the code after the
# pop error, I'm going to place information in the print statement as guidance to the user of the program.
# 1/11/2020 @ 19:17pm I finished my example of the pop() function performance on an empty data structure, class NumStack(),
# function _popStack_(), and placed references in the beginning of this documentation as well as before and after the
# written code for that section.  I am also performing another git commit and Github push.
# 1/11/2020 @ 20:47 - I pushed the project to a new Github repository and called it UnitTest1:
# https://github.com/candi955/UnitTest1
# Next I am going to work on peek() from an empty stack.
# 1/11/2020 @ 22:39pm - I have successfully completed executing tests of the peek function with a stack data structure
# made of four numbers, and then after the pop() function implemented on a new set of only the three latter numbers.
# I then created an empty data structure, and proved that the peek() function will not show any result on implementation
# to an empty data structure.
# For the peek() function to work in Pycharm utilizing Python3, I had to use iter tools (I couldn't get .peek() to
# work). The reference for this functionality that I utilized is shown at the website:
# https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator
# 1/11/2019 @ 22:55pm - I believe to the best of my knowledge that I have fully completed all of the requirements of
# this project, and will begin to video the project and submit.  It appears to have taken me approximately eight hours
# to complete, totaling research, breaks, documentation, and the utilization and check on git and Github repository,
# commits, and functionality of storage.


class TestStack():
    def _unitTestStackEven_(self):
        testNum = int

        # reference for the idea of creating the below variable and equation that is intended to result in an even number:
        # https://medium.com/programminginpython-com/python-program-to-find-whether-an-integer-is-even-or-odd-number-a028da555922
        if testNum(4) % 2 == 0:
            return print("Test is successful!")
        else:
            return print("Test is not successful")

    def _unitTestStackFail_(self):
        testNum = int

        # reference for the idea of creating the below variable and equation that is intended to result in an even number:
        # https://medium.com/programminginpython-com/python-program-to-find-whether-an-integer-is-even-or-odd-number-a028da555922
        if testNum(3) % 2 == 0:
            return print("Test is successful!")
        else:
            return print("Test is not successful")

TestStack()

class NumStack():
    def _intStack_(self):
        # reference for append to stack: https://dbader.org/blog/stacks-in-python

        intStackLIFO = []

        intStackLIFO.append(2)
        intStackLIFO.append(4)

        print("\n\nBelow I have added two numbers utilizing push(append) to the iStackLIFO stack:")
        print(intStackLIFO)
        print("\n")



        intStackLIFO.append(6)
        intStackLIFO.append(7)

        print("Below I have added two more numbers (four numbers total) utilizing push(append) to the iStackLIFO stack:")
        print(intStackLIFO)

        # reference for append to stack: https://dbader.org/blog/stacks-in-python

    def _popStack_(self):
        intStackLIFO = []

        # reference for pop() performance on data structure and from empty list:
        # https://dbader.org/blog/stacks-in-python
        print("I will now demonstrate the results of attempting to utilize the pop function on an empty stack " +
              "LIFO data structure.")

        print("Data structure before pop (is empty):")
        print(intStackLIFO)


        while True:
            try:

                # attempting the pop function from and empty stack data structure
                intStackLIFO.pop()

                # reference for pop() performance on data structure and from empty list:
                # https://dbader.org/blog/stacks-in-python

            # reference for exception code: https://stackoverflow.com/questions/41596810/how-to-print-an-exception-in-python-3
            except Exception as ex:
                print("An error has occurred upon attempting to execute this request (performing pop() on an empty " +
                "data structure):")
                print(ex)
                break
            # reference for exception code: https://stackoverflow.com/questions/41596810/how-to-print-an-exception-in-python-3

            else:
                break

         #reference for append to stack: https://dbader.org/blog/stacks-in-python

    def _peekStack_(self):

        nextIntStackLIFO = []

        # reference for peek() performance on data structure utilizing iter tools (couldn't get .peek() to work)
        # first example will be with a data structure of four numbers
        # https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator
        print("Next I will demonstrate the results of attempting to utilize the peek function on a stack " +
              "LIFO data structure.")

        nextIntStackLIFO.append(2)
        nextIntStackLIFO.append(5)
        nextIntStackLIFO.append(9)
        nextIntStackLIFO.append(10)

        print("I am going to first demonstrate peek() with a stack data structure containing four integers:")
        print("Following is the created stack data structure after push of numbers, to create a stack to give " +
              "examples and test the peek function:")
        print(nextIntStackLIFO)
        print("\n")

        # reference for peek() performance on data structure utilizing iter tools (couldn't get .peek() to work)
        # https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator

        peekStack = iter(nextIntStackLIFO)
        peek = peekStack.__next__()

        print("Integer that shows as result upon initialization of the peek() function. It is 'peeking' " +
              "at the first number in the stack:")
        print(list(iter([peek, peekStack])))
        print("\n")

        # reference for peek() performance on data structure utilizing iter tools (couldn't get .peek() to work)
        # https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator


        nextIntStackLIFO.pop(0)

        print("Data structure after pop() of first number on list.  I will use this new and updated data structure,\n " +
              "made of three numbers, to check that the peek() function is working properly with the new set of data:")
        print(nextIntStackLIFO)
        print("\n")

        print("Integer that shows as result upon initialization of the peek() function, after pop() function removed " +
        "the initial number 2 from the data structure:")

        # reference for peek() performance on data structure utilizing iter tools (couldn't get .peek() to work)
        # I have 'popped' the initial number off of the data structure, to show a peek() function on an
        # adjusted dataset of three numbers.
        # https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator

        peekStack = iter(nextIntStackLIFO)
        peek = peekStack.__next__()
        print(list(iter([peek, peekStack])))
        print("\n")

        # reference for peek() performance on data structure utilizing iter tools (couldn't get .peek() to work)
        # https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator

        print("Next I will attempt to implement the peek() function on an empty data structure.")
        print("Please see the empty stack data structure as follows:")

        emptyDataStructure = []
        print(emptyDataStructure)

        while True:
            try:

                # attempting the peek() function from and empty stack data structure
                # reference for peek() performance on data structure utilizing iter tools (couldn't get .peek() to work)
                # https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator

                peekEmptyStack = iter(emptyDataStructure)
                peek = peekEmptyStack.__next__()
                print(list(iter([peek, peekEmptyStack])))

                # reference for peek() performance on data structure utilizing iter tools (couldn't get .peek() to work)
                # https://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-peek-in-a-python-generator

            # reference for exception code: https://stackoverflow.com/questions/41596810/how-to-print-an-exception-in-python-3
            except Exception as ex:
                print("An error has occurred upon attempting to execute this request (performing peek() on an empty " +
                "data structure).")
                print(ex)
                break
            # reference for exception code: https://stackoverflow.com/questions/41596810/how-to-print-an-exception-in-python-3

            else:
                break


NumStack()

#_____________________________________________________________________________________________________________________
def main():

    test = TestStack()
    intStackLIFO_orig = NumStack()

    print("\nTest results for the even number of 4 (should be successful if program functioning properly):")
    test._unitTestStackEven_()


    print("\nTest results for the odd number of 3 (should fail if program functioning properly):")
    test._unitTestStackFail_()


    intStackLIFO_orig._intStack_()
    print("\n")

    intStackLIFO_orig._popStack_()
    print("\n")

    intStackLIFO_orig._peekStack_()
    print("\n")

main()









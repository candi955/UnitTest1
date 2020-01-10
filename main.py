# MS549 assignment: Test Driven Development

# References:

# for Unit Test: https://www.jetbrains.com/pycharm/guide/tips/run-single-test/
# for peek: https://www.jetbrains.com/pycharm/guide/tips/run-single-test/
# https://stackoverflow.com/questions/46801747/peek-stack-in-python-3
# for stacks and queues, push and pop:
# https://www.geeksforgeeks.org/using-list-stack-queues-python/
# for sets and frozensets: https://www.python-course.eu/sets_frozensets.php
# for modulo: https://www.java67.com/2014/11/modulo-or-remainder-operator-in-java.html
# https://medium.com/programminginpython-com/python-program-to-find-whether-an-integer-is-even-or-odd-number-a028da555922

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

class TestStack():
    def unitTestStackEven(self):
        testNum = int

        # reference for the idea of creating the below variable and equation that is intended to result in an even number:
        # https://medium.com/programminginpython-com/python-program-to-find-whether-an-integer-is-even-or-odd-number-a028da555922
        if testNum(4) % 2 == 0:
            return print("Test is successful!")
        else:
            return print("Test is not successful")

    def unitTestStackFail(self):
        testNum = int

        # reference for the idea of creating the below variable and equation that is intended to result in an even number:
        # https://medium.com/programminginpython-com/python-program-to-find-whether-an-integer-is-even-or-odd-number-a028da555922
        if testNum(3) % 2 == 0:
            return print("Test is successful!")
        else:
            return print("Test is not successful")

TestStack()

class NumStack():





def main():

    test = TestStack()

    print("\nTest results for the even number of 4 (should be successful if program functioning properly):")
    test.unitTestStackEven()
    print("\n")

    print("\nTest results for the even number of 3 (should fail if program functioning properly):")
    test.unitTestStackFail()
    print("\n")

main()









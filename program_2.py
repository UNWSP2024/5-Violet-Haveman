# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

def math_quiz(n1, n2):
    answer = n1+n2
    print ("What is the sum of these two numbers:")
    print (n1, "+", n2)
number_1 = 129
number_2 = 303
math_quiz(number_1, number_2)
guess = int(input("Answer: "))
if guess != 432:
    print ("Incorrect")
    print ("Correct Answer: 432")
else:
    print ("Correct!")

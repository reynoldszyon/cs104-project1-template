# Knowledge-Based Quiz
# Author: Zy'on Reynolds
# A quiz/questionnaire program built for CS 104 Project 1

# TODO: Define your variables here.
name = input ("What is your name?")
score = 0
total_questions = 5
# TODO: Print a welcome message introducing your program.
print()
print("Welcome to the Knowledge-Based Quiz on Music," + name + "!")
print("Answer each question by entering the number of your choice.")
print()

# TODO: Write your questions and conditional logic here.
# Follow the outline you planned in your README.

# Quesiton 1
print("Question 1: Which artist has her own self-titled album?")
print("1. Cardi B")
print("2. SZA")
print("3. Beyoncé") 
print("4. Alicia Keys")

answer1 = int(input("Enter your answer: "))

if answer1 == 3:
    print("Correct! Beyoncé is the correct answer.")
    score = score + 1
else:
    print("Incorrect. The correct answer is 3, Beyoncé.")

print ()

# Question 2
print("Question 2: Who released the hit song 'Love on the Brain'?")
print("1. TLC")
print("2. H.E.R.")
print("3. Ari Lennox")
print("4. Rihanna")

answer2 = int(input("Enter your answer: "))

# TODO: Display the final results to the user.

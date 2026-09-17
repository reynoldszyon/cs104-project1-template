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

if answer2 == 4:
    print("Correct! Rihanna released 'Love on the Brain'.")
    score = score + 1
else:
    print("Incorrect. The correct answer is 4, Rihanna.")

print()

#Question 3
print("Question 3: Which artist released the song 'Heartbreak Anniversary'?")
print("1. Daniel Caesar")
print("2. Giveon")
print("3. Lucky Daye")
print("4. Brent Faiyaz")

answer3 = int(input("Enter your answer: "))

if answer3 == 2:
    print("Correct! Giveon is the correct answer.")
    score = score + 1
else:
    print("Incorrect. The correct answer is 2, Giveon.")

print()

# Question 4
print("Question 4: Which artist released the album Confessions in 2004?")
print("1. Usher")
print("2. Chris Brown")
print("3. Trey Songz")
print("4. Ne-Yo")

answer4 = int(input("Enter your answer: "))

if answer4 == 1:
    print("Correct! Usher released the album Confessions in 2004.")
    score = score + 1
else:
    print("Incorrect. The correct answer is 1, Usher.")

print()

# Question 5
print("Question 5: Who released the song 'Trip'?")
print("1. Summer Walker")
print("2. Kwn")
print("3. Adele")
print("4. Ella Mai")

answer5 = int(input("Enter your answer: "))

if answer5 == 4:
    print("Correct! Ella Mai is the correct answer.")
    score = score + 1
# TODO: Display the final results to the user.

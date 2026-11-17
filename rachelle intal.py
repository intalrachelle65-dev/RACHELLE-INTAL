print("==========================================")
print("          PYTHON TUTORIAL PROGRAM   ")
print("       START YOUR LEARNING PYTHON HERE    ")
print("==========================================")

name = input("\nEnter your name: ")

if name == "":
    print("INVALID NAME")
    exit()

print("Hello!", name)

mini_score = 0
surprise_score = 0

# HIDDEN MINI QUIZ
print("\n=====================================================")
print("             MINI QUIZ")
print("=======================================================")
print("Before starting, answer these 5 questions first!", name)

score = 0

# IDENTIFICATION

print("\n--- IDENTIFICATION ---")

print("\n1. Who created Python Programming?")
answer = input("Your answer: ").lower()

if answer == "guido van rossum":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer: guido van rossum")

print("\n2. What data type is used for whole numbers?")
answer = input("Your answer: ").lower()

if answer == "int":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer: int")

print("\n3. What loop repeats while a condition is True?")
answer = input("Your answer: ").lower()

if answer == "while loop":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer: while loop")

    # MULTIPLE CHOICE

print("\n--- MULTIPLE CHOICE ---")

print("\n4. What function displays output in Python?")

print("A. input")
print("B. meow")
print("C. output")

answer = input("Your answer: ").upper()

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer: A")

print("\n5. Which operator is used for multiplication?")
print("A. *")
print("B. +")
print("C. /")

answer = input("Your answer: ").upper()

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer: A")

mini_score = score

print("\n========== MINI QUIZ RESULT ==========")
print("Your Score:", mini_score, "/ 5")
print("Your learning journey starts now!")

while True:

    print("\n==========================================")
    print("                 LESSONS")
    print("==========================================")
    print("[1] PRELIM LESSONS")
    print("[2] MIDTERM LESSONS")
    print("[3] FINALS LESSONS")
    print("[4] VIEW SCORE")
    print("[5] EXIT")

    choice = input("\nChoose your lesson: ")

    # ======================================
    # PRELIM LESSONS
    # ======================================

    if choice == "1":

        while True:

            print("\n========== PRELIM LESSONS ==========")
            print("[1] Introduction to Programming")
            print("[2] Python Basic Syntax")
            print("[3] Printing Output")
            print("[4] Variables, Constants and Data")
            print("[5] Basic Data Types")
            print("[6] Arithmetic Operators and Expressions")
            print("[7] Basic Input and Output")
            print("[8] Back to lesson")

            lesson = input("\nChoose a lesson: ")

            if lesson == "1":
                print("\nPYTHON PROGRAMMING")
                print(
                    "Python Programming is a high level, simple, readable, and easy to learn."
                )
                print("was created by GUIDO VAN ROSSUM in 1991.")

                print("\nExample:")
                print("Hello World")

            elif lesson == "2":
                print("\nPYTHON BASIC SYNTAX")
                print("Syntax refers to the set of rules.")
                print("tell us how to correctly write a program in Python.")

                print("\nExample:")
                name = "John"
                print("name")
                print("\nINDENTATION")
                print("uses indentation (spaces) to define blocks  of code.")
                print("\nExample:")
                age = 18

                if age >= 18:
                    print("Adult")

            elif lesson == "3":
                print("\nPRINTING OUTPUT")
                print("The print() function displays information on the screen.")

                print("\nExample:")
                print('print("Hello, World!")')
                print("print(100)")
                print("# this is a comment")

            elif lesson == "4":
                print("\nVARIABLES, CONSTANTS, AND DATA")
                print("A variable is a storages location to stores a value.")

                print("\nExample:")
                print("a, b, c, age, name")

            elif lesson == "5":
                print("\nBASIC DATA TYPES")
                print("OPERATORS")
                print("int - Whole numbers")
                print("float - Decimal numbers")
                print("str - Text or Letter")
                print("bool - True or False")

                print("\nExample:")
                print("10, 25, -7, 100")
                print("12.5, 3.14")
                print('Ana, "Hello", "CCST")')
                print("True, Flase")

            elif lesson == "6":
                print("\nARITHMETIC OPERATORS AND EXPRESSIONS")
                print("Arithmetic operators are symbols used to perform mathematical calculations on numbers")
                print("ARITHMETIC OPERATORS")
                print("+ Addition")
                print("- Subtraction")
                print("* Multiplication")
                print("/ Division")
                print("// Floor Division")
                print("% Modulus")
                print("** Exponentiation")

                print("\nExample:")
                print("5+3=8")
                print("10-4=6")
                print("7*2=14")
                print("15/3=5.0")
                print("17//3=5")
                print("10% 3=1")
                print("2**3=8")
                print("Expression is a combination of values")
                print("Example:")
                a = 10
                b = 5
                result = a + b
                print("The result is:", result)

            elif lesson == "7":
                print("\nBASIC INPUT AND OUTPUT")
                print("input() gets information from the user.")
                print("print() displays information.")

                print("\nExample:")
                print('name = input("Enter your name: ")')
                print('print("Hello", name)')

            elif lesson == "8":
                break

            else:
                print("Invalid lesson number!")
                exit()

    # ======================================
    # MIDTERM LESSONS
    # ======================================

    elif choice == "2":

        while True:

            print("\n========== MIDTERM LESSONS ==========")
            print("[1] Conditional Statement")
            print("[2] If-Elif-Else Statement")
            print("[3] Logical Operator")
            print("[4] Back to Lesson")

            lesson = input("\nChoose a lesson: ")

            if lesson == "1":
                print("\nCONDITIONAL STATEMENT")
                print("A conditional statement allows the program to make decision.")
                print("whether a condition is True or False.")

                print("\nExample:")
                print("age = 18")
                print("if age >= 18:")
                print(" You are an adult")

            elif lesson == "2":
                print("\nIF-ELIF-ELSE STATEMENT")
                print("if True.")
                print("elif False.")
                print("else provides an alternative when the if condition is false.")

                print("\nExample:")
                if score >= 90:
                    print("Excellent")
                elif score >= 80:
                    print("Very Good")
                elif score >= 75:
                    print("PASSED")
                else:
                    print("FAILED")

            elif lesson == "3":
                print("\nLOGICAL OPERATORS")
                print("and - Both conditions must be True.")
                print("or - At least one condition must be True.")
                print("not - Reverses the result.")

                print("\nExample:")
                age = 18
                has_id = True
                if age >= 18 and has_id:
                    print("Allowed to enter.")
                else:
                    print("Not Allowed to enter.")

            elif lesson == "4":
                break

            else:
                print("Invalid lesson number!")
                exit()

    # ======================================
    # FINALS LESSONS
    # ======================================

    elif choice == "3":

        while True:

            print("\n========== FINALS LESSONS ==========")
            print("[1] Introduction to Iteration and Loop")
            print("[2] For Loop")
            print("[3] While Loop")
            print("[4] While True and Break")
            print("[5] Back to lesson")

            lesson = input("\nChoose a lesson: ")

            if lesson == "1":
                print("\nINTRODUCTION TO ITERATION AND LOOP")
                print("ITERATION means repeating a process. ")

                print("\nExample:")
                for x in range(3):
                    print("Welcome to Python!")

            elif lesson == "2":
                print("\nLOOP")
                print(" for loop repeats instructions for each item in a sequence.")

                print("\nExample:")
                for x in range(1, 6):
                    print("hi")

            elif lesson == "3":
                print("\nWHILE LOOP")
                print("while loop repeats instructions while a condition is True.")

                print("\nExample:")
                count = 1
                while count <= 3:
                    print("meow")
                    count += 1

            elif lesson == "4":
                print("\nWHILE TRUE AND BREAK")
                print("While True keeps the program repeating.")
                print("The break statement stops the loop.")

                print("\nExample:")

                while True:
                    print("Welcome to Python!")
                    break

                print("The loop has stopped.")

            elif lesson == "5":
                break

            else:
                print("Invalid choice! Please try again.")
                exit()

    # VIEW SCORE
    elif choice == "4":

        print("\n========== YOUR SCORE ==========")
        print("Mini Quiz Score:", mini_score, "/ 5")
        print("Surprise Quiz: Not yet taken")
        print("Total Score:", mini_score, "/ 5")

    # EXIT - SURPRISE QUIZ
    elif choice == "5":

        print("\n==========================================")
        print(" EXIT?! NO!!! BCS THERE WAS ONE LAST CHALLENGE!")
        print("==========================================")
        print("\nWoop! You thought your journey was over...")
        print("But there's one more challenge!")
        print("\n             SURPRISE QUIZ!")
        print("                10 ITEMS")
        print("==========================================")

        surprise_score = 0

        # MULTIPLE CHOICE

        print("\n========== MULTIPLE CHOICE ==========")

        print("\n1. Which function gets information from the user?")
        print("A. print()")
        print("B. input()")
        print("C. type()")

        answer = input("Your answer: ").upper()

        if answer == "B":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: B")

        print("\n2. Which of the following is an example of a variable?")
        print("A. age = 18")
        print("B. print(age)")
        print("C. input()")

        answer = input("Your answer: ").upper()

        if answer == "A":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: A")


        print("\n3. What is the output of this code?")
        print("x = 10")
        print("y = 5")
        print("print(x * y)")
        print("A. 15")
        print("B. 50")
        print("C. 5")

        answer = input("Your answer: ").upper()

        if answer == "B":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: B")


        print("\n4. What happens if the condition in an if statement is False and there is no else statement?")
        print("A. The if block will not execute.")
        print("B. The program will restart.")
        print("C. The program will automatically print False.")

        answer = input("Your answer: ").upper()

        if answer == "A":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: A")


        print("\n5. Which logical operator allows the condition to be True if at least one condition is True?")
        print("A. and")
        print("B. not")
        print("C. or")

        answer = input("Your answer: ").upper()

        if answer == "C":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: C")

        # IDENTIFICATION

        print("\n========== IDENTIFICATION ==========")

        print("\n6. What function is used to get information from the user?")
        answer = input("Your answer: ").lower()

        if answer == "input":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: input")

        print("\n7. What If-Elif-Else statement is executes a block of code only when the condition is True?")
        answer = input("Your answer: ").lower()

        if answer == "if":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: if")

        print("\n8. What keyword is used to check another condition?")
        answer = input("Your answer: ").lower()

        if answer == "elif":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: elif")

        print("\n9. What keyword is used to stop a loop immediately?")
        answer = input("Your answer: ").lower()

        if answer == "break":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: break")

        print("\n10. What logical operators is at least one condition must be True?")
        answer = input("Your answer: ").lower()

        if answer == "or":
            print("Correct!")
            surprise_score += 1
        else:
            print("Incorrect! Answer: or")


        # FINAL RESULT
        total = mini_score + surprise_score

        print("\n==========================================")
        print("           SURPRISE QUIZ RESULT")
        print("==========================================")
        print("Mini Quiz Score:", mini_score, "/ 5")
        print("Surprise Quiz Score:", surprise_score, "/ 10")
        print("Total Score:", total, "/ 15")

        print("\n========== YOUR ACHIEVEMENT ==========")

        if total >= 12:
            print("PYTHON MASTER!")
            print("Amazing! You did a great job!")

        elif total >= 8:
            print("PYTHON EXPLORER!")
            print("Good work! Keep improving!")

        else:
            print("KEEP LEARNING!")
            print("Every expert starts as a beginner!")

        # CERTIFICATE
        print("\n==========================================")
        print("         CERTIFICATE OF COMPLETION")
        print("==========================================")
        print("\nThis certificate is proudly presented to:")
        print("\n              ", name)
        print("\nFor completing the PYTHON STUDY program.")
        print("Thank you for joining this learning journey!")
        print("\n==========================================")
        print("       CONGRATULATIONS,", name, "!")
        print("          THANK YOU FOR PLAYING!")
        print("==========================================")

        break

    else:
        print("\nInvalid choice! Please select 1-5.")
        exit()

print("\nProgram ended. Goodbye!")

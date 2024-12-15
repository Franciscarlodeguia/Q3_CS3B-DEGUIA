import random  #import the module to pick a random number

#user guess and computer guess variables
userGuess = 0 #userGuess
computerGuess = 0 #computerGuess

def guesses():  #initialize a function
    global userGuess  #access global variable userGuess
    userGuess = input("There are 10 Students, how many do you guess passed? ")   #this program must accept an input from the user

  
    global computerGuess  #access global variable computerGuess
    computerGuess = random.randint(1, 10)  # Generate a random number between 1 and 10 for the computer's guess
    print(f"Your Guess is {userGuess}")  #print or display the user guess
    print(f"The Computer Guess is {computerGuess}")  #print or display the computer guess
    continueProgram = input("Continue the evaluation? (Yes/YES) ")  #ask if the user want to continue the evaluation only 'Yes/YES' the choices to proceed

guesses()

#students and their details information list
studentList = {
    "studentOne": {
        "studentName": "Ricardo P",  # Student 1
        "studentGrade": 85,   # Stores the student grade as an integer
        "classSubject": "DSA"# Stores the subject of the student that he want to enrolled in a string
    }, 
    "studentTwo": { #student2
        "studentName": "Anagracia A",  # studentName
        "studentGrade": 82,  #stdentGrade
        "classSubject": "DSA" #student classSubjectj
    }, 
    "studentThree": {
        "studentName": "Anastacia D",  # Student 3
        "studentGrade": 75,
        "classSubject": "DSA"
    }, 
    "studentFour": {
        "studentName": "Gregorio D",  # Student 4
        "studentGrade": 74,
        "classSubject": "DSA"
    }, 
    "studentFive": {
        "studentName": "Alegro",  # Student 5
        "studentGrade": 95,
        "classSubject": "DSA"
    }, 
    "studentSix": {
        "studentName": "Maria Juana",  # Student 6
        "studentGrade": 90,
        "classSubject": "DSA"
    }, 
    "studentSeven": {
        "studentName": "Shantal T",  # Student 7
        "studentGrade": 83,
        "classSubject": "OS"
    }, 
    "studentEight": {
        "studentName": "Mariano J",  # Student 8
        "studentGrade": 91,
        "classSubject": "OS"
    }, 
    "studentNine": {
        "studentName": "Josefa G",  # Student 9
        "studentGrade": 73,
        "classSubject": "OS"
    }, 
    "studentTen": {
        "studentName": "Eliseo S",  # Student 10
        "studentGrade": 75,
        "classSubject": "OS"
    }
}

sizeClass = len(studentList)  #assign the length  of the student length 
passStudents = []  # List to store students who passed
failedStudents = []  # List to store students who failed
pStudentCounter = 0  # Counter for passed students
fStudentCounter = 0  # Counter for failed students

def counterPass():  # Function to increment passed students counter
    global pStudentCounter  # Access global variable pStudentCounter
    pStudentCounter += 1  # Increment the counter for passed students

def counterFail():  # Function to increment failed students counter
    global fStudentCounter  # Access global variable fStudentCounter
    fStudentCounter += 1  # Increment the counter for failed students

def testGrade(name, grade, subject):  # Function to evaluate whether a student passed or failed
    if grade >= 75:  # If the grade is 75 or higher, student passes
        passStudents.append([name, grade, subject])  # Add the student to the pass list
        counterPass()  # Increment the passed students counter
    else:  # print the student fails
        failedStudents.append([name, grade, subject])  # Add the student to the fail list
        counterFail()  # Increment the failed students counter

def guessedNear():  # Function to compare how close the user's and computer's guesses are to the actual number of passed students
    global userGuess, computerGuess, pStudentCounter  # Access global variables
    nearUGuess = abs(pStudentCounter - int(userGuess))  # Difference between user's guess and actual number of passed students
    nearCGuess = abs(pStudentCounter - computerGuess)  # Difference between computer's guess and actual number of passed students

    if nearUGuess < nearCGuess:  # If the user is closer
        print("")
        #print the user guessed closer
        print("User Guess is nearer!", ({nearUGuess}))  
    elif nearUGuess == nearCGuess:  # If both guesses are equally close
        print("")
        print("User and Computer Guesses are the same")  # Display that both guesses are the same
    else:  # If the computer is closer
        print("")
        print("Computer Guess is nearer", ({nearCGuess}))  # Display that the computer guessed closer

def printList():  # Function to display the lists of passed and failed students
    print("")
    print("----------- List of Students who Passed --------------------")
    print(passStudents)  #print the list of students passed
    print(f"Total no. of Passed Students: {pStudentCounter}")  #print the total number of students passed
    print("")
    print("------------ List of Students who Failed ---------------------")
    print(failedStudents)  #print the list of students failed
    print(f"Total no. of Failed Students: {fStudentCounter}")  #print the total number of students failed

print(f"The following are the List of Students.\nTotal of {sizeClass}")  #print the total number of students
print("----------------------------------------------------")

# Loop to display student names and the subjects they are enrolled in
for x, obj in studentList.items():
    print(f"{obj.get('studentName')} is enrolled in {obj.get('classSubject')}")  # Print student name and subject

# Loop to test if each student passed or failed
for x, obj in studentList.items():
    testGrade(obj.get("studentName"), obj.get("studentGrade"), obj.get("classSubject"))  # Check student grades

printList()  #print or display all the lists of pass and failed students
guessedNear()  #compare guesses

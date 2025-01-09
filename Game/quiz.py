# Function to run the quiz
print(" Welcome To The Interesting Quiz Game to Play\n")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

player_name = input("Enter Your Name: ")

print("Let's Start the Game :) ",player_name)

print(f"\n Welcome to the Quiz! Player : {player_name} \n")

def quiz(question, options, correct_option):
    
    print("Answer the following question by typing the correct option number (1, 2, 3, or 4).\n")
    score = 0   
    # Display the question and options
    print("\nQuestion:")
    print(question)
    print("Options:")
    for option in options:
        print(option)
    
    # Get user input
    try:
        answer = int(input("\nEnter the option number (1-4): "))
        
        # Validate answer
        if answer == correct_option:
            print("Correct! Well done! 🎉 \n")
            return 1
        elif answer in range(1, 5):
            print("Incorrect Answer.\n")
            return 0
        else:
            print("Invalid input. Please select a number between 1 and 4.\n")
            quiz(question, options, correct_option)
            return 0
    except ValueError:
        print("Invalid input. Hence Incorrect \n")
        return 0

score = 0
question = "Which command is used to display the contents of a file?"
options = [
        "1. grep",
        "2. cat",
        "3. mkdir",
        "4. ls"
    ]
correct_option = 2 
score += quiz(question, options, correct_option)

question = "2. Which AWS service is used for object storage?"
options = [
        "1. S3",
        "2. IAM",
        "3. Cloud Trail",
        "4. EC2"
    ]
correct_option = 1  # Correct option number
score += quiz(question, options, correct_option)


question = " 3. What does IAM stands for? \n "
options = [
        "1. Identity Admin Manager",
        "2. Identity Access Manager",
        "3. Identity and Access Management",
        "4. Identity Admin Management"
    ]
correct_option = 3  # Correct option number
score += quiz(question, options, correct_option)

question = " 4. Which of the following tools is commonly used for Continuous Integration? \n "
options = [
        "1. Ansible",
        "2. Jenkins",
        "3. Docker",
        "4. Kubernetes"
    ]
correct_option = 2  # Correct option number
score += quiz(question, options, correct_option)

question = " 5. Which of these is NOT a configuration management tool? \n "
options = [
        "1. Puppet",
        "2. Chef",
        "3. Terraform",
        "4. Nagios"
    ]
correct_option = 4  # Correct option number
score += quiz(question, options, correct_option)

total_questions = 5
print(f"\nYou got {score} correct answers out of {total_questions}")
print(f"You scored {(score / total_questions) * 100}%")


import random

def generateRandoms():
    num1 = random.randint(100, 999)
    num2 = random.randint(1, 999)  # Adjusted to avoid division by zero
    return num1, num2

# Function to either divide or multiply
def calculate(num1, num2):
    operation = random.choice(['divide', 'multiply'])
    if operation == 'divide':
        result = round(num1 / num2, 1)
    else:  # operation == 'multiply'
        result = round(num1 * num2, 1)
    return result, operation

def main():
    game = True
    score = 0
    corrects = 0
    while game:
        num1, num2 = generateRandoms()
        result, operation = calculate(num1, num2)
        tryAgain = True
        attempts = 1
        gains = 100
        while tryAgain:
            if operation == 'divide':
                print(f"{operation.capitalize()}: \n{num1}\n--- = ?\n{num2}")
            else:
                print(f"{operation.capitalize()}: \n{num1} X {num2} = ?")
            answer = input("Enter your answer: ")
            while answer.isalpha():
                print("Invalid Input! Please enter a number.")
                answer = input("Enter your answer: ")

            if float(answer) != result:
                print(f"Your Answer: {answer}")

                if float(answer) < result:
                    print("Too Low!")
                else:
                    print("Too High!")
                        
                print(f"!!!!Incorrect!!!!\n----Current Number of Attempts: {attempts}----")
                if gains > 11:
                    gains -= 10
                test = input("Do you want to try again? Lose 10 points? (y/n): ")

                if test.lower() in ['n', 'no']:
                    score -= 10
                    print(f"The Answer was {result} in {attempts} attempts\n===== Your Score is {score} =====")
                    tryAgain = False
                    test = input("Go for another round? (y/n): ")
                    if test.lower() in ['n', 'no']:
                        game = False
                        tryAgain = False
                    else:
                        game = True
                        tryAgain = False
                else:
                    attempts += 1
                    tryAgain = True
            else:
                score += gains
                corrects +=1
                print(f"!!!Correct!!!!!\n----Your Score is {score}----\n====You gained {gains} points====")
                test = input("Go for another round? (y/n): ")
                if test.lower() in ['n', 'no']:
                    game = False
                    tryAgain = False
                else:
                    game = True
                    tryAgain = False
    print(f"Goodbye! You ended with a score of {score} points with {corrects} correct answers!")

if __name__ == "__main__":
    main()
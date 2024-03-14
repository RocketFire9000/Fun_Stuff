from random import randint
questions = ["What is the capital of Texas?\n", "Who was the fourth President of the United States?\n", "What's 2 + 4 * 8?\n", "Which planet is known as the 'Red Planet'?\n", "What is the chemical symbol for the element gold?\n", "Who painted the Mona Lisa?\n", "Which country is known for inventing the game of cricket?\n", "What is the capital city of Australia?\n", "Which famous physicist developed the theory of general relativity?\n", "What is the largest ocean in the world?\n", "Which musical instrument has pedals, strings, and is played with the feet?\n", "Which animal is known for its ability to change its color to blend with its surroundings?\n", "Who wrote the famous novel 'Pride and Prejudice'?\n"]
answers = ["Austin", "James Madison", "34", "Mars", "Au", "Leonardo da Vinci", "England", "Canberra", "Albert Einstein", "Pacific Ocean", "Harp", "Chameleon", "Jane Austen"]
already_done = []
x = randint(0, 12)
while len(already_done) < 13:
    if x not in already_done:
        answer = input(questions[x])
        if answer == answers[x]:
            print("Correct!")
            
            already_done.append(x)
            x = randint(0, 12)
        else:
            print("Incorrect. Try again!")
            x = randint(0, 12)
    else:
        x = randint(0, 12)
print('Good job! You completed all of the questions!')
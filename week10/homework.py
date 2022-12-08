quiz = [
    {
        "question": "What's Obama's last name?",
        "choices": [
            "pyramid",
            "soda",
            "Michele",
            "ObAma"
        ],
        "answer": "ObAma"
    },
    {
        "question": "What's the best thing you could use a time machine to do?",
        "choices": [
            "ressurect santa",
            "prevent the existence of TikTok",
            "invent Flex-Tape",
            "shake hands with a monkey"
        ],
        "answer": "shake hands with a monkey"
    }
]

problemNumber = 0
correct = 0
for problem in quiz:
    problemNumber += 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choice in problem['choices']:
        print(f" {choice}")

    guess = input("Your guess: ")
    if guess == problem['answer']:
        correct += 1
        print(f"correct you are, young one")
    else:
        print(f"sir, what you've just said is one of the most insanely, idiotic things I have ever heard. At no point in your rambling, incoherent response, were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it. I award you no points, and may God have mercy on your soul.")
           
    print() # print a blank line for space

print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")
import random
quiz= [
    {
        "question": "what is green lanturn's weakness?",
        "choices": [
            "mirrors",
            "darkrings",
            "the color yellow",
            "kryptonite"

        ],
        "answer":"the color yellow"
    },
    {
        "question": "what is baby yoda's real name?",
        "choices": [
            "yando",
            "yoda the second",
            "grogu",
            "hank"
        ],
        "answer":"grogu"
    },
    {
        "question": "do you know da wae?",
        "choices": [
            "yes",
            "yes I know da way brother",
            "no",
            "clucking noises"
        ],
        "answer": "clucking noises"
    },
    {
        "question": "say my name",
        "choices":[
            "Luke",
            "William",
            "Walter",
            "Dora"
        ],
        "answer": "Walter"
    },
    {
        "question": "The Heavey is what?",
        "choices": [
            "thick", 
            "beg",
            "dead",
            "undead"

        ],
        "answer": "dead"
    },
    {
        "question": "I'm on the highway to what?",
        "choices": [
            "heck",
            "non-homeschool word",
            "heaven",
            "church"

        ],
        "answer": "non-homeschool word"
    },
    {
        "question": "who is the character known as god in Toy Story?",
            "choices": [
                "woody",
                "Buz",
                "Andy",
                "the guy made out of pork"
            ],
            "answer": "woody"
        
    },
    {
        "question": "in what movie does a frog propose to a thicc slab of ham?",
            "choices": [
                "Amphibia",
                "frogs find somthing better than love",
                "veggie tales",
                "kermit the movie"
            ],
            "answer": "kermit the movie"
    }

]
random.shuffle(quiz)
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
        print(f"you have a brain, yay i guess")
    else:
        print(f"commits virtual slap")
           
    print() 

print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")

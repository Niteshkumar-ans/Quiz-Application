import random

questions = [
    {
        "question": "Which keyword is used to define a function?",
        "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
        "answer": "B"
    },
    {
        "question": 'What is len("Hi")?',
        "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
        "answer": "B"
    },
    {
        "question": "Which of these is a mutable type?",
        "options": {"A": "tuple", "B": "str", "C": "list", "D": "int"},
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {"A": "//", "B": "#", "C": "/*", "D": "&"},
        "answer": "B"
    },
    {
        "question": "Which function displays output?",
        "options": {"A": "input()", "B": "show()", "C": "print()", "D": "display()"},
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": {"A": "int", "B": "str", "C": "float", "D": "bool"},
        "answer": "D"
    },
    {
        "question": "Which loop is used to iterate over a list?",
        "options": {"A": "for", "B": "if", "C": "def", "D": "print"},
        "answer": "A"
    },
    {
        "question": "Which brackets are used to create a list?",
        "options": {"A": "()", "B": "[]", "C": "{}", "D": "<>"},
        "answer": "B"
    },
    {
        "question": "Which keyword checks a condition?",
        "options": {"A": "for", "B": "while", "C": "if", "D": "import"},
        "answer": "C"
    },
    {
        "question": "Which module is used to select random items?",
        "options": {"A": "math", "B": "random", "C": "time", "D": "os"},
        "answer": "B"
    }
]

test_mode = True

if test_mode:
    quiz_questions = questions[:3]
else:
    quiz_questions = questions[:]
    random.shuffle(quiz_questions)

score = 0

print("=" * 40)
print("       PYTHON QUIZ APPLICATION")
print("=" * 40)
print("Answer the questions using A, B, C or D.")
print()

for i, q in enumerate(quiz_questions):
    print("Question", i + 1, ":", q["question"])

    for option in q["options"]:
        print(option + ".", q["options"][option])

    answer = input("Enter your answer: ").strip().upper()

    while answer not in ["A", "B", "C", "D"]:
        print("Invalid option. Enter A, B, C or D.")
        answer = input("Enter your answer: ").strip().upper()

    if answer == q["answer"]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! Correct answer:", q["answer"])

    print()

total = len(quiz_questions)
percentage = (score / total) * 100

print("=" * 40)
print("           QUIZ RESULT")
print("=" * 40)
print("Score:", str(score) + "/" + str(total))
print("Percentage:", format(percentage, ".2f") + "%")

if percentage >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

print("=" * 40)
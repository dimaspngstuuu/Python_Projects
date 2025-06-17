questions = [
    {
        "prompt" : "What is the capital of france ?",
        "options" : ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer" : "A"
    },
     {
        "prompt" : "Which language is primaily spoken in Brazin ?",
        "options" : ["A. English", "B. Portuguese", "C. Spanish", "D. Frech"],
        "answer" : "B"
    },
     {
        "prompt" : "Who wrote 'To Kill a Mockingbird ?'",
        "options" : ["A. Harper Lee", "B. Mark Zuckerburg", "C. John Kings", "D. Ernest"],
        "answer" : "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter Your Answer (A,B,C or D) : ").upper()
        if answer == question["answer"]:
            print("Correct your answer !!")
            score += 100
        else:
            print("Your Answer is Wrong")

    print(f"you got {score} from {len(questions)} questions")


        



run_quiz(questions)
        
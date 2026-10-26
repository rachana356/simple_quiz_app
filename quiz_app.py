from datetime import datetime
questions = [
    {
        "question": "What does len() do in Python?",
        "options": ["Prints text", "Gives the length of something", "Deletes a list", "Adds numbers"],
        "correct_ans": "B",
        "topic": "Python",
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["function", "define", "def", "func"],
        "correct_ans": "C",
        "topic": "Python",
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["#", "//", "<!--", "--"],
        "correct_ans": "A",
        "topic": "Python",
    },
    {
        "question": "What is the result of 10 // 3?",
        "options": ["3.33", "4", "1", "3"],
        "correct_ans": "D",
        "topic": "Python",
    },
    {
        "question": "Which of these is a dictionary?",
        "options": ["[1, 2, 3]", "(1, 2, 3)", "{\"a\": 1}", "{1, 2, 3}"],
        "correct_ans": "C",
        "topic": "Python",
    },
    {
        "question": "What type of value does input() always give back?",
        "options": ["int", "str", "float", "bool"],
        "correct_ans": "B",
        "topic": "Python",
    },
    {
        "question": "Which keyword gives a result back from a function?",
        "options": ["return", "give", "send", "output"],
        "correct_ans": "A",
        "topic": "Python",
    },
    {
        "question": "Which is the highest mountain in the world?",
        "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"],
        "correct_ans": "C",
        "topic": "General Knowledge",
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Tool Markup Language",
            "High Text Machine Language",
            "Hyper Text Making Language",
            "Hyper Text Markup Language",
        ],
        "correct_ans": "D",
        "topic": "Web",
    },
    {
        "question": "Which tool installs Python packages?",
        "options": ["pit", "pip", "pop", "ppi"],
        "correct_ans": "B",
        "topic": "Python",
    },
]



order = "ABCD"
score_inc = 0

try:
 with open("result.txt","r") as file:
    content = file.read().splitlines()
    content1=(content[-3:])
    for data in content1:
     print(data)

except FileNotFoundError:
    print("file doesnt exist")





def inputt():
    input_answer = input("enter your answer : ")
    input_answer = input_answer.upper()
    while input_answer not in order or len(input_answer) != 1  :
        print("select A , B , C , D")
        input_answer = input("enter your answer : ")
        input_answer = input_answer.upper()
    return input_answer


for question in questions:
    print(question["question"])
    for index, choices in enumerate (question["options"]):
        print(order[index],choices) 
    input_answer  = inputt()
   
    if input_answer == (question["correct_ans"]):
        print("The answer is correct")
        score_inc = score_inc +  1
    else:
        print("the answer is incorrect")
        print(f"the correct answer is {question['correct_ans']}")
    

total_score =(f"Your total score is : {score_inc} / {len(questions)}")
print(total_score)
now = datetime.now()
now=(now.strftime("%Y-%m-%d %H:%M"))

with open("result.txt","a") as file:
    file.write("\n")
    file.write(f"{now} : {total_score} ")
    


    
    





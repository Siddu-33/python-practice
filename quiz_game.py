score = 0

questions = {
    "Capital of India?": "delhi",
    "5 + 7 = ?": "12",
    "Python is a programming language?": "yes"
}

for q in questions:
    answer = input(q + " ").lower()
    
    if answer == questions[q]:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print("Final Score:", score)

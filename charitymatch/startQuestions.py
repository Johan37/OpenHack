questions = []
alternatives = []

questions.append("Recipient?")
alternatives.append(["Children", "Environment", "Poor"])

questions.append("Method?")
alternatives.append(["Cash transfer", "Short term aid"])

def getQandA(index):
    return (questions[index], alternatives[index])


print(questions)
print(alternatives)
print(getQandA(1))
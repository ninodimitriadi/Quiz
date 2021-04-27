import requests
import json

r = requests.get('https://opentdb.com/api.php?amount=10&category=10&type=multiple')
res = json.loads(r.text)

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = []
for each in range(0, 10):
    question_prompts.append(res['results'][each]['question'])

answers = []
for each in range(0, 10):
    n_list = []
    for i in range(0, 3):
        n_list.append(res['results'][each]["incorrect_answers"][i])
    n_list.append(res['results'][each]["correct_answer"])
    answers.append(n_list)


answ = []
for each in range(0, 10):
    answ.append(res['results'][each]["correct_answer"])


for each in range(0, 10):
    score = 0
    question = question_prompts[each]
    answer = input(f"{question}\n{answers[each]}\nEnter the answer:")
    if answer == answ[each]:
        score += 1

print(f"you got {score}")

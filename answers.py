def get_answer(question, answers):
	return answers.get(question.lower(), "Not Found")
answers={"привет":"И тебе привет!","как дела?":"Лучше всех","пока":"Увидимся"}
question=input("Type something: ")
print(get_answer(question,answers))
class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self):
        score = 0
        total_questions = len(self.questions)

        for index, question in enumerate(self.questions, start=1):
            print(f"Question {index}: {question.text}")
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")
            
            user_answer = int(input("Enter your choice (1-4): "))
            
            if 1 <= user_answer <= 4:
                if question.is_correct(user_answer):
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {question.correct_option}.\n")
            else:
                print("Invalid choice. Skipping question.\n")

        print(f"Quiz complete! Your score: {score}/{total_questions}")

def main():
    quiz = Quiz("General Knowledge Quiz")

    q1 = Question("What is the capital of France?", ["London", "Berlin", "Madrid", "Paris"], 4)
    q2 = Question("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 2)
    q3 = Question("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3)

    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)

    print(f"Welcome to the {quiz.name}!")

    while True:
        print("\nOptions:")
        print("1. Take Quiz")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            quiz.take_quiz()
        elif choice == "2":
            print("Exiting the Quiz. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

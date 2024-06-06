import random
import tkinter as tk

# Defineerime trivia küsimused ja vastuse variandid iga taseme jaoks
questions = {
    1: [
        ("Milline on Eesti pealinn?", ["Tallinn", "Tartu", "Pärnu", "Narva"], "Tallinn"),
        ("Mis on 2+2?", ["3", "4", "5", "6"], "4"),
        ("Mis on maailma suurim ookean?", ["Vaikne ookean", "Atlandi ookean", "India ookean", "Põhjajäämeri"], "Vaikne ookean")
    ],
    2: [
        ("Kes kirjutas 'Tõde ja õigus'?", ["A. H. Tammsaare", "Oskar Luts", "Jaan Kross", "Lennart Meri"], "A. H. Tammsaare"),
        ("Mis riigis asub Machu Picchu?", ["Peruu", "Mehhiko", "India", "Nepaal"], "Peruu"),
        ("Kes on Harry Potteri parim sõber?", ["Hermione", "Ron", "Hagrid", "Draco"], "Ron")
    ],
    3: [
        ("Mis on Suurbritannia pealinn?", ["London", "Manchester", "Liverpool", "Birmingham"], "London"),
        ("Kes maalis Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], "Leonardo da Vinci"),
        ("Mis on päikese süsteemi suurim planeet?", ["Jupiter", "Saturn", "Uraan", "Neptuun"], "Jupiter")
    ],
    4: [
        ("Mis on Aafrika suurim järv?", ["Victoria järv", "Baiikal", "Erie järv", "Huron"], "Victoria järv"),
        ("Kes leiutas telefoni?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Galileo Galilei"], "Alexander Graham Bell"),
        ("Mis on maailma kõrgeim mägi?", ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "Mount Everest")
    ],
    5: [
        ("Kes kirjutas 'Romeo ja Julia'?", ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "William Shakespeare"),
        ("Mis on maailma suurim mandril?", ["Aasia", "Aafrika", "Põhja-Ameerika", "Lõuna-Ameerika"], "Aasia"),
        ("Mis on maailma suurim linn?", ["Tokyo", "Shanghai", "Delhi", "Mumbai"], "Tokyo")
    ],
    6: [
        ("Mis on kõige levinum element Maa koores?", ["Räni", "Alumiinium", "Raud", "Kuld"], "Räni"),
        ("Kes kirjutas 'Kuritöö ja karistus'?", ["Fjodor Dostojevski", "Leo Tolstoi", "Anton Tšehhov", "Ivan Turgenev"], "Fjodor Dostojevski"),
        ("Mis on maailma suurim jõgi?", ["Amazon", "Nile", "Jangtse", "Mississippi-Missouri"], "Amazon")
    ],
    7: [
        ("Kes avastas penitsilliini?", ["Alexander Fleming", "Louis Pasteur", "Robert Koch", "Joseph Lister"], "Alexander Fleming"),
        ("Mis on maailma pikim jõgi?", ["Nile", "Amazon", "Mississippi-Missouri", "Jangtse"], "Nile"),
        ("Mis on maailma kõrgeim hoone?", ["Burj Khalifa", "Shanghai Tower", "Abraj Al-Bait Clock Tower", "Pingan International Finance Centre"], "Burj Khalifa")
    ],
    8: [
        ("Mis on maailma suurim saar?", ["Gröönimaa", "Madagaskar", "Borneo", "Sumatra"], "Gröönimaa"),
        ("Kes kirjutas 'Kääbik'?", ["J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "George R.R. Martin"], "J.R.R. Tolkien"),
        ("Mis on maailma suurim loom?", ["Sinivaal", "Aafrika elevandil", "Giraf", "Nisuvaal"], "Sinivaal")
    ],
    9: [
        ("Kes avastas gravitatsiooniseadused?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Johannes Kepler"], "Isaac Newton"),
        ("Mis on maailma pikim mägi?", ["Mauna Kea", "Mount Everest", "Chimborazo", "Kangchenjunga"], "Mauna Kea"),
        ("Kes kirjutas 'Anna Karenina'?", ["Leo Tolstoi", "Fjodor Dostojevski", "Anton Tšehhov", "Ivan Turgenev"], "Leo Tolstoi")
    ],
    10: [
        ("Mis on kõige tihedamalt asustatud riik maailmas?", ["Monaco", "India", "Hiina", "Bangladesh"], "Monaco"),
        ("Kes kirjutas 'Don Quijote'?", ["Miguel de Cervantes", "Fyodor Dostoevsky", "Victor Hugo", "Leo Tolstoy"], "Miguel de Cervantes"),
        ("Mis on kõige kuumem asukoht maailmas?", ["Lut Desert", "Death Valley", "Dasht-e Lut", "Flaming Mountains"], "Death Valley")
    ]
}

class TriviaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Mäng")
        
        self.level = 1
        self.score = 0
        self.total_questions = 0
        self.wrong_answers = 0
        self.lives = 3  # Mängija alustab kolme eluga
        
        self.questions = self.load_questions()
        
        self.level_label = tk.Label(root, text=f"Tase: {self.level}")
        self.level_label.pack(pady=10)
        
        self.lives_label = tk.Label(root, text=f"Elud: {self.lives}")
        self.lives_label.pack(pady=10)
        
        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=20)
        
        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=50, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)
        
        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Järgmine küsimus", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=20)
        
        self.next_question()
    
    def load_questions(self):
        questions_copy = {}
        for level, q_list in questions.items():
            questions_copy[level] = random.sample(q_list, len(q_list))
        return questions_copy
    
    def next_question(self):
        if self.wrong_answers == 3:
            self.feedback_label.config(text="Kolm vale vastust! Mäng algab uuesti.")
            self.root.after(2000, self.reset_game)
            return
        
        if self.level not in self.questions:
            self.feedback_label.config(text=f"Mäng läbi! Lõplik skoor: {self.score}/{self.total_questions}")
            self.root.after(2000, self.reset_game)
            return
        
        if not self.questions[self.level]:
            self.level += 1
            self.level_label.config(text=f"Tase: {self.level}")
            self.next_question()
            return
        
        self.current_question = self.questions[self.level].pop()
        question_text, self.options, self.correct_answer = self.current_question
        
        self.question_label.config(text=question_text)
        for i, option in enumerate(self.options):
            self.buttons[i].config(text=option, state=tk.NORMAL)
        
        self.feedback_label.config(text="")
        self.next_button.config(state=tk.DISABLED)
    
    def check_answer(self, index):
        selected_option = self.options[index]
        if selected_option.lower() == self.correct_answer.lower():
            self.score += 1
            self.feedback_label.config(text="Õige vastus!")
        else:
            self.wrong_answers += 1
            self.lives -= 1
            self.lives_label.config(text=f"Elud: {self.lives}")
            self.feedback_label.config(text=f"Vale vastus! Õige vastus on: {self.correct_answer}")
        
        self.total_questions += 1
        
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
        
        self.next_button.config(state=tk.NORMAL)
    
    def reset_game(self):
        self.level = 1
        self.score = 0
        self.total_questions = 0
        self.wrong_answers = 0
        self.lives = 3  # Reset elud kolmele
        self.level_label.config(text=f"Tase: {self.level}")
        self.lives_label.config(text=f"Elud: {self.lives}")
        self.questions = self.load_questions()
        self.next_question()

# Mängu käivitamine
if __name__ == "__main__":
    root = tk.Tk()
    game = TriviaGame(root)
    root.mainloop()



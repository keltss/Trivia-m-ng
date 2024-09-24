import random
import tkinter as tk

# Defineerime trivia küsimused ja vastuse variandid iga taseme jaoks
questions = {
    1: [
        ("Mis on muutuja programmeerimises?", 
         ["Konteiner andmete hoidmiseks", "Funktsioon", "Tsükkel", "Kommentaar"], 
         "Konteiner andmete hoidmiseks"),
        
        ("Mis on 'for' tsükkel?", 
         ["Käsk", "Tsükkel kindla arvu korduste jaoks", "Andmetüüp", "Muusika instrument"], 
         "Tsükkel kindla arvu korduste jaoks"),
        
        ("Mis on if-else lause?", 
         ["Tingimuslaused koodi hargnemiseks", "Korduv funktsioon", "Andmetüüp", "Kommentaar"], 
         "Tingimuslaused koodi hargnemiseks"),

        ("Mis on funktsioon programmeerimises?", 
         ["Koodilõik, mida saab uuesti kasutada", "Andmetüüp", "Tsükkel", "Kommentaar"], 
         "Koodilõik, mida saab uuesti kasutada"),
        
        ("Mis on list (loend) Pythonis?", 
         ["Andmestruktuur elementide hoidmiseks", "Tsükkel", "Kommentaar", "Funktsioon"], 
         "Andmestruktuur elementide hoidmiseks"),

        ("Mis tähendus on 'return' lausel funktsioonis?", 
         ["Väärtuse tagastamine funktsioonist", "Kommentaari lisamine", "Tsükli katkestamine", "Muutuja loomine"], 
         "Väärtuse tagastamine funktsioonist"),

        ("Mis on klass programmeerimises?", 
         ["Mall objektide loomiseks", "Muutuja", "Funktsioon", "Kommentaar"], 
         "Mall objektide loomiseks"),
        
        ("Mis süntaksiga saab luua klassi Pythonis?", 
         ["class MyClass:", "def MyClass:", "for MyClass:", "if MyClass:"], 
         "class MyClass:"),

        ("Mis on rekursioon programmeerimises?", 
         ["Funktsioon, mis kutsub iseennast", "Tsükkel", "Muudetav andmestruktuur", "Muutuja"], 
         "Funktsioon, mis kutsub iseennast"),

        ("Mis süntaksiga saab defineerida funktsiooni Pythonis?", 
         ["def my_function():", "for my_function():", "class my_function():", "if my_function():"], 
         "def my_function():")
    ]
}

class TriviaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Programmeerimise Trivia Mäng")
        
        self.level = 1
        self.score = 0
        self.total_questions = 0
        self.wrong_answers = 0
        self.lives = 3
        
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
        
        random.shuffle(self.options)  # Segame vastuse variandid iga küsimuse jaoks
        
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
        self.lives = 3
        self.level_label.config(text=f"Tase: {self.level}")
        self.lives_label.config(text=f"Elud: {self.lives}")
        self.questions = self.load_questions()
        self.next_question()

# Mängu käivitamine
if __name__ == "__main__":
    root = tk.Tk()
    game = TriviaGame(root)
    root.mainloop()


import random
import tkinter as tk
from tkinter import ttk

money = 0

# Programmeerimise teemalised küsimused igale tasemele
questions = {
    1: [
        ("Mis on muutuja programmeerimises?", ["Konteiner andmete hoidmiseks", "Funktsioon", "Tsükkel", "Kommentaar"], "Konteiner andmete hoidmiseks"),
        ("Mis on 'for' tsükkel?", ["Tsükkel kindla arvu korduste jaoks", "Andmetüüp", "Muusika instrument", "Kommentaar"], "Tsükkel kindla arvu korduste jaoks"),
        ("Mis on if-else lause?", ["Tingimuslaused koodi hargnemiseks", "Andmetüüp", "Loop", "Kommentaar"], "Tingimuslaused koodi hargnemiseks"),
    ],
    2: [
        ("Mis on funktsioon programmeerimises?", ["Koodilõik, mida saab korduvalt kasutada", "Kommentaar", "Tsükkel", "Muutuja"], "Koodilõik, mida saab korduvalt kasutada"),
        ("Mis on andmetüüp?", ["Määratleb andmete vormingu", "Loop", "Tingimuslaused", "Kommentaar"], "Määratleb andmete vormingu"),
        ("Kuidas tähistatakse Pythonis kommentaari?", ["#", "//", "/* */", "<!-- -->"], "#"),
    ],
    3: [
        ("Mis on klass objektorienteeritud programmeerimises?", ["Objektide mall", "Andmetüüp", "Funktsioon", "Tsükkel"], "Objektide mall"),
        ("Mis on pärilikkus (inheritance)?", ["Võimalus kasutada teise klassi omadusi", "Loop", "Andmetüüp", "Kommentaar"], "Võimalus kasutada teise klassi omadusi"),
        ("Mis on polümorfism programmeerimises?", ["Sama liidese kasutamine eri tüüpi objektidel", "Tsükkel", "Andmetüüp", "Kommentaar"], "Sama liidese kasutamine eri tüüpi objektidel"),
    ],
    4: [
        ("Mis on SQL-i põhikäsk?", ["SELECT", "INSERT", "DELETE", "CREATE"], "SELECT"),
        ("Mis on JSON?", ["Andmestruktuuride vahetamise formaat", "Programmeeringu keel", "Muutuja tüüp", "Funktsioon"], "Andmestruktuuride vahetamise formaat"),
        ("Milleks kasutatakse try-except konstruktsiooni?", ["Vigade käsitlemiseks", "Loop", "Andmetüüpide määramiseks", "Kommentaaride lisamiseks"], "Vigade käsitlemiseks"),
    ],
    5: [
        ("Mis on API?", ["Rakenduste suhtlusliides", "Andmetüüp", "Programmeeringu keel", "Kommentaar"], "Rakenduste suhtlusliides"),
        ("Mis on Git?", ["Versioonihaldussüsteem", "Andmetüüp", "Objekt", "Kommentaar"], "Versioonihaldussüsteem"),
        ("Mis on Docker?", ["Platvorm konteinerite haldamiseks", "Tsükkel", "Objekt", "Loop"], "Platvorm konteinerite haldamiseks"),
    ],
    6: [
        ("Mis on lambda-funktsioon Pythonis?", ["Anonüümne funktsioon", "Muuttuja", "Tsükkel", "Andmetüüp"], "Anonüümne funktsioon"),
        ("Mis on pip?", ["Pythoni pakettide haldur", "Andmetüüp", "Tsükkel", "Kommentaar"], "Pythoni pakettide haldur"),
        ("Mis on veebiraamistiku Flask põhikasutus?", ["Veebirakenduste loomine", "Andmetöötlus", "Kommentaaride haldus", "Failide lugemine"], "Veebirakenduste loomine"),
    ],
    7: [
        ("Mis on Big O notatsioon?", ["Algoritmi efektiivsuse mõõtmine", "Muutuja tüüp", "Andmestruktuur", "Kommentaar"], "Algoritmi efektiivsuse mõõtmine"),
        ("Mis on rekursioon programmeerimises?", ["Funktsioon, mis kutsub iseennast", "Loop", "Klass", "Kommentaar"], "Funktsioon, mis kutsub iseennast"),
        ("Mis on andmestruktuur HashMap?", ["Kaardistamise struktuur", "Tsükkel", "Klass", "Kommentaar"], "Kaardistamise struktuur"),
    ],
    8: [
        ("Mis on SQL JOIN?", ["Andmete ühendamine mitmest tabelist", "Funktsioon", "Klass", "Kommentaar"], "Andmete ühendamine mitmest tabelist"),
        ("Mis on singleton muster?", ["Klass, mis võimaldab ainult üht eksemplari", "Loop", "Funktsioon", "Kommentaar"], "Klass, mis võimaldab ainult üht eksemplari"),
        ("Mis on REST API?", ["Veebiliides andmete edastamiseks", "Andmestruktuur", "Kommentaar", "Andmetüüp"], "Veebiliides andmete edastamiseks"),
    ],
    9: [
        ("Mis on Python Decorator?", ["Funktsiooni modifitseerimise viis", "Loop", "Andmestruktuur", "Andmetüüp"], "Funktsiooni modifitseerimise viis"),
        ("Mis on WebSocket?", ["Protokoll reaalajas andmesideks", "Muutuja tüüp", "Klass", "Kommentaar"], "Protokoll reaalajas andmesideks"),
        ("Mis on Kubernetes?", ["Konteinerite orkestraator", "Loop", "Andmestruktuur", "Kommentaar"], "Konteinerite orkestraator"),
    ],
    10: [
        ("Mis on graafialgoritm Dijkstra?", ["Lühima tee leidmise algoritm", "Klass", "Tsükkel", "Kommentaar"], "Lühima tee leidmise algoritm"),
        ("Mis on serverless arhitektuur?", ["Arhitektuur ilma püsiserveriteta", "Andmestruktuur", "Kommentaar", "Klass"], "Arhitektuur ilma püsiserveriteta"),
        ("Mis on Blockchain?", ["Hajutatud andmeplokkide süsteem", "Loop", "Andmetüüp", "Kommentaar"], "Hajutatud andmeplokkide süsteem"),
    ],
}
class TriviaGame:
    def __init__(self, root, level):
        global money  # Access global money
        self.root = root
        self.level = level
        self.money = money  # Use global money value
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title(f"Programmeerimise Trivia - Tase {self.level}")
        self.root.geometry("800x600")
        self.root.configure(bg="#2B2D42")

        self.score = 0
        self.total_questions = 0
        self.wrong_answers = 0
        self.lives = 3

        self.questions = self.load_questions()

        self.style = ttk.Style()
        self.style.configure("TLabel", background="#2B2D42", foreground="#EDF2F4", font=("Arial", 18))
        self.style.configure("TButton", font=("Arial", 14), padding=10)

        for widget in self.root.winfo_children():
            widget.destroy()

        self.top_frame = tk.Frame(self.root, bg="#2B2D42")
        self.top_frame.pack(pady=20)

        self.level_label = ttk.Label(self.top_frame, text=f"Tase: {self.level}")
        self.level_label.grid(row=0, column=0, padx=20)

        self.lives_label = ttk.Label(self.top_frame, text=f"Elud: {self.lives}")
        self.lives_label.grid(row=0, column=1, padx=20)

        self.money_label = ttk.Label(self.top_frame, text=f"Raha: €{self.money}")
        self.money_label.grid(row=0, column=2, padx=20)

        self.question_frame = tk.Frame(self.root, bg="#2B2D42")
        self.question_frame.pack(pady=20)

        self.question_label = tk.Label(
            self.question_frame, text="", wraplength=600, bg="#2B2D42", fg="#EDF2F4", font=("Arial", 20), justify="center"
        )
        self.question_label.pack(pady=10)

        self.button_frame = tk.Frame(self.root, bg="#2B2D42")
        self.button_frame.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(
                self.button_frame, text="", width=30, height=2, bg="#8D99AE", fg="#FFFFFF",
                font=("Arial", 14, "bold"), command=lambda i=i: self.check_answer(i)
            )
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.feedback_label = ttk.Label(self.root, text="", anchor="center")
        self.feedback_label.pack(pady=10)

        self.hint_button = ttk.Button(self.root, text="Osta vihje (€10)", command=self.use_hint, state=tk.DISABLED)
        self.hint_button.pack(pady=10)

        self.next_button = ttk.Button(self.root, text="Järgmine küsimus", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.main_menu_button = ttk.Button(self.root, text="Tagasi avalehele", command=self.return_to_main_menu)
        self.main_menu_button.pack(pady=10)

        self.next_question()

    def load_questions(self):
        return random.sample(questions[self.level], len(questions[self.level]))

    def next_question(self):
        if self.wrong_answers == 3:
            self.feedback_label.config(text="Kolm vale vastust! Pead taseme uuesti läbima.", foreground="red")
            self.root.after(2000, self.return_to_main_menu)
            return

        if not self.questions:
            if self.score == 3:  # Level is passed only if 3 questions are answered correctly
                self.feedback_label.config(text=f"Tase {self.level} läbitud! Skoor: {self.score}/3", foreground="green")
                self.next_button.config(state=tk.DISABLED)
                self.hint_button.config(state=tk.DISABLED)
                global money  # Update global money after level completion
                money = self.money
                return
            else:
                self.feedback_label.config(text="Sa ei vastanud kõigile küsimustele õigesti. Proovi uuesti!", foreground="red")
                self.root.after(2000, self.reset_level)

        self.current_question = self.questions.pop()
        question_text, self.options, self.correct_answer = self.current_question

        random.shuffle(self.options)

        self.question_label.config(text=question_text)
        for i, option in enumerate(self.options):
            self.buttons[i].config(text=option, state=tk.NORMAL, bg="#8D99AE")

        self.feedback_label.config(text="")
        self.next_button.config(state=tk.DISABLED)
        self.hint_button.config(state=tk.NORMAL if self.money >= 10 else tk.DISABLED)

    def check_answer(self, index):
        selected_option = self.options[index]
        if selected_option.lower() == self.correct_answer.lower():
            self.score += 1
            self.money += 5
            self.money_label.config(text=f"Raha: €{self.money}")
            self.feedback_label.config(text="Õige vastus!", foreground="green")
        else:
            self.wrong_answers += 1
            self.lives -= 1
            self.lives_label.config(text=f"Elud: {self.lives}")
            self.feedback_label.config(text=f"Vale vastus! Õige vastus on: {self.correct_answer}", foreground="red")

        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

        self.next_button.config(state=tk.NORMAL)
        self.hint_button.config(state=tk.DISABLED)

    def use_hint(self):
        if self.money >= 10:
            self.money -= 10
            self.money_label.config(text=f"Raha: €{self.money}")
            self.feedback_label.config(text="Vihje kasutatud!", foreground="blue")

            correct_option = self.correct_answer
            reduced_options = [correct_option]

            while len(reduced_options) < 2:
                option = random.choice(self.options)
                if option != correct_option and option not in reduced_options:
                    reduced_options.append(option)

            random.shuffle(reduced_options)

            for i, btn in enumerate(self.buttons):
                if btn["text"] not in reduced_options:
                    btn.config(state=tk.DISABLED)

    def reset_level(self):
        self.score = 0
        self.wrong_answers = 0
        self.lives = 3
        self.questions = self.load_questions()
        self.next_question()

    def return_to_main_menu(self):
        MainMenu(self.root)


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("Programmeerimise Trivia")
        self.root.geometry("800x600")
        self.root.configure(bg="#2B2D42")

        for widget in self.root.winfo_children():
            widget.destroy()

        ttk.Label(self.root, text="Tere tulemast Trivia Mängu!", font=("Arial", 24), background="#2B2D42", foreground="#EDF2F4").pack(pady=20)

        ttk.Label(self.root, text="Vali tase, mida alustada:", font=("Arial", 18), background="#2B2D42", foreground="#EDF2F4").pack(pady=10)

        for level in range(1, 11):
            ttk.Button(self.root, text=f"Tase {level}", command=lambda level=level: self.start_game(level)).pack(pady=5)

    def start_game(self, level):
        TriviaGame(self.root, level)


if __name__ == "__main__":
    root = tk.Tk()
    MainMenu(root)
    root.mainloop()



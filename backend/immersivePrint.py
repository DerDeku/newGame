from time import sleep
from msvcrt import getch

skip = False

def iprint(text : str, time_s = None):
    if skip:
        print(text)
        return
    if isinstance(time_s, int) or isinstance(time_s, float):
        for char in text:
            print(char, end='', flush=True) 
            sleep(time_s) 
        print("")
        sleep(time_s)
    elif isinstance(time_s, bool):
        for char in text:
            print(char, end='', flush=True) 
            sleep(0.1)  
        print("")
        getch()
    else:
        for char in text:
            print(char, end='', flush=True)  
            sleep(0.06)  
        print("")
        sleep(0.1)

def dprint(time_s = None):
    if skip:
        return
    if isinstance(time_s, int) or isinstance(time_s, float):
        for i in range(3):  
            print(". ", end="")
            sleep(0.4)
        print("")
    else:
        for i in range(3):  
            print(". ", end="")
            sleep(0.4)
        print("")
        getch()
        
    
class Dialog:
    def __init__(self) -> None:
        self.questions = []
        self.answers = []
        self.children = []

    def setQuestions(self, *opts: str):
        self.questions.extend(opts)

    def setAnswers(self, *opts: str):
        self.answers.extend(opts)

    def addChild(self, dialog_child):
        self.children.append(dialog_child)

    def start(self):
        if skip:
            return
        current_dialog = self
        while current_dialog:
            print("\n".join(f"{i + 1} - {opt}" for i, opt in enumerate(current_dialog.questions)))
            try:
                user_input = int(input())
                if user_input < 1 or user_input > len(current_dialog.questions):
                    raise ValueError
                user_input -= 1
                if current_dialog.answers:
                    print(current_dialog.answers[user_input])
                if current_dialog.children:
                    current_dialog = current_dialog.children[user_input]
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid option.")

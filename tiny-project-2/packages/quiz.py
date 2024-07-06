from .questions import questions

class quiz:
    def __init__(self, privilege: str):
        self.privilege = privilege
        return

    def compose(self, author:str):
        questionairre = questions()  # Instantiate an object of the questions class
        questionairre.composeQuestion(author)
        return

    def examination(self, user: str):
        print('Welcome to the quiz buzzes questionairre', user)
        return
    
    def quiz_operations(self, user: str):
        if self.privilege != 'admin':
            self.examination(user)
        else:
            answer = int(input('''\nPlease make your choice. 
            \n 1. Compose Exams
            \n 2. Give Exam
            \n (ensure the choice is entered in numerics [1/2]):'''))
            if answer not in [1,2]:
                print('\n Invalid choice')
                self.quiz_operations(user)
            else:
                if answer==1:
                    self.compose(user)
                else:
                    self.examination(user)


import os as os
import json

class questions:
    def __init__(self):
        self.title = ''
        self.optionCount = 0
        self.options = {}
        self.score = 0
        self.time = 0
        self.author = ''
        self.questionLog = os.path.join('/tiny-project-2/storage', 'questions.json')
        return

    def composeTitle(self):
        answer = str(input('\n *** \n Enter the question text : \n'))
        if answer!= None:
            self.title=answer
        else:
            raise RuntimeError('Invalid question title entered')
        return True

    def composeOptions(self, isItCount=True):
        if isItCount:
            answer = int(input('\n *** \n How many options does the question have ? : \n'))
            if answer!= None and answer >1 and answer <=4:
                self.optionCount=answer
            else:
                raise RuntimeError("Invalid count of options entered. Number of options that can be provided should be with in 1 and 4")
        else:
            for opt in range(self.optionCount):
                answer = str(input(f'Enter the value of option - ${opt}'))
                if answer !=None:
                    self.options[opt]=answer
                else:
                    raise RuntimeError("Invalid Option Value entered")
        return True
        
    def composeWeightage(self):
        answer = int(input('What is the weightage of this question ? '))
        if answer>=1 and answer <=10:
            self.score = answer
        else:
            raise RuntimeError('Invalid score value entered. The value of individual score question should be with in 1 and 10')
        return True

    def composeTime(self):
        answer = int(input('In seconds quantify the time it should take to solve this question :'))
        if answer>=10 and answer<=60:
            self.time=answer
        else:
            raise RuntimeError('Invalid time entered to solve the question. Time should be within 10 and 60 (seconds)')
        return True   

    def updateStorage(self) -> bool:
        questionairreStorage = open(os.getcwd()+self.questionLog, mode='r',encoding='utf-8')
        questionairreObject = [] if len(questionairreStorage.readlines())==0 else list(json.load(questionairreStorage))
        questionairreStorage.close()
        questionairreObject.append({
            "author": self.author,
            "title" : self.title,
            "optionCount" : self.optionCount,
            "options" : self.options,
            "score" : self.score,
            "time" : self.time,
        })
        try:
            questionairreStorage = open(os.getcwd()+self.questionLog, mode='w',encoding='utf-8')
            json.dump(questionairreObject, questionairreStorage,indent=3)
            questionairreStorage.close()
            return True
        except Exception as e:
            print('Error updating the questionairre to the storage', e)
            return False

    def fetchStorage(self, author=''):
        if len(author)==0:
            print('Randomizing selections')
        else:
            print('Picking questions of the author', author)
        return {}
    
    def composeQuestion(self, author) -> bool:
        self.author = author
        try:
            if self.composeTitle(): 
                if self.composeOptions(True):
                    if self.composeOptions(False):
                        if self.composeWeightage():
                            if self.composeTime():
                                print('Question successfully composed ! Saving it to storage !')
                                if(self.updateStorage()):
                                   print('''\n Saved successfully !\n''')
                                   return True
        except Exception as e:
            print('Failed finishing question composition !', e)

    def __repr__(self):
        return "Auth module for Quiz App"

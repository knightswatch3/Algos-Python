import time
from .questions import questions
import random
import os
import json

class quiz:
    def __init__(self, privilege: str):
        self.privilege = privilege
        self.questionairre = questions()
        self.testQuestions = None
        self.currentQuestionValidity = False
        self.quizLog = os.path.join('/tiny-project-2/storage', 'quizzes.json')
        self.testLog=[]
        self.currentUser=''
        return

    def compose(self, author:str):
          # Instantiate an object of the questions class
        self.questionairre.composeQuestion(author)
        return

    def examination(self, user: str):
        self.currentUser = user
        print('''\nPlease choose your exam questions spec:\n
        1. Pick finite-number(of my choice) of questions.
        2. Pick a random-number of questions.''')
        answer = int(input('Enter your response in numerics: [1/2]'))
        if answer not in [1,2]:
                print('\n Invalid choice')
                self.quiz_operations(self.currentUser)
                return
        else:
            if answer==1:
                qCount = int(input('''\nEnter how many questions would you like to answer:\n
                (NOTE: If the number you entered is higher then the upper limit is available number of questions in the log book)\n'''))
                self.triggerExam(qCount)
            else:
                self.triggerExam()

    def triggerExam(self,count=0):
        count = random.randint(0, self.questionairre.getQuestions()-1) if count==0 else count
        examQuestions = random.sample(self.questionairre.getQuestions(False), count)
        examInformation = self.testAnalysis(examQuestions)
        print(f'''\n\tWelcome to the test ! In this test you will be asked {len(examQuestions)} quizzes. \n
        for a score of {examInformation['tScore']} . The exam is timed for a total of {examInformation['tTime']} secs \n
        The time for each question will be provided along with the question along with the weightage. \n
        NOTE: There is a penanly of 2 points for questions taken longer than the allowed time to answer.\n
        GOOD LUCK !''')
        self.testQuestions=examQuestions
        print('''\nAre you ready to take the test ?\n
            1. Yes\n
            2. No \n
        ''')
        answer = int(input("NOTE-> Enter your choice in numerics[1/2]:"))
        if answer != 1:
            print ('Terminating session ! Have a nice day')
            return
        else:
            self.poseQuestions()
        return True

    def poseQuestions(self):
        for idx,qsn in enumerate(self.testQuestions):
            answer= None
            isItFirstTime = True
            while self.validateAnswer(qsn, answer, isItFirstTime):
                print(f'''\n
                {idx}.{qsn['title']}\n            
                ''')
                options = qsn['options'].values()
                for oidx,opt in enumerate(options):
                    print(f'''{oidx+1}.{opt}''')
                print('\n Time reqd. -> sec(s)', {qsn['time']})
                self.question_start_time = time.time()
                answer = int(input('\n Enter your answer with numerics [1,2,3,4]:'))  
                isItFirstTime=False             
                if not self.validateAnswer(qsn, answer, isItFirstTime):
                    qsn['validity'] = self.currentQuestionValidity
                    qsn['given'] = answer-1
            self.testLog.append(qsn)
        self.resultAnnouncement()
        return True

    def validateAnswer(self, question: dict, answer: int, isItFirstTime):
        if isItFirstTime:
            return True
        else:
            if answer<=0 and answer>len(question['options']):
                print('\n Looks like you entered incorrect option value. Try again !')
                return True
            else:
                self.currentQuestionValidity = answer-1 == int(question['answer'])
                question['timeTaken'] = time.time()-self.question_start_time
            return False



    def testAnalysis(self,questions: list):
        # Calculating the score for the selected questions
        totalScore =sum([qsn['score'] for qsn in list(questions)])
        totalTime =sum([qsn['time'] for qsn in list(questions)])
        return {
            "tTime": totalTime,
            "tScore":totalScore
        }
        # Calculating the total time for the selected questions

    def quiz_operations(self, user):
        if self.privilege != 'admin':
            self.examination(self.currentUser)
        else:
            answer = int(input('''\nPlease make your choice. 
            \n 1. Compose Exams
            \n 2. Give Exam
            \n 3. Check my score
            \n (ensure the choice is entered in numerics [1/2/3]):'''))
            if answer not in [1,2,3]:
                print('\n Invalid choice')
                self.quiz_operations(user)
            else:
                if answer==1:
                    self.compose(user)
                else: 
                    if answer==2:
                        self.examination(user)
                    if answer==3:
                        self.getTestResults()

    def resultAnnouncement(self):
        scored_points = sum([item['score'] if item['validity'] is True else 0 for item in self.testLog])
        questions_time_lapsed=len([item for item in self.testLog if item['timeTaken'] > item['time']])
        print("\n Your score :", scored_points)
        print("\n points lost :", questions_time_lapsed*2)
        print("\n Final score :", scored_points-(questions_time_lapsed*2))
        self.updateQuizLog()
        return

    def updateQuizLog(self):
        quizStorage = open(os.getcwd()+self.quizLog, mode='r',encoding='utf-8')
        quizObject = dict(json.load(quizStorage))
        quizStorage.close()
        quizStorage = open(os.getcwd()+self.quizLog, mode='w',encoding='utf-8')
        if self.currentUser not in quizObject.keys():
            quizObject[self.currentUser]=self.testLog
        else:
            quizObject[self.currentUser]=self.testLog
        json.dump(quizObject, quizStorage, indent=3)
        quizStorage.close()
        print("\n Successfully logged your test results")

    def getTestResults(self):
        quizStorage = open(os.getcwd()+self.quizLog, mode='r',encoding='utf-8')
        quizObject = dict(json.load(quizStorage))
        quizStorage.close()
        if self.currentUser not in quizObject.keys():
            print('\nLooks like you never took a test ! Please take a test before you can see your results')
            return
        else:
            for idx,qsn in quizObject[self.currentUser]:
                print(f'''\n
                {idx}.{qsn['title']}\n            
                ''')
                options = qsn['options'].values()
                for oidx,opt in enumerate(options):
                    print(f'''{oidx+1}.{opt}''')
                print('\n Your answer: ', qsn["given"])
                self.testLog = quizObject[self.currentUser]
                self.resultAnnouncement()
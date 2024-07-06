from packages.auth import auth
from packages.quiz import quiz
def Welcome(firstTime=False):
    if(firstTime):
        print("\n" + "="*40)
        print(" " * 10 + "Welcome to QuizBuzz !\n")
        print("="*40)
    print("\nChoose what you want to perform:")
    print(" " * 4 + "1. Sign-Up")
    print(" " * 4 + "2. Log-In")
    print("="*40 + "\n")
    if(not firstTime):
        print("*"*20 + "\n")
        print('\n You can cancel this by using CMD+d(macOs) or CTL+C(winOs).')
        print("*"*20 + "\n")

    answer= int(input('Enter [1/2] only:'))
    if answer not in [1,2]:
        print('\n Invalid selection ! Try again')
        Welcome()
    else:
        authorizeUser = auth()
        if answer==1:
            authorizeUser.sign_up()
            Welcome()
        else:
            authenticationStatus = authorizeUser.sign_in()
            if authenticationStatus['status']:
                quizInstance = quiz(authenticationStatus['privilege'])
                response = quizInstance.quiz_operations(authenticationStatus['user'])
                if response:
                    

Welcome(True)

from packages.user import user

class auth(user):
    def __init__(self):
        super().__init__()
        return

    def sign_up(self):
        print('\n Please enter the following details')
        uType = int(input('''\n Please enter your choice for type of user: \n
        1. Admin\n
        2. User\n
        
        Note: Enter your choice with number: [1/2]'''))
        if(int(uType) not in [1,2]):
            raise RuntimeError('Invalid user type choice selected')
        else:
            self.usertype = 'admin' if uType == 1 else 'user'
        uName = str(input('''\n UserName (this should be unique): '''))
        if(len(uName)==0):
            raise RuntimeError('Invalid username entered')
        else:
            self.username = uName
            pwd = str(input('''\n Password : '''))
            if(len(pwd)==0):
                raise RuntimeError('Invalid username entered')
            else:
                self.password = pwd
                if self.updateUserBase():
                    print('\n User successfully signed up !')
                else:
                    print("\n Unable to signup the user with above information !")
                    return False
        return True

    def sign_in(self) -> bool:
        print('\n Please enter the following details')
        self.username = str(input('''\n UserName : '''))
        if(len(self.username)==0):
            raise RuntimeError('Invalid username entered')
        else:
            self.password = str(input('''\n Password : '''))
            if(len(self.password)==0):
                raise RuntimeError('Invalid username entered')
            else:
                authenticationStatus =  self.authenticate()
                if authenticationStatus['status']:
                    print('\n Authentication successful !')
                    return authenticationStatus
                else:
                    print("Invalid credentials")
                    return authenticationStatus
        return True
    
     


    def validations(self):
        return

    def __repr__(self):
        return "Auth module for Quiz App"

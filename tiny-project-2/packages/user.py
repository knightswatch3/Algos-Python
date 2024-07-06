import os as os
import json as json
import base64 as cipher

class user:
    def __init__(self):
        #  username: str, password: str, isNew: False
        self.usertype = ''
        self.username = ''
        self.password = ''
        self.userBaseFile = os.path.join('/tiny-project-2/storage', 'users.json')
        return

    def authenticate(self):
        userBaseStorage = open(os.getcwd()+self.userBaseFile, mode='r',encoding='utf-8')
        userBaseList = list(json.load(userBaseStorage))
        authenticationStatus = {
            "status": False,
            "privilege": "unknown",
            "user": "unknown"
        }
        for user in userBaseList:
            currentUser = dict(user)
            if currentUser['user']==self.username and self.password == self.decipher(currentUser['pwd']):
                authenticationStatus['status']=True
                authenticationStatus['privilege']=currentUser['type']
                authenticationStatus['user']=currentUser['user']
                return authenticationStatus
        userBaseStorage.close()
        return authenticationStatus

    def encipher(self,pwd: str):
        encoded_bytes = cipher.b64encode(pwd.encode("utf-8"))
        encoded_string = encoded_bytes.decode("utf-8")
        return encoded_string

    
    def decipher(self,e_pwd: str):
        decoded_bytes = cipher.b64decode(e_pwd.encode("utf-8"))
        decoded_string = decoded_bytes.decode("utf-8")
        return decoded_string

    def userBaseValidation(self):
        userBaseStorage = open(os.getcwd()+self.userBaseFile, mode='r',encoding='utf-8')
        userBaseList = list(json.load(userBaseStorage))
        userBaseStorage.close()
        if len(userBaseList)<=1:
            return False
        else:
            return True

    def updateUserBase(self):
        if len(self.usertype) == 0:
            raise RuntimeError("Insufficient information to save the credentials")
        userBaseStorage = open(os.getcwd()+self.userBaseFile, mode='r',encoding='utf-8')
        userBaseList = list(json.load(userBaseStorage))
        userBaseList.append({
            "user": self.username,
            "pwd": self.encipher(self.password),
            "type": self.usertype
        })
        try:
            json.dump(userBaseList,userBaseStorage, indent=4)                           
            return True
        except Exception as e:
            print(e)
            return False


    def __repr__(self):
        return "User module for Quiz App"

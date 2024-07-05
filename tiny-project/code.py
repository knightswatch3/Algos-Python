import json as json
import os as os
class StudentDetails:
    # constructor
    def __init__(self, name: str, age: int, score: int):
        self.name = name
        self.age = age
        self.score = score
        self.log_file = 'tiny-project/details.txt'
        self.rangeFile = 'tiny-project/ranges.json'
    def validations(self, listofStudents, newStudentName: str):
        duplicates = [studentObject for studentObject in listofStudents if newStudentName in studentObject.values()]
        if len(duplicates)>0:
            return True
        return False

    # log details to details file
    def logDetails(self):
        log_file = open(self.log_file, mode='r', encoding='utf-8')
        if len(log_file.readlines())==0:
            log_file.close()
            writelog_file = open(self.log_file, mode='w', encoding='utf-8')
            writelog_file.write(f"-----Entry-----\n")
            writelog_file.write(f"Name: {self.name}\n")
            writelog_file.write(f"Age: {self.age}\n")
            writelog_file.write(f"Score: {self.score}\n")
            writelog_file.write(f"---------------\n")
            writelog_file.close()
        else:
            log_file.close()
            appendlog_file = open(self.log_file, mode='a', encoding='utf-8')
            appendlog_file.write(f"-----Entry-----\n")
            appendlog_file.write(f"Name: {self.name}\n")
            appendlog_file.write(f"Age: {self.age}\n")
            appendlog_file.write(f"Score: {self.score}\n")
            appendlog_file.write(f"---------------\n")
            appendlog_file.close()
    
    def fetchInformation(self, choice):
        final_file=None
        # Logic for fetching from log files
        if choice==True:
            log_file = open(self.log_file, mode='r', encoding='utf-8')
            print(type(log_file))
            file_content = ('').join(log_file.readlines()).split('\n')
            extractedInfo = [str(detail)+str('\n'+file_content[idx+1])+str('\n'+file_content[idx+2]) for idx,detail in enumerate(list(file_content)) if len(detail.split(':'))>1 and detail.split(':')[1].strip()==self.name]
            final_file = log_file
            if(len(extractedInfo)>0):
                
                print('''\n##### Information Found ! #####\n''',extractedInfo[0],'''\n##########\n''')
            else:
                print('''\n#### None found ! ####\n''')
            return 
        # Logic for fetching from range file
        else:
            log_file = open(self.rangeFile, mode='r', encoding='utf-8')
            dictionarizedData = json.load(log_file)
            for studentRange in dictionarizedData:
                extractedList = dictionarizedData[studentRange]
                if(len([detail for detail in extractedList if detail['Name']==self.name])>0):
                    print('''\n##### Given student falls in below range ! #####\n''',studentRange,'''\n##########\n''')
            final_file = log_file
        final_file.close()
        return


    # 280-289
    def ranger(self):
        keyExists = self.rangePartitioner()
        print(os.getcwd())
        rangeFile = open(self.rangeFile, mode='r', encoding='utf-8')
        if len(rangeFile.readlines())==0:
            #block to inject data
            dictionarizedData = {}
            rangeFile.close()
            writeRangeFile = open(self.rangeFile, mode='w', encoding='utf-8')
            
            dictionarizedData[keyExists]=[{"Name": self.name,
                                        "Age": self.age,
                                        "Score": self.score}]
            json.dump(dictionarizedData,writeRangeFile, indent=4)                           
            writeRangeFile.close()
            return
        rangeFile.close()
        updateRangefile = open(self.rangeFile, mode='r', encoding='utf-8')
        dictionarizedData = json.load(updateRangefile) 
        updateRangefile.close()
        updateRangefile = open(self.rangeFile, mode='w', encoding='utf-8')
        least_score_range = keyExists.split('-')[0]
        max_score_range = keyExists.split('-')[1]
        print('type ', type(max_score_range), 'with', type(self.score))
        if self.score >= int(least_score_range) and self.score < int(max_score_range):
            if keyExists in dictionarizedData:
                buffer = dictionarizedData[keyExists]
                if self.validations(dictionarizedData[keyExists], self.name):
                    raise RuntimeError('Duplicate identity entered ! Your name should be unique')
                    return
                buffer.append(dict({"Name": self.name,
                                        "Age": self.age,
                                        "Score": self.score,
                                        }))
                dictionarizedData[keyExists]=buffer
                json.dump(dictionarizedData,updateRangefile,ensure_ascii=False, indent=4)                           
            else:
                dictionarizedData[keyExists] = [dict({"Name": self.name,
                                        "Age": self.age,
                                        "Score": self.score,
                                        })]
             
                json.dump(dictionarizedData,updateRangefile,ensure_ascii=False, indent=4)                           
            updateRangefile.close()
        return

    def rangePartitioner(self):
        if 280 <= self.score <= 289:
            return '280-289'
        if 290 <= self.score <= 299:
            return '290-299'
        if 300 <= self.score <= 309:
            return '300-309'
        if 310 <= self.score <= 319:
            return '310-319'
        if 320 <= self.score <= 329:
            return '320-329'
        if 330 <= self.score <= 340:
            return '330-340'

def updateOperations():
    Name = input('Please enter your name:')
    Age = int(input('Please enter your age:'))
    Score = int(input('Please enter your score:'))
    if(Age<15 or Age > 120):
        print('Invalid age entered ! Please enter valid details')
        return
    if(Score<280 or Score > 340):
        print('Invalid score entered ! Please enter valid score')
        return
    else:
        studentInfo = StudentDetails(Name, Age, Score)
        try:
            studentInfo.ranger()
            print('saved details to the range lo file !')
            studentInfo.logDetails()
            print('Saved details to the log file !')
        except Exception as e:
            print(f'Oops ! looks like we hit a problem. {e}')

def readOperations():
    answer = int(input('''What do you want to perform ?\n 
                        ###############################\n
                        1.  Search my details from log file.\n
                        2.  What range do I fall in ?\n
                        ###############################\n 
                        Enter 1 or 2 only ! : \n
    '''))
    if answer not in [1,2]:
        print("Invalid read operation choice entered !")
        return
    else:
        answer = str(input(''' \n 1.  Enter the name to search: \n
'''))
        student = StudentDetails(answer,'<search>','<search>')
        if(answer==1):
            student.fetchInformation(True)
            return 
        else:
            student.fetchInformation(False)
            return


def executor():
    answer = int(input('''What do you want to perform ?\n 
                        ###############################\n
                        1.  Do-Entry\n
                        2.  Get-Information\n
                        ###############################\n 
                        Enter 1 or 2 only ! : \n
    '''))
    if answer not in [1,2]:
        executor()
    else:
        if answer==1:
            updateOperations()
        else:
            readOperations()   
    answer = str(input('Do you want to fetch info for name ? [y/n]'))
    if('y'==answer):
        executor()
    else:
        print('Session ends !')
        return


executor()
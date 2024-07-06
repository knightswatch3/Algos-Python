You have to make a Quiz application and have the following classes

Question - Should store the question text, the options to be presented to the user and the answer, score for the question

Quiz - s hould store a list of Question objects and for each question, the amount of duration for the quiz and other relevant information 

User - username and password and details of all the quizzes taken. 

When the application is run for the very first time, there is only one file which contains one user called "admin" and whose password is also "admin".

When the application runs you have to first tell the person to login into the system or sign up. 

The following options need to be provided when the admin logs in:
1. Create a question
2. Create a quiz. 

Whenever the above happens the details are added to respective files. You are free to choose the format in which you want to persist the data

When a user signs up, the details of that user is added to the users file which maintains the records of usernames and passwords

The user can attempt the quiz. You can keep track of how much time they actually took vs the actual duration and give a penalty of 5 points if they went above the time limit.

The user should also be able to see the details of all the quizzes they have attempted so far and show them how many correct and how many wrong they got and their score

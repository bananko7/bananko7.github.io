#
#   This code exists because the database that I am using is not clean. There are examples which do not contain ChatGPT answers or some other problems.
#   It does the same as "readjson.py" but does it a single time.
#   it will also prompt the user for a number, which will be the name of the file that it generates
#   I use this program when I need to remove a bad example from the database and generate a clean new one, which I can also review before uploading.
#   Several users have told me about questions without answers, which I quickly fixed by generating a valid example and uploading it in place of the bad one
#
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def generateexample():                                  # a function that I used for debugging, returns a 4-tuple with question,human answer, chatgpt answer and topic
    questionlist = generatequestionlist()
    currentquestion = random.choice(questionlist)
    return currentquestion.question,currentquestion.answerHUMAN,currentquestion.answerCGPT,currentquestion.topic

#import json
import random
class questionanswer:                                               # a class I use to save every example
    def __init__(self, question, answerHUMAN, answerCGPT, topic):
        self.question = question
        self.answerHUMAN = answerHUMAN
        self.answerCGPT = answerCGPT[1:]
        self.topic = topic
def generatequestionlist():

    questionslist = []
    file = open('D:/hons project/SECOND/HC3 dataset/all.jsonl','r', encoding="utf-8")
    jsonlines = file.readlines()
    file.close()
    for line in jsonlines:
        #print("QUESTION",line.split('\",\"')[0][13:],"QUESTION")
        #print("HUMAN ANSWERS",line.split('\":[\"')[1][:-19],"HUMAN ANSWERS")
        #print("CHATGPT ANSWERS",line.split('\"],\"chatgpt_answers\":[')[1].split("\"],\"index\"")[0],"CHATGPT ANSWERS")
        #print("TOPIC",line.split(",\"source\":\"")[1][:-3],"TOPIC")
        question = questionanswer(line.split('\",\"')[0][13:],line.split('\":[\"')[1][:-19],line.split('\"],\"chatgpt_answers\":[')[1].split("\"],\"index\"")[0],line.split(",\"source\":\"")[1][:-3])

        questionslist.append(question)
        #print(line)
        #json_acceptable_string = line.replace("'", "\"")
        #d = json.loads(json_acceptable_string)
        #print(type(d))
    return questionslist

if __name__ == "__main__":
    counter = 1
    while counter<=1:
        questionslisttest = generatequestionlist()
        currentquestion = random.choice(questionslisttest)
        cls()
        print("This is the question:")
        print(currentquestion.question)
        print("This is human answer(s):")
        print(currentquestion.answerHUMAN)
        print("This is ChatGPT answer(s):")
        print(currentquestion.answerCGPT)
        print("The topic is:")
        print(currentquestion.topic)
        #save = input("save or not?")                          # filter database mode
        save = 'y'
        if save == 'y':
            examplefile = open('D:/hons project/SECOND/HC3 dataset/newexamples/'+input("example number")+'.txt','w',encoding = 'utf-8')
            examplefile.write(currentquestion.question+"<>"+currentquestion.answerHUMAN.split("\",\"")[0]+"<>"+currentquestion.answerCGPT+"<>"+currentquestion.topic)
            examplefile.close()
            counter += 1
            print("okay, I've saved this one, here's a new example:")
        else:
            print("okay I've not saved this one, here's a new example:")



    file = open('D:/hons project/SECOND/HC3 dataset/all.jsonl','r', encoding="utf-8")
    lines = file.readlines()
    chars = 0
    numberoflines = 0
    for line in lines:
        numberoflines += 1
        chars = chars + len(line)
    print('lines:', numberoflines, 'chars:', chars)
    file.close()

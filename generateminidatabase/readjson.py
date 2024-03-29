#
#
#   This python code opens the json file containing the whole HC3 database
#   that the original authors of the study uploaded and saves it to individual files
#   that the JS code in my website opens and shows to the users
#   it generates 1000 txt files each of which contains an example
#   I've uploaded the 1000 files to github so that they can be used from everywhere and anyone
#
#
import os
def cls():                                          #this is a function that clears the console, I used it for cleaner debugging, it wes crucial to an earlier 
    os.system('cls' if os.name=='nt' else 'clear')  #version  of the code during which I was planning to manually clean the database from invalid examples

def generateexample():  # this function generates a random example and returns the question, topic and answers
    questionlist = generatequestionlist() # separately. used for debugging. not necessary anymore
    currentquestion = random.choice(questionlist)
    return currentquestion.question,currentquestion.answerHUMAN,currentquestion.answerCGPT,currentquestion.topic

#import json
import random
class questionanswer:
    def __init__(self, question, answerHUMAN, answerCGPT, topic):
        self.question = question
        self.answerHUMAN = answerHUMAN
        self.answerCGPT = answerCGPT[1:]
        self.topic = topic
        if topic == 'reddit_eli5': # these indexes are later used (row 64-65) to ensure an equal distribution among topics
            self.topicindex = 0
        if topic == 'medicine':
            self.topicindex = 1
        if topic == 'finance':
            self.topicindex = 2
        if topic == 'open_qa':
            self.topicindex = 3
        if topic == 'wiki_csai':
            self.topicindex = 4
def generatequestionlist(): 
    #this function opens the original dataset json file and creates a list of questionanswer objects that contain the <question,answer,answer> triples
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
    questionslisttest = generatequestionlist()
    while counter<=1000:
        #for j in range(50000000):      # uncomment this to have a bit of time to look at the examples
        #    pass                       # very much not recommended to use 
        currentquestion = random.choice(questionslisttest)
        while currentquestion.topicindex != counter%5:          # this ensures the equal distribution among topics
            currentquestion = random.choice(questionslisttest)  #
        cls()
        print("This is the question:")
        print(currentquestion.question)
        print("This is human answer(s):")                       # test prints
        print(currentquestion.answerHUMAN)                      # not needed
        print("This is ChatGPT answer(s):")
        print(currentquestion.answerCGPT)
        print("The topic is:")
        print(currentquestion.topic)
        #save = input("save or not?")                          # filter dataset mode
        save = 'y'
        if save == 'y':
            examplefile = open('D:/hons project/SECOND/HC3 dataset/newexamplesEQUAL2/'+str(counter)+'.txt','w',encoding = 'utf-8') 
            examplefile.write(currentquestion.question+"<>"+currentquestion.answerHUMAN.split("\",\"")[0]+"<>"+currentquestion.answerCGPT+"<>"+currentquestion.topic)
            examplefile.close() # newexamplesEQUAL and newexamplesEQUAL2 are the new equally distributed 1000 entry database sample that I generate (folder with 1000 files)
            counter += 1
            print("okay, I've saved this one, here's a new example:")
        else:
            print("okay I've not saved this one, here's a new example:")


    # the following code counts the number of lines and the chars that the program goes through
    # not necessary for project itself
    file = open('D:/hons project/SECOND/HC3 dataset/all.jsonl','r', encoding="utf-8")
    lines = file.readlines()
    chars = 0
    numberoflines = 0
    for line in lines:
        numberoflines += 1
        chars = chars + len(line)
    file.close()
    print('lines:', numberoflines, 'chars:', chars)

#       This code can be used to find a bad example
#   replace the string named 'question' with prefferably a big 
#   part of the question(or answer/s) in the example you want to find
#   when you know the index of the file that you need to replace you can
#   use generatenewexample.py to generate a new example and replace it in your database
#
question = "who actually owns the internet and if not why does n't anyone actually own it ? with the creation of something there is usually an owner of it that runs it as a business so what happened with the internet ? Explain like I'm five."
for i in range(1,1001):
    file = open("D:/hons project/SECOND/HC3 dataset/newexamplesEQUAL/"+str(i)+".txt","r",encoding = "utf-8") #replace this location with the location of your sample database (1000 '.txt' files)
    line = file.readlines()[0]
    if question in line:# finds the string and prints the index that you need
        print(i) 
question = "who actually owns the internet and if not why does n't anyone actually own it ? with the creation of something there is usually an owner of it that runs it as a business so what happened with the internet ? Explain like I'm five."
for i in range(1,1001):
    file = open("D:/hons project/SECOND/HC3 dataset/newexamples/"+str(i)+".txt","r",encoding = "utf-8")
    line = file.readlines()[0]
    if question in line:
        print(i)
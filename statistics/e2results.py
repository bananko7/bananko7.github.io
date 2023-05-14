#       This file works with and only with E2results.txt
#   to add new entries to the E2results.txt file, just copy and paste them on a NEW LINE
#   and run e2results.py again
#   This code parses the entries that my webpage returns when someone completes the replication experiment
#   Then outputs a table analogous to the one in the original experiment
#
resultsfile = open("E2results.txt","r",encoding = "utf-8")      # open E2results.py and load the entries to a list
resultslines = resultsfile.readlines()
class experiment:                                               # this is a class for the 3 turing test variants
    def __init__(self,data):
        self.data = data
        self.redditguessed = 0
        self.redditoverall = 0
        self.financeguessed = 0
        self.financeoverall = 0
        self.medicineguessed = 0
        self.medicineoverall = 0
        self.openqaguessed = 0
        self.openqaoverall = 0
        self.wikiguessed = 0
        self.wikioverall = 0
        for score in data:                                       # here I count the scores for each entry
            if score[0] == "r":
                if score[1] == "1":
                    self.redditguessed += 1
                    self.redditoverall += 1
                if score[1] == "0":
                    self.redditoverall += 1
            
            if score[0] == "f":
                if score[1] == "1":
                    self.financeguessed += 1
                    self.financeoverall += 1
                if score[1] == "0":
                    self.financeoverall += 1
            
            if score[0] == "m":
                if score[1] == "1":
                    self.medicineguessed += 1
                    self.medicineoverall += 1
                if score[1] == "0":
                    self.medicineoverall += 1
            
            if score[0] == "o":
                if score[1] == "1":
                    self.openqaguessed += 1
                    self.openqaoverall += 1
                if score[1] == "0":
                    self.openqaoverall += 1
            
            if score[0] == "w":
                if score[1] == "1":
                    self.wikiguessed += 1
                    self.wikioverall += 1
                if score[1] == "0":
                    self.wikioverall += 1
        self.guessedoverall = self.redditguessed+self.financeguessed+self.medicineguessed+self.openqaguessed+self.wikiguessed
        self.overall = self.redditoverall+self.financeoverall+self.medicineoverall+self.openqaoverall+self.wikioverall
        self.ratio = round(self.guessedoverall/self.overall,2)
        self.redditratio = round(self.redditguessed/self.redditoverall,2)
        self.financeratio = round(self.financeguessed/self.financeoverall,2)
        self.medicineratio = round(self.medicineguessed/self.medicineoverall,2)
        self.openqaratio = round(self.openqaguessed/self.openqaoverall,2)
        self.wikiratio = round(self.wikiguessed/self.wikioverall,2)
class ehtexperiment():              # due to the structure of the helpfulness test, I needed to edit the class a bit 
    def __init__(self,data):        # in this test, scores are organised in a way that h means that the human response was preferred
        self.data = data            # and c means that the chatgpt response was preferred
        self.redditCpref = 0        # this class is very similar to the experiment class
        self.redditHpref = 0
        self.financeCpref = 0
        self.financeHpref = 0
        self.medicineCpref = 0
        self.medicineHpref = 0
        self.openqaCpref = 0
        self.openqaHpref = 0
        self.wikiCpref = 0
        self.wikiHpref = 0
        for score in data:
            if score[0] == "r":
                if score[1] == "c":
                    self.redditCpref += 1
                if score[1] == "h":
                    self.redditHpref += 1
            
            if score[0] == "f":
                if score[1] == "c":
                    self.financeCpref += 1
                if score[1] == "h":
                    self.financeHpref += 1
            
            if score[0] == "m":
                if score[1] == "c":
                    self.medicineCpref += 1
                if score[1] == "h":
                    self.medicineHpref += 1
            
            if score[0] == "o":
                if score[1] == "c":
                    self.openqaCpref += 1
                if score[1] == "h":
                    self.openqaHpref += 1
            
            if score[0] == "w":
                if score[1] == "c":
                    self.wikiCpref += 1
                if score[1] == "h":
                    self.wikiHpref += 1
        self.Cprefoverall = self.redditCpref+self.financeCpref+self.medicineCpref+self.openqaCpref+self.wikiCpref
        self.Hprefoverall = self.redditHpref+self.financeHpref+self.medicineHpref+self.openqaHpref+self.wikiHpref
        self.ratioC = round(self.Cprefoverall/(self.Cprefoverall+self.Hprefoverall),2)
        self.ratioH = round(self.Hprefoverall/(self.Cprefoverall+self.Hprefoverall),2)
        
        self.redditratio = round(self.redditCpref/(self.redditCpref+self.redditHpref),2)
        self.financeratio = round(self.financeCpref/(self.financeCpref+self.financeHpref),2)
        self.medicineratio = round(self.medicineCpref/(self.medicineCpref+self.medicineHpref),2)
        self.openqaratio = round(self.openqaCpref/(self.openqaCpref+self.openqaHpref),2)
        self.wikiratio = round(self.wikiCpref/(self.wikiCpref+self.wikiHpref),2)
etsscores = []      # lists in which the code puts ALL of the scores for a given type of test
etpscores = []
ehtscores = []
atsscores = []

for line in resultslines:                                                           # for every line, depending on the type of experiment that it represents
    if line.startswith("ETS"):                                                      # adds the scores. This creates a big string of scores for each type of test
        etsscores += [line[3:][i:i + 2] for i in range(0, len(line[3:]), 2)][:-1]   # which is evaluated when the ets,etp,eht,ats objects are created on rows 131-134
    if line.startswith("ETP"):
        etpscores += [line[3:][i:i + 2] for i in range(0, len(line[3:]), 2)][:-1]
    if line.startswith("EHT"):                                                 
        ehtscores += [line[3:][i:i + 2] for i in range(0, len(line[3:]), 2)][:-1]
    if line.startswith("ATS"):
        atsscores += [line[3:][i:i + 2] for i in range(0, len(line[3:]), 2)][:-1]

ets = experiment(etsscores)         #Expert Turing test Single-text
etp = experiment(etpscores)         #Expert Turing test Paired-text
eht = ehtexperiment(ehtscores)      #Expert Helpfulness Test
ats = experiment(atsscores)         #Amateur Turing test Single-text
print("expert turing test single detection rate:",  ets.guessedoverall,"out of",ets.overall,"ratio",round(ets.guessedoverall/ets.overall,2))
print("expert turing test paired detection rate:",  etp.guessedoverall,"out of",etp.overall,"ratio",round(etp.guessedoverall/etp.overall,2))
print("amateur turing test single detection rate:", ats.guessedoverall,"out of",ats.overall,"ratio",round(ats.guessedoverall/ats.overall,2))
print("result from all turing tests combined:",ets.guessedoverall+etp.guessedoverall+ats.guessedoverall,"out of",ets.overall+etp.overall+ats.overall,"ratio",round((ets.guessedoverall+etp.guessedoverall+ats.guessedoverall)/(ats.overall+etp.overall+ets.overall),2))

print("number of times that users considered the ChatGPT answer more helpful:",eht.Cprefoverall)
print("number of times that users considered the Human answer more helpful:",  eht.Hprefoverall)
print("as ratios, respectively:",eht.ratioC,"and",eht.ratioH)
print("=====================================================================")
print("Human evaluation","Pair-expert","Single-expert","Single-amateur","Helpfulness") # output table analogous to the one in the original experiment
print("All             ",etp.ratio,"      ",         ets.ratio,"        ",         ats.ratio,"         ",        eht.ratioC)
print("reddit_eli5     ",etp.redditratio,"      ",   ets.redditratio,"        ",   ats.redditratio,"         "  ,eht.redditratio)
print("open_qa         ",etp.openqaratio,"       ",  ets.openqaratio,"         ",  ats.openqaratio,"         ",  eht.openqaratio)
print("wiki-csai       ",etp.wikiratio,"       ",    ets.wikiratio,"         ",    ats.wikiratio,"         ",   eht.wikiratio)
print("medicine        ",etp.medicineratio,"       ",ets.medicineratio,"         ",ats.medicineratio,"         ",eht.medicineratio)
print("finance         ",etp.financeratio,"       ", ets.financeratio,"        ",  ats.financeratio,"         ", eht.financeratio)

import OrderedDict

def init():
    MyDict= OrderedDict.OrderedDict()
    MyDict.createDict()
    return MyDict

def inputting():
    string= input("Input Alphabets: ")
    return string.lower().replace("qu", "q")

def main(string, MyDict):
    if string == "quit" :
        return
    else :
        candidates= MyDict.searchDict(string)

    highest= 0
    highestString= ""

    for eachCandidates in candidates:
        scores= scoring(eachCandidates)
        if scores > highest:
            highest= scores
            highestString= eachCandidates

    print("the best one is {} with score {} ".format(highestString, highest))

    return highestString, highest


def scoring(word):
    onePoint= "abdeginorstu"
    twoPoints= "cfhlmpvwy"
    threePoints= "jkqxz"
    score= 0

    for eachChar in word[0]:
        score+= onePoint.count(eachChar)
        score+= (twoPoints.count(eachChar))*2
        score+= (threePoints.count(eachChar))*3
    if score != 0:
        score+= 1
    return score**2

if __name__ == '__main__':
    string = inputting()
    MyDict = init()
    main(string, MyDict)
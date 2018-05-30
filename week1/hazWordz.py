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
    highest_string= ""

    for each_candidates in candidates:
        scores= scoring(each_candidates)
        if scores > highest:
            highest= scores
            highest_string= each_candidates

    print("the best one is {} with score {} ".format(highest_string, highest))

    return highest_string, highest


def scoring(word):
    onePoint= "abdeginorstu"
    twoPoints= "cfhlmpvwy"
    threePoints= "jkqxz"
    score= 0

    for each_char in word[0]:
        score+= onePoint.count(each_char)
        score+= (twoPoints.count(each_char))*2
        score+= (threePoints.count(each_char))*3
    if score != 0:
        score+= 1
    return score**2

if __name__ == '__main__':
    string = inputting()
    MyDict = init()
    main(string, MyDict)
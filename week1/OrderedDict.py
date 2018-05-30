import re

class OrderedDict:
    # Create NULL Dictionary
    def __init__(self):
        self.dictionary= dict()

    # Sort each word in alphabet order
    def alphaSort(self, word):
        return ''.join(sorted(word.lower()))

    # Read Dictionary file and create dict with anagram
    def createDict(self):
        with open("dictionary.txt", "r") as fp:
            for line in fp:
                word= line.strip('\n').replace("qu", "q")
                orderedWord= self.alphaSort(word)
                if orderedWord in self.dictionary :
                    self.dictionary[orderedWord].append(word)
                else :
                    self.dictionary[orderedWord]= [word]

    def searchDict(self, inputted):
        candidates= []
        orderedInput= self.alphaSort(inputted)

        for key, value in self.dictionary.items():
            check= True
            tmpString = orderedInput

            # break the for-loop once there are no more characters in string to match
            for each_alphabet in key:
                if each_alphabet not in tmpString:
                    check= False
                    break
                else:
                    tmpString= tmpString.replace(each_alphabet, "", 1)  #Replace only one time
            if check == True:
                candidates.append(value)
        return candidates

    def printDict(self):
        print(self.dictionary)

from collections import defaultdict

class createDict:
    def __init__(self):
        # if v>u than regular, u>v than reverse
        self.regularGraph= defaultdict(list)
        self.fullConnected= defaultdict(list)
        self.nameList= defaultdict(list)

    def readFiles(self, path):
        print("start creating dictionary ...")
        fp_links= open(path+"links.txt", 'r')
        fp_pages= open(path+"pages.txt", 'r')
        regularEnd= -1

        for line in fp_links:
            [u, v]= line.split()
            if int(u)> int(v):
                if v in self.regularGraph.keys() and u in self.regularGraph[v]:
                    if v in self.fullConnected.keys():
                        self.fullConnected[v].append(u)
                    else:
                        self.fullConnected[v]= [u]
            else:
                if u != regularEnd:
                    self.regularGraph[u]= [v]
                    regularEnd= u
                else:
                    self.regularGraph[u].append(v)

        for line in fp_pages:
            [u, v]= line.split()
            if u in self.fullConnected.keys():
                self.nameList[u]=[v]

        fp_links.close()
        fp_pages.close()

    def getGraph(self):
        return self.fullConnected

    def getNameList(self):
        return self.nameList

    def numberOfKeys(self):
        return len(self.fullConnected)

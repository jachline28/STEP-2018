import Mydict
import time
def __main__():
    start= time.time()
    Dict= Mydict.createDict()
    Dict.readFiles(path="wikipedia_links/")
    print("start finding maximun duplex route ...")
    result, length= maxDuplex(Dict.getGraph(), Dict.numberOfKeys(), Dict.getNameList())
    end= time.time()
    print("The longest is {} with length {}".format(result, length))
    print("Spent {}:{}".format( int((end-start)/60), (end-start)%60) )

#Greedy method to color all vertex
def maxDuplex(Graph, length, nameList):
    # sort with degree
    sortedNodes= sorted(Graph, key=lambda k: len(Graph[k]), reverse= True)
    longest_len= -1
    longest= []
    for key in sortedNodes:
        visited= dfs(Graph, key, [], [key])
        curr_longest_len= max(len(ans) for ans in visited)
        curr_longest = [ans for ans in visited if len(ans) == curr_longest_len]
        if curr_longest_len > longest_len:
            longest_len= curr_longest_len
            longest= curr_longest
        elif curr_longest_len == longest_len:
            longest.append(curr_longest)

    return longest, longest_len

def dfs(Graph, node, visited, path):
    visited.append(node)
    paths= []
    for pairs in Graph[node]:
        if pairs not in visited:
            temp= path+[pairs]
            paths.append(temp)
            paths.extend(dfs(Graph, pairs, visited[:], temp))
    return paths

if __name__ == '__main__':
    __main__()
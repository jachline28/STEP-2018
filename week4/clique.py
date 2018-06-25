import Mydict
import time
def __main__():
    start= time.time()
    Dict= Mydict.createDict()
    Dict.readFiles(path="wikipedia_links/")
    nameList= Dict.getNameList()
    middle= time.time()
    print("Spent {}s to create dictionary".format(middle-start))
    print("start finding maximun duplex route ...")

    key= input("Input a number> ")
    result, length= oneDuplex(Dict.getGraph(), key)
    if result == None:
        print("No duplex node for page {}".format(key))
        return

    end= time.time()
    result_name= [nameList[key]]
    for i in result:
        for each in i:
            result_name.append(nameList[each])
    print("The longest is {} with length {}".format(result_name, length))
    print("Spent {}s".format( (end-start)%60) )

#def maxDuplex(Graph, length):
#    sortedNodes= sorted(Graph, key=lambda k: len(Graph[k]), reverse= True)
#    longest_len= -1
#    longest= []
#    for key in sortedNodes:
#        visited= dfs(Graph, key, [], [key])
#        curr_longest_len= max(len(ans) for ans in visited)
#        curr_longest = [ans for ans in visited if len(ans) == curr_longest_len]
#        if curr_longest_len > longest_len:
#            longest_len= curr_longest_len
#            longest= curr_longest
#        elif curr_longest_len == longest_len:
#            longest.append(curr_longest)

#    return longest, longest_len

def oneDuplex(Graph, key):
    visited= dfs(Graph, key, [key], [])
    if visited == []:
        return None, 0
    curr_longest_len= max(len(ans) for ans in visited)
    curr_longest = [ans for ans in visited if len(ans) == curr_longest_len]
    return curr_longest, curr_longest_len

def dfs(Graph, key, visited, path):
    visited.append(key)
    paths = []
    for t in Graph[key]:
        if t not in visited:
            t_path = path + [t]
            paths.append(t_path)
            if len(paths) > 20:
                return paths
            paths.extend(dfs(Graph, t, visited[:], t_path))
    return paths

if __name__ == '__main__':
    __main__()
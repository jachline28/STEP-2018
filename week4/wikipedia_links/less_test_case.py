
def __main__():
    limitation= 100


    count= 0
    smallFp= open('less_links.txt', 'w')
    with open ('links.txt', 'r') as fp:
        for line in fp:
            [u, v]= line.split()
            if int(u) >= limitation:
                break
            else:
                if int(v) > limitation:
                    continue
                else:
                    smallFp.write(line)
                    count+= 1

    smallFp.close()
    print("{} links in total".format(count))
    smallPageFp= open('less_pages.txt', 'w')

    with open('pages.txt', 'r') as fp:
        for i in range(limitation):
            smallPageFp.write(fp.readline())

    smallPageFp.close()

if __name__ == "__main__":
    __main__()
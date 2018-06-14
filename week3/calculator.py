#This code is wrote by Python 3
symbol= {'+': 'PLUS',
         '-': 'MINUS',
         '*': 'MUL',
         'x': 'MUL',
         '/': 'DIV',
         '%': 'MOD',
         '^': 'POW',
         '(': 'LPAR',
         ')': 'RPAR'
}

def readNumber(line, index):
    number = 0
    flag = 0
    keta = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + int(line[index])
            if flag == 1:
                keta *= 0.1
        index += 1
    token = {'type': 'NUMBER', 'number': number * keta}
    return token, index

# (index+1) to move forward for the foor loop
def readSymbol(line, index):
    eachType= symbol[line[index]]
    return {'type': eachType}, index+1

def tokenize(line):
    line= "".join(line.split())
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] in symbol:
            (token, index) = readSymbol(line, index)
        else:
            print('Invalid character found: '.format(line[index]))
            exit(1)
        tokens.append(token)
    return tokens

def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1

    # Do MULtiplication and Division first
    while index < len(tokens):
        if tokens[index]['type'] in {'MUL', 'DIV'}:
            temp= 0
            if tokens[index]['type'] == 'MUL':
                temp = tokens[index -1]['number'] * tokens[index+ 1]['number']
            elif tokens[index]['type'] == 'DIV':
                #print("in div with token {}".format(tokens[index]))
                if tokens[index+ 1]['number'] == 0:
                    print('>> 0 cannott be a denominator')
                    return False
                temp = tokens[index-1]['number'] / tokens[index+ 1]['number']
            tokens[index-1:index+2] = [{'type':"NUMBER", 'number':temp}]
        else:
            index += 1
#    print(tokens)

    index= 1
    #Do Plus and Minus second
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
#           else:
#               print('Invalid syntax')
        index += 1

    return answer

def division(tokens):
    noParTokens= []
    ParExist= False
    index= 0
    leftIndex= [] # Stack to store all left paranthesis index

    # copy part not in paranthesis
    while index < len(tokens):
        if tokens[index]['type'] == 'LPAR':
            ParExist= True
            noParTokens= tokens[:index]
            break
        elif tokens[index]['type'] == 'RPAR':
            print('paranthesis are not pairwise ')
            return False
        index+= 1

    # no paranthesis case
    if not ParExist:
        return evaluate(tokens)

    # Start from index == LPAR, must have
    while index < len(tokens):
        if tokens[index]['type'] == 'LPAR':
            leftIndex.append(index)
        elif leftIndex == []:
            noParTokens.append(tokens[index])
        elif tokens[index]['type'] == 'RPAR':
            if leftIndex == []:
                print('paranthesis are not pairwise ')
                return False
            left= leftIndex.pop()
            result= evaluate(tokens[left+1:index])
            if leftIndex != []:                       #exist outer left parenthesis
                tokens[left:index+1]= [{'type':"NUMBER", 'number':result}]
                index -= (index-left)
            else:                                   #left one parenthesis
                noParTokens.append({'type':"NUMBER", 'number':result})
        index+= 1

    if leftIndex!= []:
        print('paranthesis are not pairwise ')
        return False

    #print("no par tokens is {}".format(noParTokens))
    return evaluate(noParTokens)



def test(line, expectedAnswer):
    print("test {}".format(line))
    tokens = tokenize(line)
    actualAnswer = division(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! ({} = {})".format(line, expectedAnswer))
    else:
        print("FAIL! ({} should be {} but was {})".format(line, expectedAnswer, actualAnswer))


# Add some special cases
#### Strip all weird whitespaces
#### Multi-use of symbol of multiplication "*" and "x"
#### Multiple multiplication and division allowed
#### Detection of demominator as zero
#### Paranthesis Faliure

def runTest():
    print("==== Test started! ====")
    test("1", 1)
    test("1+2", 3)
    test("1 +2 ", 3)
    test("1.0+2-5", -2)
    test("1x4+6/5", 5.2)
    test("1.2x3- 4/5.0",2.8)
    test("1. 5 x 2+4x2x2", 19)
    test("1x4+6*5", 34)
    test("100x4/10/80", 0.5)
    test("1x2x3x4/0", False)

    test("2x(3+1)",8)
    test("1.0*(2+4)-(0.5*2+1)/2.0",5.0)
    test("10/(8-12/(8/2-1))",2)

    test("(", False)
    test("20/((10*1)-(90/10)",False)
    test("2*3*4)", False)
    print("==== Test finished! ====\n")

def main():
    runTest()
    while True:
        line = input('>')
        tokens = tokenize(line)
        answer = evaluate(tokens)
        print("answer = {}\n".format(answer))

if __name__ == '__main__':
    __main__()
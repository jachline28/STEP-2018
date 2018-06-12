import sys

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
def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index+1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index+1

def readMul(line, index):
    token= {'type': 'MUL'}
    return token, index+1

def readDiv(line, index):
    token= {'type': 'DIV'}
    return token, index+1


def tokenize(line):
    line= "".join(line.split())
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] in ('x', '*'):
            (token, index) = readMul(line, index)
        elif line[index] == '/':
            (token, index) = readDiv(line, index)
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
        if tokens[index]['type'] in ('MUL', 'DIV'):
            temp= 0
            if tokens[index]['type'] == 'MUL':
                temp = tokens[index -1]['number'] * tokens[index+ 1]['number']
            elif tokens[index]['type'] == 'DIV':
                if tokens[index+ 1]['number'] == 0:
                    print('0 cannott be a denominator')
                    return sys.maxsize
                temp = tokens[index-1]['number'] / tokens[index+ 1]['number']
            tokens[index-1:index+2] = [{'type':"NUMBER", 'number':temp}]
        index += 1
    print(tokens)
    index= 0
    #Do Plus and Minus second
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
        index += 1

    return answer


def test(line, expectedAnswer):
    print("test {}".format(line))
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! ({} = {})".format(line, expectedAnswer))
    else:
        print("FAIL! ({} should be {} but was {})".format(line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print("==== Test started! ====")
    test("1", 1)
    test("1+2", 3)
    test("1 +2 ", 3)
    test("1.0+2-5", -2)
    test("1x4+6/5", 5.2)
    test("1.2x3- 4/5.0",2.8)
    #test("1. 5 x 2+4x2x2", 19)
    #test("1x2x3x4/0", 0)
    #test("3++2", 5)
    print("==== Test finished! ====\n")

runTest()

while True:
    print('> ')
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = {}\n".format(answer))

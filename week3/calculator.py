#This code is wrote by Python 3
import math

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
hexString= {'a':10, 'A':10, 'b':11, 'B':11, 'c':12, 'C':12, 'd':13, 'D':13, 'e':14, 'E':14, 'f':15, 'F':15}
numericalSystem= {"bi":2, "oct":8, "des":10, "hex":16}

def readNumber(line, index, currentSystem):
    number = flag = 0
    keta = 1
    base = numericalSystem[currentSystem]
    while index < len(line) and (line[index].isdigit() or line[index] == '.' or line[index] in hexString):
        if line[index] == '.':
            flag = 1
        else:
            if line[index] in hexString:
                digit= hexString[line[index]]
            else:
                digit= int(line[index])
            number = number * base + digit
            if flag == 1:
                keta *= 0.1
        index += 1
    token = {'type': 'NUMBER', 'number': number * keta}
    return token, index

# (index+1) to move forward for the foor loop
def readSymbol(line, index):
    eachType= symbol[line[index]]
    return {'type': eachType}, index+1

def tokenize(line, currentSystem):
    line= "".join(line.split())
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit() or (line[index] in hexString):
            (token, index) = readNumber(line, index, currentSystem)
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
        if tokens[index]['type'] in {'MUL', 'DIV', 'MOD', 'POW'}:
            temp= 0
            if tokens[index]['type'] == 'MUL':
                temp = tokens[index -1]['number'] * tokens[index+ 1]['number']
            elif tokens[index]['type'] == 'DIV':
                if tokens[index+ 1]['number'] == 0:
                    print('>> 0 cannot be a denominator')
                    return False
                temp = tokens[index-1]['number'] / tokens[index+ 1]['number']
            elif tokens[index]['type'] == 'MOD':
                if tokens[index+ 1]['number'] == 0:
                    print('>> 0 cannot be a divisor')
                    return False
                temp= tokens[index-1]['number']% tokens[index+ 1]['number']
            elif tokens[index]['type'] == 'POW':
                temp= math.pow(tokens[index-1]['number'], tokens[index+ 1]['number'])
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
            else:
                print('Invalid syntax')
        index += 1

    return answer

def division(tokens):
    noParTokens= []
    ParExist= False
    index= 0
    leftIndex= [] # Stack to store all left parenthesis index

    # copy part not in parenthesis
    while index < len(tokens):
        if tokens[index]['type'] == 'LPAR':
            ParExist= True
            noParTokens= tokens[:index]
            break
        elif tokens[index]['type'] == 'RPAR':
            print('>> parenthesis are not pairwise ')
            return False
        index+= 1

    # no parenthesis case
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
                print('>> parenthesis are not pairwise ')
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
        print('>> parenthesis are not pairwise ')
        return False

    #print("no par tokens is {}".format(noParTokens))
    return evaluate(noParTokens)

# Function for converting between numerical system
def printAnswer(answer, system):
    if system == "des":
        print("answer = {}\n".format(answer))
    elif system == "bi":
        print("answer = {0:b}\n".format(answer))
    elif system == "oct":
        print("answer = {0:o}\n".format(answer))
    elif system == "hex":
        print("answer = {0:x}\n".format(answer))

def test(line, expectedAnswer):
    print("test {}".format(line))
    tokens = tokenize(line, "des")
    actualAnswer = division(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! ({} = {})".format(line, expectedAnswer))
    else:
        print("FAIL! ({} should be {} but was {})".format(line, expectedAnswer, actualAnswer))

# Add some special cases
#### Strip all weird whitespaces
#### Multi-use of symbol of multiplication "*" and "x"
#### Detection of demominator as zero
#### parenthesis Faliure

def runTest():
    print("==== Test started! ====")
    test("1", 1)
    test("1+2", 3)
    test("1 +2 ", 3)
    test("1.0+2-5", -2)
    test("1x4+6/5", 5.2)
    test("1. 5 x 2+4x2x2", 19)
    test("1x2x3x4/0", False)
    test("10%7-2^2", -1)
    test("0%10", False)

    test("2x((3+1)^2)",32)
    test("1.0*(2+4)-(0.5*2+1)%2",6.0)
    test("10/(8-12/(8/2-1))",2.5)

    test("(", False)
    test("20/((10*1)-(90/10)",False)
    test("2*3*4)", False)

    print("==== Test finished! ====\n")

def graph():
    print(" ______     ______     __         ______     __  __     __         ______     ______   ______     ______   ")
    print("/\\  ___\\   /\\  __ \\   /\\ \\       /\\  ___\\   /\\ \\/\\ \\   /\\ \\       /\\  __ \\   /\\__  _\\ /\\  __ \\   /\\  == \\  ")
    print("\\ \\ \\____  \\ \\  __ \\  \\ \\ \\____  \\ \\ \\____  \\ \\ \\_\\ \\  \\ \\ \\____  \\ \\  __ \\  \\/_/\\ \\/ \\ \\ \\/\\ \\  \\ \\  __<  ")
    print(" \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_____\\  \\ \\_____\\  \\ \\_____\\  \\ \\_____\\  \\ \\_\\ \\_\\    \\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\ ")
    print("  \\/_____/   \\/_/\\/_/   \\/_____/   \\/_____/   \\/_____/   \\/_____/   \\/_/\\/_/     \\/_/   \\/_____/   \\/_/ /_/ ")
    print("")
    print("Welcome to my calculator! Please enter any mathematical formula.")
    help()
    print("Start Calculation!")
    print("")

def help():
    print("We support: Arithmetic Operators, Power, Modulo Calculation, Parenthesis Usage and Decimal to Binary, octal, hexadecimal systems")
    print("Arithmetic Operators Symbols:                 +, -, * or x, / ")
    print("Power:                                        ^")
    print("Modulo Calculation:                           %")
    print("Numeral System Convertor Keyword:             bi, oct, des, hex")
    print("Quit the calculator:                          quit")
    print("Help:                                         help")
    print("____________________________________________________________________")

def __main__():
    runTest()
    # ASCII art
    graph()
    currentSystem= "des"     #default

    while True:
        line = input('({})>'.format(currentSystem))
        if line == 'quit':
            break
        elif line == 'help':
            help()
            continue
        elif (line in numericalSystem) and (line != currentSystem):
            currentSystem= line
            continue
        tokens = tokenize(line, currentSystem)
        answer = division(tokens)
        printAnswer(answer, currentSystem)

if __name__ == '__main__':
    __main__()
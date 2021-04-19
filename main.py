from array import *
class Automata:
    states = []
    symbols = []
    initialState = ""
    finalState = []
    transitionTable = []


def buildAutomata(file):
    with open(file) as f:
            lines = f.readlines();

    A1 = Automata()

    count = 0
    for line in lines:
        count += 1
        #print(f'line {count}: {line}')

    #print("Total de lineas: " + str(count))

    #separating each state and adding it to an array
    states = lines[0].split(",")
    #print("States: " + str(states))

    A1.states = states

    #Separate alphabet symbols
    symbols = lines[1].split(",")
    #print("Symbols: " + str(symbols))
    A1.symbols = symbols

    #Assign inital state
    initialState = lines[2].split(",")
    initialState = ''.join(initialState).strip()
    #print("Initial State: " + str(initialState))
    A1.initialState =  initialState


    #Assign final state
    finalState = lines[3].split(",")
    #print("Final State: " + str(finalState))
    A1.finalState = finalState;

    #for i in range(8):
    #    print(lines[i+4])

    #Create the transition
    transitionTable = []

    for j in range(count):
        #print(j)
        if j > 3:
            transitionTable += lines[j].split('\n')

    while("" in transitionTable):
        transitionTable.remove("")

    sizeOfTT = len(transitionTable) #Save the size of the transition table to a variable
    #print(transitionTable)
    A1.transitionTable = transitionTable


    return A1


def validateString(string):
    string = string.split(",")
    print("String: "+ str(string))

    #print(var2)
    #print(nextState)
    count = 0
    transitionMatrix = []
    if Automata.initialState == "q0":
        #print("Los strings son iguales")
        for i in Automata.transitionTable:
            var1, var2 = Automata.transitionTable[count].split("=>")
            #var1 = "".join(var1)
            #var1.strip("=")
            nextState = var2.split(",")
            #print("Var1: " + str(var1))
            state, symbol = var1.split(",")
            #print(count)
            print("State: "+ str(state)+ " Symbol: "+ str(symbol) + " Regresa:" + str(nextState))
            transitionMatrix += [[state, symbol, nextState]]
            count+=1
        print(transitionMatrix)
        #temp = transitionMatrix[0][2]
        checkTransition(string, transitionMatrix, Automata.initialState)
    else:
        print("Error: Automata initial state is not q0")


def checkTransition(string, matrix, estado):
    #print("Letra: " + str(leter))
    m = matrix
    #print("Matriz: " + str(matrix[0]))
    print("Estado a validar: "+ str(estado))
    print("String a validar: " + str(string))
    c = 0
    
    
    for i in matrix:
        temp = matrix[c]
        st = temp[0]
        sym = temp[1]
        res = temp[2]
        c+=1
        #print("State: "+ str(st) + " Symbol: " + str(sym)+ " Regresa: " + str(res))
        if estado == st and sym == "lambda":
            estado = res
            print("Estado a regresar: " + str(estado))
            checkTransition(string[0], m, estado)
        if len(estado)>1:
            p = 0
            for k in estado:
                #print(estado[p])
                if estado[p] == st and sym == string[0]:
                    e = res
                    #print("Estado en p: "+ str(estado[p]))
                    #estado[p] == res
                    print("Estado a regresar cuando son mas 2 estados: " + str(e))
                    checkTransition('b', m, e[0])
                #print("P: " + str(p))
                p+=1
        if estado == st and sym == string[0]:
            estado = res
            print("Estado a regresar" + str(estado))
            checkTransition('b', m, estado[0])


if __name__ == "__main__":
    #print("Se corrio el main")
    Automata = buildAutomata('test1.txt') #Method that receives the name of the file to use and returns an Automata class

    #print(Automata.states)
    #print(Automata.symbols)
    #print(Automata.initialState)
    #print(Automata.finalState)
    print(Automata.transitionTable)

    #string = input("Input a string separated by commas: ")
    validateString('b,b,a')
    

    
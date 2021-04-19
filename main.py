
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
    if Automata.initialState == "q0":
        print("Los strings son iguales")
        for i in Automata.transitionTable:
            var1, var2 = Automata.transitionTable[count].split("=>")
            #var1 = "".join(var1)
            #var1.strip("=")
            nextState = var2.split(",")
            #print("Var1: " + str(var1))
            state, symbol = var1.split(",")
            #print(count)
            count+=1
            print("State: "+ str(state)+ " Symbol: "+ str(symbol) + " Regresa:" + str(nextState))
            if len(nextState) > 1:
                #print("El estado sig es valido")
                if state == "q3":
                    print("El estado es q1")
            
    else:
        print("Error: Automata initial state is not q0")

if __name__ == "__main__":
    #print("Se corrio el main")
    Automata = buildAutomata('test1.txt') #Method that receives the name of the file to use and returns an Automata class

    #print(Automata.states)
    #print(Automata.symbols)
    #print(Automata.initialState)
    #print(Automata.finalState)
    #print(Automata.transitionTable)

    #string = input("Input a string separated by commas: ")
    validateString('b,b,a')
    

    
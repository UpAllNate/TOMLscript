import tomli
from time import sleep

"""
The run toml will have all of the highest level code
Python is then, sort of, an interpreter
"""
run = tomli.load(open('run.toml', 'rb'))

"""
This function allows a list to define the absolute
path to a dictionary location.
We'll use it to point to run.toml locations
"""
def getDVal( dictionary : dict, path : list):
    for key in path:
        dictionary = dictionary[key]
    return dictionary

"""
This portion of the code contains all of the supported functions
"""

# Loop forever, getting numbers from user
def getNumbers() -> list:
    retVal = []
    while True:
        _in = input("Please enter a number or enter \"FIN\" to complete...\n> ")

        # Parse either floats or integers
        if _in == "FIN":
            break
        
        try:
            _inInt = int(_in)
        except ValueError:
            _inInt = False
        
        if _inInt is False:
            for _ in range(20):
                print()
            print(f"You entered: {_in}. This is not a number. Try again.")
            sleep(3)
            for _ in range(20):
                print()
            continue
        else:
            retVal.append(_inInt)
            print()

    return retVal

def sort(inputs : list) -> list:
    print(f"Input list is: {inputs}")
    print(f"Sorted list is: {sorted(inputs)}")
    return sorted(inputs)

def add( input_1, input_2):
    print(f"Sum of {input_1} + {input_2} is {input_1+input_2}")
    return input_1 + input_2

def print_TextValue(text, value):
    print(text + str(value))

"""
Finally, parse the sequences and execute
"""
while True:
    for _seq in run["sequence"]:
        seq = run["sequence"][_seq]

        print(f"\nRunning sequence {seq['name']}\n\n")

        for step in range(1,len(seq)+1):
            stepStr = str(step)

            if seq[stepStr]["function"] == "getNumbers":
                seq[stepStr]["result"] = getNumbers()

            elif seq[stepStr]["function"] == "sort":
                inputList = getDVal(run, seq[stepStr]["input"])
                seq[stepStr]["result"] = sort(inputList)

            elif seq[stepStr]["function"] == "add":
                input_1 = getDVal(run, seq[stepStr]["input_1"])
                input_2 = getDVal(run, seq[stepStr]["input_2"])
                seq[stepStr]["result"] = add(input_1, input_2)
            
            elif seq[stepStr]["function"] == "print_TextValue":
                input_Text = seq[stepStr]["input_Text"]
                input_Value = getDVal(run, seq[stepStr]["input_Value"])
                seq[stepStr]["result"] = print_TextValue(input_Text, input_Value)

    
from pathlib import Path
import json 

pathToOriginalBytecode = Path("./bytecode/original/")
pathToChangedBytecode = Path("./bytecode/changed/")

classesOriginal = {}
def updateAndGetOriginalClasses():    
    for f in pathToOriginalBytecode.glob("**/*.json"):
        with open(f) as p:
            doc = json.load(p)
            classesOriginal[doc["name"]] = doc

    return classesOriginal

methodsOriginal = {}
def updateMethodsOriginal():
    for cls in updateAndGetOriginalClasses().values():
        for m in cls["methods"]:
            methodsOriginal[(cls["name"], m["name"])] = m

classesChanged = {}
def updateAndGetClassesChanged():
    for f in pathToChangedBytecode.glob("**/*.json"):
        with open(f) as p:
            doc = json.load(p)
            classesChanged[doc["name"]] = doc

    return classesChanged

methodsChanged = {}
def updateMethodsChanged():
    for cls in updateAndGetClassesChanged().values():
        for m in cls["methods"]:
            methodsChanged[(cls["name"], m["name"])] = m

def find_changed_method(am):
    updateMethodsChanged()
    return methodsChanged[(am)]

def find_original_method(am):
    updateMethodsOriginal()
    return methodsOriginal[(am)]
    
def print_changed_bytecode(am):
    m = find_changed_method(am)
    assert m is not None
    print(m["code"]["bytecode"])

def print_original_bytecode(am):
    m = find_original_method(am)
    assert m is not None
    print(m["code"]["bytecode"])

def bytecode_interp(am, log, checkForChanged):
    memory = {}
    mstack = [([], [], (am, 0))]
    for i in range(0, 10):
        log("->", mstack, end="")
        (lv, os, (am_, i)) = mstack[-1]
        if (checkForChanged):
            b = find_changed_method(am)["code"]["bytecode"][i]
        else: 
            b = find_original_method(am)["code"]["bytecode"][i]
        if b["opr"] == "return": 
            if b["type"] == None:
                log(" (return)")
                return None
            elif b["type"] == "int":
                log(" (return)")
                return os[-1]
            elif b["type"] == "ref":
                log(" (return)")
                return os[-1]
            else: 
                log("unsupported operation", b)
                return None
        elif b["opr"] == "push": 
            log(" (push)")
            v = b["value"]
            _ = mstack.pop()
            mstack.append((lv, os + [v["value"]], (am_, i + 1)))
        elif b["opr"] == "get": 
            log(" (get)")
            return True
        else: 
            log("unsupported operation", b)
            return None

# Grouping States
def retTrue(a, b): 
    # < a in [..0..] , b in [..0..] >
    if (a > b):  # [true, false]
        # < a in [..0..] , b in [..0..] >
        return a > b
        # [true, false]
    return True

err = {
    "IndexOutOfBoundsExecption",
    "ArithmeticException",
    "NullPointerException",
    "UnsupportedOperationException"
}

# stepping function
def abstract_step(bc, s, pc, mstack): 
    if bc.opr == "add":
        s1, s2 = mstack.pop(), mstack.pop()
        mstack.push(s1.plus(s2))
        s2, pc + 1

def abstract_args(bc): 
    params = bc["params"]
    type = params["type"]
    base = type["base"]

    group_of_states = {}
    if base == "int":
        return {}

def abstract_join(npc, ns):
    print

def is_error(ns):
    (pc, args) = ns
    return False

class Pc:
    def __init__(self, m, counter):
        self.m = m
        self.counter = counter
    
    def getM(self):
        return self.m
    
    def getCounter(self):
        return self.counter


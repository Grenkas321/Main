import math
import sys

commands = {}
labels = {}
to_check = []
i = 0
while s := sys.stdin.readline():
    s = s.split()
    if len(s) == 0:
         continue
    if s[0][-1] == ':':
        labels[s[0][:-1]] = i
        s = s[1:]
    match s:
        case ["stop"]:
            commands[i] = s
            break
        case [("ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle"), str(), str(), str()]:

            to_check.append(s[-1])
            commands[i] = s
        case _:
            commands[i] = s
    i += 1
if not all(i in labels for i in to_check):
    exit()

i = 0
namespace = {}
while True:
    if i >= len(commands): break
    match commands[i]:
        case ["stop"]:
            break
        case ["store", a, str()]:
            namespace[commands[i][2]] = commands[i][1]
            i += 1
        case [("add" | "sub" | "div" | "mul"), str(), str(), str()]:
            try:
                op1 = float(namespace[commands[i][1]])
            except:
                op1 = 0
            try:
                op2 = float(namespace[commands[i][2]])
            except:
                op2 = 0
            try:
                match commands[i][0]:
                    case "add":
                        namespace[commands[i][3]] = op1 + op2
                    case "sub":
                       namespace[commands[i][3]] = op1 - op2
                    case "div":
                        namespace[commands[i][3]] = op1 / op2
                    case "mul":
                        namespace[commands[i][3]] = op1 * op2
            except:
                namespace[commands[i][3]] = math.inf
            i += 1

        case [("ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle"), str(), str(), str()]:
            try:
                op1 = float(namespace[commands[i][1]])
            except:
                op1 = 0
            try:
                op2 = float(namespace[commands[i][2]])
            except:
                op2 = 0
            match commands[i][0]:
                case "ifeq":
                    res = op1 == op2
                case "ifne":
                    res = op1 != op2
                case "ifgt":
                    res = op1 > op2
                case "ifge":
                    res = op1 >= op2
                case "iflt":
                    res = op1 < op2
                case "ifle":
                    res = op1 <= op2
            if res: i = labels[commands[i][-1]]
            else: i += 1
        case ["out", str()]:
            if commands[i][1] in namespace:
                print(namespace[commands[i][1]])
            else:
                print(0)
            i += 1
        case _:
            i += 1
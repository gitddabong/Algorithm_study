from collections import defaultdict

def solution(s):    
    d = defaultdict(str)
    d["zero"] = "0"
    d["one"] = "1"
    d["two"] = "2"
    d["three"] = "3"
    d["four"] = "4"
    d["five"] = "5"
    d["six"] = "6"
    d["seven"] = "7"
    d["eight"] = "8"
    d["nine"] = "9"
    
    result = ""
    temp = ""    
    for char in s:
        if char.isdigit():
            result += char
        else:
            temp += char
            if d[temp] == "":
                continue
            else:
                result += d[temp]
                temp = ""
        print(temp)

    return int(result)
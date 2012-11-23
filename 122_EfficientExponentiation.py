from collections import deque

# Basic BFS with a queue
def effExp(exp):
    if exp == 1:
        return 0
    expQueue = deque([(1,)]) # Starts with exponent 1
    while expQueue:
        expList = expQueue.popleft() # Gets first item in the list
        maxExp = max(expList)
        foundExp = []
        # Finds all combinations of exponents from the current list
        for ind, oldExp1 in enumerate(expList):
            for oldExp2 in expList[ind:]:
                newExp = oldExp1 + oldExp2

                if newExp < maxExp:
                    continue

                if newExp in foundExp:
                    continue

                if newExp == exp: # Found match
                    return len(expList)

                if newExp not in expList: # Found new exponent
                    foundExp.append(newExp)
                    expQueue.append( (newExp,)+expList )

print sum(map(effExp,range(1,201)))
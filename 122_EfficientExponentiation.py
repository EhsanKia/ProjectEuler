from collections import deque

# Basic BFS with a queue

res = [-1]*200
res[0] = 0

expQueue = deque([(1,)]) # Starts with exponent 1
while -1 in res:
    expList = expQueue.popleft() # Gets first item in the list
    maxExp = max(expList)
    foundExp = []
    # Finds all combinations of exponents from the current list
    for ind, oldExp1 in enumerate(expList):
        for oldExp2 in expList[ind:]:
            newExp = oldExp1 + oldExp2

            if newExp > 200:
                continue

            if newExp < maxExp:
                continue

            if newExp in foundExp:
                continue

            if res[newExp-1] == -1: # Found match
                res[newExp-1] = len(expList)

            if newExp not in expList: # Found new exponent
                foundExp.append(newExp)
                expQueue.append( (newExp,)+expList )

print sum(res)
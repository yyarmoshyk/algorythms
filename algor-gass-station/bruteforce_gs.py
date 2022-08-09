def can_traverse(gas,cost,start):
    n = len(gas)
    remain = 0
    i = start
    started = False
    while i != start or not started:
        started = True
        remain  += gas[i] - cost[i]
        if remain < 0:
            return False
        i = (i+1)%n
    return True

def gas_station(gas,cost):
    for i in range(len(gas)):
        if can_traverse(gas,cost,i):
            return i
    return -1
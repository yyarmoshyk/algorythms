from cmath import cos


def gas_station(gas,cost):
    remaining = 0
    candidate = 0
    prev_remaining = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i+1
            remaining = 0
            prev_remaining += remaining
    if candidate == len(gas) or remaining + prev_remaining < 0:
        return -1
    else:
        return candidate
Given a circular list of gas stations, where we go from station i to i+1 and the last one goes bact to
the first one.
Find the index of from where we start to be able to traverse all the stations and go back to the initial one
without running our of gas.

Note:
• we go only forward
• the tank is empty
• gas(i) represents the amount of gas on the station i
• cost[i] is the cost to go from station i to i+1
• the answers is guaranteed to be uniq
• if the station doesn't exist - return -1 (return to the beginning of the list)

```bash
python3

gas = [1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]

import importlib as i
import bruteforce_gs as bbg
import gas_station as gs

bgs.gas_station(gas,cost)
gs.gas_station(gas,cost)
```
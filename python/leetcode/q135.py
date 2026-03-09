def canCompleteCircuit(gas, cost):
    # If total gas is less than total cost, it's impossible
    if sum(gas) < sum(cost):
        return -1
    
    total_tank = 0
    start_index = 0
    
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        

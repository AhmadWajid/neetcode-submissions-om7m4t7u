class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            # Add gas gained and subtract travel cost
            tank += gas[i] - cost[i]

            # Not enough gas to continue from current start
            if tank < 0:
                start = i + 1  # Try the next station
                tank = 0       # Reset gas for the new start

        return start
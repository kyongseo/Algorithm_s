from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights = deque(t for t in truck_weights)
    answer = 0
    bridge_weight = 0
    
    while bridge:
        answer += 1
        bridge_weight -= bridge.popleft()

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)

    return answer
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_information = []
        for i in range(len(position)):
            car_information.append((position[i], speed[i]))
        
        car_information.sort(reverse=True, key=lambda information: information[0])

        fleet_count = 0
        i = 0
        while i < len(position):
            fleet_count += 1
            curr_car_time = (target - car_information[i][0]) / car_information[i][1]
            i += 1
            while i < len(position) and ((target - car_information[i][0]) / car_information[i][1]) <= curr_car_time:
                i += 1
        return fleet_count

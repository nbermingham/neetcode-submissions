class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_boats = len(people)
        people.sort()
        
        l, r = 0, len(people) - 1

        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                num_boats -= 1
            else:
                r -= 1
        
        return num_boats


from typing import List

def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    res = 0
    
    # Iterate through the points up to the second to last one
    for i in range(len(points) - 1):
        current_point = points[i]
        next_point = points[i+1]
        
        # Calculate absolute difference in X and Y
        diff_x = abs(next_point[0] - current_point[0])
        diff_y = abs(next_point[1] - current_point[1])
        
        # The time taken is the maximum of the two differences
        # (because diagonal moves cover 1 unit of X and 1 unit of Y simultaneously)
        res += max(diff_x, diff_y)
            
    return res

print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])) 
# Output: 7
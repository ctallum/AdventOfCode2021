from typing import List

class Region():
    def __init__(self, bounds: List[List[int]], state: bool) -> None:
        self.bounds = bounds
        self.state = state

    @property
    def area(self) -> int:
        area = 1
        for axis in range(3):
            area *= self.bounds[axis][1] - self.bounds[axis][0] + 1
        return area
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for el in asteroids:
            if el <= mass:
                mass += el
            else:
                return False
        return True
        
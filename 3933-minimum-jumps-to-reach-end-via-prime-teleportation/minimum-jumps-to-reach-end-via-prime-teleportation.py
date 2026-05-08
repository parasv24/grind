class Solution:
    def minJumps(self, nums: List[int]) -> int:        
        def prime_factors(num):
            d = 2
            factors = set()
            while d * d <= num:
                while num % d == 0:
                    num = num // d
                    factors.add(d)
                d += 1
            if num > 1:
                factors.add(num)
            return factors
        
        primes_indexes = defaultdict(list)

        for idx, el in enumerate(nums):
            for factor in prime_factors(el):
                primes_indexes[factor].append(idx)
        queue = deque()
        vis = {}
        queue.append([0, 0])
        vis[0] = True
        used_primes = {}
        while queue:
            # print(queue)
            idx, steps = queue.popleft()
            if idx == len(nums) - 1:
                return steps
            if nums[idx] not in used_primes:
                for j in primes_indexes[nums[idx]]:
                    if j not in vis:
                        queue.append([j, steps + 1])
                        vis[j] = True
                        if j == len(nums) - 1:
                            return steps + 1
            used_primes[nums[idx]] = True
            if not (idx + 1) in vis:
                queue.append([idx+1, steps + 1])
                vis[idx+1] = True
            if idx > 0  and not (idx - 1) in vis:
                queue.append([idx-1, steps + 1])
                vis[idx-1] = True





        
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        block_size = ceil(sqrt(len(nums2)))
        blocks = []
        for i in range(len(nums2)):
            if i % block_size == 0:
                blocks.append(defaultdict(int))
            blocks[i // block_size][nums2[i]] += 1
        lazy = [0] * len(blocks)
        
        ans_arr = []
        for query in queries:
            if query[0] == 2:
                total = query[1]
                ans = 0
                for el in nums1:
                    target = total - el
                    for i in range(len(blocks)):
                        laz_target = target - lazy[i]
                        ans += blocks[i][laz_target]
                ans_arr.append(ans)
            else:
                _, x, y, val = query
                while x % block_size != 0 and x <= y:
                    prev_val = nums2[x]
                    blocks[x // block_size][prev_val] -= 1
                    blocks[x // block_size][prev_val + val] += 1
                    nums2[x] = prev_val + val
                    x += 1
                
                while x + block_size <= y:
                    lazy[x // block_size] += val
                    x += block_size
                
                while x <= y:
                    prev_val = nums2[x]
                    blocks[x // block_size][prev_val] -= 1
                    blocks[x // block_size][prev_val + val] += 1
                    nums2[x] = prev_val + val
                    x += 1
        return ans_arr



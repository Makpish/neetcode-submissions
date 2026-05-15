class TimeMap:

    def __init__(self):
        self.hmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = [[-1,""]]
        self.hmap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        # print(self.hmap)
        if key not in self.hmap:
            return ""
        nums = self.hmap[key]

        l = 0
        r = len(nums)-1

        while l<r:
            m = (l+r)//2+1

            if nums[m][0]>timestamp:
                r = m-1
            else:
                l=m
        return nums[l][1]
        

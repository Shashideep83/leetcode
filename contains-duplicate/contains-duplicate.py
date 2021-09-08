class Solution(object):
    def containsDuplicate(self, nums):
        data = []
        for count in nums:
            if count not in data:
                value = 1
                data.append(count)
            else:
                value=2
            if value==2:
                return True
        return False
        
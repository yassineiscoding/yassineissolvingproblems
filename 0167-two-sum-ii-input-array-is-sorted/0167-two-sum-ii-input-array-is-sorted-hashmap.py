class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_1 = 0
        index_2 = len(numbers) - 1

        while index_1 < index_2:
            val_sum = numbers[index_1] + numbers[index_2]
            if val_sum == target: 
                return [index_1 + 1, index_2 + 1]
            elif val_sum > target:
                index_2 -= 1
            else:  # val_sum < target
                index_1 += 1
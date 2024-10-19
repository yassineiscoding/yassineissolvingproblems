class Solution {
    public int findDuplicate(int[] nums) {
        HashMap<Integer, Boolean> checklist = new HashMap<Integer, Boolean>();
        for(int i = 0; i<nums.length; i++){
            if(!checklist.containsKey(nums[i])){
                checklist.put(nums[i], true);
            } else {
                return nums[i];
            }
        }
        return nums[-1];
    }
}
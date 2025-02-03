class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        if (nums.size()==1){
            return 1;
        }
        int countinc = 1, countdec = 1, m = 1;

        for(int i = 0;i<nums.size()-1;i++){
            if(nums[i]<nums[i+1]){
                countinc++;
                m = max(m,countinc);
            }
            else{
                countinc = 1;
            }
        }
        for(int i = 0;i<nums.size()-1;i++){
            if(nums[i]>nums[i+1]){
                countdec++;
                m = max(m,countdec);
            }
            else{
                countdec = 1;
            }
        }
        return m;
    }
};

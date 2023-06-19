#include <vector>

using namespace std;
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0,
            r = nums.size() - 1;
        
        int min = nums[0];
        while(l <= r) {
            int mid = (l + r) / 2;
            if(nums[mid] < min) 
                min = nums[mid];
            

            if(l > r) 
                r = mid - 1;
            else 
                l = mid + 1;
            
        }
        return min;
    }
};
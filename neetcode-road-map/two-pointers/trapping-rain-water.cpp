#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
class Solution1 {
public:
    int trap(std::vector<int>& height) {
        int max_l[height.size()];
        int max_r[height.size()];

        max_l[0] = 0; 
        for (size_t i = 1; i < height.size(); i++) {
            max_l[i] = std::max(height[i - 1],max_l[i - 1]);
        }
        max_r[height.size() - 1] = 0;
        for (int i = height.size() - 2; i >= 0; i--) {
            max_r[i] = std::max(height[i + 1],max_r[i + 1]);
        }
        
        int traped = 0;
        for (size_t i = 0; i < height.size(); i++) { 
            max_r[i] = std::min(max_r[i],max_l[i]);
            traped += std::max(0,max_r[i] - height[i]);
        }
        return traped;
    }
};
class Solution {
public:
    int trap(std::vector<int>& height) {
        int traped = 0;
        int last_l = height[0],
            last_r = height[height.size() - 1];
        int l  = 0,
            r  = height.size() - 1;

        while(r > l) {
            if(last_l < last_r) {
                l++;
                last_l  = std::max(last_l,height[l]);
                traped += last_l - height[l];
            } else {
                r--;
                last_r  = std::max(last_r,height[r]);
                traped += last_r - height[r];
            }
        }
        return traped;
    }
};


int main() {
    std::vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    std::cout << Solution().trap(height)   << "\n";
    return 0;
}
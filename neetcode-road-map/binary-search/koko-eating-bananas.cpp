#include <vector>
#include <cmath>
#include <stdio.h>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        auto max = *max_element(std::begin(piles), std::end(piles)); // C++11

        int l = 1,
            r = max;
        int min_mid = max;
        while(l <= r) {
            int mid = (r + l) / 2;
            int time = 0;

            for (size_t i = 0; i < piles.size() && time <= h; i++) {
                time +=  ceil((float) piles[i] / (float)  mid);           
            }
            if(time <= h) {
                if(min_mid > mid) {
                    min_mid = mid;
                }

                r = mid - 1;
            
            } else {
                l = mid + 1;
            }


        }
        return min_mid;
    }
};
#include <vector>

using namespace std;

class Solution {
public:
    pair<int,int> get_coords(int index, int cols,  int rows) {
        pair<int , int> out;
        out.first  = index / rows;
        out.second  = index % cols;
        return out;
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int size = rows * cols;

        int l  = 0 , 
            r = size;
        
        while(l <= r) {
            int mid = (l + r) / 2;
            auto coords = get_coords(mid,cols,rows);
            
            if(matrix[coords.first][coords.second] == target) {
                return true;
            } else if (matrix[coords.first][coords.second] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return false;

    }
};
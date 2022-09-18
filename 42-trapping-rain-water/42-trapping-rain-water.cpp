class Solution {
public:
    int trap(vector<int>& height) {
        int N = height.size();
        vector<int> left(N,0),right(N,0);
        int mx = height[0];
        for(int i = 0;i<N;i++){
            mx = max(mx,height[i]);
            left[i] = mx;
        }
        mx = height[N-1];
        for(int i = N-1;i>=0;i--){
            mx = max(mx,height[i]);
            right[i] = mx;
        }
        // reverse(right.begin(), right.end());
        int water = 0;
        for(int i = 0;i<N;i++){
            water += abs(min(left[i],right[i])-height[i]);
        }
        return water;
    }
};
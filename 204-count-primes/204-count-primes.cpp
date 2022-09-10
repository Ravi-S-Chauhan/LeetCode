class Solution {
public:
    int countPrimes(int n) {
        vector<int> dp(n,1);
        if (n<=1) return 0;
        for(int i =2;i*i<n;i++){
            if (dp[i]==1){
                for(int j = i*i;j<n;j=i+j) dp[j] = 0;
            }
        }
        return(accumulate(dp.begin(), dp.end(), 0)-2);
    }
};
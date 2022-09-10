class Solution {
public:
    int countPrimes(int n) {
        vector<int> dp(n,1);
        if (n<=1) return 0;
        int count = 0;
        for(int i =2;i<n;i++){
            if (dp[i]==1){
                count ++;
                for(int j = 2*i;j<n;j=i+j) dp[j] = 0;
            }
        }
        return(count);
    }
};
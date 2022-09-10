class Solution {
public:
    int minSteps(int n) {
        int result;
        for(int i = 2;i*i<=n;i++){
            while(n%i == 0){
                result += i;
                n /= i;
            }
        }
        if (n>1){
            result += n;
        }
        return result;
    }
};
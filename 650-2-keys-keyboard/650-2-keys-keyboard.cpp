class Solution {
public:
    int minSteps(int n) {
        if (n<=1) return 0;
        int result;
        while (n%2 == 0){
            result += 2;
            n /= 2;
        }
        while(n%3 == 0){
            result += 3;
            n /= 3;
        }
        
        for(int i = 5;i*i<=n;i=i+6){
            while(n%i == 0){
                result += i;
                n /= i;
            }
            while(n%(i+2) == 0){
                result += (i+2);
                n /= (i+2);
            }
        }
        if (n>3){
            result += n;
        }
        return result;
    }
};
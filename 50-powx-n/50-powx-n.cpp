class Solution {
public:
    double myPow(double x, int n) {
        if (n>=0) return solve2(x,n);
        else return solve(x,n);
    }
    double solve2 (double x,int n){
        double result = 1;
        while (n>0){
            if (n&1) result *= x;
            x *= x;
            n /= 2;
        }
        return result;
    }
    double solve(double x,int n){
        if (n == 0) return 1;
        double temp = solve(x,n/2);
        temp *= temp;
        if (!(n&1)) return temp;
        else{
            if (n>0) return temp*x;
            else return temp/x;
        }
    }
};
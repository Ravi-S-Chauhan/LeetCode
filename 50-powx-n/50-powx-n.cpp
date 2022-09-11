class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        double temp = myPow(x,n/2);
        temp *= temp;
        if (!(n&1)) return temp;
        else{
            if (n>0) return temp*x;
            else return temp/x;
        }
    }
};
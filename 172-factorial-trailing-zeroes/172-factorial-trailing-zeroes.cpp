class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0,mul = 5;
        while (mul<=n){
            count += n/mul;
            mul *= 5;
        }
        return count;
    }
};
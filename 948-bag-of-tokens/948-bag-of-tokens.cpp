class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int N = tokens.size();int score = 0;
        int start = 0;int end = N-1;
        sort(tokens.begin(),tokens.end());
        if (N == 0 || tokens[0]>power) return 0;
        while (start<=end){
            if (power>=tokens[start]){
                power -= tokens[start];
                start++;score++;
            }
            else if (score>0){
                power += tokens[end];
                end--;score--;
            }
            else break;
        }
        if (start<N and power>=tokens[start]) score++;
        return score;
    }
};
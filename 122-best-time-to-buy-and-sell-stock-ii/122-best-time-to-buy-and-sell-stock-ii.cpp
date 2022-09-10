class Solution {
public:
    int maxProfit(vector<int>& prices,int start = -1) {
        int N = prices.size();
        if (start>=N-1) return 0;
        if (start == -1) start = 0;
        while (start+1<N && prices[start]>prices[start+1]) start++;
        int end = start+1;
        while (end+1<N && prices[end]<prices[end+1]) end++;
        if (start<N &&end<N) return prices[end]-prices[start]+maxProfit(prices,end+1);
        return 0;
    }
};
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int check = 0;
        for(int each:data){
            if (check == 0){
                if ((each>>7) == 0b0) check = 0;
                else if ((each>>5) == 0b110) check = 1;
                else if ((each>>4) == 0b1110) check = 2;
                else if ((each>>3) == 0b11110) check = 3;
                else return false; //For 255
            }
            else{
                if ((each>>6) != 0b10) return false;
                check--;
            }
        }
        if (check == 0) return true;
        return false;
    }
};
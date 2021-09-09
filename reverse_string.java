class Solution {
    public void reverseString(char[] s) {
        int j = 0;
        char temp;
        
        for(int i = s.length-1; i >= s.length/2; i--) {
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            j++;
        }
    }
}

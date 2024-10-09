class Solution {
    public static int reverse(int x) {
        int reverse = 0;
        int quotient = x;
        while(quotient != 0){
            if(reverse > Integer.MAX_VALUE / 10 || reverse < Integer.MIN_VALUE / 10) return 0;
            reverse = reverse * 10 + quotient % 10;
            quotient = quotient / 10;
        }
        return reverse;
    }
}
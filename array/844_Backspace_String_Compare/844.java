class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1;
        int j = t.length() - 1;
        while (i >= 0 || j >= 0) {
            int skipS = 0;
            while (i >= 0 && (s.charAt(i) == '#' || skipS > 0)) {
                if (s.charAt(i) == '#') {
                    skipS += 1;
                } else {
                    skipS -= 1;
                }
                i -= 1;
            }

            int skipT = 0;
            while (j >= 0 && (t.charAt(j) == '#' || skipT > 0)) {
                if (t.charAt(j) == '#') {
                    skipT += 1;
                } else {
                    skipT -= 1;
                }
                j -= 1;
            }

            if (i >= 0 && j >= 0 && s.charAt(i) != t.charAt(j)) {
                return false;
            }

            if ((i >= 0) != (j >= 0)) {
                return false;
            }

            i -= 1;
            j -= 1;
        }
        return true;
    }
}
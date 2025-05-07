import java.util.*;

public class Boj1316 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int result = 0;
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            boolean[] apv = new boolean[26]; // 선언시 기본값 false로 초기화됨

            apv[s.charAt(0) - 'a'] = true;
            boolean isGroupWord = true;
            for (int j = 1; j < s.length(); j++) {
                char prev = s.charAt(j - 1);
                char cur = s.charAt(j);
                if (prev != cur) {
                    if (apv[cur - 'a']) {
                        isGroupWord = false;
                        break;
                    } else {
                        apv[cur - 'a'] = true;
                    }
                }
            }
            if (isGroupWord) {
                result++;
            }
        }
        System.out.println(result);
    }
}

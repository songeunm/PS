import java.util.*;

public class Boj10809 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        String s = sc.next();

        int[] arr = new int[26];
        // Arrays.fill => arr -1로 초기화
        Arrays.fill(arr, -1);

        // s.length() => 문자열의 길이 반환
        for (int i = 0; i < s.length(); i++){
            // 'a'의 아스키코드를 빼서 'a'부터 0이 되도록 함
            int idx = s.charAt(i) - 'a';
            if (arr[idx] == -1){
                arr[idx] = i;
            }
        }

        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }

    }
}
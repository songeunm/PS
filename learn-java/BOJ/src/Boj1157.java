import java.util.*;

public class Boj1157 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine().toUpperCase();
        int[] apv = new int[26];
        for (int i = 0; i < s.length(); i++){
            int idx = s.charAt(i) - 'A';
            apv[idx]++;
        }
        // java에서는 배열을 출력할 때 Arrays.toString(arr)을 사용한다.
        // System.out.println(Arrays.toString(apv));

        int max_cnt = 1;
        int max = 0;
        for (int i = 1; i < apv.length; i++){
            if (apv[max] < apv[i]){
                max = i;
                max_cnt = 1;
            } else if (apv[max] == apv[i]){
                max_cnt ++;
            }
        }

        if (max_cnt > 1){
            System.out.println("?");
        } else{
            char result = (char) (max + 'A');
            System.out.println( result );
        }
    }
}

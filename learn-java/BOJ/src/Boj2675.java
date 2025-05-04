import java.util.*;

public class Boj2675 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i = 0; i < t; i++){
            int r = sc.nextInt();
            String s = sc.next();

            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < s.length(); j++){
                sb.append(String.valueOf(s.charAt(j)).repeat(r));
            }
            System.out.println(sb.toString());
        }
    }
}

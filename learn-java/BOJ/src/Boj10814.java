import java.util.*;
import java.io.*;

public class Boj10814 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();
        String[][] people = new String[n][2];
        for (int i = 0; i < n; i++){
            people[i][0] = sc.next();
            people[i][1] = sc.next();
        }

        Arrays.sort(people, (a, b) -> {
            return Integer.parseInt(a[0]) - Integer.parseInt(b[0]);
        });

        for (int i = 0; i < n; i++){
            sb.append(people[i][0]).append(" ");
            sb.append(people[i][1]).append("\n");
        }
//        sb.delete(sb.length()-1, sb.length());

        System.out.print(sb);
    }
}

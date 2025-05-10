import java.util.*;
import java.io.*;

public class Boj1181 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();
        sc.nextLine();
        String[] words = new String[n];
        for (int i = 0; i < n; i++){
            words[i] = sc.nextLine();
        }

        Arrays.sort(words, (a, b) -> {
            if (a.length() != b.length()){
                return a.length() - b.length();
            }
            return a.compareTo(b);
        });

        sb.append(words[0]).append("\n");

        for (int i = 1; i < n; i++){
            if (!words[i-1].equals(words[i])) {
                sb.append(words[i]).append("\n");
            }
        }

        System.out.print(sb);
    }
}

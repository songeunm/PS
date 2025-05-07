import java.util.*;
import java.io.*;

public class Boj11866 {

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] inps = br.readLine().split(" ");
        int n = Integer.parseInt(inps[0]);
        int k = Integer.parseInt(inps[1]);

        sb.append('<');
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 1; i <= n; i++){
            dq.addFirst(i);
        }
        while (!dq.isEmpty()){
            for (int i = 0; i < k-1; i++){
                dq.addFirst(dq.pollLast());
            }
            sb.append(dq.pollLast()).append(", ");
        }
        sb.delete(sb.length()-2, sb.length());
        sb.append(">");

        System.out.println(sb);
    }
}

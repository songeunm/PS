import java.util.*;
import java.io.*;

public class Boj18258 {

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<Integer> q = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++){
            String[] cmd = br.readLine().split(" ");
            if ( cmd[0].equals("push") ){
                q.addLast(Integer.parseInt(cmd[1]));
            } else if ( cmd[0].equals("pop") ){
                if (q.isEmpty()){
                    sb.append(-1).append('\n');
                } else{
                    sb.append(q.pollFirst()).append('\n');
                }
            } else if ( cmd[0].equals("size") ){
                sb.append(q.size()).append('\n');
            } else if ( cmd[0].equals("empty") ){
                if (q.isEmpty()){
                    sb.append(1).append('\n');
                } else{
                    sb.append(0).append('\n');
                }
            } else if ( cmd[0].equals("front") ){
                if (q.isEmpty()){
                    sb.append(-1).append('\n');
                } else{
                    sb.append(q.peekFirst()).append('\n');
                }
            } else if ( cmd[0].equals("back") ){
                if (q.isEmpty()){
                    sb.append(-1).append('\n');
                } else{
                    sb.append(q.peekLast()).append('\n');
                }
            }
        }
        System.out.println(sb);
    }
}

import java.util.*;
import java.io.*;

public class Boj10828 {

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        Deque<Integer> st = new ArrayDeque<>();
        for (int i = 0; i < n; i++){
            String[] cmd = br.readLine().split(" ");

            if (cmd[0].equals("push")){
                st.addLast(Integer.parseInt(cmd[1]));
            } else if (cmd[0].equals("pop")){
                if (st.isEmpty()){
                    sb.append(-1).append("\n");
                } else{
                    sb.append(st.pollLast()).append("\n");
                }
            } else if (cmd[0].equals("size")){
                sb.append(st.size()).append("\n");
            } else if (cmd[0].equals("empty")){
                if (st.isEmpty()){
                    sb.append(1).append("\n");
                } else{
                    sb.append(0).append("\n");
                }
            } else if (cmd[0].equals("top")){
                if (st.isEmpty()){
                    sb.append(-1).append("\n");
                } else{
                    sb.append(st.peekLast()).append("\n");
                }
            }
        }

        System.out.println(sb);
    }
}

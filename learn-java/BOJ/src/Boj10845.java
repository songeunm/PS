import java.util.*;

public class Boj10845 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine(); // nextInt() 이후 숫자만 먹고 엔터가 남아있으므로 (추후 sc.nextLine()에 영향) 엔터를 삭제해줌
        Deque<Integer> q = new ArrayDeque<Integer>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++){
            String[] cmd = sc.nextLine().split(" ");

            if (cmd[0].equals("push")){
                q.addLast( Integer.parseInt(cmd[1]) );
            } else if (cmd[0].equals("pop")){
                if (q.isEmpty()){
                    sb.append(-1).append('\n');
                } else{
                    sb.append(q.pollFirst()).append('\n');
                }
            } else if (cmd[0].equals("size")){
                sb.append(q.size());
                sb.append("\n");
            } else if (cmd[0].equals("empty")){
                if (q.isEmpty()){
                    sb.append(1).append('\n');
                } else{
                    sb.append(0).append('\n');
                }
            } else if (cmd[0].equals("front")){
                if (q.isEmpty()){
                    sb.append(-1).append('\n');
                } else{
                    sb.append(q.peekFirst()).append('\n');
                }
            } else if (cmd[0].equals("back")){
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

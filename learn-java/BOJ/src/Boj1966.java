import java.util.*;
import java.io.*;

public class Boj1966 {

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++){
            // int list를 queue에 삽입.
            // 비교는 a, b가 들어왔을 시 ()안의 내용인 a[1] - b[1]을 통해 수행
            // Queue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
            Deque<int[]> q = new ArrayDeque<>();
            Queue<Integer> pq = new PriorityQueue<>();

            String[] inps = br.readLine().split(" ");
            int n = Integer.parseInt(inps[0]);
            int m = Integer.parseInt(inps[1]);
            String[] docs = br.readLine().split(" ");

            for (int j = 0; j < n; j++){
                q.addLast( new int[]{j, Integer.parseInt(docs[j])} );
                pq.add( -Integer.parseInt(docs[j]) );
            }
            int result = 0;
            while (true){
                int[] cur = q.pollFirst();
                if (cur[1] < -pq.peek()){
                    q.addLast(cur);
                } else{
                    result ++;
                    pq.poll();
                    if (cur[0] == m){
                        break;
                    }
                }
            }
            System.out.println(result);
        }
    }
}

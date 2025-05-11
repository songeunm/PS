import java.util.*;
import java.io.*;

public class Boj2075 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();
        int[][] arr = new int[n][n];
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                arr[i][j] = sc.nextInt();
                pq.add(arr[i][j]);
                if (pq.size() > n){
                    pq.poll();
                }
            }
        }

        System.out.println(pq.poll());
    }
}

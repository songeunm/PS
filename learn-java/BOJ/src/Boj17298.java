import java.util.*;
import java.io.*;

public class Boj17298 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        Deque<Integer> stack = new ArrayDeque<>();
        int[] result = new int[n];
        for (int i = n-1; i >= 0; i--){
            while (!stack.isEmpty()){
                if (stack.peekLast() > arr[i]){
                    break;
                }
                stack.pollLast();
            }
            if (stack.isEmpty()){
                result[i] = -1;
            } else{
                result[i] = stack.peekLast();
            }
            stack.addLast(arr[i]);
        }

        for (int i = 0; i < n; i++){
            sb.append(result[i]).append(" ");
        }
        System.out.print(sb);
    }
}

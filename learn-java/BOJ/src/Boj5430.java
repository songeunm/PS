import java.util.*;
import java.io.*;

public class Boj5430 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int t = sc.nextInt();
        sc.nextLine();
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 0; i < t; i++){
            sb.setLength(0);
            deque.clear();
            boolean front = true;
            boolean error = false;

            String p = sc.nextLine();
            int n = sc.nextInt();
            sc.nextLine();
            String inps = sc.nextLine();
            String[] arr = inps.substring(1, inps.length()-1).split(",");

            if (n != 0) {
                for (int j = 0; j < arr.length; j++) {
                    deque.addLast(Integer.parseInt(arr[j]));
                }
            }

            for (int j = 0; j < p.length(); j++){
                char c = p.charAt(j);
                if (c == 'R'){
                    if (front){
                        front = false;
                    } else{
                        front = true;
                    }
                } else {
                    if (deque.isEmpty()){
                        error = true;
                        break;
                    }else if (front){
                        deque.pollFirst();
                    } else{
                        deque.pollLast();
                    }
                }
            }

            if (error){
                sb.append("error");
            } else{
                sb.append('[');
                if (front){
                    while (!deque.isEmpty()){
                        sb.append(deque.pollFirst()).append(',');
                    }
                } else{
                    while (!deque.isEmpty()){
                        sb.append(deque.pollLast()).append(',');
                    }
                }
                if (sb.length() >= 2) {
                    sb.delete(sb.length() - 1, sb.length());
                }
                sb.append(']');
            }

            System.out.println(sb);
        }
    }
}

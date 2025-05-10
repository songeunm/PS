import java.util.*;
import java.io.*;

public class Solution {
    public int[] solution(int []arr) {
        Deque<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < arr.length; i++){
            // System.out.println(arr[i]);
            if (q.isEmpty() || q.peekLast() != arr[i]){
                q.addLast(arr[i]);
            }
        }
        // System.out.println(q.toString());

        int[] result = new int[q.size()];
        int i = 0;
        while (!q.isEmpty()){
            result[i] = q.pollFirst();
            i++;
        }

        return result;
    }
}
import java.util.*;

public class Boj2562 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        int n = 9;
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int max = arr[0];
        int idx = 0;
        for (int i = 1; i < n; i++){
            if (max < arr[i]){
                max = arr[i];
                idx = i;
            }
        }
        System.out.println(max);
        System.out.println(idx+1);
    }
}

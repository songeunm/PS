import java.util.*;

public class Boj3052 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < 10; i++){
            int nums = sc.nextInt();
            set.add(nums % 42);
        }
        System.out.println(set.size());
    }
}

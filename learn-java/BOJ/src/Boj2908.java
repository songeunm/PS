import java.util.*;

public class Boj2908 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();
        String reverse_a = new StringBuilder(a).reverse().toString();
        String reverse_b = new StringBuilder(b).reverse().toString();
        int num_a = Integer.parseInt(reverse_a);
        int num_b = Integer.parseInt(reverse_b);
        if (num_a < num_b){
            System.out.println(num_b);
        } else if (num_a > num_b){
            System.out.println(num_a);
        }
    }
}

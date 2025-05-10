import java.util.*;
import java.io.*;

public class Boj9012 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();
        sc.nextLine();
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            stack.clear();
            String ps = sc.nextLine();
//            System.out.println(ps);
            boolean wrong = false;
            for (int j = 0; j < ps.length(); j++){
//                System.out.println(stack.toString());
                char c = ps.charAt(j);
                if (c == '('){
                    stack.addLast(c);
                } else if (stack.isEmpty()){
//                    System.out.println("연게 없는데 닫음");
                    wrong = true;
                    break;
                } else{
                    stack.pollLast();
                }
            }
            if (!stack.isEmpty()){
//                System.out.print("얄고 안닫음");
                wrong = true;
            }

            if (wrong){
                sb.append("NO\n");
            } else{
                sb.append("YES\n");
            }
        }
        System.out.print(sb);
    }
}

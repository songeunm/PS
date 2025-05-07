import java.util.*;

public class Boj2525 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        // java에서는 int끼리의 나눗셈의 결과가 몫 (//)이다. // 연산자는 없다.
        int m = (b + c) % 60;
        int added_h = (b + c) / 60;
        int h = (a + added_h) % 24;
        System.out.println(h + " " + m);
    }
}

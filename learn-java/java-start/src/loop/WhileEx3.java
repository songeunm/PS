package loop;

public class WhileEx3 {

    public static void main(String[] args) {
        int max = 100;
        int sum = 0;
        int i = 1;

        while (i <= max) {
            sum += i++;
        }
        System.out.println(sum);
    }
}

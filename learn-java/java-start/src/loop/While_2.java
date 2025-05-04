package loop;

public class While_2 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 1;
        int endNum = 5;
        while (i < endNum){
            sum += i++;
            System.out.println("sum = " + sum);
        }
    }
}

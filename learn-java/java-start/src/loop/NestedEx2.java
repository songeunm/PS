package loop;

public class NestedEx2 {

    public static void main(String[] args) {
        int rows = 5;

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

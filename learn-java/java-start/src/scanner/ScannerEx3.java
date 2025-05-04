package scanner;

import java.util.Scanner;

public class ScannerEx3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int res = 0;
        while (true) {
            System.out.print("숫자 입력: ");
            int num = scanner.nextInt();

            if (num == 0) {
                System.out.println("종료합니다.");
                break;
            }
            res += num;
        }
        System.out.println("누계: " + res);
    }
}

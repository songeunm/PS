package scanner;

import java.util.Scanner;

public class ScannerEx2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("첫번째 숫자 입력: ");
            int num1 = scanner.nextInt();
            System.out.print("두번째 숫자 입력: ");
            int num2 = scanner.nextInt();

            if (num1 == 0 && num2 == 0) {
                System.out.println("종료합니다.");
                break;
            } else {
                int res = num1 + num2;
                System.out.println("두 숫자의 합: " + res);
            }

        }
    }
}

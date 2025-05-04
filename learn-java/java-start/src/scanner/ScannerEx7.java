package scanner;

import java.util.Scanner;

public class ScannerEx7 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("1~9 사이의 정수 입력: ");
        int num = scanner.nextInt();

        for (int i = 1; i<10; i++){
            int res = num * i;
            System.out.println(num + " x " + i + " = " + res);
        }
    }
}

package scanner;

import java.util.Scanner;

public class ScannerEx4 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("이름: ");
        String name = scanner.nextLine();
        System.out.print("나이: ");
        int age = scanner.nextInt();

        System.out.println("당신의 이름은 " + name + "이고, 당신의 나이는 " + age + "살 입니다.");
    }
}

package scanner;

import java.util.Scanner;

public class ScannerEx1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("입력: ");
            String inp = scanner.nextLine();

            if (inp.equals("exit")){
                System.out.println("종료합니다.");
                break;
            } else {
                System.out.println(inp);
            }

        }
    }
}

package operator;

public class Operator6 {

    public static void main(String[] args) {
        // 전위 증감 연산자
        int a = 1;
        int b = 0;
        b = ++a; // a 값 증감 후 b 대입
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        // 후위 증감 연산자
        a = 1;
        b = 0;
        b = a++; // b에 a 값 대입 후 a 값 증감
        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}

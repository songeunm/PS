package operator;

public class Operator7 {

    public static void main(String[] args) {
        int a = 2;
        int b = 3;

        // 비교 연산자
        System.out.println(a == b);
        System.out.println(a != b);
        System.out.println(a > b);
        System.out.println(a < b);
        System.out.println(a >= b);
        System.out.println(a <= b);

        boolean result = a == b;
        System.out.println(result);

        System.out.println("");
        // 문자열 비교
        String str1 = "string1";
        String str2 = "string2";
        boolean result1 = "hello".equals("hello"); // 리터럴 비교
        boolean result2 = str1.equals("string1"); // 문자열 변수, 리터럴 비교
        boolean result3 = str1.equals(str2); // 문자열 변수 비교
        System.out.println(result1);
        System.out.println(result2);
        System.out.println(result3);
    }
}

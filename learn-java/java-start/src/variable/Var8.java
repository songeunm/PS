package variable;

public class Var8 {
    public static void main(String[] args) {
        // 정수형
        byte b = 127; // -128 ~ 127 (1byte, 2^8)
        short s = 32767; // -32768 ~ 32767 (2byte, 2^16)
        int i = 2147483647; // -2147483648 ~ 2147483647 (약 20억) (4byte, 2^32)
        long l = 9223372036854775807L; // 정수 중 제일 큼 (8byte, 2^64)

        // 실수형
        float f = 10.0f; // 뒤에 f 붙여줘야 함 (4byte, 2^32)
        double d = 10.0; // float 보다 정밀도가 높음 (8byte, s^64)

        // 기타
        boolean bl = true; // true, false (1byte)
        char c = 'c'; // 문자 하나 (1byte)
        String st = "string"; // 문자열 (문자열 길이에 따라 메모리가 동적으로 변경)
    }
}
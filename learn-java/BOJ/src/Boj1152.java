import java.util.*;

public class Boj1152 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        // 공백을 포함한 문자열 받기 + 앞뒤 공백 제거
        String s = sc.nextLine().trim();

        if (s.length() == 0){
            System.out.println(0);
        } else {
            // 공백 하나 이상을 기준으로 split
            String[] word = s.split("\\s+");
            System.out.println(word.length);
        }
    }
}

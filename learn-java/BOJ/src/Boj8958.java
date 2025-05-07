import java.util.*;

public class Boj8958 {

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            String quiz = sc.next();
            int total_score = 0;
            int score = 0;
            for (int j = 0; j < quiz.length(); j++){
                char q = quiz.charAt(j);
                if (q == 'O'){
                    score++;
                } else{
                    score = 0;
                }
                total_score += score;
            }
            System.out.println(total_score);
        }
    }
}

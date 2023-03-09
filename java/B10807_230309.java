import java.util.Scanner;

public class B10807_230309 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ans = 0;

        int N = sc.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int v = sc.nextInt();

        for (int a : arr) {
            if (a == v) ans++;
        }

        System.out.println(ans);
    }
}

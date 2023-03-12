package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B10986_230312 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());   // 전체 수의 개수
        int M = Integer.parseInt(st.nextToken());   // 나눌 수
        long ans = 0;

        st = new StringTokenizer(br.readLine());

        long[] arr = new long[N];
        arr[0] = Integer.parseInt(st.nextToken()) % M;
        if (arr[0] == 0) ans++;

        long[] cnt = new long[M];

        for (int i = 1; i < N; i++) {
            long n = (arr[i - 1] + Integer.parseInt(st.nextToken())) % M;
            arr[i] = n;
            if (n == 0) ans++;
        }

        for (long a : arr) {
            cnt[(int)a]++;
        }


        for (long c : cnt) {
            if (c >= 2) ans += c * (c - 1) / 2;
        }


        System.out.println(ans);
    }
}

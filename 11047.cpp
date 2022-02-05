#include <iostream>
using namespace std;
int N, K, coin;
int arr[11];
int main() {
    // 숫자 입력 받기
    cin >> N >> K;
    for (int i = 0; i < N; i++) {
        // N만큼 배열에 입력 받기
        cin >> arr[i];
    }

    // 인덱스 거꾸로 접근하기
    for (int i = N - 1; i >= 0; i--) {
        // K가 배열의 값보다 클 때 패스
        if (K / arr[i] == 0) continue;
        // K가 배열의 값보다 작을 때 몫 구하기
        else {
            coin += (K / arr[i]); // 몫의 합 구하기
            K -= arr[i] * (K / arr[i]); // 몫을 구하고 해당 경우의 값 빼기
        }
        if (K == 0) {
            break;
        }

    }
    cout << coin;
}
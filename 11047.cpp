#include <iostream>
using namespace std;
int N, K, coin;
int arr[11];
int main() {
    // ���� �Է� �ޱ�
    cin >> N >> K;
    for (int i = 0; i < N; i++) {
        // N��ŭ �迭�� �Է� �ޱ�
        cin >> arr[i];
    }

    // �ε��� �Ųٷ� �����ϱ�
    for (int i = N - 1; i >= 0; i--) {
        // K�� �迭�� ������ Ŭ �� �н�
        if (K / arr[i] == 0) continue;
        // K�� �迭�� ������ ���� �� �� ���ϱ�
        else {
            coin += (K / arr[i]); // ���� �� ���ϱ�
            K -= arr[i] * (K / arr[i]); // ���� ���ϰ� �ش� ����� �� ����
        }
        if (K == 0) {
            break;
        }

    }
    cout << coin;
}
// Repo: https://github.com/SergheiMihailov/competitive-prog
// Link to problem: http://codeforces.com/contest/1041/problem/A
// Language: GNU C++ 11

using namespace std;

int main() {
  int n, k;
  cin >> n;
  cin >> k;
  int min, max;
  min = k;
  max = k;

  for (int i = 1; i < n; i++) {
    cin >> k;
    if (min > k) {
      min = k;
    }
    if (max < k) {
      max = k;
    }
  }

  cout << max - min - n + 1;
}

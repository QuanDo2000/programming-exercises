#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using str = string;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;
using vvi = vector<vi>;
using vl = vector<ll>;
using vd = vector<ld>;
using vvd = vector<vd>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1024 + 2;

const bool DEBUG = 0;

int limN;
bool used[MAX_N][MAX_N];
int cnt[MAX_N * MAX_N], grid[MAX_N][MAX_N];

void check(int x, int y) {
  int num = grid[x][y];
  if (num == 0) {
    used[x][y] = 1;
    cnt[0] = 1;
    return;
  }
  if (x - 1 >= 0 && y - 1 >= 0 && grid[x - 1][y] == num && grid[x][y - 1] == num) {
    used[x][y] = 1;
    used[x - 1][y] = 1;
    used[x][y - 1] = 1;
    cnt[num] = 1;
  } else if (x + 1 < limN && y - 1 >= 0 && grid[x + 1][y] == num && grid[x][y - 1] == num) {
    used[x][y] = 1;
    used[x + 1][y] = 1;
    used[x][y - 1] = 1;
    cnt[num] = 1;
  } else if (x - 1 >= 0 && y + 1 < limN && grid[x - 1][y] == num && grid[x][y + 1] == num) {
    used[x][y] = 1;
    used[x - 1][y] = 1;
    used[x][y + 1] = 1;
    cnt[num] = 1;
  } else if (x + 1 < limN && y + 1 < limN && grid[x + 1][y] == num && grid[x][y + 1] == num) {
    used[x][y] = 1;
    used[x + 1][y] = 1;
    used[x][y + 1] = 1;
    cnt[num] = 1;
  }
}

void solve() {
  fill(cnt, cnt + MAX_N * MAX_N, 0);
  fill(&used[0][0], &used[0][0] + MAX_N * MAX_N, 0);

  int n;
  cin >> n;

  limN = pow(2, n);
  int limC = (pow(4, n) - 1) / 3;

  for (int i = 0; i < limN; i++) {
    for (int j = 0; j < limN; j++) {
      cin >> grid[i][j];
      cnt[grid[i][j]]++;
    }
  }

  if (cnt[0] != 1) {
    cout << 0 << "\n";
    return;
  }

  for (int i = 1; i <= limC; i++) {
    if (cnt[i] != 3) {
      cout << 0 << "\n";
      return;
    }
  }

  fill(cnt, cnt + MAX_N * MAX_N, 0);

  for (int i = 0; i < limN; i++) {
    for (int j = 0; j < limN; j++) {
      if (!used[i][j]) check(i, j);
    }
  }

  for (int i = 1; i <= limC; i++) {
    if (cnt[i] != 1) {
      cout << 0 << "\n";
      return;
    }
  }

  for (int i = 0; i < limN; i++) {
    for (int j = 0; j < limN; j++) {
      if (!used[i][j]) {
        cout << 0 << "\n";
        return;
      }
    }
  }

  cout << 1 << "\n";
  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
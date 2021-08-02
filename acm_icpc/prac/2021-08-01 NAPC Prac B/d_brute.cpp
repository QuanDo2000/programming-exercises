#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 500 + 2;

const bool DEBUG = 0;

bool used[MAX_N][MAX_N];

bool chkRect(int a, int b, int c, int d, int n, int m) {
  for (int i = a; i <= c; i++) {
    for (int j = b; j <= d; j++) {
      if (used[i][j]) return false;
    }
  }
  return true;
}

ll countRect(int n, int m) {
  ll cnt = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      for (int k = i; k <= n; k++) {
        for (int l = j; l <= m; l++) {
          if (chkRect(i, j, k, l, n, m)) {
            cnt++;
          }
        }
      }
    }
  }
  return cnt;
}

void solve() {
  fill(&used[0][0], &used[0][0] + MAX_N * MAX_N, 0);

  int n, m;
  cin >> n >> m;

  for (int i = 0; i < n * m; i++) {
    int a, b;
    cin >> a >> b;
    used[a][b] = 1;
    ll cnt = countRect(n, m);
    cout << cnt << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
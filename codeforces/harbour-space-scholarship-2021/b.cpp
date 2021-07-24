#include <bits/stdc++.h>

using namespace std;

// Macros
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define all(x) (x).begin(), (x).end()

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using vi = vector<int>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e3 + 2;

const bool DEBUG = 0;

string s, t;
int dp[MAX_N][MAX_N];

bool recur(int i, int j, bool flip) {
  if (j == t.length()) {
    return true;
  }
  if (i < 0 || i >= s.length()) {
    return false;
  }
  if (dp[i][j] != -1) {
    return dp[i][j];
  }
  bool ans = false;
  if (s[i] == t[j] && !flip) {
    ans = recur(i + 1, j + 1, 0) || recur(i - 1, j + 1, 1);
  } else if (s[i] == t[j] && flip) {
    ans = recur(i - 1, j + 1, 1);
  } else {
    ans = recur(i + 1, 0, 0);
  }
  dp[i][j] = ans ? 1 : 0;
  return ans;
}

void solve() {
  fill(&dp[0][0], &dp[0][0] + MAX_N * MAX_N, -1);

  cin >> s >> t;

  bool ans;
  ans = recur(0, 0, 0);
  if (ans) {
    cout << "YES\n";
  } else {
    cout << "NO\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int q;
  cin >> q;
  while (q--) {
    solve();
  }

  return 0;
}
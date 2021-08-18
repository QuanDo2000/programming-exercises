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

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

int a[3][3], used[3][3];

void solve() {
  fill(&a[0][0], &a[0][0] + 3 * 3, 0);
  fill(&used[0][0], &used[0][0] + 3 * 3, 0);

  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cin >> a[i][j];
    }
  }

  int n;
  cin >> n;

  for (int i = 0; i < n; i++) {
    int b;
    cin >> b;

    for (int j = 0; j < 3; j++) {
      for (int k = 0; k < 3; k++) {
        if (b == a[j][k]) used[j][k] = 1;
      }
    }
  }

  int ans = 0;
  for (int i = 0; i < 3; i++) {
    if (used[i][0] == 1 && used[i][0] == used[i][1] && used[i][0] == used[i][2]) ans++;
    if (used[0][i] == 1 && used[0][i] == used[1][i] && used[0][i] == used[2][i]) ans++;
  }

  if (used[0][0] == 1 && used[0][0] == used[1][1] && used[0][0] == used[2][2]) ans++;
  if (used[0][2] == 1 && used[0][2] == used[1][1] && used[0][2] == used[2][0]) ans++;

  cout << (ans ? "Yes" : "No") << "\n";

  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // int tc;
  // cin >> tc;
  // for (int i = 0; i < tc; i++)
  solve();

  return 0;
}
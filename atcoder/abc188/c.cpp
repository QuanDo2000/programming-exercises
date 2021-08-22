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

const bool DEBUG = 1;

void solve() {
  int n;
  cin >> n;

  vl a(1 << n), prev, curr(1 << n);
  for (int i = 0; i < (1 << n); i++) {
    cin >> a[i];
    curr[i] = i;
  }

  for (int i = 1; i <= n; i++) {
    prev = curr;
    curr = {};
    for (int j = 1; j <= (1 << (n - i)); j++) {
      if (a[prev[2 * (j - 1)]] > a[prev[2 * (j - 1) + 1]])
        curr.push_back(prev[2 * (j - 1)]);
      else
        curr.push_back(prev[2 * (j - 1) + 1]);
    }
  }

  for (int i = 0; i < 2; i++) {
    if (prev[i] != curr[0]) cout << prev[i] + 1;
  }
  cout << "\n";

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
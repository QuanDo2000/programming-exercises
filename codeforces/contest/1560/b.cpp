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

void solve() {
  int a, b, c;
  cin >> a >> b >> c;

  if (a > b) swap(a, b);
  int n = b - a;

  int ans = -1;
  if (a > 2 * n || b > 2 * n || c > 2 * n)
    ans = -1;
  else if (c > n && c - n < 1)
    ans = -1;
  else if (c + n <= 2 * n)
    ans = c + n;
  else if (c - n >= 1)
    ans = c - n;
  cout << ans << "\n";

  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tc;
  cin >> tc;
  for (int i = 0; i < tc; i++)
    solve();

  return 0;
}
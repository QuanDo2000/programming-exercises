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
  str s;
  cin >> s;

  int ans;
  if (s == "SUN")
    ans = 7;
  else if (s == "MON")
    ans = 6;
  else if (s == "TUE")
    ans = 5;
  else if (s == "WED")
    ans = 4;
  else if (s == "THU")
    ans = 3;
  else if (s == "FRI")
    ans = 2;
  else
    ans = 1;
  cout << ans << "\n";

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
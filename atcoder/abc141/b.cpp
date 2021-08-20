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

  bool ans = 1;
  for (int i = 0; i < s.size(); i++) {
    if (i % 2 == 0) {
      if (s[i] != 'R' && s[i] != 'U' && s[i] != 'D') ans = 0;
    } else {
      if (s[i] != 'L' && s[i] != 'U' && s[i] != 'D')
        ans = 0;
    }
  }
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
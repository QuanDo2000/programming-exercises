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
  str s;
  cin >> s;

  str ans = "";
  for (int i = 0; i < n; i++) {
    if (s[i] != '?')
      ans += s[i];
    else if (ans == "")
      ans += s[i];
    else if (ans.back() == 'R')
      ans += 'B';
    else if (ans.back() == 'B')
      ans += 'R';
    else if (ans.back() == '?')
      ans += '?';
  }

  s = ans;
  ans = "";
  for (int i = n - 1; i >= 0; i--) {
    if (s[i] != '?')
      ans += s[i];
    else if (ans == "")
      ans += 'R';
    else if (ans.back() == 'R')
      ans += 'B';
    else if (ans.back() == 'B')
      ans += 'R';
    else if (ans.back() == '?')
      ans += '?';
  }

  reverse(ans.begin(), ans.end());

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
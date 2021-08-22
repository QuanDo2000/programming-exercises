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

ll g1(ll x) {
  str s = to_string(x);
  sort(s.begin(), s.end(), greater<char>());
  return stol(s);
}

ll g2(ll x) {
  str s = to_string(x);
  sort(s.begin(), s.end());
  return stol(s);
}

void solve() {
  ll n, k;
  cin >> n >> k;

  ll curr = n;
  for (int i = 1; i <= k; i++) {
    curr = g1(curr) - g2(curr);
  }
  cout << curr << "\n";

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
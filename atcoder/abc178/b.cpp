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

const ll INF = 1e18;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

void solve() {
  ll a, b, c, d;
  cin >> a >> b >> c >> d;
  ll mx = -INF;

  if ((a * c) > mx) mx = a * c;
  if ((a * d) > mx) mx = a * d;
  if ((b * c) > mx) mx = b * c;
  if ((b * d) > mx) mx = b * d;
  cout << mx << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
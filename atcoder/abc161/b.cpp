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
  int n, m;
  cin >> n >> m;

  vi a(n);
  int total = 0;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    total += a[i];
  }

  ld lim = (ld)total / (4 * m);

  int ans = 0;
  for (int i = 0; i < n; i++) {
    if (a[i] >= lim) {
      ans++;
    }
  }

  if (ans >= m)
    cout << "Yes";
  else
    cout << "No";
  cout << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
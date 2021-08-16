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

const int MAX_N = 100 + 2;

const bool DEBUG = 0;

bool used[MAX_N];

void solve() {
  fill(used, used + MAX_N, 0);

  int x, n;
  cin >> x >> n;

  vi p(n);
  for (int i = 0; i < n; i++) {
    cin >> p[i];
    used[p[i]] = 1;
  }

  int offset = 0;
  while (true) {
    int lo = x - offset, hi = x + offset;
    if (used[lo] == 0) {
      cout << lo << "\n";
      return;
    } else if (used[hi] == 0) {
      cout << hi << "\n";
      return;
    }
    offset++;
  }

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
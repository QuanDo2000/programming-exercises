#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

void solve() {
  int n, m;
  cin >> n >> m;

  vii cases = {};
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      cases.push_back({i, j});
    }
  }
  random_shuffle(cases.begin(), cases.end());
  cout << n << " " << m << "\n";
  for (auto &c : cases) {
    cout << c.first << " " << c.second << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
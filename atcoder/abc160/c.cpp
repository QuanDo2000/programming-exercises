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
  int k, n;
  cin >> k >> n;

  vi a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  int gap = k - a.back() + a.front();
  for (int i = 1; i < a.size() - 1; i++) {
    if (a[i + 1] - a[i] > gap) {
      gap = a[i + 1] - a[i];
    }
  }
  cout << k - gap << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
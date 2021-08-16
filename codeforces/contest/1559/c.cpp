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
  int n;
  cin >> n;

  vi a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  if (a[0] == 1) {
    cout << n + 1 << " ";
    for (int i = 1; i <= n; i++) {
      cout << i << " ";
    }
    cout << "\n";
    return;
  } else if (a.back() == 0) {
    for (int i = 1; i <= n + 1; i++) {
      cout << i << " ";
    }
    cout << "\n";
    return;
  }
  int num = 0;
  for (int i = 0; i < n - 1; i++) {
    if (a[i] == 0 && a[i + 1] == 1) {
      num = i + 1;
      break;
    }
  }
  for (int i = 1; i <= n; i++) {
    cout << i << " ";
    if (i == num) cout << n + 1 << " ";
  }
  cout << "\n";
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
#include <bits/stdc++.h>

using namespace std;

// Macros
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define all(x) (x).begin(), (x).end()

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using vi = vector<int>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 100 + 2;

const bool DEBUG = 0;

void solve() {
  int n, a, b;
  cin >> n >> a >> b;

  char s[MAX_N];
  cin >> s;

  int ans = 0;
  if (b >= 0) {
    ans = a * n + b * n;
    cout << ans << "\n";
    return;
  }

  int c = 1;
  char prev = s[0];
  ans = a * n;
  rep(i, 0, n) {
    if (s[i] != prev) {
      c++;
    }
    prev = s[i];
  }
  cout << ans + b * (c / 2 + 1) << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  while (t--) {
    solve();
  }

  return 0;
}
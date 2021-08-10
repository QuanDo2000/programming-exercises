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

const int MAX_N = 40 + 2;

const bool DEBUG = 0;

char s[MAX_N], c[MAX_N];

void solve() {
  fill(s, s + MAX_N, 0);
  fill(c, c + MAX_N, 0);

  int n;
  cin >> n;
  cin >> s;

  strcpy(c, s);

  sort(c, c + n);

  int ans = 0;
  rep(i, 0, n) {
    if (c[i] != s[i]) {
      ans++;
    }
  }
  cout << ans << "\n";
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
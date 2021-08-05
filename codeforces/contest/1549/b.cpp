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

const int MAX_N = 2 * 1e5 + 2;

const bool DEBUG = 0;

char a[MAX_N], b[MAX_N];

void solve() {
  fill(a, a + MAX_N, '0');
  fill(b, b + MAX_N, '0');

  int n;
  cin >> n;

  cin >> b;
  cin >> a;

  if (DEBUG) {
    cout << a << " " << b << "\n";
  }

  int ans = 0;
  for (int i = 0; i < n; i++) {
    if (a[i] == '1') {
      if ((i - 1) >= 0 && b[i - 1] == '1') {
        b[i - 1] = '2';
        ans++;
      } else if (b[i] == '0') {
        ans++;
      } else if ((i + 1) < n && b[i + 1] == '1') {
        b[i + 1] = '2';
        ans++;
      }
    }
  }
  cout << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tc;
  cin >> tc;
  while (tc--) {
    solve();
  }

  return 0;
}
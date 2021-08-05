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

const int MAX_N = 10 + 2;

const bool DEBUG = 0;

int a[MAX_N];
int n, c = 0;

void dfs(int idx, int sum) {
  if (idx >= n) {
    c += sum == 0;
    return;
  }
  rep(s, -1, 2) {
    dfs(idx + 1, sum + s * a[idx]);
  }
}

void solve() {
  fill(a, a + MAX_N, 0);
  c = 0;

  cin >> n;

  rep(i, 0, n) {
    cin >> a[i];
  }

  dfs(0, 0);
  if (c > 1) {
    cout << "YES\n";
  } else {
    cout << "NO\n";
  }
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
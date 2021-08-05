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

const int MAX_N = 50000 + 2;

const bool DEBUG = 0;

int r[MAX_N][5];

void solve() {
  fill(&r[0][0], &r[0][0] + MAX_N * 5, 0);

  int n;
  cin >> n;
  rep(i, 0, n) {
    rep(j, 0, 5) {
      cin >> r[i][j];
    }
  }

  int curr = n - 1, c;
  rep(i, 0, n) {
    c = 0;
    rep(j, 0, 5) {
      if (r[curr][j] > r[i][j]) {
        c++;
      }
    }
    if (c >= 3) {
      curr = i;
    }
  }

  rep(i, 0, n) {
    c = 0;
    rep(j, 0, 5) {
      if (r[curr][j] > r[i][j]) {
        c++;
      }
    }
    if (c >= 3 && curr != i) {
      cout << "-1\n";
      return;
    }
  }
  cout << curr + 1 << "\n";
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
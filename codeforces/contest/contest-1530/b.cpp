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

const int MAX_N = 20 + 2;

const bool DEBUG = 0;

bool table[MAX_N][MAX_N] = {};

void solve() {
  int h, w;
  cin >> h >> w;

  fill(&table[0][0], &table[0][0] + MAX_N * MAX_N, 0);

  rep(i, 0, h) {
    rep(j, 0, w) {
      if (i == 0 || i == h - 1) {
        if (table[i][j - 1] != 1 && table[i][j + 1] != 1) {
          table[i][j] = 1;
        }
      } else if (i > 1 && i < h - 2) {
        if (j == 0 || j == w - 1) {
          if (table[i - 1][j] != 1 && table[i + 1][j] != 1) {
            table[i][j] = 1;
          }
        }
      }
      cout << table[i][j];
    }
    cout << "\n";
  }
  cout << "\n";
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
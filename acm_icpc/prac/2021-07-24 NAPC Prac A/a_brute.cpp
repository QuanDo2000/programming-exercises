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

const int MAX_N = 1e5 + 2;

const bool DEBUG = 0;

int barn[MAX_N];

void solve() {
  fill(barn, barn + MAX_N, 0);

  int n, q;
  cin >> n >> q;

  rep(i, 0, n) {
    cin >> barn[i];
  }

  int qi, l, r, k, c;
  rep(i, 0, q) {
    cin >> qi >> l >> r;
    if (qi == 1) {
      cin >> k;
      rep(j, l - 1, r) {
        barn[j] += k;
      }
    } else if (qi == 2) {
      rep(j, l - 1, r) {
        barn[j] = barn[j] >> 1;
      }
    } else if (qi == 3) {
      c = 0;
      rep(j, l - 1, r) {
        c += barn[j];
      }
      cout << c << "\n";
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
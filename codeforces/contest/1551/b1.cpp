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

const int MAX_N = 26 + 2;

const bool DEBUG = 0;

int cnt[MAX_N];

void solve() {
  fill(cnt, cnt + MAX_N, 0);

  string n;
  cin >> n;

  rep(i, 0, n.size()) {
    int idx = n[i] - 97;
    cnt[idx]++;
  }

  int c1 = 0, c2 = 0;
  rep(i, 0, (int)MAX_N) {
    if (cnt[i] > 1) {
      c2++;
    } else if (cnt[i] == 1) {
      c1++;
    }
  }

  cout << c2 + c1 / 2 << "\n";
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
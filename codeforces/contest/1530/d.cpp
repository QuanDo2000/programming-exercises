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

const int MAX_N = 2 * 1e5 + 2;

const bool DEBUG = 0;

int a[MAX_N], b[MAX_N], nxt[MAX_N], mark[MAX_N];

int findNext(int idx) {
  if (mark[idx] == 0) {
    return idx;
  }
  nxt[idx] = findNext(nxt[idx]);
  return nxt[idx];
}

void solve() {
  fill(a, a + MAX_N, 0);
  fill(b, b + MAX_N, 0);
  fill(mark, mark + MAX_N, 0);
  iota(nxt, nxt + MAX_N, 1);

  int n;
  cin >> n;

  nxt[n] = 1;

  int temp, k = 0;
  rep(i, 0, n) {
    cin >> a[i];
  }

  cout << k << "\n";
  rep(i, 0, n) {
    cout << b[i] << " ";
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
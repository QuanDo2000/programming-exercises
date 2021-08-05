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

int cnt[MAX_N];

void solve() {
  fill(cnt, cnt + MAX_N, 0);

  int n, m;
  cin >> n >> m;

  int dead = 0;
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    if (u > v) swap(u, v);
    cnt[u]++;
    if (cnt[u] == 1) dead++;
  }

  int q;
  cin >> q;
  while (q--) {
    int qi;
    cin >> qi;
    if (qi == 3)
      cout << n - dead << "\n";
    else {
      int u, v;
      cin >> u >> v;
      if (u > v) swap(u, v);
      if (qi == 1) {
        cnt[u]++;
        if (cnt[u] == 1) dead++;
      } else {
        cnt[u]--;
        if (cnt[u] == 0) dead--;
      }
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
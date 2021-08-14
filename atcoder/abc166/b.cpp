#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using str = string;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;
using vvi = vector<vi>;
using vl = vector<ll>;
using vd = vector<ld>;
using vvd = vector<vd>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

bool a[MAX_N];

void solve() {
  fill(a, a + MAX_N, 0);

  int n, k;
  cin >> n >> k;

  for (int i = 0; i < k; i++) {
    int nt;
    cin >> nt;
    for (int j = 0; j < nt; j++) {
      int tmp;
      cin >> tmp;
      a[tmp - 1] = 1;
    }
  }

  int ans = 0;
  for (int i = 0; i < n; i++) {
    if (a[i] == 0) ans++;
  }
  cout << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
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

void solve() {
  ll n;
  int m;
  cin >> n >> m;

  map<int, int> last;

  ll total = 0;
  for (int i = 0; i < m; i++) {
    int p;
    cin >> p;

    int unseen;
    if (last.count(p) == 1)
      unseen = i - last[p] - 1;
    else
      unseen = i;

    if (DEBUG)
      cout << i << " " << unseen << "\n";

    total = total - unseen + (n - 1);
    cout << total << "\n";

    last[p] = i;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
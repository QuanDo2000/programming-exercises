#include <bits/stdc++.h>

using namespace std;

// Macros
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define all(x) (x).begin(), (x).end()

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<pair<int, int>>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 2 * 100 + 2;

const bool DEBUG = 0;

bool used[MAX_N];

bool intersect(ii c1, ii c2) {
  if (c1.first > c2.first) {
    swap(c1, c2);
  }
  return c1.second > c2.first && c1.second < c2.second;
}

void solve() {
  fill(used, used + MAX_N, 0);
  int n, k;
  cin >> n >> k;

  vii chords;
  rep(i, 0, k) {
    int x, y;
    cin >> x >> y;
    if (x > y) {
      swap(x, y);
    }
    chords.push_back({x, y});
    used[x] = used[y] = true;
  }

  vi unused;
  rep(i, 0, 2 * n) {
    if (!used[i + 1]) {
      unused.push_back(i + 1);
    }
  }
  rep(i, 0, n - k) {
    chords.push_back({unused[i], unused[i + n - k]});
  }
  int ans = 0;
  rep(i, 0, n) {
    rep(j, i + 1, n) {
      ans += intersect(chords[i], chords[j]);
    }
  }
  cout << ans << "\n";
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
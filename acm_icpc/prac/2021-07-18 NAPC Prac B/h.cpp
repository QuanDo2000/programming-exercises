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

char s[MAX_N], r[MAX_N];

void solve() {
  int n;
  cin >> n;

  cin >> s;
  cin >> r;

  char prev = s[n - 1];
  int cs = 0, cr = 0;
  bool bs = 0, br = 0;
  int c = 1;
  rep(i, 0, n) {
    if (DEBUG) {
      cout << prev << " " << s[i] << " " << c << "\n";
    }
    if (s[i] != prev) {
      cs++;
      bs = (c > 1) ? 1 : bs;
      c = 0;
    }
    c++;
    prev = s[i];
  }

  prev = r[n - 1];
  c = 1;
  rep(i, 0, n) {
    if (r[i] != prev) {
      cr++;
      br = (c > 1) ? 1 : br;
      c = 0;
    }
    c++;
    prev = r[i];
  }

  if (DEBUG) {
    cout << br << " " << bs << "\n";
  }

  if (cs > cr) {
    cout << "yes\n";
  } else if (cs < cr) {
    cout << "no\n";
  } else {
    if (!br && !bs && (s[0] != r[0])) {
      cout << "no\n";
    } else {
      cout << "yes\n";
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
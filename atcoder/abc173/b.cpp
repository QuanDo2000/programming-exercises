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
  int n;
  cin >> n;

  int a = 0, w = 0, t = 0, r = 0;
  for (int i = 0; i < n; i++) {
    str s;
    cin >> s;
    if (s == "AC") {
      a++;
    } else if (s == "WA") {
      w++;
    } else if (s == "TLE") {
      t++;
    } else if (s == "RE") {
      r++;
    }
  }
  cout << "AC x " << a << "\n";
  cout << "WA x " << w << "\n";
  cout << "TLE x " << t << "\n";
  cout << "RE x " << r << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
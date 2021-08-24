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
  str s;
  cin >> s;

  vi v(4);
  for (int i = 0; i < s.size(); i++) {
    v[i] = s[i] - '0';
  }

  for (int i = 0; i < (1 << 3); i++) {
    int sum = v[0];
    bitset<3> state(i);

    for (int j = 1; j < 4; j++) {
      if (state[j - 1])
        sum += v[j];
      else
        sum -= v[j];
    }
    if (sum == 7) {
      for (int j = 0; j < 4; j++) {
        cout << v[j];
        if (j < 3 && state[j])
          cout << "+";
        else if (j < 3 && !state[j])
          cout << "-";
      }
      cout << "=7\n";
      return;
    }
  }

  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // int tc;
  // cin >> tc;
  // for (int i = 0; i < tc; i++)
  solve();

  return 0;
}
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

  ll ans_man = 0, ans_che = 0;
  ld ans_euc = 0;
  for (int i = 0; i < n; i++) {
    ll x;
    cin >> x;
    ans_man += abs(x);
    ans_euc += pow(x, 2);
    ans_che = max(ans_che, abs(x));
  }
  ans_euc = sqrt(ans_euc);

  cout << ans_man << "\n";
  cout << fixed << setprecision(11) << ans_euc << "\n";
  cout << ans_che << "\n";

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
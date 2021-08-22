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

bool isPalindrome(str s) {
  if (s.size() == 0)
    return true;
  else {
    bool ans = true;
    for (int i = 0; i < s.size() / 2; i++) {
      if (s[i] != s[s.size() - 1 - i]) ans = false;
    }
    return ans;
  }
}

void solve() {
  str n;
  cin >> n;

  for (int i = n.size() - 1; i >= 0; i--) {
    if (n[i] == '0')
      n.erase(i);
    else
      break;
  }
  if (DEBUG) cout << n << "\n";

  if (isPalindrome(n))
    cout << "Yes";
  else
    cout << "No";
  cout << "\n";

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
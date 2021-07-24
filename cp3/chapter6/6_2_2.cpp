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

const int MAX_N = 1e9 + 2;

const bool DEBUG = 1;

void solve() {
  string t, p;
  int pos;

  t = "I love CS3233 Competitive Programming. i also love AlGoRiThM";
  p = "book";

  pos = t.find(p, 0);
  if (pos == t.npos) {
    cout << pos;
  }
  while (pos != t.npos) {
    cout << pos << " ";
    pos = t.find(p, pos + 1);
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
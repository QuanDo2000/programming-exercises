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

const int MAX_N = 2e5 + 2;

const bool DEBUG = 0;

struct it {
  int l, r;
  it() { l = r = 0; }
  it(int L, int R) {
    l = L;
    r = R;
  }
} a[MAX_N];
bool cmp(it a, it b) {
  return a.l < b.l;
}
bool operator<(it a, it b) {
  return a.r < b.r;
}
bool operator>(it a, it b) {
  return b < a;
}
priority_queue<it, vector<it>, greater<it>> b1;
priority_queue<it> b2;

void solve() {
  int n, m;
  cin >> n >> m;

  rep(i, 1, n + 1) {
    cin >> a[i].l >> a[i].r;
  }
  sort(a + 1, a + 1 + n, cmp);

  int le = 0;
  b1.push(it(0, m + 1));
  rep(i, 1, n + 1) {
    if (le < a[i].l) {
      le++;
      b1.push(a[i]);
    } else {
      if (a[i] > b1.top()) {
        b2.push(b1.top());
        b1.pop();
        b1.push(a[i]);
      } else {
        b2.push(a[i]);
      }
    }
  }
  int ans = 0, le2 = m + 1;
  while (!b2.empty()) {
    it t = b2.top();
    b2.pop();
    if (le2 > max(t.r, le + 1)) {
      le2--;
    } else {
      ans++;
    }
  }
  cout << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
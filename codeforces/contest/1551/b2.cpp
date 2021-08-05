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

const int MAX_N = 2 * 1e5 + 2;

const bool DEBUG = 0;

int ans[MAX_N];

void solve() {
  fill(ans, ans + MAX_N, 0);

  map<int, int> mp;
  map<int, vi> idxs;
  vi stk = {};

  int n, k;
  cin >> n >> k;

  int temp;
  rep(i, 0, n) {
    cin >> temp;
    mp[temp]++;
    idxs[temp].push_back(i);
  }

  for (auto const& [key, val] : mp) {
    if (val >= k) {
      rep(i, 0, k) {
        ans[idxs[key][i]] = i + 1;
      }
    } else {
      rep(i, 0, (int)val) {
        stk.push_back(idxs[key][i]);
        if (stk.size() >= k) {
          rep(j, 0, k) {
            ans[stk.back()] = j + 1;
            stk.pop_back();
          }
        }
      }
    }
  }

  rep(i, 0, n) {
    cout << ans[i] << " ";
  }
  cout << "\n";
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
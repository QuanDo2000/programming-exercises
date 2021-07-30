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

vi v[MAX_N];

void debug(int i, priority_queue<int, vi, greater<int>> pq) {
  if (!DEBUG) {
    return;
  }
  cout << i << " | ";
  while (!pq.empty()) {
    cout << pq.top() << " ";
    pq.pop();
  }
  cout << "\n";
}

void debug(int m) {
  if (!DEBUG) {
    return;
  }
  rep(i, 0, m + 2) {
    if (!v[i].empty()) {
      cout << "\t" << i << " | ";
      for (auto& item : v[i]) {
        cout << item << " ";
      }
      cout << "\n";
    }
  }
}

void solve() {
  priority_queue<int, vi, greater<int>> pq;
  int n, m;
  cin >> n >> m;

  int l, r;
  rep(i, 1, n + 1) {
    cin >> l >> r;
    if (l == 0) {
      pq.push(r);
    } else {
      v[l].push_back(r);
    }
  }

  rep(i, 1, m + 2) {
    sort(v[i].begin(), v[i].end());
  }

  int pos = -1;
  rep(i, 1, m + 1) {
    debug(i, pq);
    debug(m);
    if (v[i].size() > 1) {
      rep(j, 0, v[i].size() - 1) {
        pq.push(v[i][j]);
      }
    } else if (v[i].size() == 0) {
      if (!pq.empty()) {
        if (pq.top() <= i) {
          pq.pop();
        } else {
          pos = max(pos, i);
          while (!v[pos].size() && pos <= m) {
            pos++;
          }
          if (v[pos].size()) {
            v[pos].pop_back();
          }
        }
      } else {
        pos = max(pos, i);
        while (!v[pos].size() && pos <= m) {
          pos++;
        }
        if (v[pos].size()) {
          v[pos].pop_back();
        }
      }
    }
  }
  debug(m + 1, pq);

  int ans = pq.size();
  cout << ans << "\n";
  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
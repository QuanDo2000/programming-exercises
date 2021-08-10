// http://zafar.cc/2017/7/19/hungarian-algorithm/

#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
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

const int MAX_N = 100 + 2;

const bool DEBUG = 0;

ld getDist(ii p1, ii p2) {
  int x = p1.first - p2.first;
  int y = p1.second - p2.second;
  return sqrt(x * x + y * y);
}

void solve() {
  int n;
  cin >> n;

  vii male, fale;
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    male.push_back({x, y});
  }
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    fale.push_back({x, y});
  }

  vvd A;

  for (int i = 0; i <= n; i++) {
    for (int j = 0; j <= n; j++) {
      ld dist;
      if (i == 0 || j == 0) {
        dist = INF;
      } else {
        dist = getDist(male[i - 1], fale[j - 1]);
      }
      if (j == 0) {
        A.push_back({dist});
      } else {
        A[i].push_back(dist);
      }
      if (DEBUG) cout << A[i][j] << " ";
    }
    if (DEBUG) cout << "\n";
  }

  vd u(n + 1), v(n + 1), p(n + 1), way(n + 1);
  for (int i = 1; i <= n; i++) {
    p[0] = i;
    int j0 = 0;
    vd minv(n + 1, INF);
    vector<bool> used(n + 1, false);
    do {
      used[j0] = true;
      int i0 = p[j0], delta = INF, j1;
      for (int j = 1; j <= n; j++) {
        if (!used[j]) {
          ld cur = A[i0][j] - u[i0] - v[j];
          if (cur < minv[j]) {
            minv[j] = cur, way[j] = j0;
          }
          if (minv[j] < delta) {
            delta = minv[j], j1 = j;
          }
        }
      }
      for (int j = 0; j <= n; j++) {
        if (used[j]) {
          u[p[j]] += delta, v[j] -= delta;
        } else {
          minv[j] -= delta;
        }
      }
      j0 = j1;
    } while (p[j0] != 0);
    do {
      int j1 = way[j0];
      p[j0] = p[j1];
      j0 = j1;
    } while (j0);
  }

  for (int i = 1; i <= n; i++) {
    cout << i << " " << p[i] << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
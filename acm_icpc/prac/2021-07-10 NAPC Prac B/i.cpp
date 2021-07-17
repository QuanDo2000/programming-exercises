#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const int INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-6;

const bool DEBUG = 0;

const int MAX_N = 1000 + 2;

int x[MAX_N], y[MAX_N];

int dist(int px, int py, int x, int y) {
  return (px - x) * (px - x) + (py - y) * (py - y);
}

ll getScore(int n, int px, int py) {
  ll score = 0;
  for (int i = 0; i < n; i++) {
    score += dist(px, py, x[i], y[i]);
  }
  return score;
}

void solve(int n) {
  fill(x, x + MAX_N, 0);
  fill(y, y + MAX_N, 0);
  for (int i = 0; i < n; i++) {
    cin >> x[i] >> y[i];
  }

  int px = 0, py = 0;
  int d = 1000;
  ll score = getScore(n, px, py);
  while (d != 0) {
    if (DEBUG) {
      cout << px << " " << py << " " << d << " " << score << "\n";
    }
    ll up, down, left, right;
    up = getScore(n, px + d, py);
    down = getScore(n, px - d, py);
    left = getScore(n, px, py - d);
    right = getScore(n, px, py + d);
    if (down <= score) {
      px -= d;
      score = down;
    } else if (left <= score) {
      py -= d;
      score = left;
    } else if (up < score) {
      px += d;
      score = up;
    } else if (right < score) {
      py += d;
      score = right;
    } else {
      d /= 2;
    }
  }
  cout << px << " " << py << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  while (true) {
    cin >> n;
    if (n == 0) {
      break;
    }
    solve(n);
  }

  return 0;
}
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

const int MAX_N = 1e5 + 2;

const bool DEBUG = 0;

struct Player {
  int score = 0, n = 0, s = 0;
  priority_queue<int> mx, mn;

  void push(int temp) {
    n++;
    s = n - (n / 4);
    if (mx.size() < s) {
      if (!mn.empty() && mn.top() > temp) {
        score += mn.top();
        mx.push(-mn.top());
        mn.pop();
        mn.push(temp);
      } else {
        mx.push(-temp);
        score += temp;
      }
    } else {
      if (temp > -mx.top()) {
        score += mx.top();
        mn.push(-mx.top());
        mx.pop();
        mx.push(-temp);
        score += temp;
      } else {
        mn.push(temp);
      }
    }
  }
};

void solve() {
  int n;
  cin >> n;

  Player a, b;

  int temp;
  rep(i, 0, n) {
    cin >> temp;
    a.push(temp);
  }
  rep(i, 0, n) {
    cin >> temp;
    b.push(temp);
  }

  if (DEBUG) {
    cout << a.score << " " << b.score << "\n";
  }

  int c = 0;
  while (a.score < b.score) {
    a.push(100);
    b.push(0);
    c++;
  }
  cout << c << "\n";
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
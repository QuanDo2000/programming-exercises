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

const int MAX_N = 27 + 2;

const bool DEBUG = 0;

void setRule(vi& rule, vi& prev_rule) {
  for (int i = 0; i < rule.size(); i++) {
    prev_rule[i] = rule[i];
  }
}

void changeRule(vi& rule, vi& prev_rule) {
  for (int i = 0; i < rule.size(); i++) {
    rule[i] = prev_rule[rule[i]];
  }
}

void printRule(vi& rule) {
  for (int i = 0; i < rule.size(); i++) {
    cout << rule[i] << " ";
  }
  cout << "\n";
}

void solve() {
  vi rule(MAX_N), prev_rule(MAX_N);
  for (int i = 0; i < 27; i++) {
    char temp;
    cin >> temp;
    rule[i] = temp - 'A';
    if (temp == '_') {
      rule[i] -= 4;
    }
  }

  int n;
  cin >> n;
  setRule(rule, prev_rule);
  for (int i = 2; i <= n; i++) {
    changeRule(rule, prev_rule);
    if (DEBUG) printRule(rule);
  }

  str line;
  cin >> line;
  str ans = "";
  for (auto& ch : line) {
    int idx = ch - 'A';
    if (ch == '_') idx -= 4;
    char nxt = rule[idx];
    if (nxt == 26) nxt += 4;
    ans += (nxt + 'A');
  }
  cout << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
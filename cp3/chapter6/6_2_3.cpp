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

const bool DEBUG = 0;

bool isVowel[CHAR_MAX] = {false};

void init() {
  isVowel['A'] = true;
  isVowel['a'] = true;
  isVowel['E'] = true;
  isVowel['e'] = true;
  isVowel['I'] = true;
  isVowel['i'] = true;
  isVowel['O'] = true;
  isVowel['o'] = true;
  isVowel['U'] = true;
  isVowel['u'] = true;
}

void solve() {
  string t;
  getline(cin, t);

  int d = 0, v = 0, c = 0;

  rep(i, 0, t.length()) {
    if (isdigit(t[i])) {
      d++;
    } else if (isVowel[t[i]]) {
      v++;
    } else if (t[i] != ' ') {
      c++;
    }
  }
  cout << d << " " << v << " " << c << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  init();
  solve();

  return 0;
}
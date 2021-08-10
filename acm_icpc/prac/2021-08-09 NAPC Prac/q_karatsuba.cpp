// https://drawar.github.io/karatsuba-cpp/

#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;
using str = string;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

str add(str lhs, str rhs) {
  int len = max(lhs.size(), rhs.size());
  int carry = 0;
  int sum_col;
  str res;

  while (lhs.size() < len) {
    lhs.insert(0, "0");
  }
  while (rhs.size() < len) {
    rhs.insert(0, "0");
  }

  for (int i = len - 1; i >= 0; i--) {
    sum_col = (lhs[i] - '0') + (rhs[i] - '0') + carry;
    carry = sum_col / 10;
    res.insert(0, to_string(sum_col % 10));
  }
  if (carry) {
    res.insert(0, to_string(carry));
  }

  return res.erase(0, min(res.find_first_not_of('0'), res.size() - 1));
}

str subtract(str lhs, str rhs) {
  int len = max(lhs.size(), rhs.size());
  int diff;
  str res;

  while (lhs.size() < len) {
    lhs.insert(0, "0");
  }
  while (rhs.size() < len) {
    rhs.insert(0, "0");
  }

  for (int i = len - 1; i >= 0; i--) {
    diff = (lhs[i] - '0') - (rhs[i] - '0');
    if (diff >= 0) {
      res.insert(0, to_string(diff));
    } else {
      int j = i - 1;
      while (j >= 0) {
        lhs[j] = ((lhs[j] - '0') - 1) % 10 + '0';
        if (lhs[j] != '9') {
          break;
        } else {
          j--;
        }
      }
      res.insert(0, to_string(diff + 10));
    }
  }

  return res.erase(0, min(res.find_first_not_of('0'), res.size() - 1));
}

str multiply(str lhs, str rhs) {
  int len = max(lhs.size(), rhs.size());

  while (lhs.size() < len) {
    lhs.insert(0, "0");
  }
  while (rhs.size() < len) {
    rhs.insert(0, "0");
  }

  if (len == 1) {
    return to_string((lhs[0] - '0') * (rhs[0] - '0'));
  }

  str lhs0 = lhs.substr(0, len / 2);
  str lhs1 = lhs.substr(len / 2, len - len / 2);
  str rhs0 = rhs.substr(0, len / 2);
  str rhs1 = rhs.substr(len / 2, len - len / 2);

  str p0 = multiply(lhs0, rhs0);
  str p1 = multiply(lhs1, rhs1);
  str p2 = multiply(add(lhs0, lhs1), add(rhs0, rhs1));
  str p3 = subtract(p2, add(p0, p1));

  for (int i = 0; i < 2 * (len - len / 2); i++) {
    p0.append("0");
  }
  for (int i = 0; i < len - len / 2; i++) {
    p3.append("0");
  }
  str res = add(add(p0, p1), p3);
  return res.erase(0, min(res.find_first_not_of('0'), res.size() - 1));
}

void solve() {
  string num1, num2;
  cin >> num1 >> num2;

  cout << multiply(num1, num2) << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
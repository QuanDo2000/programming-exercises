// https://cp-algorithms.com/algebra/fft.html

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

using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd>& a, bool invert) {
  int n = a.size();
  if (n == 1)
    return;

  vector<cd> a0(n / 2), a1(n / 2);
  for (int i = 0; 2 * i < n; i++) {
    a0[i] = a[2 * i];
    a1[i] = a[2 * i + 1];
  }
  fft(a0, invert);
  fft(a1, invert);

  double ang = 2 * PI / n * (invert ? -1 : 1);
  cd w(1), wn(cos(ang), sin(ang));
  for (int i = 0; 2 * i < n; i++) {
    a[i] = a0[i] + w * a1[i];
    a[i + n / 2] = a0[i] - w * a1[i];
    if (invert) {
      a[i] /= 2;
      a[i + n / 2] /= 2;
    }
    w *= wn;
  }
}

vi multiply(vi const& a, vi const& b) {
  vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
  int n = 1;
  while (n < a.size() + b.size())
    n <<= 1;
  fa.resize(n);
  fb.resize(n);

  fft(fa, false);
  fft(fb, false);
  for (int i = 0; i < n; i++)
    fa[i] *= fb[i];
  fft(fa, true);

  vi result(n);
  for (int i = 0; i < n; i++)
    result[i] = round(fa[i].real());

  while (result.back() == 0) {
    result.pop_back();
  }

  if (a.back() == 0 || b.back() == 0) {
    result.push_back(0);
  }

  int carry = 0;
  for (int i = result.size() - 1; i >= 0; i--) {
    result[i] += carry;
    carry = result[i] / 10;
    result[i] %= 10;
  }
  if (carry) {
    result.insert(result.begin(), carry);
  }
  return result;
}

void solve() {
  str str1, str2;
  cin >> str1 >> str2;

  if (str1.size() < 9 && str2.size() < 9) {
    ll a = stoi(str1);
    ll b = stoi(str2);
    cout << a * b;
    return;
  }

  vi num1 = {}, num2 = {};
  for (auto& ch : str1) {
    if (DEBUG) cout << ch - '0';
    num1.push_back(ch - '0');
  }
  if (DEBUG) cout << "\n";
  for (auto& ch : str2) {
    if (DEBUG) cout << ch - '0';
    num2.push_back(ch - '0');
  }
  if (DEBUG) cout << "\n";

  vi ans = multiply(num1, num2);
  for (auto& num : ans) {
    cout << num;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
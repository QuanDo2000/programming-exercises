// https://stackoverflow.com/questions/1380463/sorting-a-vector-of-custom-objects

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

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

struct Info {
  str city;
  int score;
  int id;

  Info(int i, str c, int s) : id(i), score(s), city(c) {}

  bool operator<(const Info& obj) const {
    if (city < obj.city)
      return true;
    else if (city > obj.city)
      return false;
    else if (score > obj.score)
      return true;
    else
      return false;
  }
};

void solve() {
  int n;
  cin >> n;

  vector<Info> ans;
  for (int i = 1; i <= n; i++) {
    str s;
    int p;
    cin >> s >> p;
    ans.push_back(Info(i, s, p));
  }
  sort(ans.begin(), ans.end());

  for (auto& city : ans) {
    cout << city.id << "\n";
  }

  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // int tc;
  // cin >> tc;
  // for (int i = 0; i < tc; i++)
  solve();

  return 0;
}
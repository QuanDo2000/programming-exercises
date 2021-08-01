#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

bool visited[4][4][4][4];
vi path[4][4][4][4];

void reset() {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
        for (int l = 0; l < 4; l++) {
          path[i][j][k][l] = {};
          visited[i][j][k][l] = 0;
        }
      }
    }
  }
}

void use(const vi& state) {
  visited[state[0]][state[1]][state[2]][state[3]] = true;
}

bool used(const vi& state) {
  return visited[state[0]][state[1]][state[2]][state[3]];
}

void setPath(const vi& src, const vi& des) {
  vi temp(des);
  path[src[0]][src[1]][src[2]][src[3]] = temp;
}

vi getPath(const vi& v) {
  return path[v[0]][v[1]][v[2]][v[3]];
}

int nxt(int x) {
  return (x + 1) % 4;
}

vi nxtState(const vi& state, int pos) {
  vi temp(state);
  if (pos == 0) {
    temp[3] = nxt(temp[3]);
    temp[0] = nxt(temp[0]);
    temp[1] = nxt(temp[1]);
  } else if (pos == 1) {
    temp[0] = nxt(temp[0]);
    temp[1] = nxt(temp[1]);
    temp[2] = nxt(temp[2]);
  } else if (pos == 2) {
    temp[1] = nxt(temp[1]);
    temp[2] = nxt(temp[2]);
    temp[3] = nxt(temp[3]);
  } else {
    temp[2] = nxt(temp[2]);
    temp[3] = nxt(temp[3]);
    temp[0] = nxt(temp[0]);
  }
  return temp;
}

char getMove(const vi& prev, const vi& curr) {
  for (int i = 0; i < 4; i++) {
    if (prev[i] == curr[i]) {
      return (i + 2) % 4 + 65;
    }
  }
}

void bfs(vi& state) {
  queue<vi> q;
  q.push(state);
  use(state);
  setPath(state, {});

  while (!q.empty()) {
    auto v = q.front();
    q.pop();
    for (int pos = 0; pos < 4; pos++) {
      auto u = nxtState(v, pos);
      if (!used(u)) {
        use(u);
        q.push(u);
        setPath(u, v);
      }
    }
  }
  vi des = {0, 0, 0, 0};
  if (!used(des)) {
    cout << "No Path!\n";
  } else {
    vector<vi> moves;
    vi v(des);
    while (!v.empty()) {
      moves.push_back(v);
      v = getPath(v);
    }
    reverse(moves.begin(), moves.end());
    cout << "Path:\n";
    vi prev = moves[0];
    for (int i = 1; i < moves.size(); i++) {
      cout << getMove(prev, moves[i]) << " ";
      for (auto& item : moves[i]) {
        cout << item << " ";
      }
      cout << "\n";
      prev = moves[i];
    }
    cout << "\n";
  }
}

void solve() {
  reset();
  vi state(4);
  for (int i = 0; i < 4; i++) {
    cin >> state[i];
  }

  bfs(state);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
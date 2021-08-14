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

const int MAX_N = 2 * 1e5 + 2;

const bool DEBUG = 1;

int visited[MAX_N];
vector<vii> adj;
map<ll, set<int>> tlog;
vector<map<ll, set<int>>> path;

void bfs(int x) {
  queue<int> q;

  visited[x] = 2;
  q.push(x);

  while (!q.empty()) {
    auto v = q.front();
    q.pop();
    for (auto i = adj[v].begin(); i != adj[v].end(); i++) {
      auto edge = *i;
      auto v_to = edge.first;
      auto v_cost = edge.second;
      visited[v_to] = 1;
      q.push(v_to);
      for (auto const& [cul_cost, val] : path[v]) {
        auto cost = cul_cost + v_cost;
        tlog[cost].insert(v_to);
        path[v_to][cost].insert(v);
      }
    }
  }
}

void solve() {
  fill(visited, visited + MAX_N, 0);

  int n, m, d;
  cin >> n >> m >> d;

  adj.resize(n + 1);
  path.resize(n + 1);
  tlog[0].insert(1);
  path[1][0].insert(1);

  for (int i = 0; i < m; i++) {
    int u, v, h;
    cin >> u >> v >> h;
    adj[u].push_back({v, h});
  }

  if (DEBUG) {
    cout << "\nEdges\n";
    for (int i = 1; i < adj.size(); i++) {
      auto& from = adj[i];
      for (auto& edge : from) {
        cout << i << " " << edge.first << " " << edge.second << "\n";
      }
    }
  }

  bfs(1);

  if (DEBUG) {
    cout << "\nPath\n";
    for (int i = 1; i < path.size(); i++) {
      auto node = path[i];
      cout << i << "\n";
      for (auto& [key, val] : node) {
        cout << key << ": ";
        for (auto& to : val) {
          cout << to << " ";
        }
        cout << "\n";
      }
    }
    cout << "\nTlog\n";
    for (auto& [key, val] : tlog) {
      cout << key << ": ";
      for (auto& node : val) {
        cout << node << " ";
      }
      cout << "\n";
    }
  }

  vi blog(d);
  for (int i = 0; i < d; i++) {
    cin >> blog[i];
  }
  sort(blog.begin(), blog.end(), greater<int>());

  if (DEBUG) {
    cout << "\nBlog: ";
    for (auto& line : blog) {
      cout << line << " ";
    }
    cout << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}
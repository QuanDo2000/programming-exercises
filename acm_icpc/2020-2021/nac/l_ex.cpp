#include <bits/stdc++.h>
using namespace std;
const int MAX_N = 200000;
const int MAX_M = 300000;
const long long INF = 1000000000000000009ll;
int n;
int m;
int k;
int a[MAX_M * 2 + 9];
int b[MAX_M * 2 + 9];
int c[MAX_M * 2 + 9];
long long p[MAX_N + 9];
vector<int> adj[MAX_N + 9];
long long dist[MAX_N + 9];
vector<int> adj2[MAX_N + 9];
int memo[MAX_N + 9];
int nxt[MAX_N + 9];
vector<int> ans;

int Dp(int x) {
  if (x == n) {
    return 1;
  }
  if (memo[x] != -1) {
    return memo[x];
  }
  int res = 0;
  for (int id : adj2[x]) {
    if (Dp(b[id]) > 0) {
      res = min(res + Dp(b[id]), 2);
      nxt[x] = b[id];
    }
  }
  memo[x] = res;
  return res;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> m >> k;
  for (int i = 1; i <= m; i++) {
    cin >> a[i] >> b[i] >> c[i];
    a[i + m] = b[i];
    b[i + m] = a[i];
    c[i + m] = c[i];
    adj[a[i]].push_back(i);
    adj[b[i]].push_back(i + m);
  }
  for (int i = 1; i <= k; i++) {
    cin >> p[i];
  }
  fill(dist, dist + n + 1, INF);
  dist[1] = 0;
  priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
  pq.push(make_pair(0, 1));
  while (!pq.empty()) {
    pair<long long, int> tmp = pq.top();
    pq.pop();
    long long d = tmp.first;
    int x = tmp.second;
    if (d > dist[x]) {
      continue;
    }
    for (int id : adj[x]) {
      if (dist[x] + c[id] < dist[b[id]]) {
        dist[b[id]] = dist[x] + c[id];
        pq.push(make_pair(dist[b[id]], b[id]));
      }
    }
  }
  sort(p + 1, p + k + 1);
  if (p[k] > dist[n]) {
    cout << "0\n";
    return 0;
  }
  for (int i = 1; i <= n; i++) {
    for (int id : adj[i]) {
      if (dist[i] + c[id] == dist[b[id]]) {
        int pos = upper_bound(p + 1, p + k + 1, dist[i]) - p;
        if (pos == k + 1 || p[pos] >= dist[b[id]]) {
          adj2[i].push_back(id);
        }
      }
    }
  }
  fill(memo, memo + n + 1, -1);
  if (Dp(1) == 0) {
    cout << "0\n";
  } else if (Dp(1) > 1) {
    cout << "1\n";
  } else {
    for (int i = 1; i != 0; i = nxt[i]) {
      ans.push_back(i);
    }
    cout << ans.size() << "\n";
    for (int x : ans) {
      cout << x << "\n";
    }
  }
  return 0;
}
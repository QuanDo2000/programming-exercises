#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using vi = vector<int>;
using vvi = vector<vi>;
using ii = pair<int, int>;
using vii = vector<ii>;
using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

istringstream iss;

char peek()
{
    return static_cast<char>(iss.peek());
}

char get()
{
    return static_cast<char>(iss.get());
}

ld expression();

ld number()
{
    ld res;
    iss >> res;
    return res;
}

ld factor()
{
    if ((peek() >= '0' && peek() <= '9') || peek() == '.')
        return number();
    else if (peek() == '(')
    {
        get();
        ld res = expression();
        get();
        return res;
    }
    else if (peek() == '-')
    {
        get();
        return -expression();
    }
    return 0;
}

ld term()
{
    ld res = factor();
    while (peek() == '*' || peek() == '/')
    {
        if (get() == '*')
            res *= factor();
        else
            res /= factor();
    }
    return res;
}

ld expression()
{
    ld res = term();
    while (peek() == '+' || peek() == '-')
    {
        if (get() == '+')
        {
            res += term();
        }
        else
        {
            res -= term();
        }
    }
    return res;
}

int main()
{
    string line;
    ld res = 0;

    for (line; getline(cin, line);)
    {
        // Remove whitespace
        line.erase(remove_if(line.begin(), line.end(), ::isspace), line.end());
        // Move line into istringstream
        iss.str(line);
        // Evaluate expression
        res = expression();
        cout << fixed << setprecision(1) << res << "\n";
    }

    return 0;
}
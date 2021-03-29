#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a, b, c = 1;
    // scanf returns the number of items read
    while (scanf("%d %d", &a, &b) != EOF)
        // notice the two '\n'
        printf("Case %d: %d\n\n", c++, a + b);
    return 0;
}
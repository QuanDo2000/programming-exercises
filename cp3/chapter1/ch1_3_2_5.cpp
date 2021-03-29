#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a, b, c = 1;
    // scanf returns the number of items read
    while (scanf("%d %d", &a, &b) != EOF)
    {
        if (c > 1)
            printf("\n"); // 2nd/more cases
        printf("Case %d: %d\n", c++, a + b);
    }
    return 0;
}
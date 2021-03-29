#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a, b;
    // scanf returns the number of items read
    while (scanf("%d %d", &a, &b) == 2)
        // or you can check for EOF, i.e.
        // while (scanf("%d %d", &a, &b) != EOF)
        printf("%d\n", a + b);
    return 0;
}
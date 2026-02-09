#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main()
{
    int a,c,b,x,ans=0;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> x;

    for (int i = 0; i <= a; i++) for (int j = 0; j <= b; j++) {

        int diff = x - (i * 500 + j * 100);
        if (diff < 0) continue;
        if (diff % 50 != 0) continue;
        if (diff / 50 > c) continue;
        ans++;
    }
    cout << ans << endl;

    return 0;
}
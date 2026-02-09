#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

using lint = long long;
using mint0 = modint998244353;
using mint1 = modint1000000007;

#define YesNo(bool) if(bool) { cout<<"Yes"<<endl; } else{ cout<<"No"<<endl; }

template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }


void solve()
{
    int n, y;
    cin >> n >> y;

    int a = -1, b = -1, c = -1;

    for (int i = 0; i <= n; i++) for (int j = 0; j <= n - i; j++){
        int k = n - i - j;
        if (k < 0) continue;

        int sum = i * 10000 + j * 5000 + k * 1000;
        if (sum == y){
            a = i;
            b = j;
            c = k;
            break;
        }
    }

    cout << a << " " << b << " " << c << endl;
}


int main()
{
    std::cin.tie(0);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
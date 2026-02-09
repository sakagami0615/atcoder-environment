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
    int n;
    cin >> n;

    vector<int> ts(n + 1, 0), xs(n + 1, 0), ys(n + 1, 0);

    for (int i=1; i<=n; i++) {
        cin >> ts[i] >> xs[i] >> ys[i];
    }

    for (int i=0; i<=n-1; i++) {
        int j = i + 1;
        int dist = abs(xs[i] - xs[j]) + abs(ys[i] - ys[j]);
        int dt = ts[j] - ts[i];
        if (dt < dist || (dist - dt) % 2 != 0) {
            YesNo(false);
            return;
        }
    }
    YesNo(true);
}


int main()
{
    std::cin.tie(0);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

using lint = long long;
using mint0 = modint998244353;
using mint1 = modint1000000007;

#define yesno(bool) if(bool) { cout<<"yes"<<endl; } else{ cout<<"no"<<endl; }
#define YesNo(bool) if(bool) { cout<<"Yes"<<endl; } else{ cout<<"No"<<endl; }
#define YESNO(bool) if(bool) { cout<<"YES"<<endl; } else{ cout<<"NO"<<endl; }

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define RREP(i, n) for (int i = (int)(n-1); i >=0; i--)

template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }


void solve()
{
    int  n, a, b;
    cin >> n >> a >> b;

    int ans = 0;

    REP(i, 10) REP(j, 10) REP(k, 10) REP(l, 10) REP(m, 10) {
        int cnt = i + j + k + l + m;
        if (cnt >= a && cnt <= b) {
            int num = i * 10000 + j * 1000 + k * 100 + l * 10 + m;
            if (num <= n) ans += num;
        }
    }
    cout << ans << endl;
}


int main()
{
    std::cin.tie(0);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}

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
    int alice=0;
    int bob=0;
    cin >> n;

    vector<int> a(n, 0);
    for (int i=0; i<n; i++) cin >> a[i];

    sort(a.begin(), a.end(), greater<int>());

    for (int i=0; i<n; i++){
        if (i%2==0) alice += a[i];
        else bob += a[i];
    }
    cout << alice - bob << endl;
}


int main()
{
    std::cin.tie(0);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
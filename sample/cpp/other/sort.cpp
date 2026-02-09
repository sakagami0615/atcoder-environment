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

#define REP(i, n) for (int i=0; i<(int)(n); i++)
#define RREP(i, n) for (int i=(int)(n)-1; i>=0; i--)

template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }


void solve()
{
    int N;
    cin >> N;

    vector<int> a(N, 0);   // error code
    REP(i, N) a[i] = (i % 2 == 0 ? i : -i);

    sort(a.begin(), a.end());

    REP(i, N) cout << a[i] << " ";
    cout << endl;
}

int main()
{
    std::cin.tie(0);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
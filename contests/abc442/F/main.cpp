#include <bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;i++)
#define all(x) (x).begin(),(x).end()
#define yesno(flag) if(flag) { cout<<"yes"<<"\n"; } else{ cout<<"no"<<"\n"; }
#define YesNo(flag) if(flag) { cout<<"Yes"<<"\n"; } else{ cout<<"No"<<"\n"; }
#define YESNO(flag) if(flag) { cout<<"YES"<<"\n"; } else{ cout<<"NO"<<"\n"; }
using namespace std;
using ll = long long;
const int INF = INT_MAX / 2;
const ll INF_LL = 1LL << 60;


void solve()
{
    int N;
    cin >> N;

    vector<string> S(N);
    rep(i, 0, N) cin >> S[N - 1 - i];

    vector<vector<int>> cost_row(N, vector<int>(N + 1, 0));
    vector<vector<int>> cost_col(N + 1, vector<int>(N, 0));

    rep(i, 0, N) rep(j, 0, N) cost_row[i][j + 1] = cost_row[i][j] + (S[i][j] == '#');
    rep(i, 0, N) rep(j, 0, N) cost_col[i + 1][j] = cost_col[i][j] + (S[i][j] == '#');
    
    vector<vector<int>> dp(N + 1, vector<int>(N + 1, INF));
    dp[0][0] = 0;

    rep(i, 0, N + 1) rep(j, 0, N + 1) {
        if (i < N && dp[i][j] != INF) dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + cost_row[i][j]);
        if (j < N && dp[i][j] != INF) dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + (i - cost_col[i][j]));
    }
    cout << dp[N][N] << endl;
}

int main()
{
    std::cin.tie(0);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
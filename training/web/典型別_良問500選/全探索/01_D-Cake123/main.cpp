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


int X, Y, Z, K;
ll A[1010], B[1010], C[1010];
vector<ll> BC;
int N_BC;


bool check(ll delicious)
{
    int cnt = 0;
    rep(i, 0, X) {
        int idx = lower_bound(all(BC), delicious - A[i]) - BC.begin();
        cnt += N_BC - idx;
        if (cnt >= K) break;
    }
    return cnt >= K;
};

void solve()
{
    cin >> X >> Y >> Z >> K;
    rep(i, 0, X) cin >> A[i];
    rep(i, 0, Y) cin >> B[i];
    rep(i, 0, Z) cin >> C[i];

    rep(i, 0, Y) rep(j, 0, Z) BC.push_back(B[i] + C[j]);
    sort(all(BC));
    N_BC = BC.size();

    ll head = 0, tail = INF_LL;
    while (head + 1 < tail) {
        ll mid = (head + tail) / 2;
        if (check(mid)) head = mid;
        else tail = mid;
    }

    vector<ll> ans;
    reverse(all(BC));
    rep(i, 0, X) {
        rep(j, 0, N_BC) {
            ll s = A[i] + BC[j];
            if (head < s) ans.push_back(s);
            else break;
        }
    }
    while (ans.size() < K) ans.push_back(head);

    sort(all(ans), greater<ll>());
    rep(i, 0, K) cout << ans[i] << "\n";
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}

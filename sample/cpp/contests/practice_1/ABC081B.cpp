#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int a[200];
int n;


int main()
{
    cin >> n;
    for (int i=0; i<n; i++) cin >> a[i];

    int ans = 0;

    while(true){
        bool is_ok = true;
        for (int i=0; i<n; i++){
            if (a[i] % 2 != 0){
                is_ok = false;
                break;
            }
            a[i] /= 2;
        }
        if(!is_ok) break;
        ans++;
    }
    cout << ans << endl;

    return 0;
}

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int A, B, ans;
    string op;
    cin >> A >> op >> B;


    if (op == "+") ans = A + B;
    else if (op == "-") ans = A - B;
    else if (op == "*") ans = A * B;
    else if (op == "/" && B != 0) ans = A / B;
    else {
        cout << "error" << endl;
        return 0;
    }

    cout << ans << endl;

    return 0;
}

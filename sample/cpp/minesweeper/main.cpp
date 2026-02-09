//include
//------------------------------------------
#include <algorithm>
#include <bitset>
#include <cstring>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

// debug
//--------------------------------------------
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

//typedef
//------------------------------------------
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

// conversion
//------------------------------------------
inline int cvt2int(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string cvt2string(T x) {ostringstream sout;sout<<x;return sout.str();}

// for loop
//------------------------------------------
#define FOR(i,b,e) for(i=(int)b;i<(int)e;++i)
#define RFOR(i,b,e) for(i=(int)(e)-1;i>=(int)b;--i)
#define REP(i,e) for(i=0;i<(int)e;++i)
#define RREP(i,e) for(i=int(e)-1;i>=0;--i)

// logical
//------------------------------------------
#define TER(x,t,f) (x)?(t):(f)
template<class T> inline bool chmax(T &m, const T &n) {if (m<n) {m=n; return true;} return false;}
template<class T> inline bool chmin(T &m, const T &n) {if (m>n) {m=n; return true;} return false;}

// math
//------------------------------------------
template<class T> inline T sqr(T x) {return (x*x);}

// array
//------------------------------------------
#define ZERO(ary) memset((ary),0,sizeof(ary))
#define FILL(ary,v) memset((ary),v,sizeof(ary))

// container
//------------------------------------------
#define ALL(obj) (obj).begin(),(obj).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define SIZE(obj) ((int)(obj).size())
#define SORT(obj) sort((obj).begin(),(obj).end())
#define PB push_back
#define MP make_pair
#define MT make_tuple

// disp
//------------------------------------------
#define DISP(s) cout << s
#define DISPL(s) cout << s << endl
#define ENDL cout << endl
#define YES(n) cout << ((n)?"YES":"NO") << endl
#define POSSIBLE(n) cout << ((n)?"POSSIBLE":"IMPOSSIBLE") << endl

//constant
//--------------------------------------------
const int INF = 1e9;
const LL LINF = 1e18;
const double EPS = 1e-15;
const int MOD = 1e9+7;
const double PI = acos(-1.0);

// global
//------------------------------------------
int i,j,k,l,m,n;

const int WIDTH = 10;
const int HEIGHT = 10;
const int BOMB_NUM = 10;

const int WALL = -2;
const int BOMB = -1;

int board_data[HEIGHT+2][WIDTH+2];
bool board_open[HEIGHT+2][WIDTH+2];



void initBoard()
{
	REP(i,HEIGHT+2){
		board_data[i][0] = board_data[i][WIDTH+1] = WALL;
		board_open[i][0] = board_open[i][WIDTH+1] = true;
	}
	REP(i,WIDTH+2){
		board_data[0][i] = board_data[HEIGHT+1][i] = WALL;
		board_open[0][i] = board_open[HEIGHT+1][i] = true;
	}

	int bomb_cnt = BOMB_NUM;
	FOR(i,1,HEIGHT+1){
		FOR(j,1,WIDTH+1){
			if(bomb_cnt>0){
				board_data[i][j] = BOMB;
				bomb_cnt--;
			}
		}
	}

	srand((unsigned int)(time(NULL)));
	int shuffle_num = 100;
	int x1,x2,y1,y2;
	REP(k,shuffle_num){
		x1 = rand()%WIDTH + 1;
		y1 = rand()%HEIGHT + 1;
		x2 = rand()%WIDTH + 1;
		y2 = rand()%HEIGHT + 1;
		swap<int>(board_data[y1][x1], board_data[y2][x2]);
	}

	FOR(i,1,HEIGHT+1){
		FOR(j,1,WIDTH+1){
			if(board_data[i][j] != BOMB){
				
				bomb_cnt = 0;
				FOR(m,-1,2){
					FOR(n,-1,2){
						if(m==0 && n==0) continue;
						if(board_data[i+m][j+n] == BOMB){
							bomb_cnt++;
						}
					}
				}
				board_data[i][j] = bomb_cnt;
			}
		}
	}
}

void drawBoard()
{
	FOR(i,1,HEIGHT+1){
		FOR(j,1,WIDTH+1){
			if(board_open[i][j]){
				if(board_data[i][j] == BOMB){
					DISP("* ");
				}
				else{
					cout << board_data[i][j] << ' ';
				}
			}
			else{
				DISP("- ");
			}
		}
		ENDL;
	}
}

bool put(int input_x, int input_y){

	if(board_open[input_y][input_x]) return true;
	
	if(board_data[input_y][input_x] == BOMB) return false;
	else if(board_data[input_y][input_x] > 0){
		board_open[input_y][input_x] = true;
	}
	else{
		board_open[input_y][input_x] = true;
		
		int x,y;
		int nx, ny;
		FOR(x,-1,2){
			FOR(y,-1,2){
				if(x==0 && y==0) continue;
				nx = input_x + x;
				ny = input_y + y;

				if(!board_open[ny][nx]){
					if(board_data[ny][nx] == 0){
						put(nx,ny);
					}
					else if(board_data[ny][nx] > 0){
						board_open[ny][nx] = true;
					}
				}
			}
		}
	}
	return true;
}

int countClose()
{
	int cnt = 0;
	FOR(i,1,HEIGHT+1){
		FOR(j,1,WIDTH+1){
			if(!board_open[i][j]){
				cnt++;
			}
		}
	}
	return cnt;
}

void mymain()
{
	initBoard();
	drawBoard();

	int input_x, input_y;

	while(true){
		cin >> input_x >> input_y;
		if((input_x<=0 || input_x>WIDTH) || (input_y<=0 || input_y>HEIGHT)) continue;
		
		system("cls");

		if(!put(input_x, input_y)){
			DISPL("YOU LOSE...");
			break;
		}
		if(countClose() == BOMB_NUM){
			DISPL("YOU WIN!");
			break;
		}
		drawBoard();
	}

	FILL(board_open, true);
	drawBoard();
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	mymain();
	
	return 0;
}
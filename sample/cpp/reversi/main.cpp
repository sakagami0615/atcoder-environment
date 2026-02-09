#include <iostream>
#include <vector>
#include <set>

#define REP(i, N) for (int i = 0; i < (int)N; i++)

using namespace std;

const int EMPTY = 0;
const int BLACK = 1;
const int WHITE = 2;


class Board
{
private:
    int m_board[8][8];

    vector<int> code2xy(string code)
    {
        vector<int> xy = {(int)code[1] - 49, (int)code[0] - 97};
        return xy;
    }

    string xy2code(int x, int y)
    {
        char code_x = (char)(x + 49);
        char code_y = (char)(y + 97);
        string  code = string(1, code_y) + string(1, code_x);
        return code;
    }

public:
    Board()
    {
        REP(i, 8) REP(j, 8) m_board[i][j] = EMPTY;
        m_board[3][3] = BLACK;
        m_board[3][4] = WHITE;
        m_board[4][3] = WHITE;
        m_board[4][4] = BLACK;
    }
    ~Board() {}

    int put_stone(int player, string code, bool is_check=false)
    {
        vector<int> xy = code2xy(code);
        int x = xy[0], y = xy[1];

        if (m_board[y][x] != EMPTY) return 0;

        int enemy = (player == WHITE ? BLACK : WHITE);
        int reverse_cnt = 0;
        for (int dy = -1; dy <= 1; dy += 1) {
            for (int dx = -1; dx <= 1; dx += 1) {
                if (dx == 0 && dy == 0) continue;

                int nx = x + dx, ny = y + dy;
                while (nx >= 0 && ny >= 0 && nx < 8 && ny < 8 && m_board[ny][nx] == enemy) {
                    nx += dx;
                    ny += dy;
                }
                if (nx >= 0 && ny >= 0 && nx < 8 && ny < 8 && m_board[ny][nx] == player) {
                    while (!(x == nx && y == ny)) {
                        nx -= dx;
                        ny -= dy;
                        reverse_cnt += 1;
                        if (!is_check) m_board[ny][nx] = player;
                    }
                }
            }
        }
        return reverse_cnt;
    }

    int get_stone_num(int stone_color)
    {
        int cnt = 0;
        REP(i, 8) REP(j, 8) if (m_board[i][j] == stone_color) cnt++;
        return cnt;
    }

    set<string> get_candidate_put_codes(int player)
    {
        set<string> codes;
        REP(i, 8) REP(j, 8){
            string code = xy2code(j, i);
            if (put_stone(player, code, true) > 0) codes.insert(code);
        }
        return codes;
    }

    void display_board()
    {
        string label = "abcdefgh";
        cout << "  1 2 3 4 5 6 7 8" << endl;
        REP(i, 8)
        {
            cout << label[i] << " ";
            REP(j, 8)
            {
                if (m_board[i][j] == BLACK)
                    cout << "● ";
                else if (m_board[i][j] == WHITE)
                    cout << "○ ";
                else
                    cout << "- ";
            }
            cout << endl;
        }
    }
};

class Game
{
private:
    Board m_board;
    int m_turn;
    int m_pass_cnt;

    string player_input()
    {
        set<string> candidate_code_set = m_board.get_candidate_put_codes(m_turn);
        if (candidate_code_set.size() == 0) return "";

        string code;
        do
        {
            cout << (m_turn == WHITE ? "white turn >> " : "black turn >> ");
            cin >> code;
            if (code.length() != 2) continue;
        } while (candidate_code_set.find(code) == candidate_code_set.end());
        return code;
    }

    void turn_change()
    {
        m_turn = (m_turn == WHITE ? BLACK : WHITE);
    }

    int is_game_over()
    {
        if(m_pass_cnt >= 2) return true;
        return false;
    }

    void display_result()
    {
        int n_black = m_board.get_stone_num(BLACK);
        int n_white = m_board.get_stone_num(WHITE);

        cout << "[result]" << endl;
        cout << "black: " << n_black << ", white: " << n_white << endl;
        if (n_black > n_white) cout << "black won!" << endl;
        else if (n_black < n_white) cout << "white won!" << endl;
        else cout << "draw..." << endl;
    }

public:
    Game(): m_board(Board()), m_turn(BLACK), m_pass_cnt(0){}
    ~Game(){}

    void run()
    {
        while (!is_game_over())
        {
            m_board.display_board();
            string code = player_input();
            if (code == ""){
                cout << (m_turn == WHITE ? "white pass" : "black pass") << endl;
                m_pass_cnt++;
            }
            else
            {
                m_board.put_stone(m_turn, code);
            }
            turn_change();
        }
        cout << "----------" << endl;
        m_board.display_board();
        display_result();
    }
};

int main()
{
    Game game;
    game.run();
    return 0;
}
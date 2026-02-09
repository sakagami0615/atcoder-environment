# ----------------------------------------
# サンプル入力の記載
# ----------------------------------------
import io
import sys

# ここにサンプルの入力を記載する
_INPUT1 = """\
4 3 3 6 2 5 10
"""

_INPUT2 = """\
3 1 4 1 5 9 2
"""

_INPUT3 = """\
1 1 1 1 1 1 1
"""

sys.stdin = io.StringIO(_INPUT1)
#sys.stdin = io.StringIO(_INPUT2)
#sys.stdin = io.StringIO(_INPUT3)


# ----------------------------------------
# 標準入力取得のサンプル
# ----------------------------------------
"""
# 文字列を取得するサンプル
a = input()
print(a)

# 数値を取得するサンプル
a = int(input())
print(a)

# 文字列から文字分割した絵リストを取得するサンプル
a = list(input())
print(a)

# スペース区切りの数値を取得するサンプル
a = list(map(int, input().split()))
print(a)
"""

# ----------------------------------------
# 以降のコードから提出フォームに貼り付ける
# ----------------------------------------
A, B, C, D, E, F, X = map(int, input().split())

t_time = X // (A + C) * B
b_time = X // (D + F) * D

t_mod = X % (A + C)
b_mod = X % (D + F)

t_time += min(t_mod, A)
b_time += min(b_mod, D)

t_move = t_time * B
b_move = b_time * E

if t_move > b_move:
    print('Takahashi')
elif t_move < b_move:
    print('Aoki')
else:
    print('Draw')

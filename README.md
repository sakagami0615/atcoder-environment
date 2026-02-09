# **AtCoder環境**

## Python での AC-Library のインストール

下記コマンドで実施できる。

```bash
pip install git+https://github.com/not522/ac-library-python
```

## **Pythonの実行に関して**

Pythonの環境としてはPoetryを使用することを想定。

### **カスタムコマンド**

プロジェクト内で`direnv`を使用してカスタムコマンドを利用できます。

#### **テストの実行**

```bash
# 問題フォルダ(A, B, Cなど)を指定してテストを実行
ac_test_py <問題フォルダ名>
```

> <例>
> ```bash
> ac_test_py A
> ```
>
> - `poetry run atcoder-tools test --dir A --exec "poetry run python main.py"` を実行します
> - `direnv`によって`tools/commands`にパスが通っているため、プロジェクトルートで実行可能

#### **コードファイルを開く**

```bash
# 特定の問題のmain.pyを開く
ac_open_py <問題フォルダ名>

# 全ての問題のmain.pyを開く
ac_open_py
```

> <例>
> ```bash
> # 問題Aのmain.pyを開く
> ac_open_py A
>
> # 全ての問題のmain.pyを開く
> ac_open_py
> ```
>
> - デフォルトのエディタはVS Code (`code`)ですが、スクリプト内で変更可能

#### **提出**

```bash
# 問題フォルダを指定して提出
ac_submit_py <問題フォルダ名>
```

> <例>
> ```bash
> ac_submit_py A
> ```
>
> - 指定した問題フォルダに移動して`poetry run atcoder-tools submit`を実行します
>  <br>

### **標準のPython実行**

```bash
# カレントディレクトリで直接実行
python main.py

# Poetry環境で実行
poetry run python main.py
```

## **C++の実行に関して**

C++の環境としてはGCCを使用することを想定。

### **[Windows(WSL2)の場合]**

TODO

#### **[MacOSの場合]**

```bash
# コンパイル(13はバージョン番号)
g++-13 main.cpp

# 実行
./a.out
```

segmentation faultが発生した場合は、下記コマンドで該当コードを確認できる。

```bash
# コンパイル(-g オプションをつける)
g++-13 -g main.cpp

lldb -f ./a.out r

# ターミナル左側に(lldb)と表示されている状態で下記コマンドを実行
r
```

`参考`：https://seiichiinoue.github.io/post/segfault/

## **AtCoder-toolsに関して**

### **概要**

- `紹介記事`：https://qiita.com/noraworld/items/17cd1960b0cd3648f599
- `ソースコード`：https://github.com/kyuridenamida/atcoder-tools

### **環境用意**

pythonのvenv環境を用意し、下記コマンドでツールをpipする。

```bash
pip install atcoder-tools
```

また、現時点でのMarkupSafeのバージョンが2.1.0であり、ツールが対応していなかったため、<br>
下記コマンドで対応バージョンに変更。

```bash
pip uninstall -y MarkupSafe
pip install MarkupSafe==2.0.1
```

### **使用方法**

#### **1. 入力のダウンロードコマンド**

##### **カスタムコマンド（推奨）**

プロジェクト内で`direnv`を使用してカスタムコマンドを利用できます。

```bash
# コンテストURLを指定して環境を生成し、自動的にフォルダに移動
source ac_gen_py <コンテストURL>
# または
. ac_gen_py <コンテストURL>
```

> <例> <br>
> AtCoder Beginners Selectionの場合
>
> ```bash
> source ac_gen_py https://atcoder.jp/contests/abs
> ```
>
> - 実行後、自動的に生成されたコンテストフォルダに移動します
> - `direnv`によって`tools/commands`にパスが通っているため、プロジェクトルートで実行可能
>  <br>

##### **標準コマンド**

```bash
atcoder-tools gen <コンテスト名> --workspace=<保存先のフォルダパス> --lang=<言語名>
```

> <例> <br>
> AtCoder Beginners Selectionの場合(言語はPython、保存先はカレントフォルダ)
>
> ```
> atcoder-tools gen abs --workspace=<保存先のフォルダパス> --lang=<言語名>
> ```
>  <br>

#### **2.まとめてテストを実施するコマンド**

問題のフォルダに移動して、以下のコマンドで複数のテストケースをまとめて確認できる。

```bash
atcoder-tools test

# ローカルのPythonで動かす場合
atcoder-tools test -e "python main.py"

# 仮想環境を指定する場合は、仮想環境内のPythonを指定する必要がある(下記例)
atcoder-tools test -e "poetry run python main.py"
```

> <補足> <br>
> コマンドが長いので、ショートカットに割り当てておくとよい。
> [Fine] > [Preference] > [Keyboard Shotrcuts]を開き、右上にある[Open Keyboard Sortcuts (JSON)]ボタンをクリックする。
> 空のkeybindings.jsonファイルが開くので、上記のコマンドをショートカット割り当てる(以下例)。
>
> ```json
> // Place your key bindings in this file to override the defaults
> [
>     {
>         "key": "ctrl+alt+t",
>         "command": "workbench.action.terminal.sendSequence",
>         "when": "terminalFocus",
>         "args": { "text": "atcoder-tools test -e \"poetry run python main.py\"" }
>     },
> ]
> ```

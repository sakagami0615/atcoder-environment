FROM debian:bookworm-slim

ENV TZ=Asia/Tokyo
ENV LANG=ja_JP.UTF-8

WORKDIR /contest/atcoder

# ロケール設定
RUN apt update && apt install -y locales
RUN echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen

# 競プロで使用するパッケージのインストール
RUN apt update
RUN apt install -y lldb nodejs npm direnv
RUN apt install -y build-essential gcc gdb libboost-all-dev python3 python3-pip pypy3
RUN mkdir ~/.pip && echo "[global]\nbreak-system-packages = true" > ~/.pip/pip.conf
RUN pip3 install poetry

# 仮想環境の準備
COPY ../pyproject.toml* ../poetry.lock* ../.envrc* ./
RUN poetry install --no-root
RUN direnv allow

# oh-my-bashのインストール
RUN apt update
RUN apt install -y curl
RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"

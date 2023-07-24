# CatGPT

CatGPT puts all your ChatGPT conversations on a single static page for easy and offline browsing and searching.

<img src="https://i.postimg.cc/3RZVD3bq/localhost-8085-my-ipad-4.png">

## Motivation

- The chat.openai.com interface is very sluggish and has no search function.

## Installation

```
git clone https://github.com/dvolk/catgpt
cd catgpt
sudo apt install python3-pip python3-venv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Get ChatGPT archive

- Request ChatGPT data export (`chat.openai.com` -> `Settings & Beta` -> `Data controls` -> `Export data`)
- Extract your data export and put `conversations.json` into the `catgpt` directory.

## Run

```
python3 app.py
```

Open http://localhost:8085 in your browser

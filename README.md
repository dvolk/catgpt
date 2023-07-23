# CatGPT

CatGPT lets you browse/search your ChatGPT history on one page.

<img src="https://i.postimg.cc/3RZVD3bq/localhost-8085-my-ipad-4.png">

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

Download your ChatGPT archive and put `conversations.json` into the `catgpt` directory.

## Running

```
python3 app.py
```

Open http://localhost:8085 in your browser

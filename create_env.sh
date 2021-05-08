#! /bin/sh

python3 -m venv venv
echo $PWD
activate () {
    source $PWD/venv/bin/activate
}
activate
python3 -m pip install -r requirements.txt
django-admin startproject d04

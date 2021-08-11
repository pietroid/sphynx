#!/bin/bash

#INSTALL DEPENDENCIES
echo 'Installing Python dependences'
python3 -m venv libs/
source libs/bin/activate
pip3 install -r requirements.txt

#DOWNLOAD VOSK MODEL
echo 'Downloading vosk model'
export $(xargs < configs)
wget $VOSK_MODEL_URL -O temp.zip
unzip temp.zip
rm temp.zip
mv $VOSK_MODEL_NAME speechToText/stt_model
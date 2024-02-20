#!/bin/bash

#yt-dlp --extract-audio --audio-format best https://www.youtube.com/watch?v=u1v-TN6j0Rk


python3 mp3 -u https://www.youtube.com/watch?v=u1v-TN6j0Rk

echo "test completed"
echo "removing test mp3"

rm "Charlotte de Witte - Overdrive (Original Mix) [KNTXT021].mp3"
rm "Charlotte de Witte - Overdrive (Original Mix) [KNTXT021].opus"

# wtf apple
rm "mp3~"
rm "runtest.sh~"

echo "[DONE]"


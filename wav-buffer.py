# wav-buffer.py　
# https://github.com/SOICHIRO-NISHIO-github/wav-buffer
# 倍音化. リングバッファを使用

import numpy as np
import soundfile as sf

#初期設定
N = 512
s, rate = sf.read('input.wav') # 音声ファイルを読み込む場合
y   = np.zeros(len(s))  # 出力格納変数．長さは入力と同じ
buf = np.zeros(N)

for n in range(len(s)):
    l = n % N
    m = (2*n) % N #2を好きな数字に置き換えてください。1未満は低倍、1以上は高倍する。
    y[n] = buf[int(m)] 
    buf[l] = s[n]

sf.write('out_buffer.wav', y, rate, format="WAV", subtype="PCM_16") # 作成波形を保存
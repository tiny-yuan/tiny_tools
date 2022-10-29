a  = "('rtsp://admin:swufe112358@192.168.71.162:554/h264/ch1/main/av_stream',)"
# a.replace("\,","")

from string import punctuation

add_punc = "( ',)"  # 自定义--中文的字符
# all_punc = punctuation + add_punc  所有符号
all_punc = add_punc
temp = []
for c in a:
    if c not in all_punc :
        temp.append(c)
newText = ''.join(temp)
print(newText)
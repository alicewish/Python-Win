from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_name = '贴吧混淆'  # 文件名

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名

# ========================执行区开始========================
# ================按行读取文本:with open(更好)================
text_readline = []  # 初始化按行存储数据列表
with open(txt_file_path) as fin:
    for line in fin:
        text_readline.append(line)

for i in range(len(text_readline)):
    print(text_readline[i], end="")
print(len(text_readline))

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))

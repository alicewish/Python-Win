from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
input_file_path="/Users/alicewish/Downloads/新浪微博关注查询工具你没有关注对方.htm"
output_file_path = "/Users/alicewish/我的坚果云/微博UID.txt"  # 输出文件的地址

# ========================执行区开始========================
read_text = open(input_file_path, 'r').read()  # 读取文本
pattern = re.compile(r'weibo.com/[0-9]{6,}')
# 使用Pattern匹配文本，获得全部匹配结果
find = pattern.findall(read_text)#列表形式存储的结果
uid=set()
for i in range(len(find)):
    path=find[i].strip("()")
    this_uid=path.replace("weibo.com/","")
    uid.add(this_uid)
# ================写入文本================
text = '\r\n'.join(uid)

print(text)
print(len(uid))

f = open(output_file_path, 'w')
try:
    f.write(text)
finally:
    f.close()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))

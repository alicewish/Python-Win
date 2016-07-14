import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
bookID = '10077'  # 图书ID

url_prefix = 'http://www.8kana.com'  # 网址前缀
url_book = "/book/"  # 图书前缀
url_suffix = '.html'  # 网址后缀
book_url = url_prefix + url_book + bookID + url_suffix  # 完整图书网址
# ========================执行区开始========================
page = requests.get(book_url)
tree = html.fromstring(page.text)
# ====================获取旧章节列表====================
chapter_old_name_list = tree.xpath('//a[@class="left"][@target="_blank"]/@title')  # 以列表形式存储的旧章节名称列表
# "他不喜欢超级英雄 001 序 他讨厌超级英..."
chapter_old_url_list = tree.xpath('//a[@class="left"][@target="_blank"]/@href')  # 以列表形式存储的旧章节地址列表
# "/read/10469.html"
# ====================获取最新6章列表====================
chapter_new_name_list = tree.xpath('//a[@class="left chapter_con_a"][@target="_blank"]/@title')  # 以列表形式存储的新章节名称列表
# "他不喜欢超级英雄 001 序 他讨厌超级英..."
chapter_new_url_list = tree.xpath('//a[@class="left chapter_con_a"][@target="_blank"]/@href')  # 以列表形式存储的新章节地址列表
# "/read/10469.html"
# 第一个元素与第二个相同
# ====================合并到总章节列表====================
chapter_name_list = chapter_old_name_list + chapter_new_name_list  # 总章节名称列表
chapter_url_list = chapter_old_url_list + chapter_new_url_list  # 总章节地址列表
first_url = chapter_url_list.pop(0)  # 剥离章节地址列表第一个元素,因为重复
chapter_name_list_length = len(chapter_name_list)  # 计算章节名称数

info = ""  # 初始化信息字符串为空
for i in range(chapter_name_list_length):
    info += chapter_name_list[i] + "\n"
    info += url_prefix + chapter_url_list[i] + "\n"

print(book_url)
print(info)
print(chapter_name_list_length)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))

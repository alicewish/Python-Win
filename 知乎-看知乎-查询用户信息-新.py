import requests, time, json

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
user_name = '张佳玮'

# ========================获取对应Hash========================
html = requests.get('http://api.kanzhihu.com/searchuser/' + user_name)
data = json.loads(html.text)  # 将json字符串转换成python对象
users = data['users']
first_user = users[0]
user_hash = first_user['hash']
# ========================函数区开始========================
html = requests.get('http://api.kanzhihu.com/userdetail2/' + user_hash)
data = json.loads(html.text)  # 将json字符串转换成python对象
# ====================一级字典====================
name = data['name']  # 用户名
avatar = data['avatar']  # 用户头像url
signature = data['signature']  # 用户签名
description = data['description']  # 用户个人描述
detail = data['detail']  # 用户详细数据
star = data['star']  # 七星阵排名
trend = data['trend']  # 近日动态，字段如下
topanswers = data['topanswers']  # 高票答案，字段如下
# ====================用户详细数据二级字典====================
ask = detail['ask'] #提问数
answer = detail['answer'] #回答数
post = detail['post'] #专栏文章数
agree = detail['agree'] #赞同数
agreei = detail['agreei'] #1日赞同数增加
agreeiratio = detail['agreeiratio'] #1日赞同数增幅
agreeiw = detail['agreeiw'] #7日赞同数增加
agreeiratiow = detail['agreeiratiow'] #7日赞同数增幅
ratio = detail['ratio'] #平均赞同（总赞同数/(回答+专栏)）
followee = detail['followee'] #关注数
follower = detail['follower'] #被关注数（粉丝）
followeri = detail['followeri'] #1日被关注数增加
followiratio = detail['followiratio'] #1日被关注数增幅
followeriw = detail['followeriw'] #7日被关注数增加
followiratiow = detail['followiratiow'] #7日被关注数增幅
thanks = detail['thanks'] #感谢数
tratio = detail['tratio'] #感谢/赞同比
fav = detail['fav'] #收藏数
fratio = detail['fratio'] #收藏/赞同比
logs = detail['logs'] #公共编辑数
mostvote = detail['mostvote'] #最高赞同
mostvotepercent = detail['mostvotepercent'] #最高赞同占比
mostvote5 = detail['mostvote5'] #前5赞同
mostvote5percent = detail['mostvote5percent'] #前5赞同占比
mostvote10 = detail['mostvote10'] #前10赞同
mostvote10percent = detail['mostvote10percent'] #前10赞同占比
count10000 = detail['count10000'] #赞同≥10000答案数
count5000 = detail['count5000'] #赞同≥5000答案数
count2000 = detail['count2000'] #赞同≥2000答案数
count1000 = detail['count1000'] #赞同≥1000答案数
count500 = detail['count500'] #赞同≥500答案数
count200 = detail['count200'] #赞同≥200答案数
count100 = detail['count100'] #赞同≥100答案数
# ====================七星阵排名二级字典====================
answerrank = star['answerrank'] #回答数+专栏文章数排名
agreerank = star['agreerank'] #赞同数排名
ratiorank = star['ratiorank'] #平均赞同排名
followerrank = star['followerrank'] #被关注数排名
favrank = star['favrank'] #收藏数排名
count1000rank = star['count1000rank'] #赞同超1000的回答数排名
count100rank = star['count100rank'] #赞同超100的回答数排名
# ====================前十高票答案链接转换====================
for i in range(10):
    if topanswers[i]['ispost']==1:
        link="zhuanlan.zhihu.com"+topanswers[i]['link']
        topanswers[i]['link']=link
    else:
        link="zhihu.com"+topanswers[i]['link']
        topanswers[i]['link']=link

print(topanswers[0]['title'])

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
info = ('用户名 ' +name, now, '用户头像url ' +avatar, '用户签名 ' +signature, '用户个人描述 ' +description, '提问数 ' +ask, '回答数 ' +answer, '专栏文章数 ' +post, '赞同数 ' +agree, '1日赞同数增加 ' +agreei, '1日赞同数增幅 ' +agreeiratio, '7日赞同数增加 ' +agreeiw, '7日赞同数增幅 ' +agreeiratiow, '平均赞同（总赞同数/(回答+专栏)） ' +ratio, '关注数 ' +followee, '被关注数（粉丝） ' +follower, '1日被关注数增加 ' +followeri, '1日被关注数增幅 ' +followiratio, '7日被关注数增加 ' +followeriw, '7日被关注数增幅 ' +followiratiow, '感谢数 ' +thanks, '感谢/赞同比 ' +tratio, '收藏数 ' +fav, '收藏/赞同比 ' +fratio, '公共编辑数 ' +logs, '最高赞同 ' +mostvote, '最高赞同占比 ' +mostvotepercent, '前5赞同 ' +mostvote5, '前5赞同占比 ' +mostvote5percent, '前10赞同 ' +mostvote10, '前10赞同占比 ' +mostvote10percent, '赞同≥10000答案数 ' +count10000, '赞同≥5000答案数 ' +count5000, '赞同≥2000答案数 ' +count2000, '赞同≥1000答案数 ' +count1000, '赞同≥500答案数 ' +count500, '赞同≥200答案数 ' +count200, '赞同≥100答案数 ' +count100, '回答数+专栏文章数排名 ' +answerrank, '赞同数排名 ' +agreerank, '平均赞同排名 ' +ratiorank, '被关注数排名 ' +followerrank, '收藏数排名 ' +favrank, '赞同超1000的回答数排名 ' +count1000rank, '赞同超100的回答数排名 ' +count100rank,topanswers[0]['title'], topanswers[0]['link'], topanswers[0]['agree'], topanswers[0]['date'], topanswers[0]['ispost'], topanswers[1]['title'], topanswers[1]['link'], topanswers[1]['agree'], topanswers[1]['date'], topanswers[1]['ispost'], topanswers[2]['title'], topanswers[2]['link'], topanswers[2]['agree'], topanswers[2]['date'], topanswers[2]['ispost'], topanswers[3]['title'], topanswers[3]['link'], topanswers[3]['agree'], topanswers[3]['date'], topanswers[3]['ispost'], topanswers[4]['title'], topanswers[4]['link'], topanswers[4]['agree'], topanswers[4]['date'], topanswers[4]['ispost'], topanswers[5]['title'], topanswers[5]['link'], topanswers[5]['agree'], topanswers[5]['date'], topanswers[5]['ispost'], topanswers[6]['title'], topanswers[6]['link'], topanswers[6]['agree'], topanswers[6]['date'], topanswers[6]['ispost'], topanswers[7]['title'], topanswers[7]['link'], topanswers[7]['agree'], topanswers[7]['date'], topanswers[7]['ispost'], topanswers[8]['title'], topanswers[8]['link'], topanswers[8]['agree'], topanswers[8]['date'], topanswers[8]['ispost'], topanswers[9]['title'], topanswers[9]['link'], topanswers[9]['agree'], topanswers[9]['date'], topanswers[9]['ispost'])
text = '\r\n'.join(info)
print(text)
# f = open('/Users/alicewish/我的坚果云/知乎.txt', 'a')
# try:
#     f.write(text)
# finally:
#     f.close()
line = (user_hash, now, name, avatar, signature, description, ask, answer, post, agree, agreei, agreeiratio, agreeiw, agreeiratiow, ratio, followee, follower, followeri, followiratio, followeriw, followiratiow, thanks, tratio, fav, fratio, logs, mostvote, mostvotepercent, mostvote5, mostvote5percent, mostvote10, mostvote10percent, count10000, count5000, count2000, count1000, count500, count200, count100, answerrank, agreerank, ratiorank, followerrank, favrank, count1000rank, count100rank,topanswers[0]['title'], topanswers[0]['link'], topanswers[0]['agree'], topanswers[0]['date'], topanswers[0]['ispost'], topanswers[1]['title'], topanswers[1]['link'], topanswers[1]['agree'], topanswers[1]['date'], topanswers[1]['ispost'], topanswers[2]['title'], topanswers[2]['link'], topanswers[2]['agree'], topanswers[2]['date'], topanswers[2]['ispost'], topanswers[3]['title'], topanswers[3]['link'], topanswers[3]['agree'], topanswers[3]['date'], topanswers[3]['ispost'], topanswers[4]['title'], topanswers[4]['link'], topanswers[4]['agree'], topanswers[4]['date'], topanswers[4]['ispost'], topanswers[5]['title'], topanswers[5]['link'], topanswers[5]['agree'], topanswers[5]['date'], topanswers[5]['ispost'], topanswers[6]['title'], topanswers[6]['link'], topanswers[6]['agree'], topanswers[6]['date'], topanswers[6]['ispost'], topanswers[7]['title'], topanswers[7]['link'], topanswers[7]['agree'], topanswers[7]['date'], topanswers[7]['ispost'], topanswers[8]['title'], topanswers[8]['link'], topanswers[8]['agree'], topanswers[8]['date'], topanswers[8]['ispost'], topanswers[9]['title'], topanswers[9]['link'], topanswers[9]['agree'], topanswers[9]['date'], topanswers[9]['ispost'])
line_text = '\t'.join(line)

print(trend[0])
print(topanswers[0])
print(len(trend))
print(len(topanswers))
# ================写入剪贴板================
import pyperclip
pyperclip.copy(line_text)
spam = pyperclip.paste()
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))

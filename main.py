from custom import match_words,unmatch_words,love_provinces
from tools import get_exam_links_str
from mail import send_mail

result = ''

if len(match_words) > 0:
  result += '<h1 style="color: #67C23A">当前匹配关键字：'
  for i in match_words:
    result += i + '、'
  result = result[0: len(result) - 1] + '</h1>'

if len(unmatch_words) > 0:
  result += '<h1 style="color: #F56C6C">当前已屏蔽关键字：'
  for i in unmatch_words:
    result += i + '、'
  result = result[0: len(result) - 1] + '</h1>'

result += get_exam_links_str()

print(result)

send_mail('最新事业单位招聘', result, 'html')
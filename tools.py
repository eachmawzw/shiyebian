import re
import requests
from bs4 import BeautifulSoup
from custom import match_words,unmatch_words,love_provinces
from constant import area_links

def match_reg_exp(keywords):
  _end = '^.*$'
  reg_str = '(?=.*match)'
  reg = ''
  for i in keywords:
    reg += reg_str.replace('match', i)
  reg += _end
  return reg

def unmatch_reg_exp(keywords):
  _start = '(?:'
  _end = ')'
  reg = ''
  for i in keywords:
    reg += i + '|'
  reg
  reg = _start + reg[0: len(reg) - 1] + _end
  return reg

def match_fun(text):
  return (
    text and
    re.compile(match_reg_exp(match_words)).search(text) and
    not re.compile(unmatch_reg_exp(unmatch_words)).search(text)
  )

def get_exam_link(area):
  a_list = []
  _link = area['link']
  for _index in range(10):
    r = requests.get(_link)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, features='html.parser')
    _list = soup.find_all(
      'a', 
      href=re.compile('http://www.shiyebian.net/xinxi'),
      string=match_fun
    )

    a_list += _list

    # 针对type == index_id的特殊处理，只有第二页才有index_2.html
    if area['type'] == 'index_id' and _index == 0:
      _link = _link + 'index_2.html'

    # 更新_link
    if area['type'] == 'index_id' and _index > 0:
      _link = re.sub('index_[0-9]+', 'index_' + str(_index + 2), _link)
    else:
      _link = re.sub('page=[0-9]+', 'page=' + str(_index + 1), _link)
  return a_list
  

def get_exam_links_str():
  love_area_links = []
  for province in love_provinces:
    for area in area_links:
      if area['name'] == province:
        love_area_links.append(area)

  exam_links_str = ''
  for area in love_area_links:
    links = get_exam_link(area)
    exam_links_str += '<h2 style="color:#E6A23C">您关注的&nbsp;<span style="color: #409EFF">' + area['name'] + '</span>&nbsp;的事业编消息有：</h2>'
    exam_links_str += '<ul>'
    for i in range(len(links)):
      exam_links_str += '\
        <li>\
          <em>' + links[i].previous_sibling.string + '</em>\
          &nbsp;&nbsp;\
          <a href="' + links[i].attrs['href'] + '">' + links[i].string + '</a>\
        </li>\
      '
    exam_links_str += '</ul>'
  
  return exam_links_str

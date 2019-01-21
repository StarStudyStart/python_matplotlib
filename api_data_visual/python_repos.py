# -*- coding:utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行api接口并存储响应
url = "https://api.github.com/search/repositories?q=python&sort=stars"
response = requests.get(url)
print("Status code:", response.status_code) #逗号可使变量在同一行内显示，且可以是不同数据类型；+号则必须是同一类型，否则会报错

#将api响应存储在一个变量中
response_dict = response.json()

#处理结果
print("Total repositories:",response_dict['total_count'])

#探究有关仓库的相关信息
repo_dicts = response_dict['items']
print("Respositories returned:",len(repo_dicts))

print("\nSelected information about each repository:")

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    '''
    print("\nName:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repositry:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])'''
    names.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])
    
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
    
#数据可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 24
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
    

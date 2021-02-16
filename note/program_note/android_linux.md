# android手机上的linux服务器

# [termux](https://www.cnblogs.com/liangblog/p/9790311.html)
- 官网下载，需要墙
- 首次更新，连vi都不能用，更新不墙更快
<pre>
apt update
apt upgrade
pkg install vim

apt edit-sources
# deb http://mirrors.tuna.tsinghua.edu.cn/termux stable main
apt update
apt upgrade

pkg install vim-python python 
apt install openssh 
pkg install screen

pip install pandas  # 发现很慢，安装慢，不是下载慢

# 生成$HOME/storage/xxx到手机根目录下xxx的文件夹链接，使得termux可以与手机交互文件
# https://wiki.termux.com/wiki/Sharing_Data
termux-setup-storage

# 没有很好用的适合在手机上用的文件编辑器
# https://wiki.termux.com/wiki/Text_Editors
</pre>

- 设置pip源
- 手机设置进程常驻，否则容易断线
- 设置ssh登录
<pre>
# port不是默认22，用户名和ip都需要查
ssh u0_a130@192.168.31.208 -p 8022
</pre>
- 设置ftp: [pyftpdlib](https://www.cnblogs.com/niansi/p/8232964.html)
<pre>
pip install pyftpdlib
cd [ftpdir]
# -w 写权限
python -m pyftpdlib [-w]

# 在电脑端匿名登录，注意ip和port
ftp://192.168.31.208:2121
</pre>

## AID Learning
不是很习惯，在手机上用图形界面貌似也没什么必要。
- 现在用[aid learning](http://www.aidlearning.net/), 只要在app市场上搜索就能找到并安装使用
    - 使用体验，界面仿苹果系统
    - [知乎专栏](https://www.zhihu.com/column/c_1208079877376901120)
    - 自己独立的空间，跟原生android隔离。还不知道怎么访问原生android上数据。
    - 看功能本身就很赞，值得探索一下
    - 不能在任务栏单独关闭一个窗口，只能点击窗口标题栏的按钮。有时会按不到。窗口不能移动，浏览器访问网络不友好。
    - 主要问题：
        - 文件交互：Aid:Finder->Storate 对应 手机文件系统根目录/
        - 安装idea
        - 安装express vpn
        - [远程ssh](http://new.aidlearning.net/d/84) 没搞定
        - [更改多内的deb源](https://blog.csdn.net/jamesdodo/article/details/106073576)
<pre>
deb http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb http://mirrors.aliyun.com/debian-security buster/updates main
deb-src http://mirrors.aliyun.com/debian-security buster/updates main
deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
</pre>    

<pre>
备份/etc/apt/sources.list
#备份
cp /etc/apt/sources.list /etc/apt/sources.list.bak
在/etc/apt/sources.list文件，注释原文件所有内容，前面添加上面的条目。

#更新
apt-get update
</pre>

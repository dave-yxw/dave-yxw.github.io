# screen

- [配置文件](https://github.com/dave-yxw/tools/tree/master/screen)

- 创建：screen -S name
- 重入(踢掉其它连接)：screen -r name
- 并入：screen -x name
screen -ls
kill pid  关闭相应pid的screen
screen -wipe
 
C-a C-c    创建新窗口
C-a C-n    next 窗口
C-a C-p    previous窗口
C-a n    n=0~9, n号窗口
C-a d    detach
C-a S-a     重命名窗口
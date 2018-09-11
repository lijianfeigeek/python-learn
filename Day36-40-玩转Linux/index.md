# 玩转Linux

## 基础命令

1. 获取登录信息 - w / who / last
2. 查看自己使用的Shell - ps
3. whatis
4. 查看命令的位置 - which / whereis
5. 查看帮助文档 - man / info / apropos
6. su
7. 以管理员身份执行命令 - sudo
8. logout / exit / adduser / userdel / passwd / ssh
9. 查看系统和主机名 - uname / hostname
10. reboot / init 6 / shutdown / init 0
11. history

## 文件和文件夹操作

1. 创建/删除目录 - mkdir / rmdir
2. 创建/删除文件 - touch / rm
    - touch命令用于创建空白文件或修改文件时间。在Linux系统中一个文件有三种时间：
      - 更改内容的时间 - mtime
      - 更改权限的时间 - ctime
      - 最后访问时间 - atime
    - rm的几个重要参数
      - -i：交互式删除，每个删除项都会进行询问
      - -r：删除目录并递归的删除目录中的文件和目录
      - f：强制删除，忽略不存在的文件，没有任何提示
3. 切换和查看当前工作目录 - cd / pwd
4. 查看目录内容 - ls
    - -l：以长格式查看文件和目录
    - -a：显示以点开头的文件和目录（隐藏文件）
    - -R：遇到目录要进行递归展开（继续列出目录下面的文件和目录）
    - -d：只列出目录，不列出其他内容
    - -S/-t：按大小/时间排序
5. 查看文件内容 - cat / head / tail / more / less
6. 拷贝/移动文件 - cp / mv
7. 查找文件和查找内容 - find / grep
8. 链接 - ln
9. 压缩/解压缩和归档/解归档 - gzip / gunzip / xz / tar
10. 其他工具 - sort / uniq / diff / tr / cut / paste / file / wc

## 别名
1. alias
    ```
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# alias ll='ls -l'
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# alias frm='rm -rf'
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# ll
    ...
    drwxr-xr-x  2 root       root   4096 Jun 20 12:52 abc
    ...
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# frm abc
    ```
2. unalias
    ```
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# unalias frm
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# frm sohu.html
    -bash: frm: command not found
    ```

## 其他程序
1. 时间和日期 - date / cal
2. 录制操作脚本 - script
3. 给用户发送消息 - mesg / write / wall / mail

## 文件系统
1. 命名规则：文件名的最大长度与文件系统类型有关，一般情况下，文件名不应该超过255个字符，虽然绝大多数的字符都可以用于文件名，但是最好使用英文大小写字母、数字、下划线、点这样的符号。文件名中虽然可以使用空格，但应该尽可能避免使用空格，否则在输入文件名时需要用将文件名放在双引号中或者通过\对空格进行转义。
2. 扩展名：在Linux系统下文件的扩展名是可选的，但是使用扩展名有助于对文件内容的理解。有些应用程序要通过扩展名来识别文件，但是更多的应用程序并不依赖文件的扩展名，就像file命令在识别文件时并不是依据扩展名来判定文件的类型。
3. 隐藏文件：以点开头的文件在Linux系统中是隐藏文件（不可见文件）。


### 目录结构
1. /bin - 基本命令的二进制文件。
2. /boot - 引导加载程序的静态文件。
3. /dev - 设备文件。
4. /etc - 配置文件。
5. /home - 普通用户主目录的父目录。
6. /lib - 共享库文件。
7. /lib64 - 共享64位库文件。
8. /lost+found - 存放未链接文件。
9. /media - 自动识别设备的挂载目录。
10. /mnt - 临时挂载文件系统的挂载点。
11. /opt - 可选插件软件包安装位置。
12. /proc - 内核和进程信息。
13. /root - 超级管理员用户主目录。
14. /run - 存放系统运行时需要的东西。
15. /sbin - 超级用户的二进制文件。
16. /sys - 设备的伪文件系统。
17. /tmp - 临时文件夹。
18. /usr - 用户应用目录。
19. /var - 变量数据目录。

### 访问权限

1. chmod - 改变文件模式比特。
    ```
    chmod 644 sohu.html
    ```
    [![](https://github.com/jackfrued/Python-100-Days/raw/master/Day31-35/res/file-mode.png)](https://github.com/jackfrued/Python-100-Days/blob/master/Day31-35/res/file-mode.png)

2. chown - 改变文件所有者。
    ```
    hown hellokitty readme.txt
    ```

### 配置服务
1. 启动服务 `systemctl start firewalld`
2. 终止服务 `systemctl stop firewalld`
3. 重启服务 `systemctl restart firewalld`
4. 查看服务 `systemctl status firewalld`
5. 设置是否开机自启.
    ```
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# systemctl enable firewalld
    Created symlink from /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service to /usr/lib/systemd/system/firewalld.service.
    Created symlink from /etc/systemd/system/multi-user.target.wants/firewalld.service to /usr/lib/systemd/system/firewalld.service.
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# systemctl disable firewalld
    Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
    Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.

    ```
  
### 计划任务

1. crontab命令

### 网络访问和管理
1. 通过网络获取资源 - wget。
  - -b 后台下载模式
  - -O 下载到指定的目录
  - -r 递归下载
2. 显示/操作网络配置 - ip。
3. 网络可达性检查 - ping。
4. 查看网络服务和端口 - netstat。
5. 安全文件拷贝 - scp
6. 安全文件传输 - sftp
    ```
    help：显示帮助信息。

    ls/lls：显示远端/本地目录列表。

    cd/lcd：切换远端/本地路径。

    mkdir/lmkdir：创建远端/本地目录。

    pwd/lpwd：显示远端/本地当前工作目录。

    get：下载文件。

    put：上传文件。

    rm：删除远端文件。

    bye/exit/quit：退出sftp。
    ```

## 进程管理
1. ps - 查询进程
    ```
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# ps -ef
    UID        PID  PPID  C STIME TTY          TIME CMD
    root         1     0  0 Jun23 ?        00:00:05 /usr/lib/systemd/systemd --switched-root --system --deserialize 21
    root         2     0  0 Jun23 ?        00:00:00 [kthreadd]
    ...
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# ps -ef | grep mysqld
    root      4943  4581  0 22:45 pts/0    00:00:00 grep --color=auto mysqld
    mysql    25257     1  0 Jun25 ?        00:00:39 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid
        ```
2. kill - 终止进程
3. 将进程置于后台运行
    - Ctrl+Z
    - &
  ```
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# mongod &
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# redis-server
  ...
  ^Z
  [4]+  Stopped                 redis-server
  ```
4. jobs - 查询后台进程
5. bg - 让进程在后台继续运行
6. fg - 将后台进程置于前台
7. top - 进程监控


## 系统性能
1. 查看系统活动信息 - sar
2. 查看内存使用情况 - free
3. 查看进程使用内存状况 - pmap
    ```
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# ps
      PID TTY          TIME CMD
    4581 pts/0    00:00:00 bash
    5664 pts/0    00:00:00 ps
    [root@iZwz97tbgo9lkabnat2lo8Z ~]# pmap 4581
    4581:   -bash
    0000000000400000    884K r-x-- bash
    00000000006dc000      4K r---- bash
    00000000006dd000     36K rw--- bash
    00000000006e6000     24K rw---   [ anon ]
    0000000001de0000    400K rw---   [ anon ]
    00007f82fe805000     48K r-x-- libnss_files-2.17.so
    00007f82fe811000   2044K ----- libnss_files-2.17.so
    ```
4. 报告设备CPU和I/O统计信息 - iostat
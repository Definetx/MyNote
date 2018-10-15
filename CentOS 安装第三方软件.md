# CentOS

## EPEL

* EPEL（Extra Packages for Enterprise Linux） 是由 Fedora 社区打造，为 RHEL 及衍生发行版如 CentOS 等提供高质量软件包的项目。装上了 EPEL，就像在 Fedora 上一样，可以通过 yum install 软件包名，即可安装很多以前需要编译安装的软件、常用的软件或一些比较流行的软件，比如现在流行的 nginx、htop、ncdu、vnstat 等等，都可以使用EPEL很方便的安装更新

### 步骤

* 安装EPEL源

```
目前可以直接通过执行命令： yum -y install epel-release 直接进行安装，如果此命令无法安装可以尝试以下方法

CentOS/RHEL 5 ：
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-5.noarch.rpm
CentOS/RHEL 6 ：
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
CentOS/RHEL 7 ：
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

### 使用

```
yum install 软件包名称
```

### 异常处理

* Package epel-release-7-11.noarch already installed and latest version

```
vim /etc/yum.repos.d/epel.repo
将 enabled=0 改为 enabled=1
```

### 参考

* [vps manage](https://www.vpser.net/manage)
* [CentOS/RHEL Linux安装EPEL第三方软件源](https://www.vpser.net/manage/centos-rhel-linux-third-party-source-epel.html)
* [Linux流量监控工具 - iftop (最全面的iftop教程)](https://www.vpser.net/manage/iftop.html)
* [CentOS 7 无法使用 epel 的解决方法](https://blog.csdn.net/u012908433/article/details/80285751)

## yum 源更换

### 步骤

1. 备份原 yum 源

```
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

1. 下载阿里云的 CentOS-Base.repo 到 /etc/yum.repos.d/

```
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

1. 清理缓存

```
sudo yum clean all
```

4. 生成新的缓存

```
sudo yum makecache
```

### 参考

* [阿里云开源镜像站](https://mirrors.aliyun.com/help/centos)
* [清华开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/centos/)

## pstree 安装

```
yum install psmisc -y
```

## iostat/sar 安装

```
yum install -y sysstat
```
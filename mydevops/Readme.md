# 运维平台

## 依赖环境

* python
* mysql
* mongodb
* redis

## 数据库配置

* mysql 使用 utf-8 字符集，在 /etc/my.cnf 文件新增语句后 systemctl restart mysqld

```
[client]
default-character-set=utf8
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
```

* 新增数据库与使用的用户

```
create database notes;
grant all on notes.* to notes@'127.0.0.1' identified by '密码';
flush privileges;
```

## 项目与应用建立

```
django-admin startproject devops
mv devops mydevops
cd mydevops
python manage.py startapp devops_app

python manage.py makemigrations
python manage.py migrate
```

## 使用 pymsql 代替 mysqlclient

* __init__.py

```
import pymysql
pymysql.install_as_MySQLdb()
``` 

* settings.py

```
import pymysql
pymysql.install_as_MySQLdb()

INSTALLED_APPS 处加上应用名称 devops_app
更改 DATABASES
``` 

* models.py

```
on_delete=models.CASCADE
```

* 参考
 * [on_delete](https://www.cnblogs.com/phyger/p/8035253.html)
 * [pymsql](https://blog.csdn.net/jaket5219999/article/details/54944729)
 
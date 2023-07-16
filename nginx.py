#!/bin/bin/env ptyhon3
# -*- coding:utf-8 -*-

import os,sys

#检查root用户
if os.getuid() != 0:
    print("当前用户不是root,请以root身份执行脚本")
    sys.exit(1)

#版本号的选择
# http://nginx.org/download/nginx-1.18.0.tar.gz

#如果没有选择安装版本，就直接将1.18.0作为默认版本
def_var = '1.18.0'
var = input('请输入版本(默认{}):'.format(def_var))
var = var or def_var

#安装目录的配置
def_path = '/usr/local/nginx'
path = input('请输入安装(默认{})'.format(def_path))
path = path or def_path

#如果存在同名文件现删除
if os.path.exists('nginx-{}.tar.gz'.format(var)):
    os.remove('nginx-{}.tar.gz'.format(var))

#下载源码包,注意wget后有空格
url = 'http://nginx.org/download/nginx-{}.tar.gz'
cmd = 'wget ' + url.format(var)
res = os.system(cmd)
if res != 0:
    print('下载失败')
    sys.exit(1)

#解压
cmd = 'tar -zxf nginx-{}.tar.gz'.format(var)
if os.system(cmd) != 0:
    print('解压失败')
    sys.exit(1)

#安装依赖
cmd = 'yum install -y gcc make libpcre3-dev zlib1g-dev openssl libssl-dev'
if os.system(cmd) != 0:
    print('安装依赖失败')
    sys.exit(1)

#配置
cmd = 'cd nginx-{} && ./configure --prefix=/usr/local/nginx --with-http_ssl_module'.format(var)
if os.system(cmd) != 0:
    print('配置失败')
    sys.exit(1)

#编译
cmd = 'cd nginx-{} make && make install'.format(var)
if os.system(cmd) != 0:
    print('编译失败')
    sys.exit(1)

print('安装成功')
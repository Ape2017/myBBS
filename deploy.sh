git pull

# 删掉 nginx default 设置
# rm -f /etc/nginx/sites-enabled/default
# rm -f /etc/nginx/sites-available/default

# 建立一个软连接
# ln -s -f /root/bbs/bbs.conf /etc/supervisor/conf.d/bbs.conf
# 不要再 sites-available 里面放任何东西
# ln -s -f /root/bbs/bbs.nginx /etc/nginx/sites-enabled/bbs

# 重启服务器
service supervisor restart
service nginx restart

# chmod o+rx /root
# chmod -R o+rx /root/bbs

echo 'deploy success'
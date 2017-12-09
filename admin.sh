#!/bin/sh
# mongo <数据库名> --eval 'db.User.update({username:"<要设为管理员的用户名>"},{$set:{admin:true}});'
mongo bbs --eval 'db.User.update({username:"admin"},{$set:{admin:true}});'

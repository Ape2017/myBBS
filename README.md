# myBBS
基于 Flask 的论坛, [Demo 地址](http://www.enin.cc/)

- 数据库使用了 MongoDB，界面实现采用前端框架 Bootstrap 及其免费主题 Bootswatch
- 实现功能：
    - 用户注册/登录、发帖/回复、私信，可修改签名、密码及头像
    - 用户可修改或删除自己发布的帖子和回复，支持在帖子或回复中 AT 其他用户
    - 帖子、回复和私信正文支持 Markdown 语法
    - 用户被 AT 或收到了新私信会有新消息提示
    - 管理员可修改或删除所有帖子和回复，可添加新板块，可删除用户或赋予用户管理员权限
### 演示
![演示图片](https://github.com/enincc/myBBS/blob/master/bbs.gif)

### 运行和部署相关

- 安装依赖库 `pip install -r requirements.txt`

- 运行前需要在 `config.py` 文件中修改密钥、数据库名等配置选项，可参照 `config_copy.py` 自行创建。

- 第一个管理员需要手动添加，可注册新账号后修改并运行 `admin.sh` 脚本将该账号升级为管理员。

- 部署使用了 Nginx + Supervisor + Gunicorn ，具体配置分别在 `bbs.nginx`、`bbs.conf` 及 `gunicorn.config.py` 中修改。

- `configuration\setup_development.sh` 和 `configuration\setup_production.sh` 分别是开发环境和生产环境部署脚本，可根据需要自行修改。


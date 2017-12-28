# 用于 Flask 框架的密钥，用于 session 加密，用os.urandom(24)生成
SECRET_KEY = '\x98y\xf4jU\xad\xe1\x08Z)\x08\x17\x07\n\x1d\x16\xcb\xe6\xd3xJx\xebH'
# 给用户密码哈希加密所用的盐(salt)值，用os.urandom(24)生成
SALT_KEY = '\x84\xcf\xe2\xa1\x11QH[\x8f\x92j\xba4\x9e\x0bd\x13\x1c\xbeb\x14\x05\x9f\xb3'
# 数据库名
DATABASE_NAME = 'bbs'
# 网站域名，调用 google 搜索时需要用到
DOMAIN_NAME = 'enin.cc/topic'

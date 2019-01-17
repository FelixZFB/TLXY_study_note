from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

# 初次登录,验证后给我们cookie
def login():
    '''
    负责初次登录
    需输入用户名和密码，用来获取cookie凭证
    '''
    # 登录用户地址，进入人人网登录首页，查看网页源码
    # 网页源码中打开查找，查找“下次自动登录”
    # 然后向上找form，里面就有login-form
    url = 'http://www.renren.com/PLogin.do'

    # 此键值需要从登录form的对应两个input中提取name属性
    data = {
        'email': '908851835@qq.com'
        'password': 'zfb123456zfb'
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = 'http://www.renren.com/969464538/profile'

    # 如果已经执行了login


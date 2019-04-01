from flask import Flask, render_template, request,redirect,make_response
import datetime
from orm import model
from orm import ormmange as manage

app = Flask(__name__)
# 配置缓存更新时间
app.send_file_max_age_default = datetime.timedelta(seconds=1)
app.debug = True


# 首页
# 将 http://127.0.0.1:5000/ 和index视图函数绑定
@app.route('/')
def index():

    user = request.cookies.get("name")
    # print(user)
    return render_template('index.html', userinfo = user)

# 注册
@app.route('/regist', methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        # args = request.args
        # print(args)
        # name = args.get('username')
        # pwd = args.get('password')
        # print(name,pwd)
        # 收到get请求','返回注册页面
        return render_template('regist.html')
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # print(username,password)
        # 收到post请求,返回登录页面
        try:
            manage.insertUser(username,password)
            return redirect('/')
        except:
            redirect('/regist')

# 登录
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        # args = request.args
        # print(args)
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # print(username,password)

        # 内容需要查询数据库
        # 第一种 不带接口
        # return render_template("list.html")
        # 第二种 带接口 重定向
        # 自动在URL 发起请求 请求list
        # return redirect('/list')

        # 为了让响应可以携带头信息 ，需要构造响应
        try:
            result = manage.checkUser(username, password)
            if result == True:
                res = make_response(redirect('/'))
                res.set_cookie('name', username, expires=datetime.datetime.now() + datetime.timedelta(days=7))
                return res
            else:
                return redirect('/login')
        except:
            return redirect('/login')


@app.route('/quit')
def quit():
    res = make_response(redirect('/'))
    res.delete_cookie('name')
    return res

# 员工信息列表
@app.route('/list')
def list():
    res = manage.findStaff()
    # print('************',res[0])
    user = request.cookies.get('name')
    return render_template('list.html', staff = res, userinfo = user)

# 添加员工
@app.route('/operate', methods=['GET','POST'])
def operate():
    if request.method == 'GET':
        user = request.cookies.get('name')
        return render_template('operate.html',userinfo=user)
    elif request.method == "POST":
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        phone = request.form['phone']
        try:
            manage.insertStaff(name, gender, age, phone)
            return redirect('/list')
        except:
            redirect('/operate')

# 删除员工
@app.route('/<num>')
def dele(num):

    try:
        manage.delteStaff(num)
        return redirect('/list')
    except:
        redirect('/list')

# 修改员工信息
@app.route('/up/<int:num>',methods=['GET','POST'])
def update(num):

    if request.method == 'GET':
        info = manage.personStaff(num)
        user = request.cookies.get('name')
        # print(num,info.id,'###########################')
        return render_template('up.html',userinfo = user,infos = info,num = num)

    elif request.method == "POST":
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        phone = request.form['phone']
        # print(name,gender,age,phone)
        try:
            manage.updateStaff(num,name,gender,age,phone)

            return redirect('/list')
        except:
            redirect('/up/<int:num>')

# # 员工模糊查询
# @app.route('/list',methods=['GET','POST'])
# def staff_find():
#     if request.method == 'POST':
#         info = request.form['name']
#         rea = manage.dim_findStaff(info)
#         user = request.cookies.get('name')
#         return render_template('list.html',userinfo=user,staff=rea)

# 商品详情
@app.route('/<num>')
def details(num):
    user = request.cookies.get('name')
    return render_template('details.html', num = num, userinfo = user)

if __name__ == "__main__":
    app.run()
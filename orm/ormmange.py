from orm import model
from sqlalchemy import create_engine,and_
engine = create_engine("mysql+mysqlconnector://root:root@localhost/flaskdb",
                                    encoding='utf8', echo=False)
from  sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# 用户添加和查看
def insertUser(username,password):
    session.add(model.User(username=username,password=password))
    session.commit()
    session.close()
    # print(result)

def checkUser(username, password):
    result = session.query(model.User).filter(model.User.username == username).filter(model.User.password==password).first()
    # print('######################',result)
    if result:
        return True
    else:
        return False

# 员工添加
def insertStaff(name, gender, age ,phone):
    result = session.add(model.Staff(name=name,gender=gender,age=age,phone=phone))
    session.commit()
    session.close()
    # print(result)

# 员工删除
def delteStaff(id):
    session.query(model.Staff).filter(model.Staff.id == id).delete()
    session.commit()
    session.close()

# 员工信息修改
def updateStaff(id,name,gender,age,phone):
    # print(id,type(id) ,'+++++++++++++')
    session.query(model.Staff).filter(model.Staff.id == id).update({model.Staff.name:name,
                                        model.Staff.gender:gender,model.Staff.age:age,model.Staff.phone:phone})
    # print(result)
    session.commit()
    session.close()


# 员工所有信息查询
def findStaff():
    result = session.query(model.Staff.id,model.Staff.name,model.Staff.gender,
                          model.Staff.age,model.Staff.phone)
    return result

# 员工个人信息查询
def personStaff(id):
    result = session.query(model.Staff).filter(model.Staff.id==id).first()
    return result

# # 员工模糊信息查询
# def dim_findStaff(name):
#     result = session.query(model.Staff.id,model.Staff.name,model.Staff.gender,
#                           model.Staff.age,model.Staff.phone).filter(and_(model.Staff.name.like('%'+name+'%'))).all()
#     # for r in result:
#     #     print(r,r[0],'###############################')
#     return result
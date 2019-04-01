class TTT():
    def __init__(self,id):
        self.id = id



class Book():
    def __init__(self, _id, _name, _price):
        self.id = _id
        self.name = _name
        self.price = _price

    def __str__(self):
        return 'id:',self.id,'name:',self.name,'price:',self.price

# 创建管理员和员工表
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:root@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from  sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

from sqlalchemy import  Column,Integer,String

# 管理员
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50),nullable=False)
    password = Column(String(50),nullable=False)
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

# 员工资料
class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50),nullable=False)
    gender = Column(String(10))
    age = Column(Integer,nullable=False)
    phone = Column(Integer, nullable=False)
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

# # 员工工资
# class PersonInfo(Base):
#     __tablename__ = 'personInfo'
#     id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#     time = Column()
if __name__ == "__main__":
    # 创建表 须卸载main模块
    Base.metadata.create_all(bind=engine)




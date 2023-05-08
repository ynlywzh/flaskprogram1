import pymysql

class Student:
    """学生类"""

    def __init__(self, id, name, gender, age,classe, score):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.classe = classe
        self.score = score


class System:
    """学生信息管理系统"""

    def __init__(self):
        # 连接MySQL数据库
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="2003wzh0905",
            database="student_db",
            charset="utf8"
        )
        self.cursor = self.db.cursor()

    def login(self):
        """登录"""
        print("欢迎使用学生信息管理系统！")
        while True:
            username = input("请输入用户名：")
            password = input("请输入密码：")
            sql = "select * from user where username=%s and password=%s"
            params = (username,password)
            self.cursor.execute(sql,params)
            result = self.cursor.fetchone()
            if result:
                print("登录成功！")
                break
            else:
                print("用户名或密码错误，请重新输入！")

    def register(self):
        """注册"""
        username = input("请输入用户名：")
        password = input("请输入密码：")
        sql = "insert into user (username, password) values (%s, %s)"
        params = (username, password)
        self.cursor.execute(sql, params)
        self.db.commit()
        print("注册成功！")

    def add(self):
        """增加学生信息"""
        id = input("请输入学号：")
        classe = input("请输入班级：")
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        gender = input("请输入性别：")
        score = input("请输入成绩：")
        sql = "insert into students_data (id, classe, name, age, gender, score) values (%s, %s, %s, %s, %s, %s)"
        params = (id, classe, name, age, gender, score)
        self.cursor.execute(sql, params)
        self.db.commit()
        print("添加成功！")

    def delete(self):
        """删除学生信息"""
        id = input("请输入要删除的学号：")
        sql = "delete from students_data where id=%s"
        params = (id,)
        self.cursor.execute(sql, params)
        self.db.commit()
        print("删除成功！")

    def update(self):
        """修改学生信息"""
        id = input("请输入新学号：")
        classe = input("请输入新班级：")
        name = input("请输入新姓名：")
        age = input("请输入新年龄：")
        gender = input("请输入新性别：")
        score = input("请输入新成绩：")
        sql = "update students_data set classe=%s, name=%s, age=%s, gender=%s, score=%s where id=%s"
        params = (classe, name, age, gender, score, id)
        self.cursor.execute(sql, params)
        self.db.commit()
        print("修改成功！")

    def query(self):
        """查看学生信息"""
        sql = "select * from students_data"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        if results:
            print("学号\t班级\t姓名\t年龄\t性别\t成绩")
            for result in results:
                student = Student(*result)
                print(
                    f"{student.id}\t{student.classe}\t{student.name}\t{student.age}\t{student.gender}\t{student.score}")
        else:
            print("没有学生信息！")

    def menu(self):
        """菜单"""
        while True:
            print("请选择您要进行的操作：")
            print("1. 登录")
            print("2. 注册")
            print("3. 增加学生信息")
            print("4. 删除学生信息")
            print("5. 修改学生信息")
            print("6. 查看学生信息")
            print("0. 退出")
            choice = input()
            if choice == "1":
                self.login()
            elif choice == "2":
                self.register()
            elif choice == "3":
                self.add()
            elif choice == "4":
                self.delete()
            elif choice == "5":
                self.update()
            elif choice == "6":
                self.query()
            elif choice == "0":
                print("感谢使用，退出该系统！")
                self.db.close()
                break
            else:
                print("输入有误，请重新选择！")


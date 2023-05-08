from flask import Flask, render_template, request, redirect, url_for
import pymysql
from main import Student

# 连接MySQL数据库
db = pymysql.connect(
    host="localhost",
    user="root",
    password="2003wzh0905",
    database="students",
    charset="utf8"
)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

def menu():
    return redirect(url_for('index'))

@app.route('/login')
def signin():
    return render_template('login.html')

@app.route('/register')
def signon():
    return render_template('register.html')

@app.route('/query')
def ask():
    return render_template('query.html')
@app.route('/add')
def adds():
    return render_template('add.html')
@app.route('/delete')
def deletes():
    return render_template('delete.html')
@app.route('/update')
def updates():
    return render_template('update.html')




#登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    cursor = db.cursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = "select * from user where username=%s and password=%s"
        params = (username, password)
        result = cursor.execute(sql, params, True)
        if result:
            return redirect(url_for('index'))
        else:
            error = '用户名或密码错误，请重新输入！'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')


#注册
@app.route('/register', methods=['GET','POST'])
def register():
    cursor = db.cursor()
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = "insert into user(username,password)values(%s,%s) "
        params = (username,password)
        cursor.execute(sql,params)
        return redirect(url_for('index'))




# 显示所有学生的信息
@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students_data")
    students = cursor.fetchall()
    return render_template("index.html", students=students)


#查看学生信息
@app.route("/query",methods=["GET"])
def query():
    cursor = db.cursor()
    sql = "select * from students_data"
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        print("学号\t班级\t姓名\t年龄\t性别\t成绩")
        for result in results:
            student = Student(*result)
            print(
                f"{student.id}\t{student.classe}\t{student.name}\t{student.age}\t{student.gender}\t{student.score}")
    else:
        print("没有学生信息！")
    return redirect(url_for('index'))





# 添加学生信息
@app.route("/add", methods=["POST"])
def add():
    id = request.form["id"]
    name = request.form["name"]
    classe = request.form["class"]
    age = request.form["age"]
    gender = request.form["gender"]
    score = request.form["score"]
    cursor = db.cursor()
    sql = "INSERT INTO students (id, name, class, age, gender, score) VALUES ('%s', '%s', '%s', %d, '%s', %f)" % (id, name, classe, int(age), gender, float(score))
    cursor.execute(sql)
    db.commit()
    return redirect(url_for("index"))

# 修改学生信息
@app.route("/update", methods=["POST"])
def update():
    id = request.form["id"]
    student_id = request.form["student_id"]
    name = request.form["name"]
    classe = request.form["class"]
    age = request.form["age"]
    gender = request.form["gender"]
    score = request.form["score"]
    cursor = db.cursor()
    sql = "UPDATE students SET id='%s', name='%s', class='%s', age=%d, gender='%s', score=%f WHERE id=%d" % (id, name, classe, int(age), gender, float(score), int(id))
    cursor.execute(sql)
    db.commit()
    return redirect(url_for("index"))

# 删除学生信息
@app.route("/delete", methods=["POST"])
def delete():
    id = request.form["id"]
    cursor = db.cursor()
    sql = "DELETE FROM students WHERE id=%d" % int(id)
    cursor.execute(sql)
    db.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

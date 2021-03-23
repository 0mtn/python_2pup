from flask import Flask, redirect, url_for, jsonify # import biblioteki flask, redirect, url_for
app = Flask(_name_)

import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="python"
)

@app.route('/addPupil/<name>/<surname>/<pesel>/<class_name>')
def add_pupil(name, surname, pesel, class_name):
    mycursor = mydb.cursor()
    rand_id = random.randint(0, 1000)
    # new_pupil_query_values = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (" + str(rand_id) + ",'" + name + "','" + surname + "'," + str(pesel) + ",'" + class_name + "');"
    new_pupil_query = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (%s, %s, %s, %s, %s)"
    new_pupil_query_values = (rand_id, name, surname, pesel, class_name)
    mycursor.execute(new_pupil_query, new_pupil_query_values)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info="User " + name + " " + surname + " added successfully",
        responseCode=200
    )

@app.route('/addTeacher/<name>/<surname>/<pesel>/<subject>')
def add_teacher(name, surname, pesel, subject):
    mycursor = mydb.cursor()
    rand_id = random.randint(0, 1000)
    # new_pupil_query_values = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (" + str(rand_id) + ",'" + name + "','" + surname + "'," + str(pesel) + ",'" + class_name + "');"
    new_teacher_query = "INSERT INTO TEACHER (teacher_id, name, surname, pesel, subject) VALUES (%s, %s, %s, %s, %s)"
    new_teacher_query_values = (rand_id, name, surname, pesel, subject)
    mycursor.execute(new_teacher_query, new_teacher_query_values)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info="User " + name + " " + surname + " added successfully",
        responseCode=200
    )

@app.route('/addSubject/<name>')
def add_subject(name):
    mycursor = mydb.cursor()
    rand_id = random.randint(0, 1000)
    # new_pupil_query_values = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (" + str(rand_id) + ",'" + name + "','" + surname + "'," + str(pesel) + ",'" + class_name + "');"
    new_subject_query = "INSERT INTO SUBJECT (subject_id, name) VALUES (%s, %s)"
    new_subject_query_values = (rand_id, name)
    mycursor.execute(new_subject_query, new_subject_query_values)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info="Subject " + name + " added successfully",
        responseCode=200
    )

@app.route('/addGrade/<value>/<weight>')
def add_grade(value, weight):
    mycursor = mydb.cursor()
    rand_id = random.randint(0, 1000)
    # new_pupil_query_values = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (" + str(rand_id) + ",'" + name + "','" + surname + "'," + str(pesel) + ",'" + class_name + "');"
    new_grade_query = "INSERT INTO GRADE (pupil_id, value, weight) VALUES (%s, %s, %s)"
    new_grade_query_values = (rand_id, value, weight)
    mycursor.execute(new_grade_query, new_grade_query_values)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info="Grade " + value + " added successfully",
        responseCode=200
    )

@app.route('/addPupilSubject/<pupil_id>/<subject_id>')
def add_pupilsubject(pupil_id, subject_id):
    mycursor = mydb.cursor()
    # new_pupil_query_values = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (" + str(rand_id) + ",'" + name + "','" + surname + "'," + str(pesel) + ",'" + class_name + "');"
    new_pupilsubject_query = "INSERT INTO PUPIL_SUBJECT (pupil_id, subject_id) VALUES (%s, %s)"
    new_pupilsubject_query_values = (pupil_id, subject_id)
    mycursor.execute(new_pupilsubject_query, new_pupilsubject_query_values)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info= pupil_id + " added successfully",
        responseCode=200
    )

@app.route('/addPupilTeacher/<pupil_id>/<teacher_id>')
def add_pupilteacher(pupil_id, teacher_id):
    mycursor = mydb.cursor()
    # new_pupil_query_values = "INSERT INTO pupil (pupil_id, name, surname, pesel, class) VALUES (" + str(rand_id) + ",'" + name + "','" + surname + "'," + str(pesel) + ",'" + class_name + "');"
    new_pupilteacher_query = "INSERT INTO PUPIL_TEACHER (pupil_id, teacher_id) VALUES (%s, %s)"
    new_pupilteacher_query_values = (pupil_id, teacher_id)
    mycursor.execute(new_pupilteacher_query, new_pupilteacher_query_values)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info= pupil_id + " added successfully",
        responseCode=200
    )

#####

@app.route('/showPupil')
def show_pupil():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM PUPIL")
    myresult = mycursor.fetchone()
    print(myresult)
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info= myresult,
        responseCode=200
    )

@app.route('/showTeacher')
def show_teacher():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM TEACHER")
    myresult = mycursor.fetchone()
    print(myresult)
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info= myresult,
        responseCode=200
    )

@app.route('/showSubject')
def show_subject():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM SUBJECT")
    myresult = mycursor.fetchone()
    print(myresult)
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info= myresult,
        responseCode=200
    )

@app.route('/showGrade')
def show_grade():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM GRADE")
    myresult = mycursor.fetchone()
    print(myresult)
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info= myresult,
        responseCode=200
    )

@app.route('/showPupilSubject')
def show_pupilsubject():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM PUPIL_SUBJECT")
    myresult = mycursor.fetchone()
    print(myresult)
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info= myresult,
        responseCode=200
    )

@app.route('/showPupilTeacher')
def show_pupilteacher():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM PUPIL_TEACHER")
    myresult = mycursor.fetchone()
    print(myresult)
    return jsonify( # zwrócenie jsona (pamiętaj o imporcie tej bibliteki)
        info= myresult,
        responseCode=200
    )

if _name_ == "_main_":
    app.run("localhost", 3000, True, {}) # odpalenie serwera (host, port, debug, options)
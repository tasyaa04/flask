from flask import Flask, render_template, redirect, request, make_response, session
import db_session
from users import User
from jobs import Jobs
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


def main():
    db_session.global_init("mars_explorer.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Smith"
    user.name = "Jacob"
    user.age = 18
    user.position = "colonist"
    user.speciality = "farmer"
    user.address = "module_2"
    user.email = "withnosurvivors@mars.org"
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Bruh"
    user.name = "Duh"
    user.age = 22
    user.position = "colonist"
    user.speciality = "engineer"
    user.address = "module_3"
    user.email = "bruh@mars.org"
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Bennet"
    user.name = "-_-"
    user.age = 16
    user.position = "colonist"
    user.speciality = "warrior"
    user.address = "module_4"
    user.email = "bennet@mars.org"
    db_sess.add(user)
    db_sess.commit()
    jobs = Jobs(team_leader=1, job="deployment of residential modules 1 and 2",
                work_size=15, collaborators="2, 3",
                is_finished=False)
    db_sess.add(jobs)
    db_sess.commit()
    jobs = Jobs(team_leader=1, job="deployment of residential modules 3 and 4",
                work_size=20, collaborators="3, 4",
                is_finished=True)
    db_sess.add(jobs)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
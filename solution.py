name = input()
global_init(name)
db_sess = create_session()

for user in db_sess.query(User).filter(User.address == "module_1", User.position.notilike("%engineer%"),
                                       User.speciality.notilike("%engineer%")):
    print(user.id)

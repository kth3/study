def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    else:
        if id_pw[0] in [id[0] for id in db]:
            return 'wrong pw'
        else:
            return 'fail'
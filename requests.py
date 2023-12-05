from random import setstate
from typing import Optional
from sqlmodel import Field,Session, SQLModel, select, or_
from models import engine, Users, Application, ApplEl, PhReq, Photo, Req

"""
Переделать tt-шки в json или около того, для апишки
убрать принты
Переделать vievApll в другой формат без принтов, как вариант запихнуть все в json
"""

# Краткая информация по заявкам клиента
def select_apl_for_client():
    with Session(engine) as session:
        statement = select(Application).where(Application.user == 4)
        results = session.exec(statement)
        for apl in results:
            tt = "Application number: " + str(apl.id) + '\nDescription: ' + apl.text + '\nStatus: ' + apl.status
    return tt


# отбор заявок с определенным статусом
def select_apl_status():
    with Session(engine) as session:
        statement = select(Application).where(or_(Application.status == 'отправлена', Application.status == 'на рассмотрении'))
        results = session.exec(statement)
        for apl in results:
            tt = "Application number: " + str(apl.id) + '\nDescription: ' + apl.text + '\nStatus: ' + apl.status
    return tt

# информация о клиенте 
def select_inf_client():
    with Session(engine) as session:
        statement = select(Users).where(Users.id == 3)
        results = session.exec(statement)
        for apl in results:
            tt = "Client id: " + str(apl.id) + '\nName: ' + apl.name + '\nEmail: ' + apl.email + '\nPhone' + apl.phone
    return tt
        
# отбор фоток к 1 заявке
def select_photo_for_apl(id_app):
    with Session(engine) as session:
        statement = select(ApplEl).where(ApplEl.idap == id_app)
        el_apl = session.exec(statement)
        inf_req = dict()
        for i in el_apl:
            statement = select(PhReq).where(PhReq.id == i.phr)
            el_req = session.exec(statement)
            for j in el_req:
                if j.idreq not in inf_req:
                    inf_req[j.idreq] = []
                inf_req[j.idreq]. append((j.id, j.idph))
    return inf_req

# description req
def select_description(id_req):
    with Session(engine) as session:
        statement = select(Req).where(Req.id == id_req)
        res = session.exec(statement)
        for i in res:
            t = i.description
        return t

# photopath
def select_photo(id_photo):
    with Session(engine) as session:
        statement = select(Photo).where(Photo.id == id_photo)
        res = session.exec(statement)
        for i in res:
            t = i.path
        return t

# =============================================================
def viewAppl(id_app):
    info = select_photo_for_apl(id_app)
    for key in info:
        des = "Требование к фото: " + select_description(key)
        print(des)
        print("Photo(now->photopath)")
        for j in info[key]:
            print(select_photo(j[1]))


def main():
    select_apl_for_client()
    select_apl_status()    
    select_inf_client()
    select_photo_for_apl(2)
    select_description(3)
    viewAppl(3)
if __name__ == "__main__":
    main()
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
import random
from faker import Faker
faker = Faker(['ru', 'en'])

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    role: str
    name: str
    login: str
    password: str
    email: str
    phone: str
    tg: str


class Req(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str


class Photo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    path: str


class PhReq(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    idreq: Optional[int] = Field(default=None, foreign_key="req.id")
    idph: Optional[int] = Field(default=None, foreign_key="photo.id")


class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: Optional[int] = Field(default=None, foreign_key="users.id")
    text: str
    status: str


class ApplEl(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    idap: Optional[int] = Field(default=None, foreign_key="application.id")
    phr: Optional[int] = Field(default=None, foreign_key="phreq.id")
    mark: Optional[str] = None


DB_url = "postgresql+psycopg2://postgres:password@localhost:5432/home_insurance" 

engine = create_engine(DB_url, echo=True)

def create_req():
    req1 = Req(description="общий вид участка: несколько ракурсов участка для определения расстояний между объектами страхования,\
               ограждением (забором), соседними сооружениями/зданиями, подъездными дорогами, объектами повышенного риска (стройка, водоемы и т.п.)")
    req2 = Req(description="наружные инженерные коммуникации и сооружения: электроснабжения, водоснабжения, водоотведения, \
               теплоснабжения, такие как: септик, эл.станция, трансформатор, распределительный щит, скважина, колодец, насос и т.п.")
    req3 = Req(description="фасады строений: каждое строение с 4-х сторон, элементы внешней отделки фасадов, кровлю, фундамент;")
    req4 = Req(description="механическую защиту окон и дверей: наружние жалюзи, решетки и т.п. крупным планом, окна снаружи при отсутствии защиты;")
    req5 = Req(description="входные (наружные) двери: с внешней стороны крупным планом;")
    req6 = Req(description="внутреннее инженерное оборудование: сантехника, электрика (внутридомовой электрощит \
               с автоматами в открытом виде), котел, бойлер, батареи, насос, камин,  кондиционер, емкости для топлива и/или воды и т.п. - крупным планом;")
    req7 = Req(description="пожарную сигнализацию - все элементы крупным планом;")
    req8 = Req(description="охранная сигнализация - все элементы крупным планом;")
    req9 = Req(description="внутреннюю отделку: общие планы каждого помещения (с двух противоположных сторон), необходимо отразить все элементы \
               внутренней отделки крупным планом: пол, потолок, стены, двери, встроенная мебель;")
    req10 = Req(description="оконный блок: если имеются различные типы окон, то элементы конструкций оконных блоков различных типов, \
                если все окна одинаковы – то достаточно фотографий 1-го оконного блока);")
    req11 = Req(description="дефекты и/или повреждения: имеющиеся дефекты и/или повреждения отделки и основных конструкций \
                (трещины подтеки, сколы, копоть, влага и т.п.) крупным планом;")
    req12 = Req(description="домашнее имущество в строениях: крупным планом каждый предмет, заявляемый на страхование;")
    req13 = Req(description="забор: \
                с каждой стороны участка забор должен быть снят с внутренней и внешней стороны (т.к. материал забора может быть разный), \
                отразить ширину и покрытие дорог, проходящих рядом с забором с каждой стороны участка,\
                отразить наличие/отсутствие искусственного рва между забором и дорогой.")
    

    with Session(engine) as session:
        session.add(req1)
        session.add(req2)
        session.add(req3)
        session.add(req4)
        session.add(req5)
        session.add(req6)
        session.add(req7)
        session.add(req8)
        session.add(req9)
        session.add(req10)
        session.add(req11)
        session.add(req12)  
        session.add(req13)
        session.commit()
  
        
def create_user():
    admin1 = Users(role="admin", name=faker.name(), login=faker.word(), password=faker.password(), email=faker.email(),
                   phone=faker.phone_number(), tg=faker.word())
    admin2 = Users(role="admin",name=faker.name(), login=faker.word(), password=faker.password(), email=faker.email(),
                   phone=faker.phone_number(), tg=faker.word())
    user1 = Users(role="client",name=faker.name(), login=faker.word(), password=faker.password(), email=faker.email(),
                   phone=faker.phone_number(), tg=faker.word())
    user2 = Users(role="client",name=faker.name(), login=faker.word(), password=faker.password(), email=faker.email(),
                   phone=faker.phone_number(), tg=faker.word())
    user3 = Users(role="client",name=faker.name(), login=faker.word(), password=faker.password(), email=faker.email(),
                   phone=faker.phone_number(), tg=faker.word())
    
    with Session(engine) as session:
        session.add(admin1)
        session.add(admin2)
        session.add(user1)
        session.add(user2)
        session.add(user3)
        session.commit()


def create_application():
    statuss = ['одобрена', 'отклонена', 'отправлена', 'на рассмотрении', 'на корректировке', ' подписан акт']
    apl1 = Application(user=3, text=faker.text(max_nb_chars=70), status=random.choice(statuss))
    apl2 = Application(user=4, text=faker.text(max_nb_chars=70), status=random.choice(statuss))
    apl3 = Application(user=4, text=faker.text(max_nb_chars=70), status=random.choice(statuss))
    apl4 = Application(user=5, text=faker.text(max_nb_chars=70), status=random.choice(statuss))
    
    with Session(engine) as session:
        session.add(apl1)
        session.add(apl2)
        session.add(apl3)
        session.add(apl4)
        session.commit()


def create_photo():
    ph1 = Photo(path=faker.file_path())
    ph2 = Photo(path=faker.file_path())    
    ph3 = Photo(path=faker.file_path())
    ph4 = Photo(path=faker.file_path())
    ph5 = Photo(path=faker.file_path())
    ph6 = Photo(path=faker.file_path())
    ph7 = Photo(path=faker.file_path())
    ph8 = Photo(path=faker.file_path())
    ph9 = Photo(path=faker.file_path())
    ph10 = Photo(path=faker.file_path())
    ph11 = Photo(path=faker.file_path())
    ph12 = Photo(path=faker.file_path())
    ph13 = Photo(path=faker.file_path())
    
    with Session(engine) as session:
        session.add(ph1)
        session.add(ph2)
        session.add(ph3)
        session.add(ph4)
        session.add(ph5)
        session.add(ph6)
        session.add(ph7)
        session.add(ph8)
        session.add(ph9)
        session.add(ph10)
        session.add(ph11)
        session.add(ph12)
        session.add(ph13)
        session.commit()
        

def create_phreq():
    with Session(engine) as session:
        session.add(PhReq(idreq=1,idph=1))
        session.add(PhReq(idreq=1,idph=2))
        session.add(PhReq(idreq=2,idph=3))
        session.add(PhReq(idreq=3,idph=4))
        session.add(PhReq(idreq=3,idph=5))
        session.add(PhReq(idreq=4,idph=6))
        session.add(PhReq(idreq=5,idph=7))
        session.add(PhReq(idreq=5,idph=8))
        session.add(PhReq(idreq=6,idph=9))
        session.add(PhReq(idreq=7,idph=10))
        session.add(PhReq(idreq=8,idph=11))
        session.add(PhReq(idreq=9,idph=12))
        session.add(PhReq(idreq=10,idph=13))
        session.commit()

    
def create_applel():
    marks = ['принято', 'отклонено']
    with Session(engine) as s:
        s.add(ApplEl(idap=1, phr=1, mark=random.choice(marks)))
        s.add(ApplEl(idap=1, phr=2, mark=random.choice(marks)))
        s.add(ApplEl(idap=1, phr=3, mark=random.choice(marks)))
        s.add(ApplEl(idap=2, phr=4, mark=random.choice(marks)))
        s.add(ApplEl(idap=3, phr=5, mark=random.choice(marks)))
        s.add(ApplEl(idap=2, phr=6, mark=random.choice(marks)))
        s.add(ApplEl(idap=2, phr=7, mark=random.choice(marks)))
        s.add(ApplEl(idap=4, phr=8, mark=random.choice(marks)))
        s.add(ApplEl(idap=3, phr=9, mark=random.choice(marks)))
        s.add(ApplEl(idap=4, phr=10, mark=random.choice(marks)))
        s.add(ApplEl(idap=4, phr=11, mark=random.choice(marks)))
        s.add(ApplEl(idap=1, phr=12, mark=random.choice(marks)))
        s.add(ApplEl(idap=2, phr=13, mark=random.choice(marks)))
        s.commit() 

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()
    create_req()
    create_user()
    create_application()
    create_photo()
    create_phreq()
    create_applel()
    
if __name__ == "__main__":
    main()

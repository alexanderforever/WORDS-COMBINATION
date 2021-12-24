from app import *



class Ztable(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    word= db.Column(db.String(64),nullable=False)
    __tablename__='ztable'
    def __init__(self,word):
        self.word=word

    @classmethod
    def create(cls):
        cls.__table__.create(engine)
    
    @classmethod
    def remove(cls):
        cls.__table__.drop(engine)
        
    def __repr__(self):
        return '<Z {}>'.format(self.id)



db.create_all()
Ztable.remove()
Ztable.create()
for item in ['a','b','#']:
    b=Ztable(item)
    db.session.add(b)
    db.session.commit()

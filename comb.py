from Model import Ztable as Z
from app import *

@login_manager.user_loader
def load_user(user_id):
    return A.query.get(user_id)

B=[a for a in Z.query.all()]
def comb():
    while True:
        count=Z.query.count()
        for i in range(1,count+1):
            w1=Z.query.filter_by(id=i).first()
            for w2 in B:
                if Z.query.filter_by(word=w1.word+w2.word).first():
                    pass
                else:
                    print(w1.word+w2.word)
                    z1=Z(w1.word +w2.word)
                    db.session.add(z1)
                    db.session.commit()
       
        

a=comb() 

admin.add_view(ModelView(Z, db.session))


# app.run(debug=True)
        
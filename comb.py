from Model import Ztable as Z
from app import *


def comb(passwordsizeEstimate):
    B=[a for a in Z.query.all()]

    passwordminlen=0 #a=eeeee,b=2 =>min length=6 consider ab
    for item in Z.query.all():
        passwordminlen+=len(item.word)
    
    if passwordsizeEstimate<passwordminlen:
        print("Sorry! try again")
        return 0
    while True:
        count=Z.query.count()
        for i in range(1,count+1):
            w1=Z.query.filter_by(id=i).first()
            for w2 in B:
                if Z.query.filter_by(word=w1.word+w2.word).first():
                    pass
                else:
                    password=w1.word+w2.word
                    if len(password)>passwordsizeEstimate:
                        print("WE ARE DONE :)")
                        return 0
                    print(password)
                    z1=Z(password)
                    db.session.add(z1)
                    db.session.commit()
       
        

a=comb(4) 

# admin.add_view(ModelView(Z, db.session))


# app.run(debug=True)
        

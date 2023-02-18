import os
from deta import Deta








DETA_KEY = "c0zww4by_rWk3mYtpe6b9sQsCquTfxBY2WsE73RZA"




deta = Deta(DETA_KEY)


db1 = deta.Base("Prostate Cancer Prediction")

def insert_period(radius,texture,perimeter,area,smoothness, prostate_diagnosis):
    """Returns the report onasuccessful creation,otherwise raises an error"""
    return db1.put({"radius":radius,"texture":texture,"perimeter":perimeter,"area":area,"smoothness":smoothness,"result": prostate_diagnosis})

# encoding=utf-8
from sklearn.externals import joblib
from PIL import Image
import numpy as np
def predict():
    photo_path='./cache/yzm-{}.png'
    X = []
    for i in range(1,5):
        img = Image.open(photo_path.format(i))
        ls = np.array(img).tostring()
        ls=np.fromstring(ls,dtype=bool)
        X.append(ls)
    file_path = './model/knn.pkl'
    knn=joblib.load(file_path)
    ls=knn.predict(X)
    return "".join(ls)

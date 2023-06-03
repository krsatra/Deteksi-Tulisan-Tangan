from sklearn.neighbors import KNeighborsClassifier 
from PIL import Image
import os
import numpy as np

def load_dataset():
    HurufA = []
    HurufB = []
    HurufC = []
    HurufD = []
    HurufE = []
    HurufF = []
    HurufG = []
    HurufH = []
    HurufI = []
    HurufJ = []
    HurufK = []
    HurufL = []
    HurufM = []
    HurufN = []
    HurufO = []
    HurufP = []
    HurufQ = []
    HurufR = []
    HurufS = []
    HurufT = []
    HurufU = []
    HurufV = []
    HurufW = []
    HurufX = []
    HurufY = []
    HurufZ = []

    for file in os.listdir("HurufA"):
        img = Image.open("HurufA/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufA.append(img)
    
    for file in os.listdir("HurufB"):
        img = Image.open("HurufB/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufB.append(img)

    for file in os.listdir("HurufC"):
        img = Image.open("HurufC/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufC.append(img)
    for file in os.listdir("HurufD"):
        img = Image.open("HurufD/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufD.append(img)
    for file in os.listdir("HurufE"):
        img = Image.open("HurufE/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufE.append(img)
    for file in os.listdir("HurufF"):
        img = Image.open("HurufF/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufF.append(img)
    for file in os.listdir("HurufG"):
        img = Image.open("HurufG/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufG.append(img)
    for file in os.listdir("HurufH"):
        img = Image.open("HurufH/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufH.append(img)
    for file in os.listdir("HurufI"):
        img = Image.open("HurufI/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufI.append(img)
    for file in os.listdir("HurufJ"):
        img = Image.open("HurufJ/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufJ.append(img)
    for file in os.listdir("HurufK"):
        img = Image.open("HurufK/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufK.append(img)
    for file in os.listdir("HurufL"):
        img = Image.open("HurufL/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufL.append(img)
    for file in os.listdir("HurufM"):
        img = Image.open("HurufM/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufM.append(img)
    for file in os.listdir("HurufN"):
        img = Image.open("HurufN/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufN.append(img)
    for file in os.listdir("HurufO"):
        img = Image.open("HurufO/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufO.append(img)
    for file in os.listdir("HurufP"):
        img = Image.open("HurufP/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufP.append(img)
    for file in os.listdir("HurufQ"):
        img = Image.open("HurufQ/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufQ.append(img)
    for file in os.listdir("HurufR"):
        img = Image.open("HurufR/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufR.append(img)
    for file in os.listdir("HurufS"):
        img = Image.open("HurufS/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufS.append(img)
    for file in os.listdir("HurufT"):
        img = Image.open("HurufT/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufT.append(img)
    for file in os.listdir("HurufU"):
        img = Image.open("HurufU/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufU.append(img)
    for file in os.listdir("HurufV"):
        img = Image.open("HurufV/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufV.append(img)
    for file in os.listdir("HurufW"):
        img = Image.open("HurufW/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufW.append(img)
    for file in os.listdir("HurufX"):
        img = Image.open("HurufX/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufX.append(img)
    for file in os.listdir("HurufY"):
        img = Image.open("HurufY/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufY.append(img)
    for file in os.listdir("HurufZ"):
        img = Image.open("HurufZ/" + file)
        img = np.array(img)
        img = img.flatten()
        HurufZ.append(img)

    return HurufA, HurufB, HurufC, HurufD, HurufE, HurufF, HurufG, HurufH, HurufI, HurufJ, HurufK, HurufL, HurufM, HurufN, HurufO, HurufP, HurufQ, HurufR, HurufS, HurufT, HurufU, HurufV, HurufW, HurufX, HurufY, HurufZ

def load_ai():
    model = KNeighborsClassifier(n_neighbors = 5)
    print("[INFO] Loading Dataset")
    HurufA, HurufB, HurufC, HurufD, HurufE, HurufF, HurufG, HurufH, HurufI, HurufJ, HurufK, HurufL, HurufM, HurufN, HurufO, HurufP, HurufQ, HurufR, HurufS, HurufT, HurufU, HurufV, HurufW, HurufX, HurufY, HurufZ = load_dataset()
    print("[INFO] Loading Model")
    y_HurufA = np.zeros(len(HurufA))
    y_HurufB = np.ones(len(HurufB))
    y_HurufC = np.ones(len(HurufC)) * 2
    y_HurufD = np.ones(len(HurufD)) * 3
    y_HurufE = np.ones(len(HurufE)) * 4
    y_HurufF = np.ones(len(HurufF)) * 5
    y_HurufG = np.ones(len(HurufG)) * 6
    y_HurufH = np.ones(len(HurufH)) * 7
    y_HurufI = np.ones(len(HurufI)) * 8
    y_HurufJ = np.ones(len(HurufJ)) * 9
    y_HurufK = np.ones(len(HurufK)) * 10
    y_HurufL = np.ones(len(HurufL)) * 11
    y_HurufM = np.ones(len(HurufM)) * 12
    y_HurufN = np.ones(len(HurufN)) * 13
    y_HurufO = np.ones(len(HurufO)) * 14
    y_HurufP = np.ones(len(HurufP)) * 15
    y_HurufQ = np.ones(len(HurufQ)) * 16
    y_HurufR = np.ones(len(HurufR)) * 17
    y_HurufS = np.ones(len(HurufS)) * 18
    y_HurufT = np.ones(len(HurufT)) * 19
    y_HurufU = np.ones(len(HurufU)) * 20
    y_HurufV = np.ones(len(HurufV)) * 21
    y_HurufW = np.ones(len(HurufW)) * 22
    y_HurufX = np.ones(len(HurufX)) * 23
    y_HurufY = np.ones(len(HurufY)) * 24
    y_HurufZ = np.ones(len(HurufZ)) * 25
    X = HurufA + HurufB + HurufC + HurufD + HurufE + HurufF + HurufG + HurufH + HurufI + HurufJ + HurufK + HurufL + HurufM + HurufN + HurufO + HurufP + HurufQ + HurufR + HurufS + HurufT + HurufU + HurufV + HurufW + HurufX + HurufY + HurufZ
    y = np.concatenate([y_HurufA, y_HurufB, y_HurufC, y_HurufD, y_HurufE, y_HurufF, y_HurufG, y_HurufH, y_HurufI, y_HurufJ, y_HurufK, y_HurufL, y_HurufM, y_HurufN, y_HurufO, y_HurufP, y_HurufQ, y_HurufR, y_HurufS, y_HurufT, y_HurufU, y_HurufV, y_HurufW, y_HurufX, y_HurufY, y_HurufZ])
    model.fit(X, y)
    return model
import tkinter as tk


from scipy.stats.stats import power_divergence
import AI
import numpy as np
from PIL import Image, ImageTk, ImageDraw

model = AI.load_ai()

window = tk.Tk()

# Background
img = Image.new(mode = "1", size = (500,500), color = 0)
tkimage = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image = tkimage)
canvas.pack()

# Membuat Kuas
draw = ImageDraw.Draw(img)
last_point = (0,0)
prediction = tk.StringVar()
label = tk.Label(window, textvariable=prediction)

def draw_image(event):
    global last_point, tkimage
    current_point = (event.x, event.y)
    draw.line([last_point, current_point], fill = 255, width= 50)
    last_point = current_point
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()
    img_temp = img.resize((28,28))
    img_temp = np.array(img_temp)
    img_temp = img_temp.flatten()
    output = model.predict([img_temp])
    if(output[0] == 0):
       prediction.set("A")
    elif(output[0] == 1):
        prediction.set("B")
    elif(output[0] == 2):
        prediction.set("C")
    elif(output[0] == 3):
       prediction.set("D")
    elif(output[0] == 4):
       prediction.set("E")
    elif(output[0] == 5):
       prediction.set("F")
    elif(output[0] == 6):
       prediction.set("G")
    elif(output[0] == 7):
       prediction.set("H")
    elif(output[0] == 8):
       prediction.set("I")
    elif(output[0] == 9):
       prediction.set("J")
    elif(output[0] == 10):
       prediction.set("K")
    elif(output[0] == 11):
       prediction.set("L")
    elif(output[0] == 12):
       prediction.set("M")
    elif(output[0] == 13):
       prediction.set("N")
    elif(output[0] == 14):
       prediction.set("O")
    elif(output[0] == 15):
       prediction.set("P")
    elif(output[0] == 16):
       prediction.set("Q")
    elif(output[0] == 17):
       prediction.set("R")
    elif(output[0] == 18):
       prediction.set("S")
    elif(output[0] == 19):
       prediction.set("T")
    elif(output[0] == 20):
       prediction.set("U")
    elif(output[0] == 21):
       prediction.set("V")
    elif(output[0] == 22):
       prediction.set("W")
    elif(output[0] == 23):
       prediction.set("X")
    elif(output[0] == 24):
       prediction.set("Y")
    elif(output[0] == 25):
       prediction.set("Z")
    label.pack()

# Membuat gambar
def start_draw(event):
    global last_point
    last_point = (event.x, event.y)

# Menghapus gambar
def reset_canvas(event):
    global tkimage, img, draw
    img = Image.new(mode = "1", size = (500,500), color = 0)
    draw = ImageDraw.Draw(img)
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()

HurufA = 0
HurufB = 0
HurufC = 0
HurufD = 0
HurufE = 0
HurufF = 0
HurufG = 0
HurufH = 0
HurufI = 0
HurufJ = 0
HurufK = 0
HurufL = 0
HurufM = 0
HurufN = 0
HurufO = 0
HurufP = 0
HurufQ = 0
HurufR = 0
HurufS = 0
HurufT = 0
HurufU = 0
HurufV = 0
HurufW = 0
HurufX = 0
HurufY = 0
HurufZ = 0

def save_image(event):
    global HurufA, HurufB, HurufC, HurufD, HurufE, HurufF, HurufG, HurufH, HurufI, HurufJ, HurufK, HurufL, HurufM, HurufN, HurufO, HurufP, HurufQ, HurufR, HurufS, HurufT, HurufU, HurufV, HurufW, HurufX, HurufY, HurufZ
    img_temp = img.resize((28,28))
    if (event.char == "a"):
        img_temp.save(f"HurufA/{HurufA}.png")
        HurufA += 1
    elif(event.char == "b"):
        img_temp.save(f"HurufB/{HurufB}.png")
        HurufB += 1
    elif(event.char == "c"):
        img_temp.save(f"HurufC/{HurufC}.png")
        HurufC += 1
    elif(event.char == "d"):
       img_temp.save(f"HurufD/{HurufD}.png")
       HurufD += 1
    elif(event.char == "e"):
       img_temp.save(f"HurufE/{HurufE}.png")
       HurufE += 1
    elif(event.char == "f"):
       img_temp.save(f"HurufF/{HurufF}.png")
       HurufF += 1
    elif(event.char == "g"):
       img_temp.save(f"HurufG/{HurufG}.png")
       HurufG += 1
    elif(event.char == "h"):
       img_temp.save(f"HurufH/{HurufH}.png")
       HurufH += 1
    elif(event.char == "i"):
       img_temp.save(f"HurufI/{HurufI}.png")
       HurufI += 1
    elif(event.char == "j"):
       img_temp.save(f"HurufJ/{HurufJ}.png")
       HurufJ += 1
    elif(event.char == "k"):
       img_temp.save(f"HurufK/{HurufK}.png")
       HurufK += 1
    elif(event.char == "l"):
       img_temp.save(f"HurufL/{HurufL}.png")
       HurufL += 1
    elif(event.char == "m"):
       img_temp.save(f"HurufM/{HurufM}.png")
       HurufM += 1
    elif(event.char == "n"):
       img_temp.save(f"HurufN/{HurufN}.png")
       HurufN += 1
    elif(event.char == "o"):
       img_temp.save(f"HurufO/{HurufO}.png")
       HurufO += 1
    elif(event.char == "p"):
       img_temp.save(f"HurufP/{HurufP}.png")
       HurufP += 1
    elif(event.char == "q"):
       img_temp.save(f"HurufQ/{HurufQ}.png")
       HurufQ += 1
    elif(event.char == "r"):
       img_temp.save(f"HurufR/{HurufR}.png")
       HurufR += 1
    elif(event.char == "s"):
       img_temp.save(f"HurufS/{HurufS}.png")
       HurufS += 1
    elif(event.char == "t"):
       img_temp.save(f"HurufT/{HurufT}.png")
       HurufT += 1
    elif(event.char == "u"):
       img_temp.save(f"HurufU/{HurufU}.png")
       HurufU += 1
    elif(event.char == "v"):
       img_temp.save(f"HurufV/{HurufV}.png")
       HurufV += 1
    elif(event.char == "w"):
       img_temp.save(f"HurufW/{HurufW}.png")
       HurufW += 1
    elif(event.char == "x"):
       img_temp.save(f"HurufX/{HurufX}.png")
       HurufX += 1
    elif(event.char == "y"):
       img_temp.save(f"HurufY/{HurufY}.png")
       HurufY += 1
    elif(event.char == "z"):
       img_temp.save(f"HurufZ/{HurufZ}.png")
       HurufZ += 1

window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", reset_canvas)
window.bind("<Key>", save_image)

window.mainloop()
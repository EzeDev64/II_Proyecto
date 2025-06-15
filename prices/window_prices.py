from tkinter import *
import json_read, API_conection,datetime

window = Tk()
window.minsize(500,500)

fecha = datetime.date.today()
cambio = API_conection.get_convertion(fecha.day,fecha.month,fecha.year)
print(datetime.date.today())
#prize = 1/puntaje ∗ 100∗ CambioDolar

lbl_title = Label(text="Prices")
lbl_title.pack()
json_data = json_read.read_file()
txt= ""
for i in range(0,5):
    print(isinstance(cambio,tuple))
    prize = 1/int(json_data["val"+str(i+1)]) * 100 * float(cambio)
    txt += "Top "+str(i+1)+f": {'%2.f' % prize} $" + "\n"

txt_hall = Label(text=txt, bg="black", fg="white")
txt_hall.pack(expand=True)

btn_return = Button(text="Return")
btn_return.pack(side=BOTTOM)

window.mainloop()

import tkinter
from tkinter.ttk import *
from tkinter import *
import time
def execute():
    global var_1
    var_2=combo.get()
    var_3=combo1.get()
    var_3=int(var_3)
    var_4=var.get()
    var_5=var1.get()
    var_6=combo5.get()
    var_6=var_6.lower()
    var_10=combo4.get()
    var_10=int(var_10)
    flag_fly_ash_used=int_var.get()
    var_7=int(var_2[1])*10+int(var_2[2])

    if (var_7==15):
        water_cement_ratio=0.6
    elif(var_7==20):
        if(var_6=='very severe'):
            water_cement_ratio=0.45
        elif(var_6=='severe'):
            water_cement_ratio=0.5
        else:
            water_cement_ratio=0.55
    elif(var_7==25):
        if(var_6=='extreme'):
            water_cement_ratio=0.4
        else:
            water_cement_ratio=0.5
    elif(var_7==30):
        water_cement_ratio=0.45
    elif(var_7==35):
        water_cement_ratio=0.45
    elif(var_7==40):
        water_cement_ratio=0.4
    if(var_3==10):
        var_9=208
    elif(var_3==20):
        var_9=186
    elif(var_3==40):
        var_9=165
    if(var_3==10):
        if (var_10==4):
            var_1=0.5
        elif(var_10==3):
            var_1=0.48
        elif(var_10==2):
            var_1=0.46
        elif(var_10==1):
            var_1=0.44
    elif(var_3==20):
        if (var_10==4):
            var_1=0.66
        elif(var_10==3):
            var_1=0.64
        elif(var_10==2):
            var_1=0.62
        elif(var_10==1):
            var_1=0.60
    elif(var_3==40):
        if (var_10==4):
            var_1=0.75
        elif(var_10==3):
            var_1=0.73
        elif(var_10==2):
            var_1=0.71
        elif(var_10==1):
            var_1=0.69
    if (var_4>=75):
      for _ in range(0,int((var_4-50)/25)):
          var_9=1.03*var_9
      var_12=((var_4-50))%25
      var_9=var_9+(var_12*.03*var_9)
    mass_of_water=(var_9*(100-var_5))/100
    temp_water_cem_ratio=float(mass_of_water)/float(water_cement_ratio)
    if (flag_fly_ash_used==1):
        mass_of_cement=temp_water_cem_ratio*.7
        mass_of_fly_ash_used=temp_water_cem_ratio*.3

    else:
        mass_of_cement=temp_water_cem_ratio
        mass_of_fly_ash_used=0
    water_cement_ratio=mass_of_water/mass_of_cement
    p=((.5-water_cement_ratio)/5)+var_1
    s=p*0.9
    t=1-s
    u=mass_of_cement/3150
    v=mass_of_water/1000
    w=(.02*mass_of_cement)/1450
    xx=mass_of_fly_ash_used/2200
    x=1-w-v-u-xx
    mass_of_coarse_aggregate=2740*s*x
    mass_of_fine_aggregate=2740*t*x
    print("Mass of water to be used:",round(mass_of_water,2),"kg")
    print("Mass of Cement to be used:",round(mass_of_cement,2),"kg")
    print("Mass of Admixture to be used: ",round(.02*mass_of_cement,2),"kg")
    print("Mass of Coarse Aggregate to be used:",round(mass_of_coarse_aggregate,2),"kg")
    print("Mass of Fine Aggregate to be used:",round(mass_of_fine_aggregate,2),"kg")
    print("Mass of Fly ash to be used:",round(mass_of_fly_ash_used,2),"kg")
    print("Water cement ratio",round(water_cement_ratio,2))


window=tkinter.Tk()
#rename the title of the window
window.title("Mix Design")

label=tkinter.Label(window,text="Please enter the details to find the Mix Design Proportion: ")
label.config(font=('Courier', 20))
label1=tkinter.Label(window,text="Grade to be used: ")
label1.config(font=('Courier', 15))
label2=tkinter.Label(window,text="Nominal Size of Aggregate:")
label2.config(font=('Courier', 15))
combo1= Combobox(window,state="readonly")
combo1['values']=(10,20,40)
combo1.current(1)
combo= Combobox(window,state="readonly")
combo['values']=('M15','M20','M25','M30','M35','M40')
combo.current(1)
label3=tkinter.Label(window,text="Want to use Flyash? Default=No")
label3.config(font=('Courier', 15))
int_var=IntVar()
rad2=Radiobutton(window,text='Yes',value=1,variable=int_var)
var = IntVar()
scale = Scale( window, variable = var, from_=20, to=200, orient=HORIZONTAL )
label4=tkinter.Label(window,text="Slump to be used:")
label4.config(font=('Courier', 15))
var1=IntVar()
scale1 = Scale( window, variable = var1, from_=0, to=100, orient=HORIZONTAL )
label5=tkinter.Label(window,text="Percentage Reduction By Plasticizers:")
label5.config(font=('Courier', 15))
label6=tkinter.Label(window,text="Select Zone: ")
label6.config(font=('Courier', 15))
combo4= Combobox(window,state="readonly")
combo4['values']=(1,2,3,4)
combo4.current(3)
label7=tkinter.Label(window,text="Weather Condition ")
label7.config(font=('Courier', 15))
combo5= Combobox(window,state="readonly")
combo5['values']=('Mild','Moderate','Severe','Very Severe','Extreme')
combo5.current(1)
btn=Button(window, text='Execute',command=execute)
label.pack()
label1.pack()
combo.pack()
label2.pack()
combo1.pack()
label3.pack()
rad2.pack()
label4.pack()
scale.pack(anchor=CENTER)
label5.pack()
scale1.pack()
label6.pack()
combo4.pack()
label7.pack()
combo5.pack()
btn.pack()
window.mainloop()

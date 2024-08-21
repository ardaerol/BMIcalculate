import tkinter

#Windows
window = tkinter.Tk()
window.title("BMI Calculate")
window.minsize(width=200,height=200)
window.config(bg="white")
#Windows

#fonks
def calculate_BMI():
    weight = weight_input.get()
    height = height_input.get()
    if weight == "" or height=="":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string2 = write_result(bmi)
            result_label.config(text=result_string2)
        except:
            result_label.config(text="Enter a valid number!")

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string


#UI
weight_label = tkinter.Label(text="Enter your weight (Kg)")
weight_label.config(bg="white",fg="black")
weight_label.pack()

weight_input = tkinter.Entry(width=10,bg="white",fg="black")
weight_input.pack()


height_label = tkinter.Label(text="Enter your height (Cm)")
height_label.config(bg="white",fg="black")
height_label.pack()

height_input = tkinter.Entry(width=10,bg="white",fg="black")
height_input.pack()


my_button = tkinter.Button(text="calculate",width=10,command=calculate_BMI)
my_button.pack()

result_label = tkinter.Label(bg="white",fg="black")
result_label.pack()
#UI




window.mainloop()
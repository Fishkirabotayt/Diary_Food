import PySimpleGUI as sg
sg.theme("DarkBlue9")
file = open("food.txt", "r", encoding="utf-8")
act = file.readlines()
label = sg.Text("Питание", font=("Times New Roman", 30), text_color="Red")
label2 = sg.Text("Время", font=("Times New Roman", 30), text_color="Black")
label3 = sg.Text("Количество каллорий", font=("Times New Roman", 30), text_color="Green")
label4 = sg.Text("Часы",font=("Times New Roman", 25), text_color="Blue")
label5 = sg.Text("Минуты", font=("Times New Roman", 25), text_color="Blue")
listbox = sg.Listbox(values=act, key="foods", size=(100,10), font=("Times New Roman", 15))
combo_time = sg.Combo(values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], default_value='08', key="time",font=("Times New Roman", 20))
combo_time2 = sg.Combo(values=['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55'], default_value='00', key="time2", font=("Times New Roman", 20))
amount_of_kkalory = sg.InputText(key="kkal", font=("Times New Roman", 30))
button = sg.Button("Добавить", font=("Times New Roman", 20), button_color="Pink on")
button2 = sg.Button("Удалить", font=("Times New Roman", 20), button_color="#A0A0A0 on")
window = sg.Window("Приложение о питании",
                   layout=[[label],
                           [listbox],
                           [label2],
                           [label4, label5],
                           [combo_time, combo_time2],
                           [label3],
                           [amount_of_kkalory],
                           [button, button2]], size=(600,620))

while True:
    event, values = window.read(timeout=10)

    match event:
        case "Добавить":
            hour_of_food = values["time"]
            minute_of_food = values["time2"]
            kkal = values["kkal"]
            result = hour_of_food + ":" + minute_of_food + "-" + kkal + " каллории"
            act.append(result)
            file = open("food.txt", "a", encoding="utf-8")
            file.write(result + "\n")
            file.close()
            listbox.update(values=act)
        case "Удалить":
            try:
                enter_food = values["foods"][0]
                act.remove(enter_food)
                file = open("food.txt", "w", encoding="utf-8")
                file.writelines(act)
                file.close()
                listbox.update(values=act)
            except IndexError:
                print("Вы нажали на кнопку удалить не записав информацию")

        case sg.WIN_CLOSED:
            break

window.close()
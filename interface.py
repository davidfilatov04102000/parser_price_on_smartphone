from smartphones import smartphone_list
from main_Class import MainObject
import customtkinter
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

global_info_list = []
global_info_list_2 = []
global_full_list_non_clear_price = []

def get_val():
    local_list = []
    gt1, gt2, gt3, gt4 = vid1_1.get_value(), vid2_1.get_value(), vid3_1.get_value(), vid4_1.get_value()
    local_list.append(gt1[0]), local_list.append(gt1[1]), local_list.append(gt1[2]), local_list.append(gt1[3])
    local_list.append(gt1[4]), local_list.append(gt1[5]), local_list.append(gt1[6]), local_list.append(gt1[7])
    local_list.append(gt1[8]), local_list.append(gt1[9]), local_list.append(gt2[0]), local_list.append(gt2[1])
    local_list.append(gt2[2]), local_list.append(gt2[3]), local_list.append(gt2[4]), local_list.append(gt2[5])
    local_list.append(gt2[6]), local_list.append(gt2[7]), local_list.append(gt2[8]), local_list.append(gt2[9])
    local_list.append(gt3[0]), local_list.append(gt3[1]), local_list.append(gt3[2]), local_list.append(gt3[3])
    local_list.append(gt3[4]), local_list.append(gt3[5]), local_list.append(gt3[6]), local_list.append(gt3[7])
    local_list.append(gt3[8]), local_list.append(gt3[9]), local_list.append(gt4[0]), local_list.append(gt4[1])
    local_list.append(gt4[2]), local_list.append(gt4[3]), local_list.append(gt4[4]), local_list.append(gt4[5])
    local_list.append(gt4[6]), local_list.append(gt4[7]), local_list.append(gt4[8]), local_list.append(gt4[9])
    import trying
    fin_info = trying.main_func(local_list)
    global global_info_list
    global_info_list = fin_info.copy()
    distance_y = 0.10
    for sr in fin_info:
        res = str(sr)
        distance_y += 0.05
        fin_info_lbl = customtkinter.CTkLabel(info_job_place, text=res, font=("Arial Bold", 18))
        fin_info_lbl.place(relx=0.03, rely=distance_y)


def get_val_2():
    local_list_2 = []
    gt1, gt2, gt3, gt4 = vid1_1.get_value(), vid2_1.get_value(), vid3_1.get_value(), vid4_1.get_value()
    local_list_2.append(gt1[0]), local_list_2.append(gt1[1]), local_list_2.append(gt1[2]), local_list_2.append(gt1[3])
    local_list_2.append(gt1[4]), local_list_2.append(gt1[5]), local_list_2.append(gt1[6]), local_list_2.append(gt1[7])
    local_list_2.append(gt1[8]), local_list_2.append(gt1[9]), local_list_2.append(gt2[0]), local_list_2.append(gt2[1])
    local_list_2.append(gt2[2]), local_list_2.append(gt2[3]), local_list_2.append(gt2[4]), local_list_2.append(gt2[5])
    local_list_2.append(gt2[6]), local_list_2.append(gt2[7]), local_list_2.append(gt2[8]), local_list_2.append(gt2[9])
    local_list_2.append(gt3[0]), local_list_2.append(gt3[1]), local_list_2.append(gt3[2]), local_list_2.append(gt3[3])
    local_list_2.append(gt3[4]), local_list_2.append(gt3[5]), local_list_2.append(gt3[6]), local_list_2.append(gt3[7])
    local_list_2.append(gt3[8]), local_list_2.append(gt3[9]), local_list_2.append(gt4[0]), local_list_2.append(gt4[1])
    local_list_2.append(gt4[2]), local_list_2.append(gt4[3]), local_list_2.append(gt4[4]), local_list_2.append(gt4[5])
    local_list_2.append(gt4[6]), local_list_2.append(gt4[7]), local_list_2.append(gt4[8]), local_list_2.append(gt4[9])
    import work_func_2
    info_list_for_bot = work_func_2.main_func_2(local_list_2)
    global global_info_list_2
    global_info_list_2 = info_list_for_bot.copy()
    send_teleg_2()


def output_in_program():
    shet = 0
    print("функция вывода активирована")
    # for ver in global_full_list_non_clear_price:
    #     shet += 1
    #     unravel = ver.split(", ")
    #     obj = customtkinter.CTkLabel(info_job_place_2, text=unravel[0])
    #     obj.grid(row=shet, column=1)
    #     obj_2 = customtkinter.CTkLabel(info_job_place_2, text=unravel[1])
    #     obj_2.grid(row=shet, column=2)
    #     obj_3 = customtkinter.CTkLabel(info_job_place_2, text=unravel[2])
    #     obj_3.grid(row=shet, column=3)
    # jfg = customtkinter.CTkLabel(info_job_place_2, text="Приветики")
    # jfg.place(relx=0.10, rely=0.35)


def send_teleg_2():
    local_list_for_output_bot = global_info_list_2.copy()
    one_val = ""
    list_not_clear_price = []
    bot = Bot("5688586160:AAEbospQ4PrVcLvwaKf9EeqC7FJsS86YGEs")

    dp = Dispatcher(bot)

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Верно")).insert(KeyboardButton("Не верно"))

    @dp.message_handler(commands=["start"])
    async def start_send_message(message: types.Message):
        print("декоратор с функцией работает")
        await bot.send_message(chat_id=message.from_user.id, text=f"<b>{local_list_for_output_bot[0]}</b>", reply_markup=kb,
                               parse_mode="html")
        nonlocal one_val
        one_val = local_list_for_output_bot[0]
        local_list_for_output_bot.pop(0)

    @dp.message_handler(content_types=["text"])
    async def main_work(message: types.Message):
        nonlocal one_val
        if len(local_list_for_output_bot) == 0:
            await bot.send_message(chat_id=message.from_user.id, text="Проверка завершена, список моделей цены на "
                                                                      "которые нужно поменять")
            for gty in list_not_clear_price:
                await bot.send_message(chat_id=message.from_user.id, text=f"<b>{gty}</b>", parse_mode="html")

        elif message.text == "Верно":
            await bot.send_message(chat_id=message.from_user.id, text=f"<b>{local_list_for_output_bot[0]}</b>",
                                   reply_markup=kb, parse_mode="html")

            one_val = local_list_for_output_bot[0]
            local_list_for_output_bot.pop(0)
        elif message.text == "Не верно":

            one_val = one_val
            list_not_clear_price.append(one_val)
            await bot.send_message(chat_id=message.from_user.id, text=f"<b>{local_list_for_output_bot[0]}</b>",
                                   reply_markup=kb, parse_mode="html")
            one_val = local_list_for_output_bot[0]
            local_list_for_output_bot.pop(0)

    if __name__ == "__main__":
        executor.start_polling(dp)




# def send_teleg():
#     bot = Bot("5688586160:AAEbospQ4PrVcLvwaKf9EeqC7FJsS86YGEs")
#
#     dp = Dispatcher(bot)
#
#     # kb = ReplyKeyboardMarkup(resize_keyboard=True)
#     # clot = KeyboardButton("start")
#     # kb.add(clot)
#
#     @dp.message_handler(commands=["start"])
#     async def send_message(message: types.message_id):
#         await message.reply(text="Устройства на которые изменилась цена:")
#         for g in global_info_list:
#             await bot.send_message(chat_id=2130259987, text=g)
#
#     if __name__ == "__main__":
#         executor.start_polling(dp)


memory_place_model = []
pust_list = []
index_for_drive = 0

pr = open("place_models.txt", "r")
for line in pr:
    memory_place_model.append(line[:-1])

pr.close()

print(memory_place_model)

var_smartphone_model = []

if memory_place_model == pust_list:
    var_smartphone_model = smartphone_list.copy()
else:
    var_smartphone_model = memory_place_model.copy()


win = customtkinter.CTk(fg_color="#FAEBD7")
win.title("Inspect Price")
win.geometry("1700x900")
win.resizable(False, False)

rely_fr_frame = 0.09
color1 = "#FFA07A"


def rely_distance(distance=0.19):
    global rely_fr_frame
    rely_fr_frame += distance
    global index_for_drive
    index_for_drive += 10


label_1 = customtkinter.CTkLabel(win, text="Первая витрина от ресепшена")
label_1.place(relx=0.01, rely=rely_fr_frame - 0.025)
vid1_1 = MainObject(win, rely_fr_frame, color_frame=color1, smartphone_model=var_smartphone_model,
                    smart_list=smartphone_list, index=index_for_drive)

rely_distance()

label_2 = customtkinter.CTkLabel(win, text="Вторая витрина от ресепшена")
label_2.place(relx=0.01, rely=rely_fr_frame - 0.025)
vid2_1 = MainObject(win, rely_fr_frame, color_frame=color1, smartphone_model=var_smartphone_model,
                    smart_list=smartphone_list, index=index_for_drive)

rely_distance()

label_3 = customtkinter.CTkLabel(win, text="Третья витрина от ресепшена")
label_3.place(relx=0.01, rely=rely_fr_frame - 0.025)
vid3_1 = MainObject(win, rely_fr_frame, color_frame=color1, smartphone_model=var_smartphone_model,
                    smart_list=smartphone_list, index=index_for_drive)

rely_distance()

label_3 = customtkinter.CTkLabel(win, text="Четвертая витрина от ресепшена")
label_3.place(relx=0.01, rely=rely_fr_frame - 0.025)
vid4_1 = MainObject(win, rely_fr_frame, color_frame=color1, smartphone_model=var_smartphone_model,
                    smart_list=smartphone_list, index=index_for_drive)


info_job_place = customtkinter.CTkTabview(win, width=495, height=870, corner_radius=15, fg_color="#FFDEAD")
info_job_place.place(relx=0.70, rely=0.01)

frame_for_info_str = customtkinter.CTkTabview(info_job_place, width=470, height=100, corner_radius=10, fg_color="#E6E6FA")
frame_for_info_str.place(relx=0.025, rely=0.03)

info_label = customtkinter.CTkLabel(frame_for_info_str, text="Устройства на которые изменилась цена:", font=("Arial Bold", 20))
info_label.place(relx=0.08, rely=0.30)

model_lbl = customtkinter.CTkLabel(frame_for_info_str, text="Модели   -   Цена 12   -   Цена 24       -       Кол-во:", font=("Arial Bold", 18))
model_lbl.place(relx=0.07, rely=0.60)

info_job_place_2 = customtkinter.CTkTabview(info_job_place, width=470, height=650, corner_radius=10, fg_color="#E6E6FA")
info_job_place_2.place(relx=0.025, rely=0.16)

# textbox = customtkinter.CTkTextbox(info_job_place, width=470, height=650, corner_radius=10, fg_color="#E6E6FA")
# textbox.place(relx=0.025, rely=0.16)

send_in_telegram = customtkinter.CTkButton(info_job_place, text="Результат в телеграм", font=("Arial Bold", 18))
send_in_telegram.place(relx=0.30, rely=0.93)

vidget_job_plc = customtkinter.CTkTabview(win, width=600, height=70, corner_radius=15)
vidget_job_plc.place(relx=0.20, rely=0.01)

ent_btn = customtkinter.CTkButton(vidget_job_plc, text="RUN", corner_radius=10, command=get_val)
ent_btn.place(relx=0.20, rely=0.43)

ent_btn_2 = customtkinter.CTkButton(vidget_job_plc, text="Work_with_telegram", corner_radius=10, command=get_val_2)
ent_btn_2.place(relx=0.60, rely=0.43)


win.mainloop()
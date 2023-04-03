import customtkinter


class MainObject:
    def __init__(self, win, plc_y_frame, smartphone_model, smart_list, index, relx_fr_frame1= 0.01,  color_frame="#FFFAFA"):

        def boardcast_1():
            res = self.main_vidget.get()
            self.main_vidget_3.set(res)

        def boardcast_2():
            res = self.main_vidget_3.get()
            self.main_vidget_5.set(res)

        def boardcast_3():
            res = self.main_vidget_5.get()
            self.main_vidget_7.set(res)

        def boardcast_4():
            res = self.main_vidget_7.get()
            self.main_vidget_9.set(res)

        def boardcast_5():
            res = self.main_vidget_2.get()
            self.main_vidget_4.set(res)

        def boardcast_6():
            res = self.main_vidget_4.get()
            self.main_vidget_6.set(res)

        def boardcast_7():
            res = self.main_vidget_6.get()
            self.main_vidget_8.set(res)

        def boardcast_8():
            res = self.main_vidget_8.get()
            self.main_vidget_10.set(res)


        job_pls = customtkinter.CTkTabview(win, width=215, height=145, corner_radius=10, fg_color=color_frame)
        job_pls.place(relx=relx_fr_frame1, rely=plc_y_frame)
        color_all_vidget = "#FFF8DC"

        self.main_vidget = customtkinter.CTkComboBox(job_pls, width=200, height=40, values=smart_list,
                                                     fg_color=color_all_vidget, button_color=color_all_vidget,
                                                     border_color=color_all_vidget, corner_radius=12)
        self.main_vidget.place(relx=0.02, rely=0.25)
        elem_smart1 = smartphone_model[index]
        ind_smart1 = smart_list.index(elem_smart1)
        self.main_vidget.set(smart_list[ind_smart1])

        self.main_vidget_2 = customtkinter.CTkComboBox(job_pls, width=200, height=40, values=smart_list,
                                                       fg_color=color_all_vidget, button_color=color_all_vidget,
                                                       border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_2.place(relx=0.02, rely=0.60)
        elem_smart2 = smartphone_model[index + 1]
        ind_smart2 = smart_list.index(elem_smart2)
        self.main_vidget_2.set(smart_list[ind_smart2])

        help_btn = customtkinter.CTkButton(win, text=">", fg_color="red", width=20, command=boardcast_1)
        help_btn.place(relx=relx_fr_frame1 + 0.127, rely=plc_y_frame + 0.045)

        help_btn = customtkinter.CTkButton(win, text=">", fg_color="red", width=20, command=boardcast_5)
        help_btn.place(relx=relx_fr_frame1 + 0.127, rely=plc_y_frame + 0.105)

        relx_fr_frame1 += 0.14

        job_pls2 = customtkinter.CTkTabview(win, width=215, height=145, corner_radius=10, fg_color=color_frame)
        job_pls2.place(relx=relx_fr_frame1, rely=plc_y_frame)
        color_all_vidget = "#FFF8DC"

        self.main_vidget_3 = customtkinter.CTkComboBox(job_pls2, width=200, height=40, values=smart_list,
                                                     fg_color=color_all_vidget, button_color=color_all_vidget,
                                                     border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_3.place(relx=0.02, rely=0.25)
        elem_smart3 = smartphone_model[index + 2]
        ind_smart3 = smart_list.index(elem_smart3)
        self.main_vidget_3.set(smart_list[ind_smart3])

        self.main_vidget_4 = customtkinter.CTkComboBox(job_pls2, width=200, height=40, values=smart_list,
                                                       fg_color=color_all_vidget, button_color=color_all_vidget,
                                                       border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_4.place(relx=0.02, rely=0.60)
        elem_smart4 = smartphone_model[index + 3]
        ind_smart4 = smart_list.index(elem_smart4)
        self.main_vidget_4.set(smart_list[ind_smart4])

        help_btn = customtkinter.CTkButton(win, text=">", fg_color="red", width=20, command=boardcast_2)
        help_btn.place(relx=relx_fr_frame1 + 0.127, rely=plc_y_frame + 0.045)

        help_btn = customtkinter.CTkButton(win, text=">", fg_color="red", width=20, command=boardcast_6)
        help_btn.place(relx=relx_fr_frame1 + 0.127, rely=plc_y_frame + 0.105)

        relx_fr_frame1 += 0.14

        job_pls3 = customtkinter.CTkTabview(win, width=215, height=145, corner_radius=10, fg_color=color_frame)
        job_pls3.place(relx=relx_fr_frame1, rely=plc_y_frame)
        color_all_vidget = "#FFF8DC"

        self.main_vidget_5 = customtkinter.CTkComboBox(job_pls3, width=200, height=40, values=smart_list,
                                                     fg_color=color_all_vidget, button_color=color_all_vidget,
                                                     border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_5.place(relx=0.02, rely=0.25)
        elem_smart5 = smartphone_model[index + 4]
        ind_smart5 = smart_list.index(elem_smart5)
        self.main_vidget_5.set(smart_list[ind_smart5])

        self.main_vidget_6 = customtkinter.CTkComboBox(job_pls3, width=200, height=40, values=smart_list,
                                                       fg_color=color_all_vidget, button_color=color_all_vidget,
                                                       border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_6.place(relx=0.02, rely=0.60)
        elem_smart6 = smartphone_model[index + 5]
        ind_smart6 = smart_list.index(elem_smart6)
        self.main_vidget_6.set(smart_list[ind_smart6])

        help_btn = customtkinter.CTkButton(win, text=">", fg_color="red", width=20, command=boardcast_3)
        help_btn.place(relx=relx_fr_frame1 + 0.127, rely=plc_y_frame + 0.045)

        help_btn = customtkinter.CTkButton(win, text=">", fg_color="red", width=20, command=boardcast_7)
        help_btn.place(relx=relx_fr_frame1 + 0.127, rely=plc_y_frame + 0.105)

        relx_fr_frame1 += 0.14

        job_pls4 = customtkinter.CTkTabview(win, width=215, height=145, corner_radius=10, fg_color=color_frame)
        job_pls4.place(relx=relx_fr_frame1, rely=plc_y_frame)
        color_all_vidget = "#FFF8DC"

        self.main_vidget_7 = customtkinter.CTkComboBox(job_pls4, width=200, height=40, values=smart_list,
                                                     fg_color=color_all_vidget, button_color=color_all_vidget,
                                                     border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_7.place(relx=0.02, rely=0.25)
        elem_smart7 = smartphone_model[index + 6]
        ind_smart7 = smart_list.index(elem_smart7)
        self.main_vidget_7.set(smart_list[ind_smart7])

        self.main_vidget_8 = customtkinter.CTkComboBox(job_pls4, width=200, height=40, values=smart_list,
                                                       fg_color=color_all_vidget, button_color=color_all_vidget,
                                                       border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_8.place(relx=0.02, rely=0.60)
        elem_smart8 = smartphone_model[index + 7]
        ind_smart8 = smart_list.index(elem_smart8)
        self.main_vidget_8.set(smart_list[ind_smart8])

        help_btn = customtkinter.CTkButton(win, text=">", fg_color="red", width=20, command=boardcast_4)
        help_btn.place(relx=relx_fr_frame1 + 0.127, rely=plc_y_frame + 0.045)

        help_btn = customtkinter.CTkButton(win, text=">", fg_color="red", width=20, command=boardcast_8)
        help_btn.place(relx=relx_fr_frame1 + 0.127, rely=plc_y_frame + 0.105)

        relx_fr_frame1 += 0.14

        job_pls5 = customtkinter.CTkTabview(win, width=215, height=145, corner_radius=10, fg_color=color_frame)
        job_pls5.place(relx=relx_fr_frame1, rely=plc_y_frame)
        color_all_vidget = "#FFF8DC"

        self.main_vidget_9 = customtkinter.CTkComboBox(job_pls5, width=200, height=40, values=smart_list,
                                                     fg_color=color_all_vidget, button_color=color_all_vidget,
                                                     border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_9.place(relx=0.02, rely=0.25)
        elem_smart9 = smartphone_model[index + 8]
        ind_smart9 = smart_list.index(elem_smart9)
        self.main_vidget_9.set(smart_list[ind_smart9])

        self.main_vidget_10 = customtkinter.CTkComboBox(job_pls5, width=200, height=40, values=smart_list,
                                                       fg_color=color_all_vidget, button_color=color_all_vidget,
                                                       border_color=color_all_vidget, corner_radius=12)
        self.main_vidget_10.place(relx=0.02, rely=0.60)
        elem_smart10 = smartphone_model[index + 9]
        ind_smart10 = smart_list.index(elem_smart10)
        self.main_vidget_10.set(smart_list[ind_smart10])


    def get_value(self):
        res_list = []
        res_list.append(self.main_vidget.get())
        res_list.append(self.main_vidget_2.get())
        res_list.append(self.main_vidget_3.get())
        res_list.append(self.main_vidget_4.get())
        res_list.append(self.main_vidget_5.get())
        res_list.append(self.main_vidget_6.get())
        res_list.append(self.main_vidget_7.get())
        res_list.append(self.main_vidget_8.get())
        res_list.append(self.main_vidget_9.get())
        res_list.append(self.main_vidget_10.get())
        return res_list
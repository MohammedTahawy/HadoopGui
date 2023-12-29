import customtkinter
from tkinter import filedialog
from tkterm import  *




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.jar=False
        self.input=False
        self.selected_input_files = ""
        self.selected_output_files = ""
        self.selected_jar_file = ""
        

        # configure window
        self.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.resizable(False, False)
        self.title("Big Data Project")
        self.geometry(f"{1100}x{735}")
       # self.iconbitmap("logo.ico")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.progress_bar = customtkinter.CTkFrame(self, height=10, width=800)
        self.progress_bar.grid(row=1, column=1, padx=(20, 20), pady=(10, 0), sticky="n")

        self.names_frame = customtkinter.CTkFrame(self, height=200, width=400)
        self.names_frame.grid(row=2, column=1, padx=(20, 10), pady=(10, 0), sticky="w")

        self.supervision_frame = customtkinter.CTkFrame(self, height=200, width=400)
        self.supervision_frame.grid(row=2, column=1, padx=(20, 10), pady=(10, 0), sticky="e")


        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Big Data Project",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.clear_input, text="Clear /input",font=customtkinter.CTkFont(size=16),hover_color="#47BBC6",text_color="#60EC5E")
        self.sidebar_button_1.place(x=22, y=110)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.clear_output,text="Clear /output",font=customtkinter.CTkFont(size=16),hover_color="#47BBC6",text_color="#60EC5E")
        self.sidebar_button_2.place(x=22, y=160)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.load_jar,text="select jar file",font=customtkinter.CTkFont(size=16),hover_color="#47BBC6",text_color="#60EC5E")
        self.sidebar_button_3.place(x=22, y=210)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command= self.load_input_files ,text="select input",font=customtkinter.CTkFont(size=16),hover_color="#47BBC6",text_color="#60EC5E",state="disabled")
        self.sidebar_button_4.place(x=22, y=260)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.run_program,text="Run", font=customtkinter.CTkFont(size=16), hover_color="#47BBC6", text_color="#60EC5E",state="disabled")
        self.sidebar_button_5.place(x=22, y=310)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=self.choose_output_path,text="select output path", font=customtkinter.CTkFont(size=16),hover_color="#47BBC6", text_color="#60EC5E",state="disabled")
        self.sidebar_button_6.place(x=22, y=360)
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, command=self.project_team,text="Credits", font=customtkinter.CTkFont(size=16),hover_color="#47BBC6", text_color="#60EC5E")
        self.sidebar_button_7.place(x=22, y=410)
        self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, command=self.destroy, text="Exit", font=customtkinter.CTkFont(size=16), hover_color="#47BBC6", text_color="#60EC5E")
        self.sidebar_button_8.place(x=22, y=460)


        self.progressbar = customtkinter.CTkProgressBar(self.progress_bar, orientation="horizontal",width=800,height=10,determinate_speed=10,progress_color=("#072BC1","#20F7D9"))
        self.progressbar.pack(fill="both",expand=1)
        self.progressbar.set(0)
        print(self.progressbar.get())



        self.switch_var = customtkinter.StringVar(value="off")
        self.switch = customtkinter.CTkSwitch(self.sidebar_frame, command=self.switcher, variable=self.switch_var,onvalue="on", offvalue="off", text="on/off",switch_width=50)
        self.switch.grid(row=1, column=0, padx=20, pady=10)



        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,values=["Light", "Dark", "System"],command=self.change_appearance_mode_event,dropdown_hover_color="#47BBC6")
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,values=["80%", "90%", "100%", "110%", "120%" ],command=self.change_scaling_event,dropdown_hover_color="#47BBC6")
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set("100%")




    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def switcher(self):
        if self.switch_var.get() == "on":
            tkterm.Terminal.run_command(self.terminal,'start-all.sh')
            if int(self.progressbar.get()*100 != 0):
                print(int(self.progressbar.get()*100))
                pass
            else:
                self.progressbar.step()
                print(int(self.progressbar.get()*100))
        elif self.switch_var.get() == "off":
            tkterm.Terminal.run_command(self.terminal,'stop-all.sh')
        else:
            pass

    def load_jar(self):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("JAR files", "*.jar")])
        if file_path:
            try:
                self.selected_jar_file=file_path
                print("Selected File:", file_path)
                tkterm.Terminal.run_command(self.terminal, f'echo "jar {file_path.title()} loaded"')
                self.jar=True
                if self.jar :
                    self.sidebar_button_4.configure(state="normal")
                if int(self.progressbar.get()*100 != 20):
                    pass
                else:
                    self.progressbar.step()
                    print(int(self.progressbar.get()*100))
            except Exception as ex:
                print(ex)
                pass

    def load_input_files(self):
        file_path = filedialog.askdirectory(title="Select a folder")
        
        if file_path:
            try:
                self.selected_input_files=file_path
                print("Selected File:", file_path)
                print(self.selected_input_files)
                tkterm.Terminal.run_command(self.terminal,'hadoop fs -put {} /input'.format(self.selected_input_files))
                self.input=True
                if self.input and self.jar :
                     self.sidebar_button_5.configure(state="normal")

                if int(self.progressbar.get()*100 != 40):
                    pass
                else:
                    self.progressbar.step()
                    print(int(self.progressbar.get()*100))
                
            except Exception as ex:
                print(ex)
                pass
           # self.input_label.configure(text=f"file loaded successfully", text_color="#EAF906")

    def choose_output_path(self):
        file_path = filedialog.askdirectory(title="Select a folder")
        if file_path:
            try:
                print("Selected File:", file_path)
                tkterm.Terminal.run_command(self.terminal,'hadoop fs -get /output/part-r-00000 {}'.format(file_path))

                if int(self.progressbar.get() * 100 != 80):
                    print(int(self.progressbar.get() * 100))
                    pass
                else:
                    self.progressbar.step()
                    print(int(self.progressbar.get() * 100))
            except Exception as ex:
                print(ex)
                pass

    def clear_input(self):
        try:
            if self.switch_var.get() == "on" and int(self.progressbar.get()*100) <= 100:
                self.progressbar.set(0.2)
                print(int(self.progressbar.get() * 100))
            else:
                self.progressbar.set(0)
                print(int(self.progressbar.get() * 100))
            tkterm.Terminal.run_command(self.terminal,'hdfs dfs -rm -r /input')
            InputLoaded=False

            print("input cleared")
        except Exception as ex:
            print(ex)
            pass

    def clear_output(self):
        try:
            if self.switch_var.get() == "on" and int(self.progressbar.get()*100) <= 100:
                self.progressbar.set(0.2)
                print(int(self.progressbar.get() * 100))
            else:
                self.progressbar.set(0)
                print(int(self.progressbar.get() * 100))
            tkterm.Terminal.run_command(self.terminal,'hdfs dfs -rm -r /output')
            print(" output cleared")
        except Exception as ex:
            print(ex)
            pass






 

    def open_terminal(self):
        self.terminal = Terminal(self,width=80, height=20, borderwidth=2)

        self.terminal.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")


    def run_program(self):
        try:
            tkterm.Terminal.run_command(self.terminal,"hadoop jar {} /input /output".format(self.selected_jar_file))
            self.sidebar_button_6.configure(state="normal")

            if int(self.progressbar.get() * 100) != 60:
                pass
            else:
                self.progressbar.step()
                print(int(self.progressbar.get() * 100))


        except:
            pass

        pass




    def project_team(self):
        self.preb_label = customtkinter.CTkLabel(self.names_frame, text="Prepared by:-",
                                                 font=customtkinter.CTkFont(size=19, weight="bold"),
                                                 text_color="#D82F4E")
        self.preb_label.place(x=5, y=2)
        self.s1_label = customtkinter.CTkLabel(self.names_frame,
                                               text="Abdullah Emad Eldin",
                                               font=customtkinter.CTkFont(size=16, weight="bold"), text_color="#D27C26")
        self.s1_label.place(x=5, y=24)
        self.s2_label = customtkinter.CTkLabel(self.names_frame,text="Mohamed AbdulHamid",font=customtkinter.CTkFont(size=18, weight="bold"),
                                                        text_color="#D27C26")
        self.s2_label.place(x=5, y=46)
        self.s3_label = customtkinter.CTkLabel(self.names_frame,
                                               text="Mohamed Mostafa",
                                               font=customtkinter.CTkFont(size=18, weight="bold"),
                                                        text_color="#D27C26")
        self.s3_label.place(x=5, y=68)
        self.s4_label = customtkinter.CTkLabel(self.names_frame,
                                               text="Amir Rabee3",
                                               font=customtkinter.CTkFont(size=18, weight="bold"),
                                                        text_color="#D27C26")
        self.s4_label.place(x=5, y=90)
        self.s5_label = customtkinter.CTkLabel(self.names_frame,
                                               text="Mohamed Salamah",
                                               font=customtkinter.CTkFont(size=18, weight="bold"),
                                                        text_color="#D27C26")
        self.s5_label.place(x=5, y=112)
        self.s6_label = customtkinter.CTkLabel(self.names_frame,
                                               text="Shaimaa Abdelmoaen",
                                               font=customtkinter.CTkFont(size=18, weight="bold"),
                                                        text_color="#D27C26")
        self.s6_label.place(x=5, y=134)
        self.s7_label = customtkinter.CTkLabel(self.names_frame,
                                               text="Shrouk Abdelnasser",
                                               font=customtkinter.CTkFont(size=18, weight="bold"),
                                                        text_color="#D27C26")
        self.s7_label.place(x=5, y=156)
        self.s8_label = customtkinter.CTkLabel(self.names_frame,
                                               text="Wafaa Said",
                                               font=customtkinter.CTkFont(size=18, weight="bold"),
                                                        text_color="#D27C26")
        self.s8_label.place(x=5, y=178)

        self.supervision_label = customtkinter.CTkLabel(self.supervision_frame, text="Under supervision of:-",
                                                        font=customtkinter.CTkFont(size=20, weight="bold"),
                                                        text_color="#D82F4E")
        self.supervision_label.place(x=5, y=2)

        self.s11_label = customtkinter.CTkLabel(self.supervision_frame,
                                                text="DR:Esraa Raslan",
                                                font=customtkinter.CTkFont(size=18, weight="bold"),
                                                text_color="#D27C26")
        self.s11_label.place(x=5, y=50)

        self.s22_label = customtkinter.CTkLabel(self.supervision_frame,
                                                text="ENG: Asmaa",
                                                font=customtkinter.CTkFont(size=18, weight="bold"),
                                                text_color="#D27C26")
        self.s22_label.place(x=5, y=100)

    def disable_event(self):
        pass
if __name__ == "__main__":
    app = App()
    app.open_terminal()
    app.mainloop()

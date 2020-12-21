import tkinter as tk


class WindowMain(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title = ""
        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        # 城市信息Frame
        city_info_frame = tk.Frame(self, bg='red')
        city_label = tk.Label(city_info_frame, text="沈阳", font=(None, 20))
        city_label.grid(row=0, column=0, padx=20, pady=10, sticky=tk.NW)
        time_label = tk.Label(city_info_frame,
                              text="2010/12/19 16:11",
                              font=(None, 10))
        time_label.grid(row=1, column=0, padx=20, pady=5, sticky=tk.NW)
        description_label = tk.Label(city_info_frame,
                                     text="晴转多云",
                                     font=(None, 10))
        description_label.grid(row=2, column=0, padx=20, pady=5, sticky=tk.NW)
        # 城市信息布局
        city_info_frame.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)

        # 天气信息Frame
        weather_info_frame = tk.Frame(self, bg='blue')
        # 气温Frame
        temperature_frame = tk.Frame(weather_info_frame)
        city_label = tk.Label(temperature_frame, text="假装图片")
        city_label.grid(row=0, column=0, sticky=tk.W)
        time_label = tk.Label(temperature_frame, text="19°C", font=(None, 50))
        time_label.grid(row=0, column=1, sticky=tk.W)
        # 气温布局
        temperature_frame.grid(row=0,
                               column=0,
                               columnspan=2,
                               rowspan=3,
                               sticky=tk.W)

        # 更多信息Frame
        more_message_frame = tk.Frame(weather_info_frame)
        rain_label = tk.Label(more_message_frame, text="降水概率：0%")
        rain_label.grid(row=0, column=0, sticky=tk.W)
        wet_label = tk.Label(more_message_frame, text="湿度：45%")
        wet_label.grid(row=1, column=0, sticky=tk.W)
        windspeed_label = tk.Label(more_message_frame, text="风速：45km/s")
        windspeed_label.grid(row=2, column=0, sticky=tk.W)
        # 更多信息布局
        more_message_frame.grid(row=0,
                                column=2,
                                columnspan=2,
                                rowspan=3,
                                sticky=tk.W)
        # 天气信息布局
        weather_info_frame.grid(row=3, column=0)

        daily_weather_frame = tk.Frame(self, bg='yellow')

        daily_weather_frame.grid(row=2, column=0, sticky=tk.S)

        weekly_weather_frame = tk.Frame(self, bg='black')

        weekly_weather_frame.grid(row=3, column=0, sticky=tk.S)

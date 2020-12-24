import tkinter as tk
from PIL import Image, ImageTk


class WindowMain(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.city_text = tk.StringVar()
        self.time_text = tk.StringVar()
        self.description_text = tk.StringVar()
        self.temperature_text = tk.StringVar()
        self.rain_text = tk.StringVar()
        self.wet_text = tk.StringVar()
        self.windspeed_text = tk.StringVar()
        self.img_main = None

        self.testText()
        self.setup_ui()

    def setup_ui(self):
        self.title = ""
        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        # 城市信息Frame
        city_info_frame = tk.Frame(self, bg='red')
        city_label = tk.Label(city_info_frame,
                              textvariable=self.city_text,
                              font=(None, 20))
        city_label.grid(row=0, column=0, padx=20, pady=10, sticky=tk.NW)
        time_label = tk.Label(city_info_frame,
                              textvariable=self.time_text,
                              font=(None, 10))
        time_label.grid(row=1, column=0, padx=20, pady=5, sticky=tk.NW)
        description_label = tk.Label(city_info_frame,
                                     textvariable=self.description_text,
                                     font=(None, 10))
        description_label.grid(row=2, column=0, padx=20, pady=5, sticky=tk.NW)
        # 城市信息布局
        city_info_frame.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)

        # 天气信息Frame
        weather_info_frame = tk.Frame(self, bg='blue')
        # 气温Frame
        temperature_frame = tk.Frame(weather_info_frame)
        img_label = tk.Label(temperature_frame, image=self.img_main)
        img_label.grid(row=0, column=0)
        temperature_label = tk.Label(temperature_frame,
                                     textvariable=self.temperature_text,
                                     font=(None, 50))
        temperature_label.grid(row=0, column=1, sticky=tk.W)
        # 气温布局
        temperature_frame.grid(row=0,
                               column=0,
                               columnspan=2,
                               rowspan=3,
                               sticky=tk.W)

        # 更多信息Frame
        more_message_frame = tk.Frame(weather_info_frame)
        rain_label = tk.Label(more_message_frame, textvariable=self.rain_text)
        rain_label.grid(row=0, column=0, sticky=tk.W)
        wet_label = tk.Label(more_message_frame, textvariable=self.wet_text)
        wet_label.grid(row=1, column=0, sticky=tk.W)
        windspeed_label = tk.Label(more_message_frame,
                                   textvariable=self.windspeed_text)
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

    def testText(self):
        self.city_text.set("沈阳")
        self.time_text.set("2010/12/19 16:11")
        self.description_text.set("晴转多云")
        self.temperature_text.set("19°C")
        self.rain_text.set("降水概率：0%")
        self.wet_text.set("湿度：45%")
        self.windspeed_text.set("风速：45km/s")
        image = Image.open("res/img/sunny.png").resize((100, 100))
        self.img_main = ImageTk.PhotoImage(image)

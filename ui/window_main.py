import tkinter as tk
from weather.api_master import ApiMaster
from utils.config import Config
from PIL import Image, ImageTk


class WindowMain(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.__city_text = tk.StringVar()
        self.__time_text = tk.StringVar()
        self.__description_text = tk.StringVar()
        self.__temperature_text = tk.StringVar()
        self.__rain_text = tk.StringVar()
        self.__wet_text = tk.StringVar()
        self.__windspeed_text = tk.StringVar()
        self.__img_main = None

        self.__citys = Config().get()['citys']['list']
        self.__city_show = 0
        self.__init_text()
        self.__setup_ui()
        self.__fresh_ui()

    def __setup_ui(self):
        self.title = ""
        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        # 城市信息Frame
        city_info_frame = tk.Frame(self, bg='red')
        city_label = tk.Label(city_info_frame,
                              textvariable=self.__city_text,
                              font=(None, 20))
        city_label.grid(row=0, column=0, padx=20, pady=10, sticky=tk.NW)
        time_label = tk.Label(city_info_frame,
                              textvariable=self.__time_text,
                              font=(None, 10))
        time_label.grid(row=1, column=0, padx=20, pady=5, sticky=tk.NW)
        description_label = tk.Label(city_info_frame,
                                     textvariable=self.__description_text,
                                     font=(None, 10))
        description_label.grid(row=2, column=0, padx=20, pady=5, sticky=tk.NW)
        # 城市信息布局
        city_info_frame.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)

        # 天气信息Frame
        weather_info_frame = tk.Frame(self, bg='blue')
        # 气温Frame
        temperature_frame = tk.Frame(weather_info_frame)
        img_label = tk.Label(temperature_frame, image=self.__img_main)
        img_label.grid(row=0, column=0)
        temperature_label = tk.Label(temperature_frame,
                                     textvariable=self.__temperature_text,
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
        rain_label = tk.Label(more_message_frame,
                              textvariable=self.__rain_text)
        rain_label.grid(row=0, column=0, sticky=tk.W)
        wet_label = tk.Label(more_message_frame, textvariable=self.__wet_text)
        wet_label.grid(row=1, column=0, sticky=tk.W)
        windspeed_label = tk.Label(more_message_frame,
                                   textvariable=self.__windspeed_text)
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

    def __init_text(self):
        self.__city_text.set("——")
        self.__time_text.set("————/——/—— ——:——")
        self.__description_text.set("——")
        self.__temperature_text.set("——°C")
        self.__rain_text.set("降水概率：——%")
        self.__wet_text.set("湿度：——%")
        self.__windspeed_text.set("风速：——km/s")
        image = Image.open("res/img/wutu.png").resize((100, 100))
        self.__img_main = ImageTk.PhotoImage(image)

    def __fresh_ui(self):
        if self.__citys:
            api = ApiMaster(self.__citys[self.__city_show])
            api.fresh_weather()
            curr = api.get_current_weather()
            # week = api.get_weekly_weather()
            self.__city_text.set(self.__citys[self.__city_show])
            self.__time_text.set(curr["update_time"])
            self.__description_text.set(curr["wea"])
            self.__temperature_text.set("{}°C".format(curr["tem"]))
            self.__rain_text.set("空气质量：{}".format(curr["air"]))
            self.__wet_text.set("湿度：{}".format(curr["humidity"]))
            self.__windspeed_text.set("风速：{}".format(curr["win_meter"]))
            image = Image.open("res/img/{}.png".format(
                curr["wea_img"])).resize((100, 100))
            self.__img_main = ImageTk.PhotoImage(image)

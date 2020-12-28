import tkinter as tk
import tkinter.messagebox
from ui.window_setting import WindowSetting
from utils.images import Images
from weather.api_master import ApiMaster
from utils.config import Config
from PIL import Image, ImageTk


class WindowMain(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.__citys = Config().get()['citys']['list']
        self.__city_show = 0

        self.__city_text = tk.StringVar()
        self.__time_text = tk.StringVar()
        self.__description_text = tk.StringVar()
        self.__temperature_text = tk.StringVar()
        self.__rain_text = tk.StringVar()
        self.__wet_text = tk.StringVar()
        self.__windspeed_text = tk.StringVar()
        self.__main_img_label = tk.Label()
        self.__weekly_imgs_label = [tk.Label() for _ in range(7)]
        self.__weekly_texts = [tk.StringVar() for _ in range(7)]

        self.__setup_ui()
        self.__init_text()
        self.__fresh_ui(manual=False)

    def __setup_ui(self):
        self.title("天气")
        # self.configure(bg="white")
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

        # 按钮Frame
        button_frame = tk.Frame(self, bg='cyan')
        self.__fresh_icon = Images().get_icon("refresh", (28, 28))
        fresh_button = tk.Button(button_frame,
                                 image=self.__fresh_icon,
                                 borderwidth=0,
                                 command=self.__fresh_ui)
        fresh_button.grid(row=0, column=0)
        self.__left_icon = Images().get_icon("direction-left", (28, 28))
        left_button = tk.Button(button_frame,
                                image=self.__left_icon,
                                borderwidth=0,
                                command=self.__prev)
        left_button.grid(row=0, column=1)
        self.__right_icon = Images().get_icon("direction-right", (28, 28))
        left_button = tk.Button(button_frame,
                                image=self.__right_icon,
                                borderwidth=0,
                                command=self.__next)
        left_button.grid(row=0, column=2)
        self.__setting_icon = Images().get_icon("adjust", (28, 28))
        setting_button = tk.Button(button_frame,
                                   image=self.__setting_icon,
                                   borderwidth=0,
                                   command=self.__setting)
        setting_button.grid(row=0, column=3)
        # 按钮布局
        button_frame.grid(row=0, column=1, sticky=tk.NE)

        # 天气信息Frame
        weather_info_frame = tk.Frame(self, bg='blue')
        # 气温Frame
        temperature_frame = tk.Frame(weather_info_frame)
        self.__main_img_label = tk.Label(temperature_frame, image=None)
        self.__main_img_label.grid(row=0, column=0, padx=15)
        temperature_label = tk.Label(temperature_frame,
                                     textvariable=self.__temperature_text,
                                     font=(None, 50))
        temperature_label.grid(row=0, column=1, sticky=tk.W)
        # 气温布局
        temperature_frame.grid(row=0,
                               column=0,
                               columnspan=2,
                               rowspan=3,
                               sticky=tk.W,
                               padx=25)

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
        weather_info_frame.grid(row=3, column=0, columnspan=2)

        # 小时级预报Frame
        daily_weather_frame = tk.Frame(self, bg='yellow')
        # 小时级预报布局
        daily_weather_frame.grid(row=4, column=0, sticky=tk.S, columnspan=2)

        # 天级预报Frame
        weekly_weather_frame = tk.Frame(self, bg='black')
        for i in range(7):
            self.__weekly_imgs_label[i] = tk.Label(weekly_weather_frame,
                                                   image=None,
                                                   height=72)
            self.__weekly_imgs_label[i].grid(row=0, column=1 + i)
        weekly_weather_tems = [
            tk.Label(weekly_weather_frame, textvariable=self.__weekly_texts[i])
            for i in range(7)
        ]
        for i in range(7):
            weekly_weather_tems[i].grid(row=1, column=1 + i, padx=10)
        # 天级预报布局
        weekly_weather_frame.grid(row=5, column=0, sticky=tk.S, columnspan=2)

    def __init_text(self):
        self.__city_text.set("——")
        self.__time_text.set("————/——/—— ——:——")
        self.__description_text.set("——")
        self.__temperature_text.set("——°C")
        self.__rain_text.set("降水概率：——%")
        self.__wet_text.set("湿度：——%")
        self.__windspeed_text.set("风速：——km/s")
        self.__main_img = Images().get_img("wutu", (150, 150))
        self.__main_img_label.configure(image=self.__main_img)
        self.__week_imgs = [None for _ in range(7)]
        self.__week_imgs[0] = Images().get_img("wutu", (70, 70))
        for i in range(7):
            self.__weekly_imgs_label[i].configure(image=self.__week_imgs[0])
            self.__weekly_texts[i].set("— ~ —°C")
        self.update()

    def __fresh_ui(self, manual: bool = True):
        if self.__citys:
            api = ApiMaster(self.__citys[self.__city_show])
            api.fresh_weather()
            curr = api.get_current_weather()
            week = api.get_weekly_weather()
            if curr == None or week == None:
                tkinter.messagebox.showerror(
                    title='错误：', message='获取当前天气失败，请尝试点击刷新按钮以重新获取天气。')
                return
            self.__city_text.set(self.__citys[self.__city_show])
            self.__time_text.set(curr["update_time"])
            self.__description_text.set(curr["wea"])
            self.__temperature_text.set("{}°C".format(curr["tem"]))
            self.__rain_text.set("空气质量：{}".format(curr["air"]))
            self.__wet_text.set("湿度：{}".format(curr["humidity"]))
            self.__windspeed_text.set("风速：{}".format(curr["win_meter"]))
            self.__main_img = Images().get_img(curr["wea_img"], (150, 150))
            self.__main_img_label.configure(image=self.__main_img)
            for i in range(7):
                self.__week_imgs[i] = Images().get_img(
                    week['data'][i]['wea_img'], (70, 70))
                self.__weekly_imgs_label[i].configure(
                    image=self.__week_imgs[i])
                self.__weekly_texts[i].set("{} ~ {}".format(
                    week['data'][i]['tem2'], week['data'][i]['tem1']))
        self.update()
        if manual:
            tkinter.messagebox.showinfo(title='提示：', message='刷新成功')

    def __prev(self):
        if self.__city_show > 0:
            self.__city_show -= 1
        self.__fresh_ui(manual=False)

    def __next(self):
        if self.__city_show < len(self.__citys) - 1:
            self.__city_show += 1
        self.__fresh_ui(manual=False)

    def __setting(self):
        setting_dialog = WindowSetting()
        self.wait_window(setting_dialog)
        self.__fresh_ui(manual=False)
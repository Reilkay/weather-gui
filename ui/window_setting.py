import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from utils.citys import Citys
from utils.config import Config


class WindowSetting(tk.Toplevel):
    def __init__(self) -> None:
        super().__init__()

        self.__config = Config()
        self.__config_list = self.__config.get()
        self.__citys = Citys()
        self.__city_corr = self.__citys.get_corr()
        self.__city_list = self.__citys.get_list()

        self.__appid_text = tk.StringVar()
        self.__appsecret_text = tk.StringVar()
        self.__city_entry = None
        self.__citybox = None
        # 弹窗界面
        self.__setup_ui()
        self.__init_text()
        self.grab_set()

    def __setup_ui(self) -> None:
        self.title("设置")
        # api设置Frame
        token_group = tk.LabelFrame(self, text="API设置", padx=5, pady=5)
        appid_label = tk.Label(token_group, text="appid: ")
        appid_label.grid(row=0, column=0)
        appid_entry = tk.Entry(token_group, textvariable=self.__appid_text)
        appid_entry.grid(row=0, column=1)
        appsecret_label = tk.Label(token_group, text="appsecret: ")
        appsecret_label.grid(row=1, column=0)
        appsecret_entry = tk.Entry(token_group,
                                   textvariable=self.__appsecret_text)
        appsecret_entry.grid(row=1, column=1)
        token_group.grid(row=0, column=0)

        # 城市设置Frame
        citys_group = tk.LabelFrame(self, text="城市设置", padx=5, pady=5)

        self.__city_entry = ttk.Combobox(citys_group, width=26)
        self.__city_entry.grid(row=0, column=0)
        self.__citybox = tk.Listbox(citys_group,
                                    width=26,
                                    selectmode=tk.EXTENDED)
        self.__citybox.grid(row=1, column=0)
        add_button = tk.Button(citys_group, text="+", command=self.__add)
        add_button.grid(row=0, column=1)
        delete_button = tk.Button(citys_group, text="-", command=self.__delete)
        delete_button.grid(row=1, column=1)
        citys_group.grid(row=1, column=0)

        # 按钮Frame
        button_frame = tk.Frame(self, padx=5, pady=5)
        save_button = tk.Button(button_frame, text="保存", command=self.__save)
        save_button.grid(row=0, column=0)
        exit_button = tk.Button(button_frame, text="退出", command=self.__exit)
        exit_button.grid(row=0, column=1)
        button_frame.grid(row=2, column=0)

    def __init_text(self) -> None:
        self.__appid_text.set(self.__config_list['weather-api']['appid'])
        self.__appsecret_text.set(
            self.__config_list['weather-api']['appsecret'])
        for item in self.__config_list['citys']['list']:
            self.__citybox.insert(tk.END, self.__city_corr[item])
        self.__city_entry['value'] = tuple(self.__city_list)

    def __add(self):
        city_tmp = self.__city_entry.get()
        list_tmp = self.__citybox.get(0, self.__citybox.size())
        if city_tmp in self.__city_list:
            pass
        elif city_tmp in self.__city_corr:
            city_tmp = self.__city_corr[city_tmp]
        else:
            tkinter.messagebox.showerror(title='错误：', message='查询不到该城市！')
            return
        if city_tmp not in list_tmp:
            self.__citybox.insert(tk.END, city_tmp)

    def __delete(self):
        delete_tmp = self.__citybox.curselection()
        delete_tmp_list = list(delete_tmp)
        delete_tmp_list.reverse()
        for index in delete_tmp_list:
            self.__citybox.delete(index)

    def __save(self):
        self.__config_list['weather-api']['appid'] = self.__appid_text.get()
        self.__config_list['weather-api'][
            'appsecret'] = self.__appsecret_text.get()
        list_tmp = self.__citybox.get(0, self.__citybox.size())
        list_city = []
        for item in list_tmp:
            list_city.append(item.split(" - ")[0])
        self.__config_list['citys']['list'] = list_city
        self.__config.update(self.__config_list)
        self.destroy()  # 销毁窗口

    def __exit(self):
        self.destroy()  # 销毁窗口

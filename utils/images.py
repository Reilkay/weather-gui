import os
import tkinter
from typing import Tuple
from PIL import Image, ImageTk


class Images:
    # 单例模式
    __instance = None
    __first_init = False

    def __new__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not self.__first_init:
            self.__path = './res'
            self.__img_dict = {}
            self.__icon_dict = {}
            self.__get_imgs()
            self.__get_icons()

    def __get_imgs(self) -> None:
        result = dict()
        for image in os.listdir(self.__path + '/img'):
            result[image.split('.')[0]] = Image.open(self.__path +
                                                     '/img/{}'.format(image))
        self.__img_dict = result

    def __get_icons(self) -> None:
        result = dict()
        for image in os.listdir(self.__path + '/icon'):
            result[image.split('.')[0]] = Image.open(self.__path +
                                                     '/icon/{}'.format(image))
        self.__icon_dict = result

    def get_img(self, img: str, size: Tuple) -> ImageTk.PhotoImage:
        resized_img = self.__img_dict[img].resize(size)
        photo_img = ImageTk.PhotoImage(resized_img)
        return photo_img

    def get_icon(self, img: str, size: Tuple) -> ImageTk.PhotoImage:
        resized_img = self.__icon_dict[img].resize(size)
        photo_img = ImageTk.PhotoImage(resized_img)
        return photo_img

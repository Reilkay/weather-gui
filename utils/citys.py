import json


class Citys:
    def __init__(self) -> None:
        self.__path = './res/json/citys.json'
        self.__corr = {}
        self.__list = []

    def __get(self) -> dict:
        with open(self.__path, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    def get_corr(self) -> dict:
        if self.__corr:
            return self.__corr
        else:
            city_dict = self.__get()
            for prov in city_dict:
                for city in city_dict[prov]:
                    for area in city_dict[prov][city]:
                        self.__list.append("{} - {} - {}".format(
                            area, city, prov))
                        self.__corr[area] = "{} - {} - {}".format(
                            area, city, prov)
            return self.__corr

    def get_list(self) -> list:
        if self.__list:
            return self.__list
        else:
            city_dict = self.__get()
            for prov in city_dict:
                for city in city_dict[prov]:
                    for area in city_dict[prov][city]:
                        self.__list.append("{} - {} - {}".format(
                            area, city, prov))
                        self.__corr[area] = "{} - {} - {}".format(
                            area, city, prov)
            return self.__list
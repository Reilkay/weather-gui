import toml


class Config:
    def __init__(self):
        self.__path = './config.toml'

    def get(self) -> dict:
        config = toml.load(self.__path)
        return config

    def update(self, config: dict) -> None:
        with open(self.__path, 'w') as f:
            r = toml.dump(config, f)
            # print(r)

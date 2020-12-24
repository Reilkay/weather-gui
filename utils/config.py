import toml


class Config:
    def __init__(self):
        self.path = './config.toml'

    def get(self) -> dict:
        config = toml.load(self.path)
        return config

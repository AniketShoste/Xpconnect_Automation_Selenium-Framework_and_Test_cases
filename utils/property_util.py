'''

Property class is reading values from application property file and also setting and getting value from property file.
'''
class PropertyUtils:
    # configs = Properties()
    configs = {}
    __instance = None

    def __init__(self):
        if not self.__instance:
            self.read_propertiy_file()
            self.__instance = self

    def read_propertiy_file(self):
        with open("application.properties", "r+") as config_file:
            # self.configs.load(config_file)
            all_line = config_file.readlines()
            for line in all_line:
                if line:
                    data = line.split("=", 1)
                    self.configs[data[0]] = data[1].strip()

        print(self.configs)
    def get_property(self, key):
        return self.configs.get(key)

    def set_property(self, key, value):
        self.configs[key] = value

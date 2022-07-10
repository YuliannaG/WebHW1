from abc import ABCMeta, abstractmethod
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def dump(self, data, filename):
        pass


class SerJson(SerializationInterface):
    def dump(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file)


class SerBin(SerializationInterface):
    def dump(self, data, filename):
        with open(filename, "w") as file:
            pickle.dump(data, file)

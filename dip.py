from abc import ABC, abstractmethod

''' В условии задачи вроде бы и так нет зависимости класса Car от PetrolEngine,
но наверное, подразумевается, что нужно сделать как-то так: '''


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class PetrolEngine(Engine):
    def start(self):
        pass


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()



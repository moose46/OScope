from dataclasses import dataclass
from observer import Observable, Observer


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Scope():
    def call_me(self):
        print('Scope Calling the overlord'.title())


class Multimeter():
    def call_me(self):
        print('MultiMeter Calling bob'.title())


class FileTypeAdapter:
    _initialised = False

    def __init__(self, fileType, **adapted_methods):
        super().__init__()
        self.fileType = fileType

        for key, value in adapted_methods.items():
            func = getattr(self.fileType, value)
            self.__setattr__(key, func)

        self._initialised = True

    def __getattr__(self, attr):
        return getattr(self.fileType, attr)

    def __setattr__(self, key, value):
        """Set attributes normally during initialisation"""
        if not self._initialised:
            super().__setattr__(key, value)
        else:
            """Set attributes on fileType after initialisation"""
            setattr(self.fileType, key, value)


class FileTypeFacade:
    file_type_adapters = None

    @classmethod
    def create_file_types(cls):
        print('Creating File Types ...')
        cls.file_type_adapters = [
            FileTypeAdapter(Scope(), call_me='call_me'),
            FileTypeAdapter(Multimeter(), call_me='call_me'),

        ]

    @classmethod
    def summon_file_types(cls):
        print('summoning file types'.title())
        for adapter in cls.file_type_adapters:
            adapter.call_me()


class EvilOverLord(Observer):
    def update(self, obj, *args, **kwargs):
        print('The Evil Overlord received a message!')
        print(f'Object: {obj}, Args: {args}, Kwargs: {kwargs}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    overload = EvilOverLord()

    FileTypeFacade.create_file_types()
    FileTypeFacade.summon_file_types()
    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

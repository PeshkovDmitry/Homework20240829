class Stack:

    def __init__(self, data: list = None):
        if data is None:
            self.__data = []
        else:
            self.__data = data

    def __str__(self):
        return str(self.__data)

    def put(self, value):
        if self.__data.count(value) == 0:
            self.__data.append(value)

    def get(self):
        return self.__data.pop()

    def delete(self, value):
        try:
            self.__data.remove(value)
        except ValueError:
            pass


class TaskManager:

    def __init__(self):
        self.__data = dict()

    def new_task(self, task: str, priority: int):
        stack = self.__data.setdefault(priority, Stack())
        stack.put(task)
        self.__data[priority] = stack

    def del_task(self, task: str):
        for v in self.__data.values():
            v.delete(task)

    def __str__(self):
        res = ""
        for k in sorted(self.__data.keys()):
            res += f"{k} -> {self.__data[k]}\n\r"
        return res


if __name__ == "__main__":
    manager = TaskManager()
    manager.new_task("Поспать", 1)
    manager.new_task("Поесть", 1)
    manager.new_task("Сделать домашку", 2)
    print(manager)
    manager.del_task("Поесть")
    print(manager)



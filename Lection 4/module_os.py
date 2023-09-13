# ● os.chdir(path) - смена текущей директории.
import os
os.chdir('C:/Users/79190/PycharmProjects/GB')

# ● os.getcwd() - текущая рабочая директория
import os
print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

# ● os.path - является вложенным модулем в модуль os и реализует некоторые
# полезные функции для работы с путями, такие как: ○ os.path.basename(path) - базовое имя пути
import os
print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #'main.py'

# ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.
import os
print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'
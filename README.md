# Разбиения фигур из УПС
В этом репозитории находятся файлы в формате json, содержащие необходимые разбиения фигур из УПС для доказательства верхних оценок.

Программа `check.py` считывает все разбиения, находит максимальный диаметр среди частей, проверяет корректность разбиения, и выводит соответсвующий рисунок. Проверяется корректность следующих вещей:
 - сумма площадей по всем частям совпадает с площадью разбиваемой покрышки
 - каждое ребро, которое есть в разбиении, находится ровно в двух частях в случае если ребро не на границе, и ровно в одной части, если ребро на границе
 - все вершины `Omega`, которые должны лежать на сторонах покрышки, действительно лежат на её сторонах.

Важно отметить, что сама покрышка задаётся вместе со всеми вершинами разбиения, которые находятся на её сторонах - чисто технически так удобней проверять корректность разбиения. При этом дополнительное поле `Bitmask` задаёт какие точки из `Omega` являются вершинами покрышки(`Bitmask[i] = 1`), а какие находятся на её сторонах(`Bitmask[i] = 0`). Для наглядности генерируется рисунок разбиения, где вершины(углы) покрышки выделены жирными точками.

Сам файл формата json содержит следующие 5 полей: `Title` - название разбиения, `Points` - словарь (название точки -> её координаты), `Omega` - список точек в покрышке, `Bitmask` - какие вершины на сторонах и какие нет, и `Partition` - список из многоугольников разбиения. Обход везде против часовой стрелки.

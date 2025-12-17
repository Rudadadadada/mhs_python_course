Артефакты ДЗ 2
================

Что уже сгенерено
---------------------
- `example.tex` — исходник с таблицей и картинкой.
- `sample.png` — красный пнгшный квадрат.

Как сгенерить заново
------------------------
0) Установить зависимости:
```
cd ~/<your_working_dir>
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install pdflatex
```

1) Локально:
```
cd ~/<your_working_dir>
python3 -m hw_2.generate_artifacts --pdf
```
PDF появится как `hw_2/artifacts/example.pdf`.

2) Через Docker (запускал из msh_python_course):
```
cd ~/<your_working_dir>
docker build -t hw2 .
docker run --rm -v "$PWD/hw_2/artifacts:/app/hw_2/artifacts" hw2
```
После выполнения в `hw_2/artifacts` будет `example.pdf` + логи.

Описание решений
----------------
- Таблица и картинка формируются функциями `generate_table` и `generate_figure` из `hw_2/latex_gen.py`.
- Финальный документ собирается через `build_document`.
- Скрипт `hw_2/generate_artifacts.py` создаёт артефакты; флаг `--pdf` дополнительно вызывает `pdflatex`.


# ARCHIVER

## Оглавление

1. [Описание](#Описание)
2. [Установка](#Установка)
3. [Функции](#Функции)
4. [Особенности](#Особенности)
## Описание

Библиотека предназначена для архивирования файлов в формате .zip

### Версия Python

Поддерживается версия Python 3.8

## Установка

Windows

```
py -m pip install archiver
```

## Функции

### arc()

Данная функция заходит в директорию и делает проход по папкам, подпапкам и файлам и архивирует их содержимое.
Также она выводит начальные и конечные директории.
В примере папка архивируется папка Данные

```python
from src.archiver.arciv import arc

arc()

```
```
['Данные']
['Архив содержимого.zip', 'Данные']
```

## Особенности
1.Исполняемая программа и /data должны находиться в одной и той же директории

2.Файлы,которые нужно заархивировать, должны находиться в /data/Данные
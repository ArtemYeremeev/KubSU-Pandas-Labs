# -*- coding: utf-8 -*-
"""Lab_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zecelKy1kn-P3NEAMPm-0JrEfsLZLdI_

**Лабораторная №1. Еремеев А.С.**

Импорты
"""

import numpy as np
import pandas as pd

"""Загрузка данных"""

data_url = 'https://raw.githubusercontent.com/ArtemYeremeev/KubSU-Pandas-Labs/main/Lab1/adult.data.csv'
df = pd.read_csv(data_url)
df.head(10)

"""**1. Сколько мужчин и женщин (признак sex) представлено в этом наборе данных**

Вариант 1
"""

df.groupby('sex').size()

"""Вариант 2"""

df['sex'].value_counts()

"""**2. Каков средний возраст женщин**

Вариант 1
"""

df.groupby('sex')['age'].mean()

"""Вариант 2"""

females = df['sex'] == 'Female'
df.loc[females, 'age'].mean()

"""**3. Какова доля граждан Германии**

Вариант 1
"""

is_german = df.apply(lambda x: True if x['native-country'] == 'Germany' else False, axis=1)
result_rows = len(is_german[is_german == True].index)
print("Количество нативных немцев в выборке -", result_rows)

all_rows = len(df)
print("Доля нативных немцев в выборке -", result_rows/all_rows)

"""Вариант 2"""

is_german = len(df[df['native-country'] == 'Germany'])
print("Количество нативных немцев в выборке -", is_german)

all_rows = len(df)
print("Доля нативных немцев в выборке -", is_german/all_rows)

"""**4. Средние значения возраста получающих более 50к и менее 50к в год**

Вариант 1
"""

is_more_50 = df.apply(lambda x: x['age'] if x['salary'] == '>50K' else 0, axis=1)
is_less_50 = df.apply(lambda x: x['age'] if x['salary'] == '<=50K' else 0, axis=1)

more_rows = is_more_50[is_more_50 != 0]
less_rows = is_less_50[is_less_50 != 0]

print("Средний возраст получающих больше 50k -", more_rows.mean())
print("Средний возраст получающих меньше 50k -", less_rows.mean())

"""Вариант 2"""

is_more_50 = df[df['salary'] == '>50K']
is_less_50 = df[df['salary'] == '<=50K']

print("Средний возраст получающих больше 50k -", is_more_50['age'].mean())
print("Средний возраст получающих меньше 50k -", is_less_50['age'].mean())

"""**5. Среднеквадратичные отклонения возраста получающих более 50к и менее 50к в год**

Для варианта 4.1
"""

print("Среднеквадратичные отклонения получающих больше 50K -", more_rows.std())
print("Среднеквадратичные отклонения получающих меньше 50K -", less_rows.std())

"""Для варианта 4.2"""

print("Среднеквадратичные отклонения получающих больше 50K -", is_more_50['age'].std())
print("Среднеквадратичные отклонения получающих меньше 50K -", is_less_50['age'].std())

"""**6. Получающие больше 50K имеют минимум высшее образование (да/нет)**

Вариант 1
"""

education = df.apply(lambda x: x['education'] if x['salary'] == '>50K' else 'NaN', axis=1)

suitable_education = ['Bachelors', 'Prof-school', 'Assoc-asdm', 'Assoc-voc', 'Masters', 'Doctorate']

if education.any() not in suitable_education:
  print("Найдена как минимум одна строка без высшего образования, ответ 'Нет'")
else:
  print("Строки без высшего образования не найдены, ответ 'Да'")

"""Вариант 2"""

education = df.apply(lambda x: x['education'] if x['salary'] == '>50K' else 'NaN', axis=1)
education = education.drop(education[education == 'NaN'].index) #Удаление тех, у кого меньше 50к

suitable_education = ['Bachelors', 'Prof-school', 'Assoc-asdm', 'Assoc-voc', 'Masters', 'Doctorate']

higher_education = education.apply(lambda x: x if x in suitable_education else 'NaN')
higher_education = higher_education.drop(higher_education[higher_education == 'NaN'].index) #Удаление тех, у кого не высшее образование

print('Число строк зарабатывающих больше 50к -', len(education))
print('Число строк зарабатывающих 50к с высшим образованием -', len(higher_education))

if len(education) > len(higher_education):
  print("Ответ 'Нет', так как найдены строки без высшего образования в количестве -", len(education) - len(higher_education))
else:
  print("Строк без высшего образования не найдено, ответ 'Да'")

"""**7. Статистика возраста для каждой расы и каждого пола**"""

#Статистика возраста для всех рас
print(df.groupby('race')['age'].describe())

#Статистика возраста для обоих полов
print(df.groupby('sex')['age'].describe())

#Максимальный возраст мужчин Amer-Indian-Eskimo ---- Вариант 1
american = df.apply(lambda x: x['age'] if x['race'] == 'Amer-Indian-Eskimo' and x['sex'] == 'Male' else 0, axis=1)
print("Максимальный возраст мужчин Amer-Indian-Eskimo -", american[american == american.max()].to_string(index=False))

#Максимальный возраст мужчин Amer-Indian-Eskimo ---- Вариант 2
print("Максимальный возраст мужчин Amer-Indian-Eskimo -", df[((df["race"] == "Amer-Indian-Eskimo") & (df["sex"] == 'Male'))]['age'].max())

"""**8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин**"""

marital = df.apply(lambda x: x['marital-status'] if x['salary'] == '>50K' else 'NaN', axis=1)
marital = marital.drop(marital[marital == 'NaN'].index) #Удаление тех, у кого меньше 50к

married_statuses = ["Married-civ-spouse", "Married-spouse-absent" "Married-AF-spouse"]

married_set = marital.apply(lambda x: x if x in married_statuses else 'NaN')
not_married_set = marital.apply(lambda x: x if x not in married_statuses else 'NaN')

married_set = married_set.drop(married_set[married_set == 'NaN'].index) #Удаление неженатых из списка женатых
notMarriedSet = notMarriedSet.drop(notMarriedSet[not_married_set == 'NaN'].index) #Удаление женатых из списка неженатых

if len(married_set) > len(not_married_set):
  print("Доля женатых среди богатых больше и составляет", len(married_set)/len(marital)*100, "процентов")
else:
  print("Доля неженатых среди богатых больше и состаляет", len(not_married_set)/len(marital)*100, "процентов")

"""**9. Какое максимальное число часов человек работает в неделю (признак hours-per-week)? Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?**"""

max_work_time = df['hours-per-week'].max()

target_df = df.loc[df['hours-per-week'] == max_work_time]

high_salary_df = target_df[target_df['salary'] == '>50K']

print(len(target_df), "человек работают", max_work_time, "часов в неделю.")
print("Среди них", len(high_salary_df)/len(target_df)*100, "процентов зарабатывает много")

"""**10. Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary) для каждой страны (native-country).**"""

high_salary_df = df[df['salary'] == '>50K']

print(high_salary_df.groupby("native-country")["hours-per-week"].mean())

low_salary_df = df[df['salary'] == '<=50K']

print(low_salary_df.groupby("native-country")["hours-per-week"].mean())
import pandas as pd

df = pd.DataFrame({
    'name': ['Маша', 'Вася', 'Эдуард'], 
    'age': [25, 8, 48], 
    'job': ['Программист', 'Школьник', 'Big Boss'],
    'salary': [100, 10, 200]
})

if __name__ == "__main__":
# Возможность выбрать столбец 
    print("\ndf['name']:")
    print(f"{df['name']}")
# Фильтрация 
    print("\ndf[df['age'] > 18]:")
    print(f"{df[df['age'] > 18] }")
# Математические операции 
    df['salary'] *= 2
    print("\ndf['salary'] *= 2")
    print(f"{df['salary']}")
# Транспонирование    
    print("\ndf.T")
    print(f"{df.T}")

# Доступ к данным
# обращение по индексу
    print(f"{df.loc[1:2]  = }")
# обращение по номеру строки
    print(f"{df.iloc[2]  = }")
# срезы по строкам 
    print(f"{df.iloc[:1]  = }")
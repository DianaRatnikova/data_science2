from unicodedata import name
import pandas as pd
import  numpy as np

if __name__ == "__main__":
    my_series = pd.Series([4, 7, -5, 3, -1])
    print(my_series)
    print(f"{my_series.values = }")
    print(f"{my_series.index = }")

#   Обращение по индексу 
    print("\nmy_series[1]:")
    print(f"{my_series[1]}")
#   срезы 
    print("\nmy_series[:2]")
    print(f"{my_series[:2]}")
#   Фильтрация 
    print("\nmy_series[my_series > 0]")
    print(f"{my_series[my_series > 0]}")
#   Математические операции
    print("\nmy_series * 10") 
    print(f"{my_series * 10 }")
#  numpy    
    print(f"\nnp.exp(my_series)")
    print(f"{np.exp(my_series) }")


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('salarios.csv')

print('Dados do arquivo CSV:')
print(df)

plt.figure(figsize=(8,5))
plt.bar(df['Nome'], df['Salario'],color= 'skyblue')
plt.title('Salario por Pessoa')
plt.xlabel('Nome')
plt.ylabel('Salario')
plt.show()
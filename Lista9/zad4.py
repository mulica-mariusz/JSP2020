import matplotlib.pyplot as plt
import numpy as np

langs = ['C', 'Java', 'Python', 'C++', 'C#', 'VB', 'JS', 'PHP', 'R', 'Groovy']
ratings = [17.38, 11.96, 11.72, 7.56, 3.95, 3.84, 2.20, 1.99, 1.90, 1.84]
plt.bar(langs,ratings)
x = np.arange(len(langs))
plt.xticks(x, langs)
plt.ylabel('Popularnosć [%]')
plt.title('Wykres popularności języków programowania')
plt.show()

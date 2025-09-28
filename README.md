# matplstudy
python matplotlib study

## code
**모든 값은 임의로 설정한 값들이므로, 실제 데이터와 무관하다. 말그대로 내가 학습할려고 만든 데이터다.**

### matplstudy.py
```python
import matplotlib.pyplot as plt
import numpy as np

Xdata = np.random.random(50) * 100
Ydata = np.random.random(50) * 100

plt.scatter(Xdata, Ydata, c= "green", marker = "*", s = 50)
plt.show()

```

<img width="640" height="480" alt="malp1" src="https://github.com/user-attachments/assets/baffbd81-90df-4e34-8ba9-0ea1517d38fd" />


### matplstudy2.py
```python
import matplotlib.pyplot as plt
import numpy as np

years = [2006 + x for x in range(16)]
weigth = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80,
          82, 82, 83, 81, 80, 79]

plt.plot(years, weigth, c="green", lw=3, linestyle="-")
plt.show()
```

<img width="640" height="480" alt="malp2" src="https://github.com/user-attachments/assets/47a234d4-83cb-4e29-a626-1a7f5ac0a352" />


### matplstudy3.py
```python
import matplotlib.pyplot as plt
import numpy as np

x = ["C++", "C#", "Python", "Jave", "Go"]

y = [20, 50, 140, 100, 45]

plt.bar(x, y, color='green', align='edge', width=0.5, edgecolor='red', lw=6)
plt.show()
```

<img width="640" height="480" alt="malp3" src="https://github.com/user-attachments/assets/14e2697c-238e-4d8d-80ec-a6323d9f48fa" />


### matplstudy4.py
```python
import matplotlib.pyplot as plt
import numpy as np

age = np.random.normal(20, 1.5, 1000)

plt.hist(age, bins='auto', cumulative=True)
plt.show()
```

<img width="640" height="480" alt="malp4" src="https://github.com/user-attachments/assets/fedcb32f-6b26-43dc-8828-bcdd81d75dff" />


### matplstudy5.py
```python
import matplotlib.pyplot as plt
import numpy as np

lang = ["C++", "C#", "Python", "Jave", "Go"]
votes = [50, 24, 14, 10, 17]
explode = [0, 0, 0, 0.2, 0]

plt.pie(votes, labels=lang, autopct='%.2f%%', explode=explode)
plt.show()
```
<img width="640" height="480" alt="malp5" src="https://github.com/user-attachments/assets/4783b007-1753-457c-a491-f2bdad0a63e5" />


### matplstudy6.py
```python
import matplotlib.pyplot as plt
import numpy as np

year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
income = [55, 56, 62, 61, 72, 72, 73, 75]

income_ticks = list(range(50, 81, 2))

plt.plot(year, income, color='blue')
plt.title('Income of John')

plt.xlabel('Year')
plt.ylabel('Income In USD')

plt.show()
```
<img width="640" height="480" alt="malp6" src="https://github.com/user-attachments/assets/ff92eb6d-c530-4e3c-9f04-61762ef476e3" />


### matplstudy7.py
```python
import matplotlib.pyplot as plt
import numpy as np

stock_a = [100, 102, 99, 101, 101, 100, 102]
stock_b = [98, 95, 102, 104, 105, 103, 109]
stock_c = [110, 115, 100, 105, 100, 98, 95]

plt.plot(stock_a, label='A')
plt.plot(stock_b, label='B')
plt.plot(stock_c, label='C')

plt.legend(loc='lower right')
plt.show()
```
<img width="640" height="480" alt="malp7" src="https://github.com/user-attachments/assets/bf51f73c-b455-453b-be09-22fec6cd7da1" />


### matplstudy8.py
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('dark_background')

votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes, labels=None)
plt.legend(labels=people)

plt.show()

```

<img width="640" height="480" alt="malp8" src="https://github.com/user-attachments/assets/2d41e229-bf66-4feb-bc8c-6b4b87f1c53e" />

### matplstudy9.py
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(x1, y1)

plt.figure(2)
plt.plot(x2, y2)

plt.show()
```
<img width="640" height="480" alt="malp9" src="https://github.com/user-attachments/assets/806fd839-5997-49d1-848c-1bfec5847449" />


### matplstudy10.py
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

x = np.arange(100)

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, np.sin(x))
ax[0, 0].set_title('Sine Wave')

ax[0, 1].plot(x, np.cos(x))
ax[0, 1].set_title('Cosine Wave')

ax[1, 0].plot(x, np.random.random(100))
ax[1, 0].set_title('Random Function')

ax[1, 1].plot(x, np.log(x + 1))
ax[1, 1].set_title('Log Function')
ax[1, 1].set_xlabel('x')

fig.suptitle('Four Plots')

plt.tight_layout()
plt.savefig('plot.png', dpi = 300)
```
<img width="1920" height="1440" alt="malp10" src="https://github.com/user-attachments/assets/e1e7aefc-950a-419a-8a1d-dd652344ffc6" />


### matplstudy11.py
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

ax = plt.axes(projection='3d')

x = np.arange(0, 50, 0.1)
y = np.sin(x)
z = np.cos(x)

ax.scatter(x,y,z)
ax.set_title("3D Plot")

plt.show()
```
<img width="640" height="480" alt="malp11" src="https://github.com/user-attachments/assets/9139fc3b-b57f-48eb-86b2-566835f56142" />


### matplstudy12.py
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

ax = plt.axes(projection='3d')

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# ax.plot_surface(X,Y,Z)
ax.plot_surface(X,Y,Z, cmap="Spectral")
ax.set_title("3D Plot")

plt.show()
```
<img width="640" height="480" alt="malp12" src="https://github.com/user-attachments/assets/09e1aea9-83cd-4bc9-9955-8d7b1e643ab3" />

I studied with this YouTube video(NeuralNine - Matplotlib Full Python Course - Data Science Fundamentals)

import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import waffle

data = {'Keyword': ['Men', 'Women'],
        'Number': [2887, 9398]
        }

df = pd.DataFrame(data)
fig = plt.figure(
    FigureClass=waffle,
    rows=5,
    values=df.Number,
    labels=list(df.Keyword)  # Corrected the argument name to 'labels'
)

plt.show()
print("success")

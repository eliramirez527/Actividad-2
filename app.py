import streamlit as st
import matplotlib.pyplot as plt

# Crea algunos datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crea un gráfico
plt.plot(x, y)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Muestra el gráfico en Streamlit
st.pyplot(plt)

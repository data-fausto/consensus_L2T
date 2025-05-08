
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulazione di Consenso", layout="centered")
st.title("🤝 Simulazione di Consenso tra 4 Amici")

st.write("""
Immagina che 4 amici vogliano decidere un orario per incontrarsi fra 15 giorni.
Ogni giorno, si scambiano informazioni secondo una rete fissa:

**1 ↔ 2 ↔ 3 ↔ 4**

Ogni amico aggiorna il proprio orario facendo la media con i vicini.
""")

st.header("Inserisci l'orario iniziale di ciascun amico (tra 0 e 24)")

x0 = []
cols = st.columns(4)
for i in range(4):
    val = cols[i].number_input(f"Amico {i+1}", min_value=0.0, max_value=24.0, value=float(8 + i*2), step=0.5)
    x0.append(val)

# Parametri
steps = 15
x_history = [x0]

# Matrice di adiacenza per la topologia lineare 1-2-3-4
W = np.array([
    [0.5, 0.5, 0.0, 0.0],
    [0.5, 0.0, 0.5, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.0, 0.0, 0.5, 0.5]
])

# Simulazione
x = np.array(x0)
for _ in range(steps):
    x = W @ x
    x_history.append(x.copy())

x_history = np.array(x_history)

# Grafico
st.header("📊 Evoluzione degli orari")
fig, ax = plt.subplots()
for i in range(4):
    ax.plot(range(steps+1), x_history[:, i], label=f"Amico {i+1}")

ax.set_xlabel("Giorni")
ax.set_ylabel("Orario proposto")
ax.set_title("Raggiungimento del consenso")
ax.set_ylim(0, 24)
ax.grid(True)
ax.legend()
st.pyplot(fig)

st.success("Dopo 15 giorni, gli amici raggiungono un orario comune!")

import numpy as np
import matplotlib.pyplot as plt

# Fonction pour calculer la probabilité d'acceptation
def acceptance_probability(delta, temperature):
    return np.exp(-delta / temperature)

# Paramètres
delta = 10 # Différence de coût fixe
temperatures = np.linspace(1, 100, 500)  # Plage de températures de 1 à 100

# Calcul des probabilités pour différentes températures
probabilities = [acceptance_probability(delta, T) for T in temperatures]

# Création de la figure
plt.figure(figsize=(10, 6))
plt.plot(temperatures, probabilities, linewidth=2.5)
plt.grid(True, linestyle='--', alpha=0.7)

# Ajout des labels et du titre
plt.xlabel('Température (T)', fontsize=12)
plt.ylabel('Probabilité d\'acceptation', fontsize=12)
plt.title(f'Probabilité d\'acceptation en fonction de la température (Δ = {delta})', fontsize=14)

# Ajout de repères pour certaines températures
specific_temps = [5, 10, 20, 50, 100]
for temp in specific_temps:
    prob = acceptance_probability(delta, temp)
    plt.plot([temp], [prob], 'ro')
    plt.annotate(f'T={temp}: {prob:.3f}', 
                 xy=(temp, prob),
                 xytext=(temp+5, prob),
                 arrowprops=dict(arrowstyle='->'))

# Ajout d'une légende pour expliquer le concept
plt.figtext(0.5, 0.01, 
            f"Plus la température est élevée, plus la probabilité d'accepter une solution moins bonne est grande.\n"
            f"Pour Δ={delta}, quand T=10, P={acceptance_probability(delta, 10):.3f}, mais quand T=50, P={acceptance_probability(delta, 50):.3f}",
            ha='center', fontsize=10)

# Ajout d'une fonctionnalité pour permettre à l'utilisateur de voir l'impact de différentes valeurs de delta
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('acceptance_probability.png', dpi=300)
plt.show()

# Version interactive avec slider pour delta
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)

# Configuration initiale
initial_delta = 10
temperatures = np.linspace(1, 100, 500)
line, = plt.plot(temperatures, [acceptance_probability(initial_delta, T) for T in temperatures], linewidth=2.5)

# Personnalisation du graphique
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('Température (T)', fontsize=12)
plt.ylabel('Probabilité d\'acceptation', fontsize=12)
plt.title(f'Probabilité d\'acceptation en fonction de la température (Δ = {initial_delta})', fontsize=14)

# Ajout du slider pour delta
ax_delta = plt.axes([0.25, 0.1, 0.65, 0.03])
delta_slider = Slider(
    ax=ax_delta,
    label='Δ (delta)',
    valmin=1,
    valmax=50,
    valinit=initial_delta,
    valstep=1
)

# Fonction pour mettre à jour le graphique quand delta change
def update(val):
    current_delta = delta_slider.val
    line.set_ydata([acceptance_probability(current_delta, T) for T in temperatures])
    plt.title(f'Probabilité d\'acceptation en fonction de la température (Δ = {current_delta})', fontsize=14)
    fig.canvas.draw_idle()

delta_slider.on_changed(update)

plt.show()
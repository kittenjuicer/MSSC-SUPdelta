import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

np.random.seed(42)
width, height = 8.5, 11.0
dpi = 600
fig_width_px = int(width * dpi)
fig_height_px = int(height * dpi)

fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
ax.set_facecolor('white')
ax.set_xlim(0, fig_width_px)
ax.set_ylim(0, fig_height_px)
ax.axis('off')

center_x = fig_width_px / 2
center_y = fig_height_px / 2

num_points = 25000
tower_levels = 5
n_base = 2.5
m_base = 2.5

positions = []
for i in range(num_points):
    nx = np.random.uniform(-1.5, 1.5)
    ny = np.random.uniform(-1.5, 1.5)
    base_amp = np.abs(np.sin(n_base * np.pi * nx) * np.cos(m_base * np.pi * ny))
    tower_amp = 0.0
    for layer in range(1, tower_levels + 1):
        tower_amp += np.abs(np.sin((n_base + layer) * np.pi * nx * 1.414) * 
                           np.cos((m_base + layer) * np.pi * ny * 0.707)) * (1.0 / layer)
    amplitude = base_amp + tower_amp * 0.6
    torsion_x = np.cos(tower_levels * 1.618 * nx) * np.sin(tower_levels * 0.618 * ny)
    torsion_y = np.sin(tower_levels * 1.618 * nx) * np.cos(tower_levels * 0.618 * ny)
    
    if amplitude > 0.85:
        px = center_x + nx * (fig_width_px / 3) + torsion_x * 50
        py = center_y + ny * (fig_height_px / 3) + torsion_y * 50
        px += np.random.normal(0, 8)
        py += np.random.normal(0, 8)
        positions.append((px, py))

for px, py in positions:
    if 0 < px < fig_width_px and 0 < py < fig_height_px:
        circle = Circle((px, py), radius=3, color='black', fill=True)
        ax.add_patch(circle)

plt.text(fig_width_px * 0.05, fig_height_px * 0.95, 
         'SEMANTIC SPHERE ALGEBRAIC METASURFACE PANEL\n'
         'OpenAI Unit-Distance Lattice × MSSC Flowstate (May 2026)\n'
         'Denser constructive interference via class-field towers',
         fontsize=14, fontweight='bold', color='black', va='top', ha='left')

plt.text(fig_width_px * 0.05, fig_height_px * 0.05, 
         'Print • Hold to sunlight/garden light • Observe halos & interference\n'
         'Companion to flowstate.cpp • Low-I utility priming tool',
         fontsize=10, color='black', va='bottom', ha='left')

plt.savefig('Semantic_Sphere_Metasurface_Panel.pdf', bbox_inches='tight', dpi=dpi)
plt.savefig('Semantic_Sphere_Metasurface_Panel.png', bbox_inches='tight', dpi=dpi)
plt.close()
print("✅ Panel generated! Print Semantic_Sphere_Metasurface_Panel.pdf at 100% scale.")
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def generate_garden_layer(layer_id, num_points=14000, dpi=600):
    np.random.seed(42 + layer_id)
    width, height = 8.5, 11.0
    px_w, px_h = int(width * dpi), int(height * dpi)
    center_x, center_y = px_w / 2, px_h / 2
    
    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    ax.set_facecolor('white')
    ax.set_xlim(0, px_w)
    ax.set_ylim(0, px_h)
    ax.axis('off')
    
    tower_level = 2.8 + layer_id * 0.85          # gentle organic growth
    n_base = 1.8 + layer_id * 0.35               # smoother Fuchsian flow for nature
    m_base = 2.2 + layer_id * 0.45               # elliptic smoothness for living motion
    
    positions = []
    for i in range(num_points):
        nx = np.random.uniform(-1.65, 1.65)
        ny = np.random.uniform(-1.65, 1.65)
        
        base_amp = np.abs(np.sin(n_base * np.pi * nx) * np.cos(m_base * np.pi * ny))
        tower_amp = 0.0
        for l in range(1, int(tower_level)+1):
            tower_amp += np.abs(np.sin((n_base + l) * np.pi * nx * 1.414) * 
                               np.cos((m_base + l) * np.pi * ny * 0.707)) * (1.0 / l)
        amplitude = base_amp + tower_amp * 0.58
        
        # Gentle organic torsion for garden feel
        torsion_x = np.cos(tower_level * 1.618 * nx * 0.9) * np.sin(tower_level * 0.618 * ny)
        torsion_y = np.sin(tower_level * 1.618 * nx) * np.cos(tower_level * 0.618 * ny * 0.9)
        
        if amplitude > 0.82:
            px = center_x + nx * (px_w / 3.15) + torsion_x * 32
            py = center_y + ny * (px_h / 3.15) + torsion_y * 32
            # Natural clustering (more organic than uniform)
            px += np.random.normal(0, 7 + layer_id*0.6)
            py += np.random.normal(0, 7 + layer_id*0.6)
            positions.append((px, py))
    
    for px, py in positions:
        if 0 < px < px_w and 0 < py < px_h:
            r = 2.6 + (layer_id % 5) * 0.35   # subtle size variation for living feel
            circle = Circle((px, py), radius=r, color='black', fill=True)
            ax.add_patch(circle)
    
    ax.text(px_w*0.05, px_h*0.94, 
            f'LIFE FLOW LAYER {layer_id+1}\nGarden Awareness Tower\nDepth {tower_level:.1f}', 
            fontsize=20, fontweight='bold', color='black', alpha=0.11, va='top', ha='left')
    
    filename = f'GardenLifeFlow_layer_{layer_id+1:02d}.png'
    plt.savefig(filename, bbox_inches='tight', dpi=dpi)
    plt.close()
    print(f"✅ {filename} generated")

# Generate the full 10-layer Garden LifeFlow stack
for i in range(10):
    generate_garden_layer(i)
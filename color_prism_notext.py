import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.colors as mcolors

def generate_pocket_garden_layer(layer_id, num_points=9200, dpi=600):
    np.random.seed(42 + layer_id)
    size_inches = 5.5                      # square pocket size
    px = int(size_inches * dpi)
    
    fig, ax = plt.subplots(figsize=(size_inches, size_inches), dpi=dpi)
    ax.set_facecolor('#0a0f1a')            # deep garden twilight
    ax.set_xlim(0, px)
    ax.set_ylim(0, px)
    ax.axis('off')
    
    tower_level = 2.6 + layer_id * 0.78
    n_base = 1.65 + layer_id * 0.31        # circular wing-arc flow
    m_base = 2.35 + layer_id * 0.42        # elliptic living motion
    
    # Garden LifeFlow palette - golden SUP, cyan nodes, soft greens/blues
    colors = ['#f8d68a', '#c8f0ff', '#a8e0c0', '#e0f8ff', '#ffe8b0']
    
    positions = []
    for i in range(num_points):
        nx = np.random.uniform(-1.65, 1.65)
        ny = np.random.uniform(-1.65, 1.65)
        
        base_amp = np.abs(np.sin(n_base * np.pi * nx) * np.cos(m_base * np.pi * ny))
        tower_amp = 0.0
        for l in range(1, int(tower_level)+1):
            tower_amp += np.abs(np.sin((n_base + l) * np.pi * nx * 1.414) * 
                               np.cos((m_base + l) * np.pi * ny * 0.707)) * (1.0 / l)
        amplitude = base_amp + tower_amp * 0.62
        
        # Organic torsion tuned for garden flow
        torsion_x = np.cos(tower_level * 1.618 * nx * 0.92) * np.sin(tower_level * 0.618 * ny)
        torsion_y = np.sin(tower_level * 1.618 * nx) * np.cos(tower_level * 0.618 * ny * 0.88)
        
        if amplitude > 0.81:
            px_pos = px/2 + nx * (px / 3.05) + torsion_x * 29
            py_pos = px/2 + ny * (px / 3.05) + torsion_y * 29
            px_pos += np.random.normal(0, 7.2 + layer_id*0.5)
            py_pos += np.random.normal(0, 7.2 + layer_id*0.5)
            positions.append((px_pos, py_pos, amplitude))
    
    for px_pos, py_pos, amp in positions:
        if 0 < px_pos < px and 0 < py_pos < px:
            color_idx = layer_id % len(colors)
            base_color = list(mcolors.to_rgb(colors[color_idx]))
            intensity = min(1.0, amp * 1.75)
            r = min(1.0, max(0.0, base_color[0] * 0.72 + 0.32 * intensity))
            g = min(1.0, max(0.0, base_color[1] * 0.88 + 0.35 * (1 - intensity)))
            b = min(1.0, max(0.0, base_color[2] * 0.68 + 0.55 * intensity))
            dot_color = (r, g, b)
            
            radius = 2.45 + (layer_id % 4) * 0.42
            circle = Circle((px_pos, py_pos), radius=radius, color=dot_color, fill=True, alpha=0.93)
            ax.add_patch(circle)
            
            if amp > 0.94:  # cyan node glow
                glow = Circle((px_pos, py_pos), radius=radius*1.85, color='#a0f0ff', fill=False, linewidth=0.65, alpha=0.19)
                ax.add_patch(glow)
    
  
    
    filename = f'GardenLifeFlow_Pocket_Color_layer_notext{layer_id+1:02d}.png'
    plt.savefig(filename, bbox_inches='tight', dpi=dpi, facecolor=fig.get_facecolor())
    plt.close()
    print(f"✅ {filename} generated ({size_inches}″ square)")

# Run for 10 layers (one full prism + extras for multiples)
for i in range(10):
    generate_pocket_garden_layer(i)
import numpy as np

# Task 2: Environment Setup & Synthetic Image Matrix Creation
h, w, c = 300, 400, 3
img = np.zeros((h, w, c), dtype=np.uint8)

half_h = h // 2
half_w = w // 2

# Fill the four quadrants
img[0:half_h, 0:half_w] = [255, 0, 0]      # Top-Left: Pure Red
img[0:half_h, half_w:w] = [0, 255, 0]      # Top-Right: Pure Green
img[half_h:h, 0:half_w] = [0, 0, 255]      # Bottom-Left: Pure Blue
img[half_h:h, half_w:w] = [255, 255, 255]  # Bottom-Right: White

print("--- SYNTHETIC MATRIX METRICS ---")
print(f"Array Shape (H, W, C): {img.shape}")
print(f"Data Type: {img.dtype}")
print(f"Total Elements: {img.size:,} values")
print(f"Memory Footprint: {img.nbytes:,} bytes ({img.nbytes / 1024:.2f} KB)")
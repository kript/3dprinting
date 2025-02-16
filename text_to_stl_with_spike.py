import numpy as np
import trimesh
from PIL import Image, ImageDraw, ImageFont

def text_to_3d_stl(text, font, output_file, size=(200, 50), height=5, spike_height=20, spike_radius=5):
    img = Image.new("L", size, color=0)
    draw = ImageDraw.Draw(img)
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    draw.text(text_position, text, font=font, fill=255)
    
    # Convert image to heightmap
    img_array = np.array(img) / 255.0  # Normalize to range [0, 1]
    img_array = np.flipud(img_array) * height  # Flip vertically and scale height
    
    # Generate mesh from heightmap
    img_array_3d = img_array[..., np.newaxis]  # Convert 2D to 3D by adding a new axis
    voxel_grid = trimesh.voxel.VoxelGrid(encoding=img_array_3d)
    text_mesh = voxel_grid.as_boxes()
    
    # Create spike (cone shape)
    spike = trimesh.creation.cone(radius=spike_radius, height=spike_height, sections=20)
    
    # Position the spike below the text
    spike.apply_translation([size[0] / 2, size[1] / 2, -spike_height])
    
    # Combine text mesh and spike
    combined_mesh = trimesh.util.concatenate([text_mesh, spike])
    
    # Export to STL
    combined_mesh.export(output_file)
    print(f"STL file saved as {output_file}")

import os

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found: {font_path}")
else:
    print(f"Font file found at: {font_path}")

try:
    font = ImageFont.truetype(font_path, 50)
    print("Font loaded successfully!")
except OSError as e:
    print(f"Font loading error: {e}")

# Corrected function call to pass the loaded font object
text_to_3d_stl(
    text="Hello",
    font=font,  # Pass the font object directly
    output_file="hello_text_with_spike.stl",
    size=(300, 100),
    height=5,
    spike_height=20,  # Height of spike
    spike_radius=5  # Radius of spike base
)


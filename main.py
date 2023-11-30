"""Soft Robotic Exoskeleton for Tremor Suppression Presentation.

Final project for Computer-Aided Design (MECE3030U), Dr. Aaron Yurkewich.

Code written by: Daniel Jeon (https://github.com/danielljeon)
"""

from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import art3d
from stl import mesh


def merge_stls_y(scope: list[str], output_file_path: str | None = None) -> str:
    """Merge 2 STLs on the y-axis.

    Args:
        scope: List of STLs defined by their file paths.
        output_file_path: Output file path, defaults to untitled_{datetime.now().isoformat()}.stl.

    Returns:
        Output / result file path.
    """
    # Ensure scope has at least 2 mesh.Mesh to merge.
    if not scope or len(scope) < 2:
        raise ValueError('"scope_meshes" must have at least 2 STL file paths to mesh')

    if output_file_path is None:
        output_file_path = f"untitled_{datetime.now().isoformat()}.stl"
    if not output_file_path.lower().endswith(".stl"):
        output_file_path += ".stl"

    combined_mesh = mesh.Mesh.from_file(scope[0])

    for i in range(1, len(scope)):  # Iterate from index 1 to get current and previous index.
        # Load target STL files.
        new_mesh = mesh.Mesh.from_file(scope[i])

        # Translation.
        current_mesh_max_y = max(combined_mesh.y.flatten())
        new_mesh_min_y = min(new_mesh.y.flatten())
        translation_vec = np.array([0, (current_mesh_max_y - new_mesh_min_y), 0])
        new_mesh.translate(translation_vec)

        # Combine the two meshes.
        combined_mesh = mesh.Mesh(np.concatenate([combined_mesh.data, new_mesh.data]))

    # Save the merged mesh to a new STL file.
    combined_mesh.save(output_file_path)

    return output_file_path


def get_max_dimensions(file_path: str) -> list[int]:
    """Get maximum dimensions of an STL file.

    Args:
        file_path: File path.

    Returns:
        [x, y, z] maximum lengths
    """
    # Load STL file.
    stl_mesh = mesh.Mesh.from_file(file_path)

    # Extract all axis coordinates.
    x_coordinates = stl_mesh.x.flatten()
    y_coordinates = stl_mesh.y.flatten()
    z_coordinates = stl_mesh.z.flatten()

    # Find minimum and maximum of each axis.
    return [
        max(x_coordinates) - min(x_coordinates),
        max(y_coordinates) - min(y_coordinates),
        max(z_coordinates) - min(z_coordinates),
    ]


def display_stl(file_path: str, name: str = "untitled"):
    """Matplotlib display of STL files.

    Args:
        file_path: File path of STL file.
        name: Name for window / plot naming.
    """
    # Load STL file.
    stl_mesh = mesh.Mesh.from_file(file_path)

    # Create a new plot.
    figure = plt.figure()
    axes = figure.add_subplot(111, projection="3d")

    # Window name.
    plt.get_current_fig_manager().set_window_title(name)

    # Plot name.
    # axes.set_title("Name")

    # Create a Poly3DCollection object.
    poly_collection = art3d.Poly3DCollection(stl_mesh.vectors)

    # Set properties for the collection (like color, edge color, etc).
    poly_collection.set_facecolor([0.5, 0.5, 1, 0.6])  # Face RGBA color.
    poly_collection.set_edgecolor([0, 0, 0, 0.05])  # Edge RGBA color.

    # Add the collection to the axes.
    axes.add_collection3d(poly_collection)

    # Auto-scale to the mesh size.
    scale = stl_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen.
    plt.show()

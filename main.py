"""Soft Robotic Exoskeleton for Tremor Suppression Presentation.

Final project for Computer-Aided Design (MECE3030U), Dr. Aaron Yurkewich.

Code written by: Daniel Jeon (https://github.com/danielljeon)
"""

from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import art3d
from stl import mesh


def merge_stls_y(scope: list[str]) -> mesh.Mesh:
    """Merge 2 STLs on the y-axis.

    Args:
        scope: List of STLs defined by their file paths.

    Returns:
        Output / result file path.
    """
    # Ensure scope has at least 2 mesh.Mesh to merge.
    if not scope or len(scope) < 2:
        raise ValueError('"scope_meshes" must have at least 2 STL file paths to mesh')

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

    return combined_mesh


def save_mesh_to_stl(target_mesh: mesh.Mesh, output_file_path: str | None = None) -> str:
    """Save mesh to STL file format.

    Args:
        target_mesh: Input mesh object.
        output_file_path: Output file path, defaults to untitled_{datetime.now().isoformat()}.stl.

    Returns:
        Output file path.
    """
    if output_file_path is None:
        output_file_path = f"untitled_{datetime.now().isoformat()}.stl"
    if not output_file_path.lower().endswith(".stl"):
        output_file_path += ".stl"

    target_mesh.save(output_file_path)

    return output_file_path


def get_max_dimensions(target: mesh.Mesh | str) -> list[int]:
    """Get maximum dimensions of an STL file.

    Args:
        target: File path or mesh.

    Returns:
        [x, y, z] maximum lengths
    """
    if isinstance(target, str):
        # Load STL file.
        stl_mesh = mesh.Mesh.from_file(target)
    elif isinstance(target, mesh.Mesh):
        stl_mesh = target
    else:
        raise ValueError('"target" must be either a file path or mesh')

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


def display_stl(target: mesh.Mesh | str, name: str = "untitled"):
    """Matplotlib display of a mesh or STL file.

    Args:
        target: File path or mesh.
        name: Name for window / plot naming.
    """
    if isinstance(target, str):
        # Load STL file.
        stl_mesh = mesh.Mesh.from_file(target)
    elif isinstance(target, mesh.Mesh):
        stl_mesh = target
    else:
        raise ValueError('"target" must be either a file path or mesh')

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

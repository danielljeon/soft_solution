"""Soft Robotic Exoskeleton for Tremor Suppression Presentation.

Final project for Computer-Aided Design (MECE3030U), Dr. Aaron Yurkewich.

Code written by: Daniel Jeon (https://github.com/danielljeon)
"""

import csv
from datetime import datetime

# TODO (danielljeon): Very bad practice. Temporary code.
from main import merge_stls_y, display_stl


class STLComponent:
    def __init__(
            self,
            name: str,
            finger_file_path: str | None,
            mold1_file_path: str | None,
            mold2_file_path: str | None,
            mold3_file_path: str | None,
    ):
        """STL component class for axis merging.

        Args:
            name: Name for simple identification.
            finger_file_path:
        """
        self._name = name
        self._finger_file_path = finger_file_path
        self._mold1_file_path = mold1_file_path
        self._mold2_file_path = mold2_file_path
        self._mold3_file_path = mold3_file_path

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def finger_file_path(self) -> str:
        return self._finger_file_path

    @finger_file_path.setter
    def finger_file_path(self, finger_file_path: str) -> None:
        self._finger_file_path = finger_file_path

    @property
    def mold1_file_path(self) -> str:
        return self._mold1_file_path

    @mold1_file_path.setter
    def mold1_file_path(self, mold1_file_path: str) -> None:
        self._mold1_file_path = mold1_file_path

    @property
    def mold2_file_path(self) -> str:
        return self._mold2_file_path

    @mold2_file_path.setter
    def mold2_file_path(self, mold2_file_path: str) -> None:
        self._mold2_file_path = mold2_file_path

    @property
    def mold3_file_path(self) -> str:
        return self._mold3_file_path

    @mold3_file_path.setter
    def mold3_file_path(self, mold3_file_path: str) -> None:
        self._mold3_file_path = mold3_file_path

    def __str__(self):
        return self._name


# STANDARDIZED COMPONENTS.
TUBING = STLComponent(
    "TUBING",
    "stls/finger_tubing.stl",
    "stls/mold1_tubing.stl",
    "stls/mold2_tubing.stl",
    "stls/mold3_tubing.stl",
)
BEND = STLComponent(
    "BEND",
    "stls/finger_bend.stl",
    "stls/mold1_bend.stl",
    "stls/mold2_bend.stl",
    "stls/mold3_bend.stl",
)
CUT = STLComponent(
    "BEND_NO_CUT",
    "stls/finger_cut.stl",
    "stls/mold1_cut.stl",
    "stls/mold2_cut.stl",
    "stls/mold3_cut.stl",
)
SPACER = STLComponent(
    "SPACER",
    "stls/finger_1mm spacer.stl",
    "stls/mold1_1mm spacer.stl",
    "stls/mold2_1mm spacer.stl",
    "stls/mold3_1mm spacer.stl",
)
END_CAP = STLComponent(
    "END_CAP",
    "stls/finger_1mm spacer no channel.stl",
    "stls/mold1_1mm spacer no channel.stl",
    "stls/mold2_1mm spacer no channel.stl",
    "stls/mold3_1mm spacer no channel.stl",
)
MOLD_ENDS = STLComponent(
    "MOLD_ENDS",
    None,
    "stls/mold1_ends.stl",
    "stls/mold2_ends.stl",
    "stls/mold3_ends.stl",
)


def create(dimension_csv_file_path: str, display=False):
    dimension_data = {}

    # Read dimension CSV file.
    with open(dimension_csv_file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            row_data = [int(item) if item else None for item in row[1:]]
            # Save to dimension_data dictionary where the key is the first column, "name".
            dimension_data[row[0]] = row_data

    # Loop through all design specs.
    for i, (k, v) in enumerate(dimension_data.items()):
        print(i, k, v)

        # Calculate bend component counts.
        # bend_count = num_bend + n_bend_no_cut.
        # TODO (danielljeon): Counts are currently hard coded and should be scaled to finger size.
        seg1_spacer_count = 5
        mcp_bend_count = 2 + 1
        seg2_spacer_count = 5
        pip_bend_count = 1 + 1
        seg3_spacer_count = 5
        dip_bend_count = 1 + 1
        seg4_spacer_count = 5

        # Generate segment based scopes.
        seg1 = [SPACER for _ in range(seg1_spacer_count)]
        if mcp_bend_count > 0:
            if mcp_bend_count > 1:
                for _ in range(mcp_bend_count - 1):
                    seg1.append(BEND)
                    seg1.append(CUT)
            seg1 += [BEND]

        seg2 = [SPACER for _ in range(seg2_spacer_count)]
        if pip_bend_count > 0:
            if pip_bend_count > 1:
                for _ in range(pip_bend_count - 1):
                    seg2.append(BEND)
                    seg2.append(CUT)
            seg2 += [BEND]

        seg3 = [SPACER for _ in range(seg3_spacer_count)]
        if dip_bend_count > 0:
            if dip_bend_count > 1:
                for _ in range(dip_bend_count - 1):
                    seg3.append(BEND)
                    seg3.append(CUT)
            seg3 += [BEND]

        seg4 = [SPACER for _ in range(seg4_spacer_count)]

        # Get complete scope with tubing and end cap.
        scope = [TUBING] + seg1 + seg2 + seg3 + seg4 + [END_CAP, END_CAP, END_CAP]

        # Merge the STLs.
        result_file_path = merge_components_y(scope)

        # Display the final STL if selected in the function parameter.
        if display:
            display_stl(result_file_path)


def merge_components_y(
        scope_components: list[STLComponent],
        finger: bool = True,
        finger_output_file_paths: list[str] | None = None,
        mold1: bool = True,
        mold1_output_file_paths: list[str] | None = None,
        mold2: bool = True,
        mold2_output_file_paths: list[str] | None = None,
        mold3: bool = True,
        mold3_output_file_paths: list[str] | None = None,
) -> list[str]:
    # Ensure scope has at least 2 STLComponents to merge.
    if not scope_components or len(scope_components) < 2:
        raise ValueError('"scope_components" must have at least 2 STL file paths to mesh')

    output_file_paths = []

    # Update scopes for each component type.
    if finger:
        # Corrections to output_file_path.
        if finger_output_file_paths is None:
            finger_output_file_paths = f"finger_{datetime.now().isoformat()}.stl"

        # Convert to meshes.
        finger_file_paths = [component.finger_file_path for component in scope_components]

        # Merge meshes.
        output_file_paths.append(merge_stls_y(finger_file_paths, finger_output_file_paths))

    if mold1:
        # Corrections to output_file_path.
        if mold1_output_file_paths is None:
            mold1_output_file_paths = f"mold1_{datetime.now().isoformat()}.stl"

        # Add mold ends.
        mold1_scope_components = [MOLD_ENDS] + scope_components + [MOLD_ENDS]

        # Convert to meshes.
        mold1_file_paths = [component.mold1_file_path for component in mold1_scope_components]

        # Merge meshes.
        output_file_paths.append(merge_stls_y(mold1_file_paths, mold1_output_file_paths))

    if mold2:
        # Corrections to output_file_path.
        if mold2_output_file_paths is None:
            mold2_output_file_paths = f"mold2_{datetime.now().isoformat()}.stl"

        # Add mold ends.
        mold2_scope_components = [MOLD_ENDS] + scope_components + [MOLD_ENDS]

        # Convert to meshes.
        mold2_file_paths = [component.mold2_file_path for component in mold2_scope_components]

        # Merge meshes.
        output_file_paths.append(merge_stls_y(mold2_file_paths, mold2_output_file_paths))

    if mold3:
        # Corrections to output_file_path.
        if mold3_output_file_paths is None:
            mold3_output_file_paths = f"mold3_{datetime.now().isoformat()}.stl"

        # Add mold ends.
        mold3_scope_components = [MOLD_ENDS] + scope_components + [MOLD_ENDS]

        # Convert to meshes.
        mold3_file_paths = [component.mold3_file_path for component in mold3_scope_components]

        # Add mold3 ends.
        mold3_file_paths = mold3_file_paths

        # Merge meshes.
        output_file_paths.append(merge_stls_y(mold3_file_paths, mold3_output_file_paths))

    return output_file_paths

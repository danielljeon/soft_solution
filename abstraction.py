"""Soft Robotic Exoskeleton for Tremor Suppression Presentation.

Final project for Computer-Aided Design (MECE3030U), Dr. Aaron Yurkewich.

Code written by: Daniel Jeon (https://github.com/danielljeon)
"""

# TODO (danielljeon): Very bad practice. Temporary code.
from main import merge_stls_y, save_mesh_to_stl, display_stl


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


####################################################################################################
# STANDARDIZED COMPONENTS.
TUBING = STLComponent(
    "TUBING",
    "stls/finger_tubing.stl",
    "stls/mold1_tubing.stl",
    "stls/mold2_tubing.stl",
    "stls/mold3_tubing.stl",
)
BELLOW_START = STLComponent(
    "BELLOW_START",
    "stls/finger_bellow start.stl",
    "stls/mold1_bellow start.stl",
    "stls/mold2_bellow start.stl",
    "stls/mold3_bellow start.stl",
)
BELLOW_MIDDLE = STLComponent(
    "BELLOW_MIDDLE",
    "stls/finger_bellow middle.stl",
    "stls/mold1_bellow middle.stl",
    "stls/mold2_bellow middle.stl",
    "stls/mold3_bellow middle.stl",
)
BELLOW_END = STLComponent(
    "BELLOW_END",
    "stls/finger_bellow end.stl",
    "stls/mold1_bellow end.stl",
    "stls/mold2_bellow end.stl",
    "stls/mold3_bellow end.stl",
)
SPACER = STLComponent(
    "SPACER",
    "stls/finger_spacer.stl",
    "stls/mold1_spacer.stl",
    "stls/mold2_spacer.stl",
    "stls/mold3_spacer.stl",
)
CLOSE = STLComponent(
    "CLOSE",
    "stls/finger_close.stl",
    "stls/mold1_close.stl",
    "stls/mold2_mold3_close.stl",
    "stls/mold2_mold3_close.stl",
)
####################################################################################################

####################################################################################################
# STANDARDIZED MERGES.
start = [TUBING]  # y length = 25.0.
mcp_joint = [BELLOW_START, BELLOW_MIDDLE, BELLOW_MIDDLE, BELLOW_END]  # y length = 28.0.
pip_joint = [BELLOW_START, BELLOW_END]  # y length = 14.0.
dip_joint = [BELLOW_START, BELLOW_END]  # y length = 14.0.
end = [CLOSE]  # y length = 2.5.
####################################################################################################

####################################################################################################
# DISTANCE IN mm.
start_to_mcp = 6  # seg1
mcp_to_pip = 4  # seg2
pip_to_dip = 3  # seg3
dip_to_end = 2  # seg4
####################################################################################################

####################################################################################################
seg1 = int(start_to_mcp) - 25 - 28 / 2 if int(start_to_mcp) - 25 - 28 / 2 > 0 else 0
seg2 = int(mcp_to_pip) - 28 / 2 - 14 / 2 if int(start_to_mcp) - 28 / 2 - 14 / 2 > 0 else 0
seg3 = int(pip_to_dip) - 14 / 2 - 14 / 2 if int(start_to_mcp) - 14 / 2 - 14 / 2 > 0 else 0
seg4 = int(dip_to_end) - 14 / 2 - 2.5 if int(start_to_mcp) - 14 / 2 - 2.5 > 0 else 0
# seg = int(source_value) - start_y - end_y (/2 when the end target length >1), default 0.

merger = (
    start
    + [SPACER for _ in range(seg1)]
    + mcp_joint
    + [SPACER for _ in range(seg2)]
    + pip_joint
    + [SPACER for _ in range(seg3)]
    + dip_joint
    + [SPACER for _ in range(seg4)]
    + end
)
####################################################################################################

####################################################################################################
# finger_scope_list = []
# for item in merger:
#     finger_scope_list.append(item.finger_file_path)
# finger = merge_stls_y(finger_scope_list)
# display_stl(finger, "finger")
# # print(f"Saved to: {save_mesh_to_stl(finger)}")
#
# mold1_scope_list = []
# for item in merger:
#     mold1_scope_list.append(item.mold1_file_path)
# mold1 = merge_stls_y(mold1_scope_list)
# display_stl(mold1, "mold1")
# # print(f"Saved to: {save_mesh_to_stl(mold1)}")
#
# mold2_scope_list = []
# for item in merger:
#     mold2_scope_list.append(item.mold2_file_path)
# mold2 = merge_stls_y(mold2_scope_list)
# display_stl(mold2, "mold2")
# # print(f"Saved to: {save_mesh_to_stl(mold2)}")
#
# mold3_scope_list = []
# for item in merger:
#     mold3_scope_list.append(item.mold3_file_path)
# mold3 = merge_stls_y(mold3_scope_list)
# display_stl(mold3, "mold3")
# # print(f"Saved to: {save_mesh_to_stl(mold3)}")
####################################################################################################

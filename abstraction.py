"""Soft Robotic Exoskeleton for Tremor Suppression Presentation.

Final project for Computer-Aided Design (MECE3030U), Dr. Aaron Yurkewich.

Code written by: Daniel Jeon (https://github.com/danielljeon)
"""

# TODO (danielljeon): Very bad practice. Temporary code.
from main import merge_stls_y


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


# merger = [
#     TUBING,
#     SPACER,
#     SPACER,
#     SPACER,
#     BELLOW_START,
#     BELLOW_MIDDLE,
#     BELLOW_END,
#     SPACER,
#     SPACER,
#     SPACER,
#     SPACER,
#     BELLOW_START,
#     BELLOW_END,
#     SPACER,
#     SPACER,
#     SPACER,
#     BELLOW_START,
#     BELLOW_END,
#     SPACER,
#     SPACER,
#     SPACER,
#     SPACER,
#     SPACER,
#     CLOSE,
# ]
#
# finger_scope_list = []
# for item in merger:
#     finger_scope_list.append(item.finger_file_path)
# merge_stls_y(finger_scope_list, "finger")
#
# mold1_scope_list = []
# for item in merger:
#     mold1_scope_list.append(item.mold1_file_path)
# merge_stls_y(mold1_scope_list, "mold1")
#
# mold2_scope_list = []
# for item in merger:
#     mold2_scope_list.append(item.mold2_file_path)
# merge_stls_y(mold2_scope_list, "mold2")
#
# mold3_scope_list = []
# for item in merger:
#     mold3_scope_list.append(item.mold3_file_path)
# merge_stls_y(mold3_scope_list, "mold3")

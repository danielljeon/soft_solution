# soft_solution

<div>
<img alt="Python" src="https://img.shields.io/badge/-Python-%233776AB?logo=Python&logoColor=white">
<img alt="Matplotlib" src="https://img.shields.io/badge/-Matplotlib-%231f77b4?logo=matplotlib&logoColor=white">
<img alt="NumPy" src="https://img.shields.io/badge/-NumPy-%2312130f?logo=numpy&logoColor=white">
<img alt="numpy-stl" src="https://img.shields.io/badge/-numpy--stl-%2357A143">
</div>

Soft Solution is a simple python script that generates STL files of soft robotic grippers / fingers
and simple molds for production.

![finger_example.png](pictures%2Ffinger_example.png)

![mold_example_1_of_2.png](pictures%2Fmold_example_1_of_2.png)

![mold_example_2_of_2.png](pictures%2Fmold_example_2_of_2.png)

The script generates both the STL of the final design and the 3 molds for the cuts, cavities +
channel and the bottom seal.

## Design

The script works of the basis that a soft robotic pneumatic actuators are typically made with a
repeating pattern of components. Often the optimization of such actuator designs is down to
modifying the repeating patterns. Remodeling a full gripper or finger for a simple change, such as
thickness of bellow walls, may be time-consuming and difficult.

The aim of this script is to improve prototyping and also allow for fast generation of varying
designs for different sized gripers and fingers, such as for compliant robotics and exoskeleton
applications.

## Setup

To start running any code, make sure you install all python packages using the command below.

```shell
pip install -r requirements.txt
```

## Work In Progress (WIP)

Future improvements and ideas in progress:

- CSV of finger / gripper dimensions to resultant STLs
- Adjustable pattern components
- Spline calculations and graphing for max bending / expansion

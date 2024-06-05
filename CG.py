import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate horizontal distance from front axle to CG (a)
def calculate_horizontal_cg(F2, l, W):
    return (F2 * l) / W

# Function to calculate the angle x
def calculate_angle(h, l):
    return np.arcsin(h / l)

# Function to calculate vertical distance from front axle to CG (b)
def calculate_vertical_cg(W, a, F4, l, angle):
    return ((W * a - F4 * l) * np.cos(angle)) / (W * np.sin(angle))

# Streamlit input placeholders
st.title("Center of Gravity (CG) Calculation for a Bike")

F1 = st.number_input("Front Axle Weight (F1) in kg", value=20.9)
F2 = st.number_input("Rear Axle Weight (F2) in kg", value=27.4)
W = st.number_input("Kerb Weight (W) in kg", value=48.3)
l = st.number_input("Wheelbase (l) in mm", value=1300)
h = st.number_input("Height (h) in mm", value=200)
F4 = st.number_input("Rear Axle Weight on Incline (F4) in kg", value=25.0)

# Convert wheelbase and height to meters for calculation
l_m = l / 1000
h_m = h / 1000

# Calculate horizontal and vertical CG
a = calculate_horizontal_cg(F2, l_m, W)
angle = calculate_angle(h_m, l_m)
b = calculate_vertical_cg(W, a, F4, l_m, angle)

# Convert a and b back to mm for display
a_mm = a * 1000
b_mm = b * 1000

# Display the results
st.write(f"Horizontal distance from front axle to CG (a): {a_mm:.2f} mm")
st.write(f"Angle (x): {np.degrees(angle):.2f} degrees")
st.write(f"Vertical distance from front axle to CG (b): {b_mm:.2f} mm")

# 2D plot of CG position
fig, ax = plt.subplots()
ax.plot([0, l], [0, 0], 'k-', lw=2)  # Wheelbase line
ax.plot(a_mm, b_mm, 'ro')  # CG point
ax.set_xlabel('Horizontal Distance (mm)')
ax.set_ylabel('Vertical Distance (mm)')
ax.set_title('2D CG Position')
ax.grid(True)

# Display the 2D plot
st.pyplot(fig)

# 3D plot of the bike and CG position
fig_3d = plt.figure(figsize=(10, 7))
ax_3d = fig_3d.add_subplot(111, projection='3d')

# Adjust viewing angle
ax_3d.view_init(elev=30, azim=45)

# CG point
ax_3d.scatter(a_mm, b_mm, 0, c='r', marker='o', s=200, label='CG Point')

# Lines from axes to CG point
ax_3d.plot([0, a_mm], [0, 0], [0, 0], color='red', linestyle='dashed', linewidth=2)  # X-axis line
ax_3d.plot([a_mm, a_mm], [0, b_mm], [0, 0], color='green', linestyle='dashed', linewidth=2)  # Y-axis line
ax_3d.plot([a_mm, a_mm], [b_mm, b_mm], [0, -h], color='purple', linestyle='dashed', linewidth=2)  # Z-axis line

ax_3d.set_xlabel('X Axis (mm)')
ax_3d.set_ylabel('Y Axis (mm)')
ax_3d.set_zlabel('Z Axis (mm)', labelpad=-0.01)  # Adjust label position
ax_3d.set_title('3D CG Position')

# Display the 3D plot
st.pyplot(fig_3d)

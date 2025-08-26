import matplotlib.pyplot as plt
import numpy as np


def point_from_angle_and_length(origin, angle_deg, length):
    angle_rad = np.radians(angle_deg)
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)
    return origin[0] + dx, origin[1] + dy


def plot_frame(ax, label, reach, stack, hta, sta, color, offset_x=0):
    # Head tube top (origin point)
    ht_top = (offset_x + reach, stack)
    # Head tube bottom
    ht_bottom = point_from_angle_and_length(
        ht_top, 270 + hta, 100
    )  # 100 mm head tube
    # Fork end (axle)
    fork_end = point_from_angle_and_length(ht_bottom, 270 + hta, 583.7)

    # Bottom bracket estimated ~345mm below stack line
    bb = (offset_x, 345)

    # Seat tube top
    st_top = point_from_angle_and_length(bb, 90 + sta, 450)

    # Top tube (HT top to ST top)
    ax.plot([ht_top[0], st_top[0]], [ht_top[1], st_top[1]], color=color, lw=2)

    # Down tube (HT bottom to BB)
    ax.plot([ht_bottom[0], bb[0]], [ht_bottom[1], bb[1]], color=color, lw=2)

    # Head tube
    ax.plot(
        [ht_top[0], ht_bottom[0]], [ht_top[1], ht_bottom[1]], color=color, lw=4
    )

    # Fork
    ax.plot(
        [ht_bottom[0], fork_end[0]],
        [ht_bottom[1], fork_end[1]],
        color="gray",
        ls="--",
    )

    # Label
    ax.text(ht_top[0], ht_top[1] + 40, label, color=color, ha="center")


# Setup figure
fig, ax = plt.subplots(figsize=(12, 7))

# Plot all three configurations
plot_frame(
    ax,
    "Low",
    reach=450,
    stack=628,
    hta=63.0,
    sta=70.0,
    color="blue",
    offset_x=-50,
)
plot_frame(
    ax,
    "High",
    reach=455,
    stack=623,
    hta=63.5,
    sta=70.5,
    color="green",
    offset_x=0,
)
plot_frame(
    ax,
    "High + ZS/EC",
    reach=445,
    stack=634,
    hta=62.5,
    sta=69.5,
    color="red",
    offset_x=50,
)

# Styling
ax.set_title("2021 Transition Patrol – Front Triangle Geometry Comparison")
ax.set_xlabel("Horizontal (mm)")
ax.set_ylabel("Vertical (mm)")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend(["Top Tube", "Down Tube", "Head Tube", "Fork (Axle to Crown)"])
plt.show()

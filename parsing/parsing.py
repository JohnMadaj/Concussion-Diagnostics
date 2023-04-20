data = []
with open("hammer_test_results_1ms.txt", "r") as datapacket:
    for message in datapacket:
        message = message.strip().split(': ')
        print(message)

        # device_id = int(message[0])
        # concussbool = not not int(message[2])
        # data = [float(message[1]), concussbool]
        # battery = int(message[3])
        data.append(float(message[1]))
print(data)

import math


def calculate_momentary_thresholds(timestamps, accelerations, initial_threshold):
    curve_severity = 0.2
    scaling_factor = 1.3
    momentary_thresholds = []
    duration = 0
    momentary_acceleration = 0
    for i in range(len(timestamps)):
        timestamp = timestamps[i]
        acceleration = accelerations[i]
        if acceleration >= momentary_acceleration:
            duration += timestamp - timestamps[i - 1] if i > 0 else 0
            momentary_acceleration = acceleration
        else:
            momentary_acceleration = acceleration
            duration = 0
        if momentary_acceleration > curve_severity * initial_threshold:
            momentary_threshold = initial_threshold * math.exp(-duration * scaling_factor / momentary_acceleration)
        else:
            momentary_threshold = initial_threshold
        momentary_thresholds.append(momentary_threshold)
    return momentary_thresholds


timestamps = []
for i in range(1, len(data) + 1):
    timestamps.append(i * 5)
print(timestamps)
new_dummy_thresholds = calculate_momentary_thresholds(timestamps, data, 65)
print(new_dummy_thresholds)

# prstr = ""
# for i in dummy_LA_and_thresholds:
#   prstr += "LA:%.2f\tTHRESHOLD:%.2f\n" % (i[0], i[1])
# print(prstr)


import matplotlib.pyplot as plt


def graph():
    # Sample 2D list

    # Extract the first and second float values from each sublist
    # first_vals = [sublist[0] for sublist in data]
    # second_vals = [sublist[1] for sublist in data]

    # Create the plot
    # plt.plot(range(len(data)), first_vals, label='LA')
    # plt.plot(range(len(data)), second_vals, label='Threshold')
    plt.plot(timestamps, data, label='LA')
    plt.plot(timestamps, new_dummy_thresholds, label='Threshold')

    # Add axis labels and title
    plt.xlabel('Time (ms)')
    plt.ylabel('Acceleration (g)')
    plt.title('Sample Data for Measured LA vs. Adaptive Threshold')

    # Add legend and display the plot
    plt.legend()
    # plt.show()
    # plt.savefig("hammer_curved.png", dpi=800)


# graph()

# import cv2
# import numpy as np
#
# # Define the size of the output video
# width, height = 640, 480
#
# # Define the frames per second (FPS) of the output video
# fps = 30
#
# # Define the duration of the video in seconds
# duration = 10
#
# # Define the number of frames in the video
# num_frames = int(fps * duration)
#
# # Define the x-axis values using the timestamps array
# x = timestamps
#
# # Define the figure and axis objects for the plot
# fig, ax = plt.subplots()
#
# # Set the x and y limits of the plot
# ax.set_xlim(min(x), max(x))
# ax.set_ylim(-10, 10)
#
# # Set the title and axis labels of the plot
# ax.set_title('Acceleration and Threshold Plot')
# ax.set_xlabel('Timestamp')
# ax.set_ylabel('Acceleration/Threshold')
#
# # Define the acceleration and threshold lines
# acceleration_line, = ax.plot([], [], 'r', lw=2)
# threshold_line, = ax.plot([], [], 'b', lw=2)
#
#
# # Define the function to update the plot for each frame
# def update(frame):
#     # Calculate the index of the data to be plotted for this frame
#     index = int(frame / num_frames * len(data))
#
#     # Set the x and y data for the acceleration and threshold lines
#     acceleration_line.set_data(x[:index], data[:index])
#     threshold_line.set_data(x[:index], new_dummy_thresholds[:index])
#
#     # Return the acceleration and threshold lines
#     return [acceleration_line, threshold_line]
#
#
# # Define the video writer object
# video_writer = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (width, height))
#
# # Loop through each frame of the video and plot the data
# for i in range(num_frames):
#     # Clear the plot
#     ax.clear()
#
#     # Update the plot with the data for this frame
#     update(i)
#
#     # Draw the plot
#     fig.canvas.draw()
#     plt.show()
#
#     # Convert the plot to an image
#     plot_image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(
#         fig.canvas.get_width_height()[::-1] + (3,))
#     plot_image.show()
#
#     # Resize the plot image to the desired size
#     # plot_image_resized = cv2.resize(plot_image, (width, height))
#
#     # Write the resized plot image to the video writer object
#     video_writer.write(plot_image)
#
# # Release the video writer object
# video_writer.release()

import matplotlib.animation as animation

# Define your data and plot settings
time_ms = timestamps
acceleration = data
threshold = new_dummy_thresholds

fig, ax = plt.subplots()


# Define the animation function
def animate(i):
    ax.clear()
    ax.plot(time_ms[:i + 1], acceleration[:i + 1], label='Acceleration (g)')
    ax.plot(time_ms[:i + 1], threshold[:i + 1], label='Momentary Threshold (g)')
    ax.legend()
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Acceleration/Threshold')
    ax.set_title('Acceleration and Threshold over time')


# Create the animation and save it as a video file
ani = animation.FuncAnimation(fig, animate, frames=len(time_ms), interval=1)
# FFwriter = animation.FFMpegWriter(fps=10)
# plt.show()
# writervideo = animation.FFMpegWriter(fps=60)
writergif = animation.PillowWriter(fps=30)

ani.save('hammer.gif', writer=writergif)

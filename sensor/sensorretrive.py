import csv
import random
import time

activities = ["walking", "running", "sitting", "standing", "jumping"]
file_name = "sensor_data_v2.csv"

start_time = int(time.time())

with open(file_name, "w", newline="") as wcsv:
    writer = csv.writer(wcsv)
    writer.writerow([
        "timestamp", "device_id",
        "ax", "ay", "az",
        "gx", "gy", "gz",
        "activity"
    ])

    for i in range(100):
        device_id = "sensor_01"
        activity = random.choice(activities)

        # Accelerometer + Gyroscope Pattern
        if activity == "walking":
            ax = round(random.uniform(0.8, 1.8), 2)
            ay = round(random.uniform(0.8, 1.7), 2)
            az = round(random.uniform(1.0, 2.2), 2)
            gx = round(random.uniform(5, 15), 2)
            gy = round(random.uniform(5, 15), 2)
            gz = round(random.uniform(5, 15), 2)

        elif activity == "running":
            ax = round(random.uniform(1.5, 3.2), 2)
            ay = round(random.uniform(1.5, 3.0), 2)
            az = round(random.uniform(1.8, 3.8), 2)
            gx = round(random.uniform(15, 40), 2)
            gy = round(random.uniform(15, 40), 2)
            gz = round(random.uniform(15, 40), 2)

        elif activity == "jumping":
            ax = round(random.uniform(2.0, 4.5), 2)
            ay = round(random.uniform(1.0, 3.0), 2)
            az = round(random.uniform(4.0, 8.0), 2)
            gx = round(random.uniform(20, 50), 2)
            gy = round(random.uniform(20, 50), 2)
            gz = round(random.uniform(20, 50), 2)

        elif activity == "sitting":
            ax = round(random.uniform(0.0, 0.2), 2)
            ay = round(random.uniform(0.0, 0.2), 2)
            az = round(random.uniform(0.0, 0.2), 2)
            gx = round(random.uniform(0, 2), 2)
            gy = round(random.uniform(0, 2), 2)
            gz = round(random.uniform(0, 2), 2)

        else:  # standing
            ax = round(random.uniform(0.2, 0.5), 2)
            ay = round(random.uniform(0.2, 0.5), 2)
            az = round(random.uniform(0.2, 0.5), 2)
            gx = round(random.uniform(1, 3), 2)
            gy = round(random.uniform(1, 3), 2)
            gz = round(random.uniform(1, 3), 2)

        timestamp = start_time + i  # smooth timestamps

        writer.writerow([
            timestamp, device_id,
            ax, ay, az,
            gx, gy, gz,
            activity
        ])

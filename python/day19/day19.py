import numpy as np

with open('input.txt') as f:
    data = f.read().split('\n\n')
    data = [report.split('\n') for report in data]
    data = [[reading.split(',') for reading in report[1:]] for report in data]


class SensorMap:
    def __init__(self, readings):
        self.beacons = []
        for reading in readings:
            self.beacons.append([int(coord) for coord in reading])

    def shift_map(self, shift):
        output_readings = []
        for reading in self.beacons:
            for k in range(shift['rotation'][0]):
                reading = SensorMap.rotate_beacon(reading, axis=0)
            for k in range(shift['rotation'][1]):
                reading = SensorMap.rotate_beacon(reading, axis=1)
            for k in range(shift['rotation'][2]):
                reading = SensorMap.rotate_beacon(reading, axis=2)
            reading = [reading[i] - shift['shift'][i] for i in range(3)]
            output_readings.append(reading)
        self.beacons = output_readings

    @staticmethod
    def find_shift(sensormap1, sensormap2):
        for beacon1 in sensormap1.beacons[:-11]:
            for beacon2 in sensormap2.beacons[:-11]:
                for shift in SensorMap.determine_possible_shifts(beacon1, beacon2):
                    if SensorMap.is_sufficient_overlap(sensormap1, sensormap2, shift):
                        return shift

    @staticmethod
    def rotate_beacon(beacon_reading, axis):
        output = [0, 0, 0]
        if axis == 2:
            output[2] = beacon_reading[2]
            output[0] = beacon_reading[1]
            output[1] = -beacon_reading[0]

        if axis == 1:
            output[1] = beacon_reading[1]
            output[0] = beacon_reading[2]
            output[2] = -beacon_reading[0]

        if axis == 0:
            output[0] = beacon_reading[0]
            output[1] = -beacon_reading[2]
            output[2] = beacon_reading[1]
        return output


    @staticmethod
    def get_beacon_rotations(beacon_reading):
        rotations = []
        for x_axis_rotation in range(0,4):
            for y_axis_rotation in range(0,4):
                for z_axis_rotation in range(0,4):
                    output_beacon = beacon_reading.copy()
                    for k in range(x_axis_rotation):
                        output_beacon = SensorMap.rotate_beacon(output_beacon, axis=0)
                    for k in range(y_axis_rotation):
                        output_beacon = SensorMap.rotate_beacon(output_beacon, axis=1)
                    for k in range(z_axis_rotation):
                        output_beacon = SensorMap.rotate_beacon(output_beacon, axis=2)
                    rotations.append({'rotation': [x_axis_rotation, y_axis_rotation, z_axis_rotation], 'beacon_map': output_beacon})
        return rotations

    @staticmethod
    def determine_possible_shifts(beacon1, beacon2):
        shifts = SensorMap.get_beacon_rotations(beacon2)
        for rotation in shifts:
            rotation['shift'] = [rotation['beacon_map'][i] - beacon1[i] for i in range(3)]
        return shifts

    @staticmethod
    def is_sufficient_overlap(sensormap1, sensormap2, shift):
        count_overlap = 0
        for beacon_reading in sensormap2.beacons:
            reading = beacon_reading.copy()
            for k in range(shift['rotation'][0]):
                reading = SensorMap.rotate_beacon(reading, axis=0)
            for k in range(shift['rotation'][1]):
                reading = SensorMap.rotate_beacon(reading, axis=1)
            for k in range(shift['rotation'][2]):
                reading = SensorMap.rotate_beacon(reading, axis=2)
            reading = [reading[i] - shift['shift'][i] for i in range(3)]
            if reading in sensormap1.beacons:
                count_overlap += 1
            if count_overlap >= 12:
                return True
        return False

print(data)
data = [SensorMap(entry) for entry in data]

shift_tracker = [0 for k in data]
shift_tracker[0] = 1
checked = [0 for k in data]

sensor_shifts = [{'shift': [0, 0, 0]} for k in data]

while sum(shift_tracker) < len(data):
    print(shift_tracker)
    for k in range(len(data)):
        if shift_tracker[k] == 0:
            continue
        if checked[k] == 1:
            continue
        print(k)
        checked[k] = 1
        for j in range(len(data)):
            if shift_tracker[j] == 1:
                continue
            shift = SensorMap.find_shift(data[k], data[j])
            if shift is not None:
                print("Match found for entry ", j)
                data[j].shift_map(shift)
                shift_tracker[j] = 1
                sensor_shifts[j] = shift

unique_beacons = []
for sensor_map in data:
    for beacon in sensor_map.beacons:
        if beacon not in unique_beacons:
            unique_beacons.append(beacon)

print("Part 1: ", len(unique_beacons))

max_distance = 0
for sensor1 in sensor_shifts:
    for sensor2 in sensor_shifts:
        distance = sum([np.abs(sensor1['shift'][i] - sensor2['shift'][i]) for i in range(3)])
        if distance > max_distance:
            max_distance = distance

print("Part 2: ", max_distance)
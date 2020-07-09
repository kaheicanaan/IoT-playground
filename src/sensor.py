import subprocess

import psutil


# =====================
# || Sensor readings ||
# =====================

def _get_thermal_info():
    """Get outputs from 'powermetrics' command, return outputs line by line as a generator.

    Returns:

    """
    bash_command = 'echo $SUDO_PASSWORD | sudo -S powermetrics -n 1'
    proc = subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE)

    output = proc.communicate()[0].decode()
    print(output)

    thermal_info = dict()
    for line in output.split('\n'):
        if line.startswith('CPU die temperature:'):
            thermal_info.update({
                'cpu_temperature': float(line[21:26])
            })
        elif line.startswith('GPU die temperature:'):
            thermal_info.update({
                'gpu_temperature': float(line[21:26])
            })
        elif line.startswith('Fan:'):
            thermal_info.update({
                'fan_speed': int(line[5:9])
            })

    return thermal_info


def _get_cpu_load():
    return {'cpu_load': psutil.cpu_percent()}


def get_sensor_readings():
    readings = dict()
    readings.update(_get_thermal_info())
    readings.update(_get_cpu_load())
    return readings


if __name__ == '__main__':
    sensor_readings = get_sensor_readings()

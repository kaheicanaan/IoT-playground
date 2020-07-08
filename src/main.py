import os
import subprocess


def get_thermal_info():
    """Get outputs from 'powermetrics' command, return outputs line by line as a generator.

    Returns:

    """
    bash_command = 'echo $SUDO_PASSWORD | sudo -S powermetrics -n 1'
    proc = subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE)

    output = proc.communicate()[0].decode()
    print(output)


if __name__ == '__main__':
    get_thermal_info()

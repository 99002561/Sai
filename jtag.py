import subprocess as sub
import serial.tools.list_ports

check_cmd = "C:\\ti\\MSPFlasher_1.3.20\\MSP430Flasher.exe -i "
load_cmd = "C:\\ti\\MSPFlasher_1.3.20\\MSP430Flasher.exe -n MSP430F5324 -w "


def check_jtag_connectivity(com_port):
    p = sub.Popen(check_cmd + com_port, stdout=sub.PIPE, stderr=sub.PIPE)
    while True:
        output = p.stdout.readline()
        if p.poll() is not None:
            break
        if output:
            print(output.strip())
    ret_val = p.poll()
    return ret_val


def check_dut_connectivity(com_port):
    p = sub.Popen(check_cmd + com_port, stdout=sub.PIPE, stderr=sub.PIPE)
    while True:
        output = p.stdout.readline()
        if p.poll() is not None:
            break
        if output:
            print(output.strip())
    ret_val = p.poll()
    return ret_val


def load_firmware(firmware_file):
    """
    load firmware
    :return:
    """
    cmd = load_cmd + firmware_file + " -v -z [VCC]"
    print(cmd)
    p = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
    while True:
        output = p.stdout.readline()
        if p.poll() is not None:
            break
        if output:
            print(output.strip())
    ret_val = p.poll()
    return ret_val


def get_port():
    """
    Get the port of MSP Debug Interface
    """

    for port in serial.tools.list_ports.comports():
        if "MSP Debug Interface" in port.description:
            return port.device
    return None


if __name__ == "__main__":
    port = get_port()
    ouput = check_jtag_connectivity("port")
    print(ouput)
    # ouput = load_firmware()
    # print(ouput)

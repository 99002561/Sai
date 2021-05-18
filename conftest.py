# Python fixture  for EFT Test Application
__author__ = "Gowtham Bavireddy"

import time

import pytest
import logging
from utils.nidaq import NiDAQMX
from utils.serial_conn import get_next_available

# ------------------ Variables------------------------

door_signal = "Dev1/port1/line7"
dut_signal = "Dev1/port2/line7"


@pytest.fixture(scope="session")
def dut_power():
    """
    power on dut
    :return:
    """
    power = NiDAQMX("Dev1/port0/line7")
    power.power_off_dut()
    yield
    time.sleep(5)
    power.power_off_dut()


@pytest.fixture(scope="function")
def door_check():
    """
    power on dut
    :return:
    """
    ni_daq = NiDAQMX(door_signal)
    check = ni_daq.door_signal_check()
    return check


@pytest.fixture(scope="function")
def dut_check():
    """
    power on dut
    :return:
    """
    ni_daq = NiDAQMX(dut_signal)
    check = ni_daq.dut_placement_check()
    return check


@pytest.fixture(scope="session")
def utx_under_test():
    """Fixture for UTX - EFT communication through USB serial port on the cradle."""
    # Getting the device
    utx_under_test = get_next_available("UTX", None)
    logging.info("Connected to UTX on {} port.".format(utx_under_test.port))
    yield utx_under_test
    logging.info("Releasing the device")
    logging.info("Tear down")
    utx_under_test.close()


def pytest_addoption(parser):
    parser.addoption("--barcode", action="store")


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.barcode
    if 'barcode' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("barcode", [option_value])

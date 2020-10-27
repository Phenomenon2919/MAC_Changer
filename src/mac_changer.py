#!/usr/bin/env python3

import subprocess, argparse
import re

# Changes the MAC Address of Network interface
def change_mac(interface, mac):

    print("[/] Changing MAC Address of " + interface + " to " + mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

# Get Inputs from arguments of Users
def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-i", "--interface", help="Provide network interface", dest="interface")
    arg_parser.add_argument("-m", "--mac", help="Provide New Mac Address", dest="mac")
    options = arg_parser.parse_args()

    if not options.interface or not options.mac:
        arg_parser.print_help()
        exit()
    return options

# Function to read the current MAC address for the said interface of the system
def get_mac(interface):
    # Get the stdout output for 'ifconfig <interface>' to fetch all network related information for the interface
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # Search for MAC Address in the output using Regex
    mac_address_search_list = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if not mac_address_search_list:
        print("[-] Could not read MAC Address")
        exit(0)
    return mac_address_search_list.group(0)

if __name__ == "__main__":

    # Get the network interface and the new MAC address from the user
    options = get_args()

    current_mac = get_mac(options.interface)
    print("[/] Current MAC Address: " + str(current_mac))
    change_mac(options.interface, options.mac)
    current_mac = get_mac(options.interface)

    # Check if MAC Address has been changed
    if current_mac == options.mac:
        print("[+] MAC Address for " + options.interface + " successfully changed to " + options.mac)
    else:
        print("[-] Could NOT change MAC Address")



# MAC Changer - Python3 Script
Simple modular code to change the MAC Address associated with a network interface of a Linux Device
* **get_mac(interface)** - get MAC associated with an interface
* **change_mac(interface, mac)** - change MAC of said interface


## Usage
>pip3 install -r requirements.txt

In ./src
>python3 mac_changer.py -i \<network interface> -m \<new mac>

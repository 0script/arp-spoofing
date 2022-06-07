#arp-spoofing

##Table of content
* [About the project](#about-the-project)
* [Technologies](#technologies)
* [Setup](#setup)

##About the project

Python script to perform ARP spoofing on LAN with the default network interface .

##Technologies

* python
* scapy (API) : https://scapy.net/

##Setup

```shell
#download the project
$git clone git@github.com:0script/arp-spoof.git
$cd arp-spoof/
#install scapy
$pip3 install scapy
#run the script with root privilege 
$sudo python3 spoofARP.py <victim_ip> <gateway_ip>
```
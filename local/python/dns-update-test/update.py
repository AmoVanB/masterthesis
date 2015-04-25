#!/usr/bin/python
import sys
import dns.resolver
import dns.query
import dns.update
import dns.exception
import dns.tsigkeyring

# version: http://www.dnspython.org/kits/1.12.0/

try:
  answers_IPv6 = dns.resolver.query('ks.vyncke.org', 'AAAA')
  nsserver_address = None 

  for rdata in answers_IPv6:
    nsserver_address = rdata.address
    break

  if (nsserver_address == None):
    answers_IPv4 = dns.resolver.query('ks.vyncke.org', 'A')
    for rdata in answers_IPv4:
      nsserver_address = rdata.address
      break
except dns.resolver.NXDOMAIN as e:
  print("The query name does not exist.")
  sys.exit(0)
except dns.resolver.YXDOMAIN as e:
  print("The query name is too long after DNAME substitution.")
  sys.exit(0)
except dns.resolver.NoAnswer as e:
  print("The response did not contain an answer.")
  sys.exit(0)
except dns.resolver.NoNameservers as e:
  print("No non-broken nameservers are available to answer the question.")
  sys.exit(0)
except dns.exception.Timeout as e:
  print("No answers could be found in the specified lifetime: %s.")
  sys.exit(0)
except dns.exception.DNSException as e:
  print("unexpected error (%s)", e.message)
  sys.exit(0)

key = dns.tsigkeyring.from_text({'amoupdate.': 'BK1wQkLhDySTEMhLDeDSdg=='})
update = dns.update.Update("amo.vyncke.org", keyring=key, keyalgorithm=dns.tsig.HMAC_MD5)

# After name:
# arg1: TTL
# arg2: rdtype
# arg3: string containing description
#       A(AAA): IP address
#       PTR: link
#       SRV: priority, weight, port, hostname
#       TXT  string of values separated by spaces

update.delete('b._dns-sd._udp',                    'PTR',  'brussels.amo.vyncke.org.')
update.delete('brussels.amo.vyncke.org.',          'TXT')
update.delete('_services._dns-sd._udp.brussels',   'PTR', '_ipp._tcp.brussels')
update.delete('_ipp._tcp.brussels',                'PTR', 'Meeting\ Room\ Printer\ @\ Brussels\ [Sales:v6]._ipp._tcp.brussels')
update.delete('_ipp._tcp.brussels',                'PTR', 'Reception\ Desk\ Printer\ @\ Brussels\ [IT:v6]._ipp._tcp.brussels')
update.delete('_ipp._tcp.brussels',                'PTR', 'Meeting\ Room\ Printer\ @\ Brussels\ [IT:v6]._ipp._tcp.brussels')
update.delete('Meeting Room Printer @ Brussels [Sales:v6]._ipp._tcp.brussels',  'SRV', '0 0 631 printer3-eth1-v6.brussels')
update.delete('Meeting Room Printer @ Brussels [Sales:v6]._ipp._tcp.brussels',  'TXT', '""')
update.delete('Reception Desk Printer @ Brussels [IT:v6]._ipp._tcp.brussels',   'SRV', '0 0 631 printer1-eth2-v6.brussels')
update.delete('Reception Desk Printer @ Brussels [IT:v6]._ipp._tcp.brussels',   'TXT', '""')
update.delete('Meeting Room Printer @ Brussels [IT:v6]._ipp._tcp.brussels',  'SRV', '0 0 631 printer2-eth2-v6.brussels')
update.delete('Meeting Room Printer @ Brussels [IT:v6]._ipp._tcp.brussels',  'TXT', '""')
update.delete('printer3-eth1-v6.brussels',         'AAAA', '2015:6a8:2d61:2460::babe')
update.delete('printer1-eth2-v6.brussels',         'AAAA', '2015:6a8:2d63:2460::cafe')
update.delete('printer2-eth2-v6.brussels',         'AAAA', '2015:6a8:2d61:2460::face')

update.add('b._dns-sd._udp',                   5, 'PTR',  'brussels.amo.vyncke.org.')
update.add('brussels.amo.vyncke.org.',         5, 'TXT', "public=eth0,eth1")
update.add('_services._dns-sd._udp.brussels',  5, 'PTR', '_ipp._tcp.brussels')
update.add('_ipp._tcp.brussels',               5, 'PTR', 'Meeting\ Room\ Printer\ @\ Brussels\ [Sales:v6]._ipp._tcp.brussels')
update.add('_ipp._tcp.brussels',               5, 'PTR', 'Reception\ Desk\ Printer\ @\ Brussels\ [IT:v6]._ipp._tcp.brussels')
update.add('_ipp._tcp.brussels',               5, 'PTR', 'Meeting\ Room\ Printer\ @\ Brussels\ [IT:v6]._ipp._tcp.brussels')
update.add('Meeting Room Printer @ Brussels [Sales:v6]._ipp._tcp.brussels', 5, 'SRV', '0 0 631 printer3-eth1-v6.brussels')
update.add('Meeting Room Printer @ Brussels [Sales:v6]._ipp._tcp.brussels', 5, 'TXT', '""')
update.add('Reception Desk Printer @ Brussels [IT:v6]._ipp._tcp.brussels',  5, 'SRV', '0 0 631 printer1-eth2-v6.brussels')
update.add('Reception Desk Printer @ Brussels [IT:v6]._ipp._tcp.brussels',  5, 'TXT', '""')
update.add('Meeting Room Printer @ Brussels [IT:v6]._ipp._tcp.brussels', 5, 'SRV', '0 0 631 printer2-eth2-v6.brussels')
update.add('Meeting Room Printer @ Brussels [IT:v6]._ipp._tcp.brussels', 5, 'TXT', '""')
update.add('printer3-eth1-v6.brussels',        5, 'AAAA', '2015:6a8:2d61:2460::babe')
update.add('printer1-eth2-v6.brussels',        5, 'AAAA', '2015:6a8:2d63:2460::cafe')
update.add('printer2-eth2-v6.brussels',        5, 'AAAA', '2015:6a8:2d61:2460::face')


update.delete('b._dns-sd._udp',                  'PTR',  'london.amo.vyncke.org.')
update.delete('london.amo.vyncke.org.',          'TXT')
update.delete('_services._dns-sd._udp.london',   'PTR', '_ipp._tcp.london')
update.delete('_ipp._tcp.london',                'PTR', 'Meeting\ Room\ Printer\ @\ London\ [Sales:v6]._ipp._tcp.london')
update.delete('_ipp._tcp.london',                'PTR', 'Reception\ Desk\ Printer\ @\ London\ [IT:v6]._ipp._tcp.london')
update.delete('Meeting Room Printer @ London [Sales:v6]._ipp._tcp.london',  'SRV', '0 0 631 printer3-eth1-v6.london')
update.delete('Meeting Room Printer @ London [Sales:v6]._ipp._tcp.london',  'TXT', '""')
update.delete('Reception Desk Printer @ London [IT:v6]._ipp._tcp.london',  'SRV', '0 0 631 printer1-eth2-v6.london')
update.delete('Reception Desk Printer @ London [IT:v6]._ipp._tcp.london',  'TXT', '""')
update.delete('printer3-eth1-v6.london',         'AAAA', '2001:6a8:2631:2460::babe')
update.delete('printer1-eth2-v6.london',         'AAAA', '2001:6a8:2d31:2460::cafe')

update.add('b._dns-sd._udp',                 5, 'PTR',  'london.amo.vyncke.org.')
update.add('london.amo.vyncke.org.',         5, 'TXT', "public=eth1")
update.add('_services._dns-sd._udp.london',  5, 'PTR', '_ipp._tcp.london')
update.add('_ipp._tcp.london',               5, 'PTR', 'Meeting\ Room\ Printer\ @\ London\ [Sales:v6]._ipp._tcp.london')
update.add('_ipp._tcp.london',               5, 'PTR', 'Reception\ Desk\ Printer\ @\ London\ [IT:v6]._ipp._tcp.london')
update.add('Meeting Room Printer @ London [Sales:v6]._ipp._tcp.london', 5, 'SRV', '0 0 631 printer3-eth1-v6.london')
update.add('Meeting Room Printer @ London [Sales:v6]._ipp._tcp.london', 5, 'TXT', '""')
update.add('Reception Desk Printer @ London [IT:v6]._ipp._tcp.london', 5, 'SRV', '0 0 631 printer1-eth2-v6.london')
update.add('Reception Desk Printer @ London [IT:v6]._ipp._tcp.london', 5, 'TXT', '""')
update.add('printer3-eth1-v6.london',        5, 'AAAA', '2001:6a8:2631:2460::babe')
update.add('printer1-eth2-v6.london',        5, 'AAAA', '2001:6a8:2d31:2460::cafe')


response = None

try:
  response = dns.query.tcp(update, nsserver_address)
except dns.tsig.PeerBadKey:
  print("the peer didn't know the key we used (invalid algo or invalid name)")
  sys.exit(0)
except dns.tsig.PeerBadSignature:
  print("the peer didn't like the signature we sent (invalid key val)")
  sys.exit(0)

rcode = response.rcode()
# FROM RFC2136:
if (rcode == 0): # NOERROR
  print ("Success.")
elif (rcode == 1): #FORMERR
  print ("The name server was unable to interpret the request due to a format error.")
elif (rcode == 2): #SERVFAIL
  print ("The name server encountered an internal failure while processing this request.")
elif (rcode == 3): #NXDOMAIN
  print ("Some name that ought to exist, does not exist.")
elif (rcode == 4): #NOTIMP
  print ("The name server does not support the specified opcode (UPDATE).")
elif (rcode == 5): #REFUSE
  print ("The name server refuses to perform the specified operation for policy or security reasons.")
elif (rcode == 6): #YXDOMAIN
  print ("Some name that ought not to exist, does exist.")
elif (rcode == 7): #YXRRSET
  print ("Some RRset that ought not to exist, does exist.")
elif (rcode == 8): #NXRRSET
  print ("Some RRset that ought to exist, does not exist.")
elif (rcode == 9): #NOTAUTH
  print ("The server is not authoritative for the zone.")
elif (rcode == 10): #NOTZONE
  print ("A name used in the Prerequisite or Update Section is not within the zone.")


---
title: "Attribution of Internet Probes"
abbrev: "Probes Attribution"
category: info
submissiontype: IETF
docname: draft-vyncke-opsec-probe-attribution-latest
ipr: trust200902
area: "Operations and Management"
workgroup: "Operational Security Capabilities for IP Network Infrastructure"
keyword: Internet-Draft
venue:
  group: "Operational Security Capabilities for IP Network Infrastructure"
  type: "Working Group"
  mail: "opsec@ietf.org"
  arch: "https://mailarchive.ietf.org/arch/browse/opsec/"
  github: "evyncke/opsec-probe-attribution"
  latest: "https://evyncke.github.io/opsec-probe-attribution/draft-vyncke-opsec-probe-attribution.html"

stand_alone: yes
smart_quotes: no
pi: [toc, sortrefs, symrefs]

author:
 -
    ins: E. Vyncke
    name: Ëric Vyncke
    organization: Cisco
    street: De Kleetlaan 64
    code: 1831
    city: Diegem
    country: Belgium
    email: evyncke@cisco.com
 -
    ins: J. Iurman
    name: Justin Iurman
    organization: Université de Liège
    country: Belgium
    email: justin.iurman@uliege.be

normative:

informative:


--- abstract

When doing some Internet-wide measurements, it is often necessary to send active probes to either collaborating parties or non-collaborating parties; the latter is similar scan and could be perceived as aggressive. This document proposes a couple of simple techniques allowing any party or organization to understand what this unsolicited packet is, what is its purpose, and more important who to contact.


--- middle

# Introduction

When doing some Internet-wide measurements, it is frequently necessary to send active probes to either collaborating parties or non-collaborating parties.

Sending unsolicited probes should be done at a rate low enough to avoid causing a denial of services. But even at a low rate, those probes could trigger an alarm that will request some investigation by either the party receiving the probe (i.e., when the probe destination address is one address assigned to the receiving party) or by a third party having some devices where those probes are transiting (e.g., an Internet transit router).

This document suggests a couple of simple techniques allowing any party or organization to understand:

- what this unsolicited packet is,

- what is its purpose,

- and more significant who to contact for further information or stop the probing.

Note: it is expected that only good-willing researchers will use these techniques.

# Probe / Measurement Description

## Probe Description URI {#uri}

This document defines a "probe description URI" as an URI pointing to:

- an email address, e.g., "mailto:eric@example.net";

- a web page, e.g., "https://example.net/probe containing a "Probe Description", see {{text}}.

## Probe Description Text {#text}

Similarly as in {{!I-D.draft-foudil-securitytxt}}, when a node probes other nodes over the Internet, it should create a text file following the syntax described in section 3 of {{!I-D.draft-foudil-securitytxt}} and should have the following fields:

- digital signature;

- contact;

- expires;

- preferred-languages.

Plus, another one "description" which is a URI pointing a document describing the measurement.

# In-band Probe Attribution

When the desired measurement allows for it, one "probe description URI" should be included in the payload of all probes sent. This could be:

- for a {{!RFC4443}} ICMPv6 echo request: in the optional data (see section 4.1 of {{!RFC443}});

- for a {{!RFC792}} ICMPv4 echo request: in the optional data;

- for a {{!RFC768}} UDP datagram: in the data part;

- for a {{!RFC793}} TCP packet with the SYN flag: data is allowed in TCP packets with the SYN flag per section 3.4 of {{!RFC793}} (2nd paragraph);

- for a {{!RFC8200}} IPv6 packet with either hop-by-hop or destination options headers, in the PadN option;

- etc.

The URI should start at the first octet of the payload and should be terminated by an octet of 0x0, i.e., it must be null terminated.

Note: using the above technique produces a valid and legit packet for all the nodes forwarding and receiving the probe. The node receiving the probe may or may not process the received packet, but this should cause no harm if the probing rate is very low as compared to the network bandwidth and to the processing capacity of all the nodes.

# Out-of-band Probe Attribution

When it is not possible to include the "probe description URI" in the probe, then a specific URI must be constructed based on the source address of the probe packet following {{!RFC8615}}, e.g., for a probe source address of 2001:db8::dead, the following URI are constructed:

- if the reverse DNS record for 2001:db8::dead exists, e.g., "example.net", then the URI is "https://example.net/.well-known/probing.txt" ;

- else (or in addition), the URI is "https://\[2001:db8::dead\]/.well-known/probing.txt". Of course, there will be a certificate verification issue.

The constructed URI must be a reference to the "Probe description Text" (see {{text}}).

# Security Considerations

While it is expected that only good-willing researchers will use these techniques, they will simplify and shorten the time to identify a probing across the Internet.

As both proposed techniques rely on the IP source address, they are vulnerable to IP spoofing.


# IANA Considerations

The "Well-Known URIs" registry should be updated with the following:

- additional values (using the template from {{!RFC8615}}):

- URI suffix: security.txt

- Change controller: IETF

- Specification document(s): this document

- Status: permanent



--- back

# Acknowledgments
{:numbered="false"}

The authors would like to thank Benoît Donnet, Alain Fiocco, Mark Townsley for helpful discussions as well as Raphaël Léas for an early implementation.

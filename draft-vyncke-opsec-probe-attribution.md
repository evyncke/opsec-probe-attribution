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
    name: Éric Vyncke
    organization: Cisco
    street: De Kleetlaan 64
    code: 1831
    city: Diegem
    country: Belgium
    email: evyncke@cisco.com
 -
    ins: B. Donnet
    name: Benoît Donnet
    organization: Université de Liège
    country: Belgium
    email: benoit.donnet@uliege.be
 -
    ins: J. Iurman
    name: Justin Iurman
    organization: Université de Liège
    country: Belgium
    email: justin.iurman@uliege.be

normative:

informative:
  LARGE_SCALE:
    title: Efficient Algorithms for Large-Scale Topology Discovery
    target: https://dl.acm.org/doi/pdf/10.1145/1071690.1064256
    date: 2005
    seriesinfo:
      DOI: 10.1145/1071690.1064256
    author:
      -
        name: Benoît Donnet
        org: Université Pierre & Marie Curie Laboratoire LiP6–CNRS
      -
        name: Philippe Raoult
        org: Université Pierre & Marie Curie Laboratoire LiP6–CNRS
      -
        name: Timur Friedman
        org: Université Pierre & Marie Curie Laboratoire LiP6–CNRS
      -
        name: Mark Crovella
        org: Boston University Computer Science Department
  IPV6_TOPOLOGY:
    title: In the IP of the Beholder Strategies for Active IPv6 Topology Discovery
    target: http://www.cmand.org/papers/beholder-imc18.pdf
    date: 2018
    seriesinfo:
      DOI: 10.1145/3278532.3278559
    author:
      -
        name: Robert Beverly
        org: Naval Postgraduate School
      -
        name: Ramakrishnan Durairajan
        org: University of Oregon
      -
        name: David Plonka
        org: Akamai Technologies
      -
        name: Justin P. Rohrer
        org: Naval Postgraduate School
  IPV4_TOPOLOGY:
    title: Yarrp’ing the Internet Randomized High-Speed Active Topology Discovery
    target: http://www.cmand.org/papers/yarrp-imc16.pdf
    date: 2016
    seriesinfo:
      DOI: 10.1145/2987443.2987479
    author:
      -
        name: Robert Beverly
        org: Naval Postgraduate School


--- abstract

Active measurements at Internet-scale can target either collaborating parties or non-collaborating ones. This is similar scan and could be perceived as aggressive. This document proposes a couple of simple techniques allowing any party or organization to understand what this unsolicited packet is, what is its purpose, and more importantly who to contact.


--- middle

# Introduction

Active measurements at Internet-scale can target either collaborating parties or non-collaborating ones. Such measurements include {{LARGE_SCALE}} and {{?RFC7872}}.

Sending unsolicited probes should obviously be done at a rate low enough to avoid wasting other parties resources. But even at a low rate, those probes could trigger an alarm that will request some investigation by either the party receiving the probe (i.e., when the probe destination address is one address assigned to the receiving party) or by a third party having some devices where those probes are transiting (e.g., an Internet transit router).

This document suggests a couple of simple techniques allowing any party or organization to understand:

- what this unsolicited packet is,

- what is its purpose,

- and more significantly who to contact for further information or stop the probing.

Note: it is expected that only good-willing researchers will use these techniques.

# Probe / Measurement Description

## Probe Description URI {#uri}

This document defines a "probe description URI" as a URI pointing to:

- "Probe Description", see {{text}}, e.g., "https://example.net/measurement.txt";

- an email address, e.g., "mailto:eric@example.net";

- a phone number to call, e.g., "tel:+1-201-555-0123".

## Probe Description Text {#text}

Similarly, as in {{!I-D.draft-foudil-securitytxt}}, when a node probes other nodes over the Internet, it should create a text file following the syntax described in section 3 of {{!I-D.draft-foudil-securitytxt}} and should have the following fields:

- contact;

- expires;

- preferred-languages.

Plus, another one "description" which is a URI pointing a document describing the measurement.

# In-band Probe Attribution

When the desired measurement allows for it, one "probe description URI" should be included in the payload of all probes sent. This could be:

- for a {{!RFC4443}} ICMPv6 echo request: in the optional data (see section 4.1 of {{!RFC4443}});

- for a {{!RFC792}} ICMPv4 echo request: in the optional data;

- for a {{!RFC768}} UDP datagram: in the data part;

- for a {{!RFC793}} TCP packet with the SYN flag: data is allowed in TCP packets with the SYN flag per section 3.4 of {{!RFC793}} (2nd paragraph);

- for a {{!RFC8200}} IPv6 packet with either hop-by-hop or destination options headers, in the PadN option. Note that, per the informational {{?RFC4942}} section 2.1.9.5, it is suggested that PadN option should only contain 0x0 and be smaller than 8 octets, so the proposed insertion of the URI in PadN option could have influence on the measurement itself;

- etc.

The URI should start at the first octet of the payload and should be terminated by an octet of 0x0, i.e., it must be null terminated.

Note: using the above technique produces a valid and legit packet for all the nodes forwarding and receiving the probe. The node receiving the probe may or may not process the received packet, but this should cause no harm if the probing rate is very low as compared to the network bandwidth and to the processing capacity of all the nodes.

# Out-of-band Probe Attribution

When it is not possible to include the "probe description URI" in the probe, then a specific URI must be constructed based on the source address of the probe packet following {{!RFC8615}}, e.g., for a probe source address of 2001:db8::dead, the following URI are constructed:

- if the reverse DNS record for 2001:db8::dead exists, e.g., "example.net", then the URI is "https://example.net/.well-known/probing.txt" ;

- else (or in addition), the URI is "https://\[2001:db8::dead\]/.well-known/probing.txt". Of course, there will be a certificate verification issue.

The constructed URI must be a reference to the "Probe description Text" (see {{text}}).

# Ethical Considerations

Executing some measurement experiences over the global Internet obviously require some ethical considerations when transit/destination non-solicited parties are involved.

This document proposes a common way to identity the source and the purpose of active probing in order to reduce the potential burden on the non-solicited parties.

But there are other considerations to be taken into account: from the payload content (e.g., is the encoding valid ?) to the transmission rate (see also {{IPV6_TOPOLOGY}} and {{IPV4_TOPOLOGY}} for some probing speed impacts). Those considerations are out of scope of this document.

# Security Considerations

While it is expected that only good-willing researchers will use these techniques, they will simplify and shorten the time to identify a probing across the Internet.

As both proposed techniques rely on the IP source address, they are vulnerable to IP spoofing.


# IANA Considerations

The "Well-Known URIs" registry should be updated with the following:

- additional values (using the template from {{!RFC8615}}):

- URI suffix: probing.txt

- Change controller: IETF

- Specification document(s): this document

- Status: permanent



--- back

# Acknowledgments
{:numbered="false"}

The authors would like to thank Alain Fiocco, Mehdi Kouhen, and Mark Townsley for helpful discussions as well as Raphaël Léas for an early implementation.

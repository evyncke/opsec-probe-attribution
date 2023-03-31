---
title: "Attribution of Internet Probes"
abbrev: "Probes Attribution"
category: info
submissiontype: IETF
docname: draft-ietf-opsec-probe-attribution-latest
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
  latest: "https://evyncke.github.io/opsec-probe-attribution/draft-ietf-opsec-probe-attribution.html"

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
  RIPE_ATLAS:
    title: RIPE Atlas
    target: https://atlas.ripe.net/
  NCSC:
    title: The National Cyber Security Centre
    target: https://www.ncsc.gov.uk/
  NCSC_SCAN_INFO:
    title: NCSC Scanning information
    target: https://www.ncsc.gov.uk/information/ncsc-scanning-information


--- abstract

Active measurements at Internet-scale can target either collaborating parties or non-collaborating ones. Sometimes these measurements are viewed as unwelcome or aggressive. This document proposes some simple techniques allowing any party or organization to understand what this unsolicited packet is, what is its purpose, and more importantly who to contact.


--- middle

# Introduction

Active measurements at Internet-scale can target either collaborating parties or non-collaborating ones. Such measurements include {{LARGE_SCALE}} and {{?RFC7872}}.

Sending unsolicited probes should obviously be done at a rate low enough to not unduly impact the other parties resources. But even at a low rate, those probes could trigger an alarm that will request some investigation by either the party receiving the probe (i.e., when the probe destination address is one address assigned to the receiving party) or by a third party having some devices where those probes are transiting (e.g., an Internet transit router).

This document suggests some simple techniques allowing any party or organization to understand:

- what this unsolicited packet is,

- what is its purpose,

- and more significantly who to contact for further information or to stop the probing.

Note: it is expected that only researchers with no bad intentions will use these techniques, although anyone might use them. This is discussed in {{security}}.

# Probe Description

## Probe Description URI {#uri}

This document defines a probe description URI as a URI pointing to either:

- a probe description file (see {{file}}) as defined in {{iana}}: "https://example.net/.well-known/probing.txt";

- an email address, e.g., "mailto:user@example.net";

- a phone number, e.g., "tel:+1-201-555-0123".

## Probe Description File {#file}

As defined in {{iana}}, the probe description file must be made available at "https://example.net/.well-known/probing.txt". The probe description file must follow the format defined in section 4 of {{!RFC9116}} and should contain the following fields defined in section 2 of {{!RFC9116}}:

- Canonical
- Contact
- Expires
- Preferred-Languages

A new field "Description" should also be included to describe the measurement. To match the format defined in section 4 of {{!RFC9116}}, this field must be a one line string.

### Example

        # Canonical URI (if any)
        Canonical: https://example.net/measurement.txt

        # Contact address
        Contact: mailto:user@example.net

        # Validity
        Expires: 2023-12-31T18:37:07z

        # Languages
        Preferred-Languages: en, es, fr

        # Probe/Measurement description
        Description: This is a description of the measurement. The in-band probe attribution was used by [I-D.draft-vyncke-v6ops-james].

# Out-of-band Probe Attribution

An alternative to URI inclusion is to build a specific URI based on the source address of the probe packet, following {{!RFC8615}}. For example, with a probe source address 2001:db8::dead, the following URI is built:

- if the reverse DNS record for 2001:db8::dead exists, e.g., "example.net", then the probe description URI is "https://example.net/.well-known/probing.txt";

- else (or in addition), the probe description URI is "https://\[2001:db8::dead\]/.well-known/probing.txt". In this case, there might be a certificate verification issue.

The built URI must be a reference to the probe description file (see {{file}}).

As an example, the UK National Cyber Security Centre {{NCSC}} uses a similar attribution. They scan for vulnerabilities across internet-connected systems in the UK and publish information on their scanning ({{NCSC_SCAN_INFO}}), providing the address of the webpage in reverse DNS.

# In-band Probe Attribution

When the measurement allows for it, a probe description URI should be included in the payload of all probes sent. This could be:

- for a {{!RFC4443}} ICMPv6 echo request: in the optional data (see section 4.1 of {{!RFC4443}});

- for a {{!RFC792}} ICMPv4 echo request: in the optional data;

- for a {{!RFC768}} UDP datagram: in the data part. Note that if the probe is destined to a listened-to/well-known UDP port, the inclusion of the probe description URI may produce undefined results;

- for a {{!RFC9293}} TCP packet with the SYN flag: data is allowed in TCP packets with the SYN flag per section 3.4 of {{!RFC9293}} (2nd paragraph). However, it may change the way the packet is processed, i.e., SYN packets containing data might be discarded;

- for a {{!RFC8200}} IPv6 packet with either hop-by-hop or destination options headers, in a PadN option. Indeed, the probe attribution URI can only be added to IPv6 packets in some extension headers used for the probing. However, inserting the probe description URI in PadN options could bias the measurement itself: as per the informational {{?RFC4942}}, section 2.1.9.5, it is suggested that a PadN option should only contain 0's and be smaller than 8 octets, thus limiting its use for probe attribution. If a PadN option does not respect the recommendation, it is suggested that one may consider dropping such packets. For example, the Linux Kernel follows these recommendations and discards such packets since its version 3.5;

- etc.

The probe description URI should start at the first octet of the payload and should be terminated by an octet of 0x00, i.e., it must be null terminated. If the probe description URI cannot be placed at the beginning of the payload, then it should be preceded by an octet of 0x00. Inserting the probe description URI could obviously bias the measurement itself if the probe packet becomes larger than the path MTU.

Note: the above techniques produce a valid and legitimate packet for all the nodes forwarding the probe, except maybe for a hop-by-hop options header with a PadN option containing the probe description URI. As for the receiver, it may or may not process the packet, depending on where the probe description URI is included (e.g., TCP SYN flag with the probe description URI included in data, destination options header with a PadN option containing the probe description URI). As a consequence, a response may not be received. The choice of the probe description URI location is important and highly depends on the context, which is why multiple possibilities are proposed in this document.

# Technical Considerations

Using either the out-of-band or in-band technique, or even both combined, highly depends on will or context. This section describes the upsides and downsides of each technique, so that probe owners or probe makers can freely decide what works best for their cases.

The advantage of using the out-of-band technique is a fast and easy setup, i.e., running a web server on a probe device to describe the measurements. Unfortunately, there are some disadvantages too. In some cases, using the out-of-band technique might not be possible due to several conditions: the presence of a NAT, too many endpoints to run a web server on, the probe source IP address cannot be known (e.g., RIPE Atlas {{RIPE_ATLAS}} probes are sent from IP addresses not owned by the probe owner), dynamic source addresses, etc.

The advantage of using the in-band technique is to cover the cases where the out-of-band technique is not possible, as listed above. The disadvantage is to potentially bias the measurements, since packets where the Probe Description URI is added might be discarded depending on where the Probe Description URI is located in the packets, and depending on the context.

Having both the out-of-band and in-band techniques combined also has a big advantage, i.e., it could be used as an indirect means of "authenticating" the Probe Description URI in the in-band probe, thanks to a correlation with the out-of-band technique (e.g., a reverse DNS lookup). While the out-of-band technique alone is less prone to spoofing, the combination with the in-band technique offers a more complete solution.

# Ethical Considerations

Executing some measurement experiences over the global Internet obviously require some ethical considerations when transit/destination non-solicited parties are involved.

This document proposes a common way to identity the source and the purpose of active probing in order to reduce the potential burden on the non-solicited parties.

But there are other considerations to be taken into account: from the payload content (e.g., is the encoding valid ?) to the transmission rate (see also {{IPV6_TOPOLOGY}} and {{IPV4_TOPOLOGY}} for some probing speed impacts). Those considerations are out of scope of this document.

# Security Considerations {#security}

While it is expected that only researchers with no bad intentions will use these techniques, they will simplify and shorten the time to identify a probing across the Internet.

This information is provided to identify the source and intent of specific probes, but there is no authentication possible for the inline information.  As a result, a malevolent actor could provide false information while conducting the probes, so that the action is attributed to a third party.  As a consequence, the recipient of this information cannot trust this information without confirmation.  If a recipient cannot confirm the information or does not wish to do so, it should treat the flows as if there were no attribution.

# IANA Considerations {#iana}

The "Well-Known URIs" registry should be updated with the following additional values (using the template from {{!RFC8615}}):

- URI suffix: probing.txt

- Change controller: IETF

- Specification document(s): this document

- Status: permanent



--- back

# Acknowledgments
{:numbered="false"}

The authors would like to thank Alain Fiocco, Fernando Gont, Ted Hardie, Mehdi Kouhen, and Mark Townsley for helpful discussions as well as Raphaël Léas for an early implementation.

The authors would also like to gracefully acknowledge useful review and comments received from Jen Linkova, Prapanch Ramamoorthy, Warren Kumari, and Andrew Shaw.

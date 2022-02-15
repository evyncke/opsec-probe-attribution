---
title: "Attribution of Internet Probes"
abbrev: "Probes Attribution"
category: info

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
    name: Ëric Vyncke
    organization: Cisco
    email: evyncke@cisco.com
  -
    name: Justin Iurman
    organization: Université de Liège
    email: justin.iurman@uliege.be

normative:

informative:


--- abstract

When doing some Internet-wide measurements, it is often necessary to send active probes to either collaborating parties or non collaborating parties; the latter is similar scan and could be perceived as aggressive. This document proposes a couple of simple techniques allowing any party or organization to understand what this unsolicited packet is, what is its purpose, and more important who to contact.


--- middle

# Introduction

When doing some Internet-wide measurements, it is often necessary to send active probes to either collaborating parties or non collaborating parties.

Sending unsolicited probes should be done at a rate low enough to avoid causing a denial of services. But even at a low rate, those probes could trigger an alarm that will request some investigation by either the party receiving the probe (i.e., when the probe destination address is one address assigned to the receiving party) or by a third party having some devices where those probes are transiting (e.g., an Internet transit router).

This document proposes a couple of simple techniques allowing any party or organization to understand: 
- what this unsolicited packet is, 
- what is its purpose, 
- and more important who to contact for further information or stop the probing.

Note: it is expected that only good-willing researchers will use these techniques.

# In-band Probe Attribution

# Out-of-band Probe Attribution

# Security Considerations

While it is expected that only good-willing researchers will use these techniques, they will simplify and shorten the time to identify a probing accross the Internet.

As both proposed techniques rely on the IP source address, they are vulnerable to IP spoofing.


# IANA Considerations

This document has no IANA actions.


--- back

# Acknowledgments
{:numbered="false"}

The authors would like to thank Benoît Donnet, Alain Fiocco, Mark Townsley for helpful discussion as well as Raphaël Léas for an early implementation.

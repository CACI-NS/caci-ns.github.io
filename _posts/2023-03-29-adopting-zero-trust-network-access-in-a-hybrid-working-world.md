---
layout: post
title: "Adopting Zero Trust Network Access in a hybrid working world"
date: 2023-03-29 10:01:00 -0000
categories: networking
---

In today's hybrid-working world, many employees often work remotely from the Branch - at Home, Hotels, Conferences, Coffee Shops and the like. This effectively moves the Network Perimeter from the traditional Branch and Office Boundary right into the heart of the Endpoint Laptop device itself - increasing the possible attack surface for organisational Network WANs. Zero Trust is one approach that can help to overcome some of the cybersecurity challenges that hybrid working can create.

# Not trusting anything is the goal
Zero Trust is a cybersecurity paradigm focused on resource protection and the premise that trust is never granted implicitly but must be continually evaluated. It assumes that no one and nothing on a Network can be trusted until it's proven not to be a threat to organisational security. This means that all users, whether in or outside the organisation's WAN, must be authenticated, authorised, and continuously monitored.

One of the main benefits of Zero Trust is its ability to improve Risk Management. By assuming that all users and devices are potential threats, Zero Trust forces organisations to take a more proactive approach to security. This includes implementing strong authentication mechanisms, monitoring user behavior for signs of suspicious activity, and segmenting Networks to limit the impact of any potential breaches.

# Moving beyond the tuple
Where traditional Firewall and Security approaches focussed largely on the "tuple" - Source IP Address, Destination IP Address and TCP/UDP Destination Port - Zero Trust Network Architectures (ZTNA) move beyond these three dimensions, and allow for additional dimensions of trust verification, such as:

- Time of Day
  - i.e. John in HR works 9-5, so if he's logging in to a System at 9 PM at night, is something suspect?
- Access Location
  - i.e. Sandra on the Reception Desk is normally desk-based at front of house; if she suddenly logs in from the third floor Payroll Desks, is something amiss?
- Host Posture
  - i.e. Paul may be logged in with the correct Username and Password, but if his Antivirus isn't up to date and his laptop last logged into the Domain four months ago, do you really want him on the Network?

Other additional dimensions are available depending on organisational need, but you can quickly see how the dynamic of _implicit trust_ moves instead to _explicit verification_ - moving the notion of trust further down the Network Stack, towards the Network Edge, rather than notionally dealing with arbitrary concepts such as Trusted Networks, Trusted VLANs or Trusted Segments.

# When Split Tunnel becomes No Tunnel
Zero Trust requires consideration of encryption of data, securing email, verifying the hygiene of assets and Endpoints before they connect to Applications. It also involves automating patches to ensure good Network Hygiene while preventing potential malicious actions. A successful implementation of Zero Trust can help bring context and insight into a rapidly evolving attack surface to the security team while improving Users' experience.

This moves beyond the nascent "Split Tunnel" approach which an SD-WAN might take - where, for instance, Office365 Traffic may bypass (or "split") away from the IPsec or SSL VPN Tunnel back to the Corporate Network WAN and use the Native Internet connection instead - instead towards a "No Tunnel" approach. In traditional Split Tunnel, the notion runs:

- The Default Route (0.0.0.0/0) - or the _implicit_ - is sent via the VPN Tunnel back to the Corporate WAN
- The "Split" (i.e. Office365 FQDNs and IP Ranges) - or the _explicit_ - is bypassed from the VPN Tunnel, and bypasses the VPN Tunnel to the Internet direct

In Zero Trust Remote Access, this paradigm changes instead to a notion of:

- The Default Route (0.0.0.0/0) - or the _implicit_ - is _not_ sent via the VPN Tunnel back to the Corporate WAN
- Every Corporate Application - or the _explicit_ - is sent on a case-by-case basis down the VPN Tunnel, towards the Corporate WAN

Adding to this, such VPN Tunnels are often temporal in nature, and instantiated per-Application-Request, rather than running akin to a singular, long-running IPsec or SSL VPN Tunnel session.

# Driving the adoption journey
An organisation's Zero Trust journey begins with understanding what Zero Trust offers. Conceptually, Zero Trust accomplishes this by removing implied trust from any device or user attempting to access resources on a network. Instead of trusting devices based on their location or IP address range as in traditional perimeter-based security models, Zero Trust verifies each request as though it originates from an untrusted network. This verification process includes authentication checks such as Multi-Factor Authentication (MFA), authorisation checks such as Role-Based Access Control (RBAC), Endpoint healthchecks such as patch level Compliance Monitoring or Antivirus Signature status monitoring.

Just as no two organisations look the same, neither do any two Zero Trust Network Architectures or approaches; the entire point of Zero Trust is to wrap in your specific Business context and nuances into your Technology estate. At [CACI Network Services](https://www.caci.co.uk/services/network-infrastructure-consulting/) we have deep heritage and expertise with organisations and Networks all the way from SME up to Enterprise and Public Sector, and are well placed to help you get to grips with ZTNA and associated microsegmentation cybersecurity technologies.

[Get in touch](https://www.caci.co.uk/contact/#contact-form) with us today and let us help you on your Zero Trust journey.

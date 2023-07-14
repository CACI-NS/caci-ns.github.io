---
title: SASE and SSEs are not just another Remote Access VPN
slug: sase-sse-not-just-another-remote-access-vpn
date: 2023-07-10 09:12
category: networking
icon: lock
---

Call it [Secure Access Service Edge (SASE)](https://www.networkworld.com/article/3574014/what-is-sase-a-cloud-service-that-marries-sd-wan-with-security.html); call it [Secure Services Edge (SSE)](https://www.paloaltonetworks.co.uk/cyberpedia/what-is-security-service-edge-sse); call it [Zero Trust Network Architecture (ZTNA)](https://www.zscaler.com/resources/security-terms-glossary/what-is-zero-trust-network-access)... even call it the Service Edge (Bono and U2 would be proud) - you might be forgiven for thinking talk about VPN is everywhere the moment, and wondering why everyone is [Cloudwashing](https://www.cio.com/article/3072650/cloudwashing-what-it-is-and-how-to-avoid-it.html) what you've know as Remote Access VPN for many years.

The answer, bluntly, is they aren't; the modern Business Application Landscape has vastly changed, and Remote Access needs to change with it.

## Story Time
The time was all your Business Applications would be on-premises (on-prem), and you'd need to sometimes infrequently allow employees to access these from home. Let's say you're a typical Enterprise shop, with:

* A few on-premises Data Centres from various UK Managed Services Providers (MSPs), or even Colocation (Colo) Providers
* A few thousand employees scattered across the UK
* A hundred or so Business Applications
* A few Internet Gateway Data Centres with Web Proxies, Reverse Proxies and some diverse Direct Internet Access (DIA) connectivity
* Two hundred or so Branch/Office Locations across various UK Towns, Cities and the odd Factory/out-of-town Location
* Dipping your foot into Public Cloud Providers such as Amazon AWS, Microsoft Azure and Google Cloud (GCP)

Maybe your Environment looked a little like this:

![ExampleCo current topology pre-SASE](/img/sampleco_current_topology.png)

## Current Mode of Operation (CMO)
Most of your Users were in the Office most of the time; when they needed to, they would use their VendorCo VPN Client to dial-in to `https://vpn.yourco.com` which would non-deterministically Load Balance between the Manchester VPN Concentrator and the London VPN Concentrator. This happened with complete disregard of where the User was geographically located (_"Look, it was too hard to explain to the MSP what Anycast DNS is, OK?"_). Their Productivity files (Word Documents; Excel Spreadsheets; etc) were mostly still on-prem, and located on File Servers in their Usual Office Locations; pretty much all the other 80% of the Business Support System (BSS)/Business Applications they need to perform their roles were also in your BSS Data Centres.

You were running some Proof of Concept (PoC) work in the Public Cloud/Cloud Service Providers (CSPs), but weren't too sure if this would really take off in Big Enterprise or suit your needs. Most of your Business Apps had a good heritage and came from a time before React/Vue/Node JavaScript Frameworks existed, and largely before it was thought that a Web UI could be used for anything useful. You've got lots of Fat Clients, Oracle and IBM Middleware Layers, and people generally accept that your ERP Application looks like someone threw up with a paint can, and flunked out of Data Input Class in College (_"Checkboxes? Dropdowns? Multi-selects? Has this Vendor never heard of Input Validation!"_).

Add in some Forward (Web) Proxies because Facebook won't read itself (and you have some legitimate Web Applications your Employees need to get to). Sprinkle on some Reverse Proxies because you had some Applications which - while hosted in your BSS/Backend Data Centres (that weren't natively setup to be Internet-accessible) - over the years you've found Suppliers, Systems Integrators (SIs) and Partners all need access to them. Sadly, these Apps didn't generally have a notion of an [API](https://aws.amazon.com/what-is/api/#seo-faq-pairs#what-is-an-api), so you've had to setup a Reverse Proxy or two in your Internet Gateway Data Centre to allow inbound Internet Access to them from other Systems (M2M).

Most of your Staff thought the Remote Access VPN was clunky, slow, and cumbersome to launch (_"Ever noticed http://internal-intranet doesn't load on the VPN if you left Internet Explorer open before you took your Laptop home for the day, off the VPN?"_), but because they rarely used it, they would quietly tolerate all the issues it posed. You thought it was nice and secure because you only had two entry points into your Network via the WAN.

## COVID-19 Mode of Operation
Things [rapidly change during Lockdown](https://www.instituteforgovernment.org.uk/data-visualisation/timeline-coronavirus-lockdowns), and suddenly most of your Users are now firmly Working from Home (WFH), and are struggling to use your Remote Access VPN because:

* It doesn't have the bandwidth
* It's slow to load (your Scottish Users are going via London; your Watford Users are going via Manchester; you lament not putting in Anycast DNS or Geo-based DNS GSLB)
* It's backhauling everything through two overloaded Internet Gateways (which have their DIA and MPLS pipes in a constant state of "on fire", in terms of Network Capacity Utilisation)
* It's not allowed through half the MSP Firewalls/ACLs you have on your on-prem Environment (_"I thought the VPN was 10.99.0.0/24; when did they change it to 10.98.0.0/23 on us? It'll take weeks to raise these ITIL Firewall Change Requests with MSPCo to get it done!"_)
* Your lesser-Technical Staff don't realise they have to enable it to access some on-prem Applications, and disable it to access the Applications you've quickly lift-shifted to Public Cloud

In short, it's not really working out for you. But can you blame it? Remote Access SSL/IPsec VPN comes from an era before Cloud Distributed Computing existed; it's a [Moat expecting there to be a Castle where everything is inside](https://www.cloudflare.com/en-gb/learning/access-management/castle-and-moat-network-security/). Ditto, because the Applications of it's era operated at the lower levels of the [OSI Model](https://www.networkworld.com/article/3239677/the-osi-model-explained-and-how-to-easily-remember-its-7-layers.html), it needs to give your Client a Network-level (Layer 3) IP Address, and effectively act as an extension of your Corporate WAN "just in case" the Business Application in question needs that functionality to work.

It's a Solution no longer fit for the current Application Landscape of Public Cloud, Commodified Applications and Geo-distributed Workloads.

> The 80/20 has flipped; now more of your Business Applications have found themselves outside your Network Edge castle, and beyond the security afforded by your moat. The drawbridge is firmly down, and the people are fleeing your castle-and-moat WAN architectures

## Future Mode of Operation (FMO)
Let's level-set a bit - you are still a Big Enterprise, so Digital Transformation isn't going to be quick, and you've still got Legacy and on-premises Workloads like Mainframes that can't move to the Public Cloud for lots of sensible financial, compliance and business reasons. However, now you've started to (more aggressively than you'd like to, thanks to Coronavirus):

* Move Commodified Applications (i.e. all the Apps that were never specific to YourCo PLC in the first place -  Collaboration, Document Hosting, ERP and CRM, etc) to the Public Cloud
    * Typically, as a Software as a Service (SaaS) offering (in which case it may as well not exist to your WAN/Public Internet; _"You only need a Web Browser and Internet Connection to access it"_)
    * Sometimes, as something cobbled together with a hybrid of SaaS and Platform as a Service (PaaS) because of a niche workload requirement you have (but it's still likely to bias for at least the Frontdoor of the App to be "Just access with your Web Browser and Internet", even if the Backend/M2M interaction doesn't)
* Deploy SASE Connectors (i.e. [Zscaler ZPA Connectors](https://help.zscaler.com/zpa/about-connectors)) as-close to the Applications as possible, and in multiples (unlike the SSL-VPN Concentrators you only had a few of)
* Deploy SASE Connectors into your Branch Offices
* Deploy SASE Connectors (or accept the native-Internet Frontdoor into) your Public Cloud-hosted Apps

![ExampleCo current topology post-SASE](/img/sampleco_future_topology.png)

You've come to terms that most of your Staff work well Remotely, and that the "fulltime return to Office, Mon-Fri, 9-5" is unlikely to happen. Your staff are much happier using the SASE (i.e. [Zscaler](https://www.zscaler.com), [Cato Networks](https://www.catonetworks.com), [Cloudflare](https://www.cloudflare.com), [Netskope](https://www.netskope.com)), and unexpectedly your DIA and MPLS pipes are actually quieter because of this.

Your Security Posture has improved and you've found that you have less Perimeter Breaches, but you're not too sure why. You also find that Users report the same Legacy Applications (that you've not touched since pre-COVID) are more performant when they're at home than on the Remote Access VPN Prior.

So what's the big change that's happened then? Why are most things much better, it's just SSL-VPN Tunnels, right?

## SSE is not an OSI Layer 3 Network Extender
To understand the performance and security gains that a SSE with ZTNA brings to the table, we need to compare what a SASE/SSE is doing versus what a traditional Remote Access VPN is doing. It's perhaps easier to see this in a comparable format:

| Concern | Remote Access VPN | SASE |
| ------- | ----------------- | ---- |
| OSI Operating Layer | Layer 3 (IP)<br>_"Barry's Laptop is 10.98.99.1/23 from VPN Range..."_ | Layer 4 (TCP/UDP)<br>_"Barry's Laptop just looks like the SASE Concentrator at 10.10.3.2/24"_ |
| Geo-Load Balancing | None<br>_"Claire is in Scotland but came in via the London VPN Concentrator?"_ | Yes (DNS GSLB or Anycast DNS)<br>_"Claire is in Scotland, so went to the SASE Provider's Scolocate DC-hosted SASE Control Server"_ |
| Security Granularity | Course<br>_"We need to allow the whole 10.98.0.0/23 VPN Range access to BusinessApp123"_ | Grain<br>_"Bobby from Finance can access BusinessApp123; nobody else is allowed"_ |
| Tunnel Behaviour | Always-On/All-Traffic<br>_"Janet is wasting DIA and MPLS bandwidth hairpinning in/out to get out to http://some-external-saas-app.com!"_ | Ad-Hoc/Split-Tunnel<br>_"Janet only goes via the SASE Tunnel for on-prem/defined Applications"_ |
| Activity Logging | Minimal (if any)<br>_"I've no idea what Patrick was trying to access via the VPN at 12:52 last Tuesday"_ | Holistic<br>_"Patrick was trying to get to ServerName123 via TCP/456 at 12:52, but the TCP Session never went past SYN-ACK"_ |
| Tunnel Initiation | Singular, User-to-VPN Concentrator<br>_"I see the SSL-VPN Tunnel from Nicole on TalkTalk into our London DC"_ | Multiple, SASE Connector to SASE Cloud<br>_"Regardless of nobody being logged in, the SASE Connector in Colo DC #3 auto-dials-out to SASE.com Control Plane Cloud"_ |
| Day 0 Complexity | Low<br>_"We just route through/allow in ACL 10.98.0.0/23 VPN Range, and away we go!"_ | High<br>_"But I don't know all the Apps I have or TCP/UDP Ports that make up those Apps!"_ |
| Tunnel Flow | (Tun1) User -[Internet]-> VPN Concentrator<br>_"One SSL Tunnel, from a VPN User to a VPN Concentrator"_ | (Tun1) User -[Internet]-> SASE Cloud<br>(Tun2) SASE Cloud -[Internet]-> SASE Connector<br>_"SASE Provider has a Cloud LAN that stitches these two SSL Tunnels together for the end-to-end flow"_ |
| Branch Tunnel |Branch -[Internet]-> VPN Concentrator<br>_"Branch Users always hairpin via our Internet Gateway-hosted VPN Concentrator, using our Internet Gateway DC's DIA bandwidth"_ | Branch -[Internet]-> SASE Cloud<br>_"Branch Users only use our Internet Gateway DC DIA bandwidth when communicating with on-prem Offices; Remote End User stays on SASE Internet"_ |

By far and away the main difference in the SASE model is that of the Cloud-based LAN, where the Cloud-based LAN is the "magic" that stitches together multiple SSL Tunnels, to allow the solution to efficiently only use the SSL Tunnels required for a given end-to-end flow, rather than having to "waste" Internet Gateway DIA/MPLS bandwidth for a flow that may not be to/from an on-prem System or Location. This is also what provides the main benefits of SASE over Remote Access VPN as highlighted above, as the Cloud-based LAN acts as the "Piggy in the Middle" (MITM) to any given Application Flow, and therefore can enforce Security, Bandwidth and other controls at higher-levels of the OSI Model than a Layer 3-constrained Remote Access VPN is able to do.

![ExampleCo topology using SASE as a WAN Fabric](/img/sase_the_cloud_fabric.png)

When compared to the Business Application world, which is doing mostly the same thing (the Cloud is the "world's Computer", and has multiple attachment points/PoPs that are regionally close to the _User_ as the centre of the Universe; not focussed on the App as the centre of the Universe), SASE can be seen as a better fit; in much the same way the Public Cloud uses Global Points of Presence (PoPs) as a mechanism to lessen the latency of an Application, and serve it as close to the User as possible, so too does a SASE use the closest "VPN Concentrator" to a given User. The OpEx-driven model allows a SASE Provider to do this cost-effectively for you as a singular Customer; whereas trying to build your own "Globe-spanning Cloud LAN" would cost significantly more outlay than you may be able to afford; hence using the SASE Provider's reach and expertise can only ever make sense over a more cumbersome Remote Access VPN.

> SASE is doing to the Enterprise WAN what SD-WAN did to the Enterprise MPLS Network; or the Enterprise MPLS Network did the Enterprise Leased Line Mesh that preceded it; abstracting away point-to-point SSL Tunnels into a Fabric of dynamically-run, point-to-multipoint SSL Tunnel Flows that are created and destroyed on-demand

## Struggling with your move to SSE or SASE
At [CACI Network Services](https://www.caci.co.uk/contact/#contact-form) we've had the benefit of seeing many, many Customer Environments - from Heritage, through Legacy into Microservices Modernity - and have deep knowledge architecting, deploying and optimising a variety of SSE and SASE Security Access solutions. [Get in touch](https://www.caci.co.uk/contact/#contact-form) and let us help you untangle the complex web of Secure Access into your Network Edge, and demystify the web of Zero Trust for your WAN.

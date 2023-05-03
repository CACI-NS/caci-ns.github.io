---
layout: post
title: "Rethinking Network Management through Network as a Service"
date: 2023-05-03 08:32:00 -0000
categories: networking
---

Observability as a discipline distinct from Network Management is still in its infancy within the Network Engineering realm, with newer job titles such as Network Reliability Engineer (NRE) looking to extract the same organisational value that the more DevOps-aligned Site Reliability Engineer (SRE) provide to the more traditional SysAdmin space. Network as a Service (NaaS) is a new approach to Network Operations, which often distils down to two commonly accepted meanings:

* An Operational Expenditure (OpEx)-led approach to procuring Managed Network Services and associated Network hardware
* A paradigm shift in the approach to Network Management away from legacy Network Management System (NMS) and associated Element Management System (EMS) lifecycle approaches

In this blog, we'll focus on the latter, and how the formation of a NaaS Team - or Squad - can improve Network Observability, and ultimately aid you in gleaning more insight, uptime and value out of your Network Infrastructure. We'll also touch on the former and the larger shift from Capital Expenditure (CapEx) to Operational Expenditure (OpEx) Lifecycle Management approaches, and what this means for shifts in the IT and Network Industry.

# Another "as a Service"
_"Oh no not another 'as a Service' buzzword-fest..."_ I hear you say, and yes, in some respects, you would be sadly correct. However, Network as a Service (NaaS) has its roots firmly in the overall Cloudification trend found elsewhere within the wider IT and Cloud industry; only now having perculated down towards the steadfast realms of the hardware-centric Network Industry. At its core, NaaS is about the following differentiators from other more assset-centric approaches:

* Consumption of Network Infrastructure through flexible OpEx subscription-based models
* Exploitation of Cloud-based models such as Infrastructure Elasticity and Horizontal Scaling
* Commoditisation of Private WAN Services (such as MPLS) into Public WAN Services (such as SD-WAN)
* Centralisation of Visibility of Network Insight into Application-aware Dashboards and Telemetry systems

At its core, NaaS is more an Operational Model than it is a Consumption Pattern; NaaS is chiefly about realigning thinking towards that of the upper-layers of the OSI Model, in remembering that the chief objective of the Network is to solidly underpin an ever-more complex soup of interconnected Middleware, Microservices, PaaS and SaaS Dataverse ecosystems which eventually combine toward the aspiration of the modern [Twelve-Factor App Manifesto](https://12factor.net).

# Observability versus Monitoring
Before we can dive into NaaS, we need to understand the difference in Observability versus Monitoring - or that is, focus on the Three Pillars of Observability, namely:

1. Logs
2. Metrics
3. Traces

Each is distinct in its value and requirements in the art of Observability, but in short could be defined as:

* Logs - The act of logging function or component-level activities to an off-system repository for later analysis
  * An example might be a Syslog showing the last reboot of a Linux or NOS Daemon or Service, such as NTPd maybe for System Clock
* Metrics - The performance of the Infrastructure-aligned components within the system, as typically observed over a time-graphed basis
  * An example might be a CPU Utilisation monitor, showin that the Processor has crept up to 78% utilisation over the last ten minutes
* Traces - The ability to debug low-level sub-component and function activities to derrive context of whether a piece of Software Code is working as prescribed
  * An example might be a Trace within a Python Function, showing that the error being caused by Netmiko is because a SSH Session to a Cisco Router dropped out at v1.99 instead of expected SSHv2

These differ somewhat from traditional Monitoring approaches - such as Network Management Systems (NMS), which have typically only focussed around the _Metrics_ pillar, and superficially referenced the other two pillars. What Observability has done to traditional Monitoring is comparable to the movement happening from the NMS to the NaaS arena; effectively to move the management concern "up the stack", and focus on higher-level abstraction objectives, and away from lower-level hardwared-led concerns.

# NaaS as an approach
NaaS is ultimately a conceptual change in _consumption_ of the Network as a going concern; rather than worrying about the Network Layer as a _discrete_ concern, the Network is positioned as part of the wider Technology Stack - often up to and including the Application Layer - that is services. While this may sound trivial, it is a huge step change in how Enterprise and Service Provider (SP) Networks are operated when contrasted against the current de facto practices. NaaS can be simplified as being a "Cloud model" - not in the sense that it has to be operated and hosted within Public CSP Cloud Service Providers - but more in the ideas associated around Cloud Operational Models, including Service Elasticity; OpEx-led Billing; Horizontal Scaling and API-first integrations into wider ecosystem concerns.

The main benefit of NaaS is flexibilty and adaptability to changing Technical Stack conditions; where a legacy NMS-led approach might falsely report "All clear; the Network is fine" because _Metrics_ are clean and green, a newer NaaS-led approach might instead report "Problems detected in latency experienced by the Application due to MTU Clipping" because the upper-level _Traces_ and _Logs_ collectively indicate an issue to a latency-sensitive Service Bus-based Application. The true strength of NaaS lies in it's alignment of the Network Layer to Cloud, DevOps and Observability practices to provide the ability to monitor, manage and track Network as if it were just another IaaS or PaaS component of the overall Application Stack.

# Interested in adding NaaS to your IaaS and PaaS?
With several years of Network Management and Enterprise Network Operations experience, [CACI Network Services](https://www.caci.co.uk/services/network-infrastructure-consulting/) are ideally positioned to help you make the transition from NMS to NaaS. [Contact us today](https://www.caci.co.uk/contact/#contact-form) and see how we can help your business fully shift towards the Observability promise as delivered by a NaaS approach to Network Operations.

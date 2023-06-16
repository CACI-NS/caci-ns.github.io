---
title: Demise of the CMDB - Network Source of Truth killed the ITIL Star
slug: demise-of-the-cmdb-devops-nsot-itil
date: 2023-06-16 13:16
category: itsm
icon: database
---

For years, the Configuration Management Database (CMDB) has been an integral part of IT Service Management (ITSM) for organisations. It has been the go-to tool for managing the Configuration Items (CI) of an organisation's IT environment, including hardware, software, and relationships between them. Indeed, this is to the extent that most people raising Change Requests even call them "CIs" without necessarily knowing what that stands for. But no longer.

![DevOps is greater than ITIL](/img/devops-vs-itil.jpg)

In recent times, the rise of DevOps practices - such as Network Source of Truth (NSoT), Service Bus, Event-driven Architecture and Continuous Integration/Continuous Deployment (CI/CD) have led to a decline in the use of the CMDB and IT Infrastructure Library (ITIL) practices in general. We'll discuss why the CMDB is becoming less relevant as organisations mature their DevOps Journey, and contrast some of the disadvantages of the CMDB when compared to the NSoT.

## The CMDB is Dead; long live the Source of Truth
The traditional CMDB model, as mentioned above, is used to manage Configuration Items, track Changes, and support key ITIL processes such as Incident Management, Problem Management and Capacity Management. Sadly, it also dates from a time when many of these were directly correlated with _physical_ assets - the Baremetal Server; the Office Printer; the Desktop PC - and so doesn't deal well with logical or conceptual models prevalent in Modern IT Workloads - Nested Virtualisation, Container Network Layers, Side Car Proxies and so on.

CMDB's rigid Data Model and legacy Data Structure has opened the door to a series of contenders within the space, largely grouped together under the umbrella of "Source of Truth", some notable examples in the NetDevOps and DevOps spaces being:

* [NetBox](https://netbox.dev)
* [Ralph](https://ralph.allegro.tech)
* [MAAS](https://maas.io)

Instead of CMDBs, many organisations are now turning to Source of Truth practices. This approach aims to simplify Configuration Management by focusing on a single source of information — the “source of truth”. This Source of Truth is often a repository or database used to store configuration data for an organisation's IT environment.

## Source of Truth is a DevOps Practice
The key "why" behind all this can be easily summarised when contrasting the strengths and weaknesses of the CMDB against the NSoT further. In short, Source of Truth is a DevOps practice that seeks to simplify Configuration Management by listing all Configuration Items and their relationships in a single location. This one version of truth can then be used for Deployment Automation, Infrastructure Management, and much more. Another key attribute of the SoT is the usage of data-driven, structured Data Models such as YANG, which naturally integrates with well-used DevOps Data Structures such as YAML and JSON, for frictionless flow between ITSM process and the intended Infrastructure Outcome required.

| CMDB Approach | NSoT Approach |
| ------------- | ------------- |
| - Cumbersome, semi-structured and manual GUI-driven data input | + DevOps-native Structured Data YAML, JSON and CSV data input |
| - Static assumptions around physical world constraints and data relationships | + Dynamic codification of logical or physical data relationships via YANG |
| - Rigidly aligned to static ITIL process definitions | + Loosely coupled to DevOps process guardrails |
| - Typically driven through human intervention from Configuration Engineers | + Typically driven via API interaction with other Systems, Managers and Controllers |
| - Normally present as part of a monolithic, costly ITSM system | + Normally present as either FOSS or microservices-based modules |
| - Designed for human interaction in mind with limited automation opportunities | + Designed for Automation in mind with expected third-party System Integrations |
| - No or limited integration possible with IaC tooling and frameworks | + The bedrock of any well-formed CI/CD Pipeline or IaC framework deployment |

## Integration in the age of disaggregation
Increasingly we see IT Departments stretched with their ITIL-based approaches and ITSM Systems which were designed for singular, homogenous deployments of IT Network Infrastructure within the confines of the on-premises Data Centre - unable to cope as increasing amounts of their Application Workload estate migrates off-premises into the various Public Cloud PaaS, SaaS and Hybrid Cloud models of today. As [Network Consultants](https://www.caci.co.uk/services/network-infrastructure-consulting/) and [Deployment Engineers](https://www.caci.co.uk/services/network-infrastructure-consulting/), we see first-hand the issues that CMDB-based approaches create, and frustrations throughout. Contrast this with a NSoT-led approach where we might instead see the ability to:

* Simplify Configuration Management
    * By using a single source of truth, organisations can avoid the complexity and cost of managing multiple CMDBs across their Hybrid IT Network, Compute, Storage and Application Estate
* Improve collaboration
    * Using a central repository for configuration data helps improve collaboration between Development and Operations teams (i.e. this is why they call it _DevOps_)
* Enable automation
    * With a centralised source of configuration data, it becomes easier to automate repetitive tasks such as Deployment and Testing, freeing up valuable Development and Operations resource time away from undifferentiated heavy lifting tasks
* Facilitate auditing and compliance
    * A centralised repository of Configuration Data also makes it easier to track changes and ensure compliance with IT Security Standards such as SOC2, HIPAA, NIST, PCI-DSS, CESG and DORA

## Bolster your Configuration Management journey
As well as a strong heritage in [Network Infrastructure Engineering and Consulting](https://www.caci.co.uk/services/network-infrastructure-consulting/), we have developed a strong set of [ITSM Consultants](https://www.caci.co.uk/services/data-management/) available to help with your CMDB Migration programmes - across the spectrum from Service Design, Project and Programme Management and through to Data and Solution Architecture. [Let us help](https://www.caci.co.uk/contact/#contact-form) and see how we can unlock the value of the CI data you have to bring you closer to the point of Application Observability over just plain Asset Visibility.
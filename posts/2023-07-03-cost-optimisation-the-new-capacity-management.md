---
title: Cost Optimisation is the new Capacity Management
slug: cost-optimisation-the-new-capacity-management
date: 2023-07-03 20:16
category: itsm
icon: thermometer-three-quarters
---

Capacity Management has been a stable of IT Service Management (ITSM) for many years, often historically associated with practices such as Just In Time (JIT) hardware provision to achieve Network, Storage or Compute low-watermarks which sustain Service Level Agreements (SLAs). However, as the move to commodified on-demand workload prevails - as enabled through Cloud and DevOps Provisioning practices - Capacity Management begins to become less optimal as a practice to sustain the delicate balance of cost versus performance for an IT System.

![Cost Optimisation contrasted with Capacity Management](img/cost-optimisation-capacity-management.jpg)

However, with the increased adoption of Cloud Native giving rise to OpEx, rental-based workload hosting over CapEx, ownership-based workload hosting, we're seeing a new contender for managing performance against cost in the IT Services space - _Cost Optimisation_.

## The benefits of Cost Optimisation
Cost optimisation is the process of identifying and reducing sources of wasteful spending, underutilisation, or low return in the IT budget. The goal is to reduce costs while reinvesting in new technology to speed up business growth or improve margins. Mainly, it is a continuous process of identifying and reducing sources of wasteful spending and low return in the IT budget - and unlike Capacity Management, it focuses on *System Architecture* improvements and modifications, as well as the tweaking of Compute, Storage and Network levers, in order to achieve its goal.

In the Cloud context, Cost Optimisation often looks like a FinOps team, process or mandate, which is tasked with the following to achieve the cost reduction:

* Identify and reduce mismanaged or excess resources
  * i.e. Identify Azure VM Scale Sets with overprovisioned and unused Azure Virtual Machine members
* Take advantage of advance purchase discounting options where lifecycle is prolonged
  * i.e. Purchase AWS EC2 Reserved Instance pricing for a 3-year term to achieve a 60% or more cost saving against on-demand EC2 pricing
* Take advantage of Cloud-complimentary licensing schemes for IaaS
  * i.e. Utilise Azure Hybrid User Benefit (HUB) to achieve up to 70% cost saving of an Azure SQL instance using existing on-premises Microsoft SQL Licensing
* Rightsize compute, storage or network workloads to specific requirements
  * i.e. Swap-out an underutilised, low-IO Azure Premium SSD for a Azure Standard SSD

Much of this runs contrary to traditional Capacity Management practices, as the main vehicles of achieving these are often to go _under the bonnet_ and actually _rearchitect_ elements of how the IaaS or PaaS components operate to achieve the improvements in the upper-layer Application workloads. Cost Optimisation can be a great way to build a scalable, modern infrastructure that meets the demands of your workloads without going over budget.

Ideally, you want your Cloud Infrastructure costs to go flat or increase only marginally as your Client or installed Application workload base grows over time. But if your costs rise faster than - or as quickly as - you onboard Customers, you may have a problem. Cost Optimisation can help you identify areas where you can reduce costs and reinvest those savings in other areas of your Infrastructure or Business Operations.

## Shifting away from Capacity Management
Capacity Management has traditionally focussed on ensuring that IT systems have the resources they need to perform optimally, against a backdrop of on-premises IT where Baremetal was king and OpEx was reserved purely for Software Licensing concerns. However, this approach is no longer sufficient in today's complex IT environments, where ephemeral workloads and infrastructure elasticity mean it can be difficult to keep track.

> Capacity Management isn't cutting it for your dynamic, Cloud-native workloads anymore. It is time to shift towards a more dynamic system of Resource Management through Cost Optimisation

By shifting from Capacity Management to Cost Optimisation, organisations can better align their increasingly limited IT spending with business priorities. This approach involves identifying areas where costs can be reduced _without_ sacrificing the important Observability Pillars of Performance or Reliability.

## Best Practices for Cost Optimisation
Being successful with Cost Optimisation initiatives requires a cultural shift - as enabled via DevOps and Agile Project Management practices - towards these best practices:

1. Align initiatives with business priorities
    * Cost Optimisation initiatives should be aligned and prioritised to the overall business priorities to avoid "penny-wise and pound-foolish" behaviours (i.e. skimming pennies off AWS EBS Disk size, when an exponentially-more-cost-effective AWS S3 Bucket would be a better fit for an Object Storage challenge instead)
2. Identify and right-size over-provisioned resources
    * Using the right tools (such as [Zesty](https://zesty.co), [Spot](https://spot.io), [nOps](https://www.nops.io) and [Harness](https://harness.io/products/cloud-cost/)) to identify, optimise scale-down and turn off overprovisioned Infrastructure, including automated optimisation
3. Be accountable for Infrastructure costs using chargeback, recharge or show-back
    * Accountability for costs needs to be clearly articulated and factored in to the RACI for required stakeholders to be keenly aware of their Business Unit's impact on overall IT Infrastructure spend
4. Take action to optimise spend
    * Much like "Security by Design", Spend _by Design_ should be an upfront factor in the IT Infrastructure or Network design process, from Day 0 Design rather than a Day 2 Operations afterthought
5. Use the right tool for the right job
    * When architecting a System, care should be given to tooling selection and "on-premises bias" - for instance, AWS S3 is a fantastic cost-efficient choice for Static Asset (Image/CSS/etc) storage which doesn't exist on-premises, so might otherwise be approximated with a more costly solution, such as an AWS EBS or AWS EFS Network-based File Store via AWS EC2 to achieve the same at a much higher cost

> Cost Optimisation isn't a one-shot activity, it is an ongoing, continuous process to enable optimal business operations and garner cost efficiency. Cloud waste-reduction should always be the goal to finance growth in desired USP and differentiators

## Continuing the Efficiency
Gartner predicts Cloud spending to grow to almost $600 billion in 2023, with previous trends showing the Cloud TAM (Total Addressable Market) as having increased year-on-year at a rate of 20-30%. In 2026 it is estimated Public Cloud expenditure could be as much as _half_ of all Enterprise IT budget spending. Unlike on-premises Infrastructure, which can be amortised and _deprecated_ over time; Cloud spend tends to be ongoing Operational Expenditure (OpEx), and can often _increase_ over time for a given workload as its use or Client base grows over time.

If you want those flat or diminished Infrastructure costs, this means you have to integrate Cloud Optimisation into your business processes and daily workflow; Cloud Optimisation isn't a "one and done" endeavour. Indeed, to be truly mature in Cloud Optimisation, we would advocate for FinOps practices to be engrained into the CI/CD Pipelines and ITSM Governance Gating processes - such as Design Board, CAB and ITDB - to truly treat it as a first-class citizen amongst other competing factors within the System Operation and Design.

Cost Optimisation should exist to answer these questions in providing value back to the Business:

* How much does each Product Feature or Enterprise Application cost to operate over time?
* What is the Unit Cost of Infrastructure when compared against Gained Functionality?
* How high is our Utilisation Cost per Customer (for a SaaS Company) or Application (for an Enterprise) per End User?
* Can we reduce the performance tiers of Compute, Storage or Network components to cheaper variants without reducing perceived SLA and OLA commitments?
* Do our Development workloads operate to sensible Development-sized smaller or less-performant IaaS or PaaS components?
* Can we Proof of Concept (PoC) under-provisioning against Enterprise Application workload System Requirements to measure the _actual_ impact - if any - on the SLA and OLAs our End Users are signed up to?
* Can we utilise Economies of Scale to make more Infrastructure components cost less on aggregate?
    * _Think along the lines of "Domino's Promo-Codeconomics - adding a 49p dip to your Domino's Order to push it over £50 so the "20% off £50" Promo Code takes affect_

## Finesse your FinOps
At [CACI Network Services](https://www.caci.co.uk/services/cloud-infrastructure/) we're well versed in using Cost Optimisation techniques to provide best-value for various types of Enterprise and Application Workload architectures, through our strong heritage in [Network Infrastructure Engineering and Consulting](https://www.caci.co.uk/services/network-infrastructure-consulting/). [Get in touch](https://www.caci.co.uk/contact/#contact-form) and let our experts start working alongside your FinOps Teams to tame your Cloud bills by imparting our Cloud Optimisation know-how and learnings from Industry.
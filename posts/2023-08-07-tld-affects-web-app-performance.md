---
title: How much does a TLD affect your Web Application performance
slug: tld-affects-web-app-performance
date: 2023-08-07 14:10
category: devops
icon: thermometer-empty
---

Time was the Internet consisted of just a few Top Level Domains (TLDs) - `.com`, `.net`, `.org` and a few others - but not anymore. [TLD-List](https://tld-list.com) reports there are now over **3,745** domain extensions and growing, with even some brands having their own Organisation Extensions such as `.barclays` and `.bbc` in use for Careers Sites, Product Pages and more.

As well as their obvious and [well-documented impact](https://www.semrush.com/blog/will-using-alternate-tlds-affect-your-seo-negatively/) on <abbr title="Search Engine Optimisation">SEO</abbr>, did you know they can also _negatively_ impact your Website Performance - particularly on Load Times and <abbr title="Time To First Byte">TTFB</abbr>?

![Measuring the impact of TLD on DNS performance](/img/tld-impact-on-dns-performance.jpg)

We'll investigate how we replatformed some of our web assets to overcome an issue with SEO Performance we didn't even know we were having.

## Background on the roots of DNS
_(Yes it's a pun, yes we're proud of that if you got it. Yes, we are [hiring](https://www.jobserve.com/gb/en/listings/employers/caci-network-services/?lid=6f0fd8f357)...)_

DNS - or Domain Name System - is an often overlooked part of the Internet today, but is very much a key building block to the rest of the Web. Before we can discuss why differing TLDs have impact on performance, it is useful to have some grounding in DNS concepts first.

At its heart, DNS is a [tree hierarchy](https://en.wikipedia.org/wiki/Tree_structure) - with an invisible `dot` as the mandatory root. At a base level, the main job of DNS is to resolve a domain such as `www.google.com` to an IPv4 or IPv6 Address such as `8.8.8.8` for TCP/IP to start the packet connection process to.

Let's explore this with the well-known subdomain `calendar.google.com`. Firstly, although you don't type this with the suffixed dot (`.`), it is very much there. Don't believe us? Try this in a Command Prompt:

`ping calendar.google.com.`

Here's what we get:

```Bash
ping calendar.google.com.

Pinging calendar.google.com [142.250.180.14] with 32 bytes of data:
Reply from 142.250.180.14: bytes=32 time=7ms TTL=119

Ping statistics for 142.250.180.14:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 7ms, Maximum = 7ms, Average = 7ms
```

> **ProTip**: Ever tried to `ping` or `nslookup` something external like `website.com` only to have the result come back as `website.com.internal.corp.acmeco.local` on you? Same difference; Windows commands like `nslookup` assume _everything_ is a subdomain of your DNS Suffix Search List if you don't suffix a "." (dot) at the end. Most Applications like Web Browsers automagically do this in the background for you; much the same as they silently add`:443` to the end of HTTPS websites

If we deconstruct `calendar.google.com`, and process it right-to-left from the perspective of the DNS Tree Hierarchy, it's made up of:

* **Root** - `.` (invisibly added in)
* **Top Level Domain (TLD)** - `com`
* **Domain** - `google`
* **Subdomain** - `calendar`

The hierarchy is important because each layer informs which signpost needs to be used for the IP Address Lookup up the tree. Name Servers (or "NS") are used to act as the signpost for Domain Name to IP Address resolution. There are two main "types" of Name Server (DNS Purists will come for us - we know, we know...):

* **Root Zone (Internet Bodies)**
  * Run by organisations similar to [<abbr title="Internet Assigned Numbers Authority">IANA</abbr>](https://www.iana.org) and [<abbr title="Internet Systems Consortium">ISC</abbr>](https://www.isc.org) for the good of the wider Internet itself, as a going concern
* **DNS Zone (Registrars and Organisations)**
  * Run by either Domain Registrars such as [Namecheap](https://www.namecheap.com), <abbr title="Internet Service Providers">ISP</abbr>s and <abbr title="Content Delivery Network">CDN</abbr>s such as [Cloudflare](https://www.cloudflare.com) or End User Organisations themselves - for the Organisation's self-interest

This distinction is important when it comes to the level of detail signposted by a given Name Server at any given level of the DNS Hierarchy.

## Function of a Name Server
The level of a Name Server within the hierarchy determines the amount of information it returns, and normally the higher the level (towards the root), the less information it gives (is just likely to signpost to another Name Server with the detailed IP information). Using the same example, let's see this in practice with the same `calendar.google.com` example and walk-through the hierarchy:

| Element | Level | Response | Notes |
| ------- | ----- | -------- | ----- |
| `.` (dot) | Root | `com is served by a.gtld-servers.net` | Notional "response" to show concept |
| `google.com` | TLD | `Google.com is served by Name Server ns1.google.com` | This is the response that (via the [DNS Resolution Chain](https://www.cloudflare.com/en-gb/learning/dns/glossary/dns-root-server/)) `a.gtld-servers.net` gave |
| `calendar.google.com` | Subdomain | `calendar.google.com is available at 142.250.187.238` | This is the response that `ns1.google.com` gave |

As can be seen, the function of each upper-level of the hierarchy is ultimately to point to another signpost element lower-down in the hierarchy that knows the IP Address answer. The reason for this is scaling - it wouldn't scale to have a flat hierarchy of all the [628.5 million registered Domain Names](https://colorlib.com/wp/domain-name-statistics/) in the Web, let alone the numerous hundreds or thousands of subdomains _each_ of those could have.

> In practice the Client rarely probes the _actual_ Authoritative DNS Resolver for a given DNS Zone, usually the DNS Recursion Chain is such that a Client resolves against a Caching DNS Server run by their downstream ISP, CDN, Cloud or other DNS Provider. Here caching plays a role to offload lookup stress on the DNS Ecosystem; the above example is simplified to show the concept in isolation of the impact of DNS optimisations such as DNS Caching and Anycast

## The Famous Thirteen
You may have been around the Interwebs long enough to have heard of the [infamous "13" Root Servers](https://www.cloudflare.com/en-gb/learning/dns/glossary/dns-root-server/) which effectively act as the Name Server phonebook for the original TLDs such as `.com` and `.net`, and are currently:

| Name Server | IPv4 Address | IPv6 Address |
| ----------- | ------------ | ------------ |
| a.gtld-servers.net | 192.5.6.30 | 2001:503:a83e:0:0:0:2:30 |
| b.gtld-servers.net | 192.33.14.30 | 2001:503:231d:0:0:0:2:30 |
| c.gtld-servers.net | 192.26.92.30 | 2001:503:83eb:0:0:0:0:30 |
| d.gtld-servers.net | 192.31.80.30 | 2001:500:856e:0:0:0:0:30 |
| e.gtld-servers.net | 192.12.94.30 | 2001:502:1ca1:0:0:0:0:30 |
| f.gtld-servers.net | 192.35.51.30 | 2001:503:d414:0:0:0:0:30 |
| g.gtld-servers.net | 192.42.93.30 | 2001:503:eea3:0:0:0:0:30 |
| h.gtld-servers.net | 192.54.112.30 | 2001:502:8cc:0:0:0:0:30 |
| i.gtld-servers.net | 192.43.172.30 | 2001:503:39c1:0:0:0:0:30 |
| j.gtld-servers.net | 192.48.79.30 | 2001:502:7094:0:0:0:0:30 |
| k.gtld-servers.net | 192.52.178.30 | 2001:503:d2d:0:0:0:0:30 |
| l.gtld-servers.net | 192.41.162.30 | 2001:500:d937:0:0:0:0:30 |
| m.gtld-servers.net | 192.55.83.30 | 2001:501:b1f9:0:0:0:0:30 |

As it turns out, these aren't the only Root Name Servers in town; there are an ever-increasing set of Root Servers to support the ever-increasing amount of TLDs proliferating today, as recorded by the [IANA Root Zone Database](https://www.iana.org/domains/root/db/).

What's more, these aren't all created equal - as it turns out, not everyone is as passionate about DNS Performance optimisation as internet society organisations such as the <abbr title="Internet Engineering Task Force">IETF</abbr> are.

![When Root DNS response time is 76% of your response time](/img/how-can-it-be-600ms.png)

## Sometimes Root DNS is three quarters of the response time
Please, take a seat - it _shocked_ us too. We were looking into why the response time of some parts of our previous [Job Board](https://caci.tech/careers/) `cacins.careers` were so bad, and had just moved from using cURL commands into the awesome [ReqBin REST Testing Tool](https://reqbin.com/curl/) when we spotted the above. Assuming no DNS Caching in play, of the `668ms` response time, DNS resolution took up a shocking `509ms` - or **76%** - of the entire HTTP `GET` process.

> _"Surely it's just us, surely other domains aren't affected as well?"_

> _"It can't... you can't... five-HUNDRED-milliseconds?"_

> _"You're making these quotes up just to make the Blog sound more plausible? I can't believe you'd do such a thing!"_

So the journey began. Using the [IANA Root Zone Database](https://www.iana.org/domains/root/db/), we undertook the following not-really-that-scientific process to check if it was indeed just us:

1. Collate a bunch of TLDs operated by differing [TLD Managers](https://www.iana.org/domains/root)
2. Perform a DNS Lookup to their associated Root DNS Server from the [IANA Root Zone Database](https://www.iana.org/domains/root/db/)
3. Measure the time of this lookup in Windows using `powershell "Measure-Command { nslookup domain.tld. root.tld.server.tld. }"`
  * i.e. For `fast.com` this command was: `powershell "Measure-Command { nslookup fast.com. a.gtld-servers.net. }"`

Here's our quasi-scientific results:

| TLD | Domain | First Root DNS Server | TLD Manager | Lookup Time |
| --- | ------ | --------------------- | ----------- | ----------- |
| ai | `fast.ai` | `a.lactld.org` | [Government of Anguilla](https://www.iana.org/domains/root/db/ai.html) | 92ms |
| app | `fast.app` | `ns-tld1.charlestonroadregistry.com` | [Charleston Road Registry Inc](https://www.iana.org/domains/root/db/app.html) | 88ms |
| blog | `fast.blog` | `a.nic.blog` | [Knock Knock WHOIS There LLC](https://www.iana.org/domains/root/db/blog.html) | 116ms |
| careers | `fast.careers` | `v0n0.nic.careers` | [Binky Moon LLC](https://www.iana.org/domains/root/db/careers.html) | 496ms |
| com | `fast.com` | `a.gtld-servers.net` | [VeriSign Global Registry Services](https://www.iana.org/domains/root/db/com.html) | 58ms |
| co.uk | `fast.co.uk` | `dns1.nic.uk` | [Nominet UK](https://www.iana.org/domains/root/db/uk.html) | 102ms |
| io | `fast.io` | `a0.nic.io` | [Internet Computer Bureau Limited](https://www.iana.org/domains/root/db/io.html) | 62ms |
| net | `fast.net` | `a.gtld-servers.net` | [VeriSign Global Registry Services](https://www.iana.org/domains/root/db/com.html) | 48ms |
| network | `fast.network` | `v0n0.nic.network` | [Binky Moon LLC](https://www.iana.org/domains/root/db/network.html) | 482ms |
| org | `fast.org` | `a0.org.afilias-nst.info` | [Public Internet Registry (PIR)](https://www.iana.org/domains/root/db/org.html) | 458ms |
| tech | `fast.tech` | `a.nic.tech` | [Radix FZC](https://www.iana.org/domains/root/db/tech.html) | 95ms |
| training | `fast.training` | `v0n0.nic.training` | [Binky Moon LLC](https://www.iana.org/domains/root/db/training.html) | 488ms |

> We only picked the `fast` domain because we thought it would be most-likely to be registered across a selection of some technology-related TLDs and not give a false-positive with a NXDOMAIN response. Also maybe we want you to think we're really, really fast at doing things

Clearly this isn't taking into the account the following:

* DNS Anycast affect on Root Name Server choice and availability
* DNS Anycast routing affect on geographic location
* DNS Recursion Chain affect on lookup Client (in reality an ISP, CDN, Cloud or dedicated DNS Name Server)
* DNS Caching of lookups (in reality an ISP, CD, Cloud or other downstream DNS Resolver will cache responses for a time)
* Appeasing the DNS Gods with your latest incantation...

But does give some food for thought on the impact that a seemingly invisible part of _every_ Web App request - the DNS Lookup - can have, and how such a low-level component such as choice of TLD can impact this. Turns out it's not just SEO that can be impacted by TLD choice.

## Need help with your own three-part DNS Murder Mystery?
At [CACI Network Services](https://www.caci.co.uk/services/cloud-infrastructure/) we're well practiced in going full-blown [Poirot](https://en.wikipedia.org/wiki/Hercule_Poirot) on a variety of DNS, Network and Cloud murder mystery investigations. We've completed so many we think we're in for a shot with being the guest stars on the next Midsomer Murders.

In the meantime, if you'd like us to keep go all [Pink Panther](https://en.wikipedia.org/wiki/The_Pink_Panther) on your very own Infrastructure Conundrum, we're all (pink) ears -  [get in touch](/contact/) and let us help you go from Inspector Clouseau to clue-solved.

And whatever you do, _don't_ start humming the [Pink Panther theme tune](https://www.youtube.com/watch?v=HhHwnrlZRus) in your head, you'll never get it out... Sorry. No really. Sorry.
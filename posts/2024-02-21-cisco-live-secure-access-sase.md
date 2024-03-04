---
title: Cisco Live Secure Access and SASE
slug: cisco-live-secure-access-sase
date: 2024-02-21 15:56
category: networking
icon: shield
---

With the rise of remote work and cloud applications, organisations face challenges in maintaining security and user satisfaction. Cisco Secure Access addresses these concerns by consolidating security and networking services in a cloud-based Secure Access Service Edge (SASE) solution.

Cisco Secure Access solution offers a unified approach to access control (Zero Trust principles) and enabling users to connect seamlessly from anywhere to their applications.

Let me simplify it for you...

![Cisco SASE Architecture slide from CLEUR](/img/cisco_live_2024_sase.png)

## Who? Users
The main concept of SASE is to provide seamless network access to users from anywhere, even on an airplane with the worst possible internet connection!

First a new Cisco ZTA module gets installed on managed endpoints. Then users register their laptops or mobiles, devices get a certificate and that's it! No more email, password or MFA required for remote access! Un-managed devices can also be used for accessing applications which is great for 3rd party integrations.

## What? Apps
Users can access any port, protocol or application no matter where those apps are: DC, AWS, private cloud or even SaaS. All you need to do is to install Resource Connectors (RC), basically a Cisco CSR 1000v Cloud Services Router on a VM at your destination. Cisco Secure Access configures RC's and establishes a secure tunnel to that network.

## How? Secure Access
Users opens a browser and types in their destination URL without no need to lunch VPN or sign in to multiple platforms. Cisco ZTA module (good old Umbrella) kicks in and redirects the traffic to Secure Access. Cisco Secure Access knows where each application is, so it re-directs the traffic to the best possible destination using built in monitoring agents (good old Thousand-Eye module). Obviously, traffic goes through multiple layers of security such L7 firewalls, IPS/IDS, content filtering, device posture checks and so on! 

Cisco Secure Access sounds really promising and with the right price incentives, it can be the end of corporate VPN! So if you are working with firewalls for remote-access or site to site VPNs, this is something you will really enjoy working with! 

## Help? Getting to ZTNA
If this resonaltes with you, and we can help implement Cisco SASE and Secure Access for your Network, then [get in touch](https://www.caci.co.uk/contact/#contact-form) and let us bring you the benefits of Zero Trust over the headache of traditional Remote Access VPN. Zero Trust? We've got your back.
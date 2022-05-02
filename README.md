# Sentry

A tool designed to detect drones broadcasting on WiFi frequencies based on MAC addresses.


## Disclaimer

Sentry is presented as a security and privacy tool. However, it should not be treated as the only line of defense, and you should not use it for security, safety, or other critical tasks without being fully prepared for it to fail.


## Description

Drones are unique tools that allow consumers and organizations alike to explore new areas, capture interesting videos, and increase safety. However, like most tools, commercially available drones can also be misused to carry out mass survillance, or capture images and video of people and locations without permission.

Sentry is a tool designed to detect commercial drones operating on WiFi frequencies (2.4 GHz and 5 GHz) by analyzing the MAC addresses of nearby wireless devices constantly. While not perfect, this offers a reasonable level of protection at an extremely low cost. Instead of complex radar systems that can cost tens of thousand of dollars, and Sentry system can run on affordable hardware that most consumers already have laying around.


## Features

### Lightweight

Sentry is extremely lightweight, and can work reliably even on low powered single-board computers.

### Simple

Sentry is designed intentionally with simplicity in mind. All of it's dependencies come pre-installed on the vast majority of Linux distributions, making it easy to install, and difficult to configure incorrectly.

### Extensible

Sentry uses the network manager built into the majority of Linux distributions, meaning it's easy to add external network devices and wireless adapters to Sentry.

### Customizable

Sentry uses a simple configuration file to allow the user to customize Sentry to fit their specific use case.

### Private

Sentry works completely offline, and doesn't require a central server of any kind. All information recorded by Sentry stays on the local device.

### Fast

Since Sentry uses the built-in network manager to scan for potential threats, Sentry's scanning process is as fast as your operating system's scanning process.

### Stable

While it should not be relied upon for critical tasks, Sentry is designed to be as stable as possible, and to detect potential issues before they lead to a crash.

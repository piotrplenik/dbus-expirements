#!/usr/bin/python

import dbus
bus = dbus.SystemBus()
proxy = bus.get_object('org.freedesktop.NetworkManager',
                       '/org/freedesktop/NetworkManager/Devices/eth0')
# proxy is a dbus.proxies.ProxyObject


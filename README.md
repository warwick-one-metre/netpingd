## Observatory network ping daemon

Part of the observatory software for the Warwick La Palma telescopes.

`netpingd` regularly pings machines on the network and caches the connectivity status.

`netping` is a commandline utility that reports the latest network status

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the observatory software architecture and instructions for developing and deploying the code.

### Software Setup

After installing `observatory-netping-server`, the `netpingd` must be enabled using:
```
sudo systemctl enable netpingd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start netpingd.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9012/tcp --permanent
sudo firewall-cmd --reload
```

### Hardware Setup

The IPs for the ping targets are hardcoded in `netpingd`.

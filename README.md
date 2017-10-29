## Observatory network ping daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/netpingd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/netpingd)

Part of the observatory software for the Warwick one-meter, NITES, and GOTO telescopes.

`netpingd` regularly pings machines on the network and caches the connectivity status.

`netping` is a commandline utility that reports the latest network status

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

After installing `onemetre-roomalert-server`, the `roomalertd` must be enabled using:
```
sudo systemctl enable roomalertd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start roomalertd.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9012/tcp --permanent
sudo firewall-cmd --reload
```

### Hardware Setup

The IPs for the ping targets are hardcoded in `netpingd`.

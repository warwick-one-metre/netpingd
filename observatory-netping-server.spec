Name:      observatory-netping-server
Version:   2.1.0
Release:   0
Url:       https://github.com/warwick-one-metre/netpingd
Summary:   Network ping server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick one-meter telescope.

netpingd is a Pyro frontend for checking the internal and external network health using ping times.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/netpingd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/netpingd.service %{buildroot}%{_unitdir}

%post
%systemd_post netpingd.service

%preun
%systemd_preun netpingd.service

%postun
%systemd_postun_with_restart netpingd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/netpingd
%defattr(-,root,root,-)
%{_unitdir}/netpingd.service

%changelog

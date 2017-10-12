Name:      observatory-netping-server
Version:   2.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/netpingd
Summary:   Network ping server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

netpingd is a Pyro frontend for checking the internal and external network health using ping times.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/netpingd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/netpingd.service %{buildroot}%{_unitdir}

%pre
%if 0%{?suse_version}
%service_add_pre netpingd.service
%endif

%post
%if 0%{?suse_version}
%service_add_post netpingd.service
%endif
%if 0%{?centos_ver}
%systemd_post netpingd.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal netpingd.service
%service_del_preun netpingd.service
%endif
%if 0%{?centos_ver}
%systemd_preun netpingd.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update netpingd.service
%service_del_postun netpingd.service
%endif
%if 0%{?centos_ver}
%systemd_postun_with_restart netpingd.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/netpingd
%defattr(-,root,root,-)
%{_unitdir}/netpingd.service

%changelog

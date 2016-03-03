Name:      onemetre-netping-server
Version:   1.0
Release:   1
Url:       https://github.com/warwick-one-metre/netpingd
Summary:   Network ping server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick one-meter telescope.

netpingd is a Pyro frontend for checking the google and ngtshead ping times.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/netpingd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/netpingd.service %{buildroot}%{_unitdir}

%pre
%service_add_pre netpingd.service

%post
%service_add_post netpingd.service
%fillup_and_insserv -f -y netpingd.service

%preun
%stop_on_removal netpingd.service
%service_del_preun netpingd.service

%postun
%restart_on_update netpingd.service
%service_del_postun netpingd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/netpingd
%defattr(-,root,root,-)
%{_unitdir}/netpingd.service

%changelog

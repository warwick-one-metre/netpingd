Name:      observatory-netping-server
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/netpingd
Summary:   Network ping server for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/netpingd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/netpingd.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/netpingd
%defattr(-,root,root,-)
%{_unitdir}/netpingd.service

%changelog

Name:      observatory-netping-client
Version:   2.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/netpingd
Summary:   Network ping client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-warwick-observatory-common
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

netping is a commandline utility that queries the network ping daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/netping %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/netping %{buildroot}/etc/bash_completion.d/netping

%files
%defattr(0755,root,root,-)
%{_bindir}/netping
/etc/bash_completion.d/netping

%changelog

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
Name: fatrace
Version: 0.13
Release: alt2
Summary: Reports file access events from all running processes
Group: File tools
License: GPLv3+
Url: https://launchpad.net/fatrace
Source0: https://launchpad.net/fatrace/trunk/%version/+download/fatrace-%version.tar.bz2
Source44: import.info

%description
fatrace reports file access events from all running processes.

Its main purpose is to find processes which keep waking up the disk
unnecessarily and thus prevent some power saving.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%prefix

%files
%doc COPYING NEWS
%_sbindir/fatrace
%_sbindir/power-usage-report
%_mandir/man*/*

%changelog
* Wed Dec 04 2019 Lenar Shakirov <snejok@altlinux.org> 0.13-alt2
- First build for ALT (thanks to Autoimports!)
- Spec cleaned, thanks to "cleanup_spec"

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- update by mgaimport

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- new version


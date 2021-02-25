Name: alsa-topology-conf
Version: 1.2.4
Release: alt1

Summary: Advanced Linux Sound Architecture (ALSA) topology data
License: BSD-3-Clause
Group: System/Libraries

Url: http://www.alsa-project.org
Source: %name-%version.tar
BuildArch: noarch

%define alsadata %_datadir/alsa

%description
Advanced Linux Sound Architecture (ALSA) Use Case Manager data
used to sit in libalsa but have been factored out to be maintained
in a standalone repository.

%prep
%setup

%build

%install
mkdir -p %buildroot%alsadata
cp -at %buildroot%alsadata -- topology

%files
%alsadata/*
%doc LICENSE

%changelog
* Wed Oct 21 2020 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

* Wed Jun 10 2020 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3

* Thu Feb 20 2020 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- 1.2.2

* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 1.2.1-alt1
- initial release


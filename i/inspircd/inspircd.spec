%define _inspircd_user _inspircd
%define _inspircd_group _inspircd

Name: inspircd
Version: 2.0.29
Release: alt1

Summary: InspIRCd is a modular Internet Relay Chat (IRC) server 
Group: Networking/IRC
License: GPLv2

Url: http://www.inspircd.org

Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: logrotate
Patch0: alt-main-mk.patch

BuildRequires: gcc-c++

%description
It was created from scratch to be stable, modern and lightweight.
It avoids a number of design flaws and performance issues that plague other 
more established projects, such as UnrealIRCd, while providing the same level
of feature parity.

It provides a tunable number of features through the use of an advanced but 
well documented module system. By keeping core functionality to a minimum we 
hope to increase the stability, security and speed of InspIRCd while also
making it customisable to the needs of many different users.


%prep
%setup
%patch0 -p1

%build
%add_optflags -DHAS_STRLCPY %optflags_shared
export CXXFLAGS='%optflags'

#because inspircd uses handmade configure-script written on perl.
./configure \
	--prefix=%_prefix \
	--binary-dir=%_bindir \
	--module-dir=%_libdir/%name \
	--config-dir=%_sysconfdir/%name \
	--log-dir=%_logdir/%name \
	--data-dir=%_localstatedir/%name
%make_build

%install
%makeinstall_std
install -pD -m0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -pD -m0755 %SOURCE2 %buildroot%_initdir/%name
install -pD -m0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -pD -m0644 %buildroot%_sysconfdir/%name/examples/%name.conf.example \
	%buildroot%_sysconfdir/%name/%name.conf
install -d -m0755 %buildroot%_runtimedir/%name
install -d -m0755 %buildroot%_localstatedir/%name
install -d -m0755 %buildroot%_logdir/%name

%pre
/usr/sbin/groupadd -r %_inspircd_group &>/dev/null ||:
/usr/sbin/useradd  -r -g %_inspircd_group -s /bin/false -c "InspIRCd irc server" \
    -d %_localstatedir/%name %_inspircd_user &>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%dir %_libdir/%name
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/examples
%dir %attr(0775,root,%_inspircd_group) %_var/run/%name
%dir %attr(0770,root,%_inspircd_group) %_localstatedir/%name
%dir %attr(0770,root,%_inspircd_group) %_logdir/%name

%_bindir/%name
%_initdir/%name
%_libdir/%name/*.so
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_logrotatedir/%name
%_sysconfdir/%name/examples/*
%_unitdir/%name.service
%doc README.md

%changelog
* Mon Oct 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.29-alt1
- Updated to upstream version 2.0.29 (Fixes: CVE-2019-20917, CVE-2020-25269).

* Tue Jun 26 2018 Pavel Akopov <pak@altlinux.org> 2.0.26-alt1
- initial build


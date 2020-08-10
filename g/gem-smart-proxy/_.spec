# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname smart-proxy
%define        gemname smart_proxy

Name:          gem-%pkgname
Version:       2.1.0
Release:       alt2
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart-proxy
Vcs:           https://github.com/theforeman/smart-proxy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       settings.yml
Source2:       %pkgname.service
Source3:       %pkgname.conf
Patch:         %version.patch
Patch1:        config.patch
Patch2:        config-path.patch
BuildRequires(pre): rpm-build-ruby

%gem_replace_version json ~> 2.3.1
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
  server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
  booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup
%patch
%patch1 -p1
%patch2 -p1

%build
%ruby_build

%install
%ruby_install
install -dm750 %buildroot%_logdir/%pkgname \
               %buildroot%_sysconfdir/%pkgname/config/settings.d \
               %buildroot/run/%pkgname
install -m644 %SOURCE1 %buildroot%_sysconfdir/%pkgname/config/
install -Dm644 %SOURCE2 %buildroot%_unitdir/%pkgname.service
install -Dm644 %SOURCE3 %buildroot%_tmpfilesdir/%pkgname.conf
install -Dm750 %buildroot%ruby_gemlibdir/Gemfile %buildroot%_localstatedir/%pkgname/Gemfile
#TODO move to setup.rb
cp -p config/settings.d/*.yml %buildroot%_sysconfdir/%pkgname/config/settings.d

%check
%ruby_test

%pre           -n %pkgname
getent group puppet >/dev/null || %_sbindir/groupadd -r puppet
getent group foreman >/dev/null || %_sbindir/groupadd -r foreman
getent passwd _smartforeman >/dev/null || \
   %_sbindir/useradd -r -G puppet,foreman -d %_localstatedir/%pkgname -s /bin/bash -c "Foreman" _smartforeman

%post          -n %pkgname
%post_service %pkgname

%preun         -n %pkgname
%preun_service %pkgname


%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%config(noreplace) %_sysconfdir/%pkgname/config/settings.yml
%config(noreplace) %_sysconfdir/%pkgname/config/settings.d/*.yml

%files         -n %pkgname
%doc README*
%_bindir/%{pkgname}*
%_unitdir/%pkgname.service
%_tmpfilesdir/%pkgname.conf
%attr(750,_smartforeman,foreman) %_logdir/%pkgname
%attr(751,_smartforeman,foreman) %_localstatedir/%pkgname
%attr(751,_smartforeman,foreman) /run/%pkgname

%files         doc
%ruby_gemdocdir


%changelog
* Thu Jul 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- + conf file to keep rights on some folders after reset
- + _smartforeman user with home of /var/lib/smart-proxy
- * moving config files to sysconf folder
- ! config dependent code
- ! config syntax

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.0 -> 2.1.0
- + _foreman user to puppet group

* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt4
- + copy Gemfile to %%_localstatedir/smart-proxy
- + setup foreman user and groups
- - service dep out of the foreman
- ! service work dir

* Thu Jul 09 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt3
- + settings yamls

* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt2
- * dependencies by patch

* Tue Jun 9 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0

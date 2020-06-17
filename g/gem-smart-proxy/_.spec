# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname smart-proxy
%define        gemname smart_proxy

Name:          gem-%pkgname
Version:       2.0.0
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
Patch:         %version.patch
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

%build
%ruby_build
sed 's,#libdir,%ruby_gemlibdir,' -i %SOURCE2

%install
%ruby_install
install -m644 %SOURCE1 %buildroot%ruby_gemlibdir/config/
install -Dm644 %SOURCE2 %buildroot%_unitdir/%pkgname.service
install -dm750 %buildroot%_logdir/%pkgname %buildroot%_runtimedir/%pkgname

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%config(noreplace) %ruby_gemlibdir/config/settings.yml

%files         -n %pkgname
%doc README*
%_bindir/%{pkgname}*
%_unitdir/%pkgname.service
%attr(750,_foreman,foreman) %_logdir/%pkgname
%attr(751,_foreman,foreman) %_runtimedir/%pkgname

%files         doc
%ruby_gemdocdir


%changelog
* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt2
- * dependencies by patch

* Tue Jun 9 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0

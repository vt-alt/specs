%define _unpackaged_files_terminate_build 1

%define realname sd_notify

%def_disable check

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0
Release: alt5
Summary: Erlang interface to systemd notify subsystem
Group: Development/Erlang
License: MIT
Url: https://github.com/systemd/erlang-sd_notify

#VCS: scm:git:https://github.com/systemd/erlang-sd_notify.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: /usr/bin/rebar
BuildRequires: libsystemd-devel

%description
%summary.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Tue Mar 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt5
- Fixed build with rebar2.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3
- NMU: remove %%ubt from release

* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt2
- Disabled tests.

* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Rebuilt to fix linking.

* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build

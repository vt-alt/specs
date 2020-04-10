%define _unpackaged_files_terminate_build 1

%global realname goldrush

Name: erlang-%realname
Version: 0.1.9
Release: alt4
Summary: Small, fast event processing and monitoring for Erlang/OTP applications
License: MIT
Group: Development/Erlang
Url: https://github.com/DeadZen/goldrush

BuildArch: noarch

# https://github.com/DeadZen/goldrush.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: /usr/bin/rebar

%description
A small Erlang app that provides fast event stream processing.

%prep
%setup

%build
%rebar_compile
%rebar_doc

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc doc README.org
%_erllibdir/%realname-%version

%changelog
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.9-alt4
- Fixed build with rebar2.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.9-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.9-alt2
- NMU: remove %%ubt from release

* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.9-alt1
- Updated to upstream version 0.1.9.

* Fri Apr 08 2016 Denis Medvedev <nbr@altlinux.org> 0.1.8-alt1
- Initial Sisyphus release.

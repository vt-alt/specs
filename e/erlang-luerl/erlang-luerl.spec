%define _unpackaged_files_terminate_build 1

%define realname luerl

Name: erlang-%realname
Version: 0.3
Release: alt4
Summary: Lua in Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/rvirding/luerl

BuildArch: noarch

# https://github.com/rvirding/luerl.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%description
An experimental implementation of Lua 5.2 written solely in pure Erlang.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Tue Mar 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt4
- Fixed build with rebar2.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2
- NMU: remove %%ubt from release

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt1
- Initial build for ALT.

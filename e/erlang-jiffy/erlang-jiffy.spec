%define _unpackaged_files_terminate_build 1

%define realname jiffy

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.4
Release: alt1
Summary: JSON NIFs for Erlang
Group: Development/Erlang
License: BSD-3-Clause and MIT
Url: https://github.com/davisp/jiffy

# https://github.com/davisp/jiffy.git
Source: %name-%version.tar

Patch1: erlang-jiffy-fedora-use-system-double-conversion.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: gcc-c++
BuildRequires: libdouble-conversion-devel

%description
A JSON parser as a NIF.
This new version is a hand crafted state machine
that does its best to be as quick and efficient as possible
while not placing any constraints on the parsed JSON.

%prep
%setup
%patch1 -p1
rm -rf c_src/double-conversion

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt1
- Updated to upstream version 1.0.4.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Updated to upstream version 1.0.1.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.14.8-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.14.8-alt2
- NMU: remove %%ubt from release

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.8-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

%global realname stringprep

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.20
Release: alt1
Summary: Fast Stringprep implementation for Erlang / Elixir
Group: Development/Erlang
License: Apache-2.0 and TCL
Url: https://github.com/processone/stringprep

# https://github.com/processone/stringprep.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: gcc-c++

%description
Stringprep is a framework for preparing Unicode test strings
in order to increase the likelihood that string input and string comparison work.

The principle are defined in RFC-3454: Preparation of Internationalized Strings.
This library is leverage Erlang native NIF mechanism to provide extremely fast and efficient processing.
The library includes support for several Stringprep profiles used in XMPP protocole like:
    Nodeprep
    Nameprep
    Resourceprep

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE.*
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.20-alt1
- Updated to upstream version 1.0.20.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.19-alt1
- Updated to upstream version 1.0.19.

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.16-alt1
- Updated to upstream version 1.0.16.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.15-alt1
- Updated to upstream version 1.0.15.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.14-alt1
- Updated to upstream version 1.0.14.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1
- Initial build for ALT.

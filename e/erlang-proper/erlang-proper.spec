%define _unpackaged_files_terminate_build 1

%global realname proper

Name: erlang-%realname
Version: 1.3
Release: alt2
Summary: A QuickCheck-inspired property-based testing tool for Erlang
Group: Development/Erlang
License: GPLv3+
Url: https://github.com/manopapad/proper

BuildArch: noarch

# https://github.com/manopapad/proper.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%description
PropEr (PROPerty-based testing tool for ERlang) is a QuickCheck-inspired
open-source property-based testing tool for Erlang.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
export ERL_LIBS=%buildroot%_erllibdir
%rebar_eunit -C rebar.test.config

%files
%doc COPYING
%doc doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt2
- Fixed build with rebar2.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt1
- Updated to upstream version 1.3.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Initial build for ALT.

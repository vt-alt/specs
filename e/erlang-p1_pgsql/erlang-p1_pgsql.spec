%define _unpackaged_files_terminate_build 1

%define realname p1_pgsql

Name: erlang-%realname
Version: 1.1.10
Release: alt1
Summary: Pure Erlang PostgreSQL driver
Group: Development/Erlang
License: ErlPL-1.1
Url: https://github.com/processone/p1_pgsql

BuildArch: noarch

# https://github.com/processone/p1_pgsql.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

Obsoletes: erlang-pgsql < %EVR
Provides: erlang-pgsql = %EVR

%description
This is an Erlang PostgreSQL driver.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc EPLICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.10-alt1
- Updated to upstream version 1.1.10.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.9-alt1
- Updated to upstream version 1.1.9.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.8-alt1
- Updated to upstream version 1.1.8.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.7-alt1
- Updated to upstream version 1.1.7.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.6-alt1
- Updated to upstream version 1.1.6.

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.5-alt1
- Initial build for ALT.

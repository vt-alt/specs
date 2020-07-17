%define _unpackaged_files_terminate_build 1

%define realname p1_mysql

Name: erlang-%realname
Version: 1.0.15
Release: alt1
Summary: Pure Erlang MySQL driver
Group: Development/Erlang
License: BSD-3-Clause
Url: https://github.com/processone/p1_mysql

BuildArch: noarch

# https://github.com/processone/p1_mysql.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%description
This is an Erlang MySQL driver.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc COPYING
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.15-alt1
- Updated to upstream version 1.0.15.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.14-alt1
- Updated to upstream version 1.0.14.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1
- Updated to upstream version 1.0.11.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.9-alt1
- Updated to upstream version 1.0.9.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.8-alt1
- Updated to upstream version 1.0.8.

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

%global realname lager

Name: erlang-%realname
Version: 3.6.10
Release: alt2
Summary: A logging framework for Erlang/OTP
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/erlang-lager/lager

BuildArch: noarch

# https://github.com/erlang-lager/lager.git
Source: %name-%version.tar

%add_erlang_req_modules_skiplist lager_default_tracer

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: erlang-goldrush
BuildRequires: /usr/bin/rebar

# workaround for bug #36925
Requires: erlang-goldrush

%description
Lager (as in the beer) is a logging framework for Erlang. Its purpose is to
provide a more traditional way to perform logging in an erlang application that
plays nicely with traditional UNIX logging tools like logrotate and syslog.

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
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.10-alt2
- Fixed build with rebar2.

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.10-alt1
- Updated to upstream version 3.6.10.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.7-alt1
- Updated to upstream version 3.6.7.

* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.2-alt1
- Updated to upstream version 3.4.2.

* Mon Oct 23 2017 Denis Medvedev <nbr@altlinux.org> 3.1.0-alt1.1
- Rebuild with fixed rpm-build-erlang.

* Fri Apr 08 2016 Denis Medvedev <nbr@altlinux.org> 3.1.0-alt1
- Initial Sisyphus release

%define _unpackaged_files_terminate_build 1

%global realname p1_oauth2

Name: erlang-%realname
Version: 0.6.8
Release: alt1
Summary: An Oauth2 implementation for Erlang
Group: Development/Erlang
License: MIT
Url: https://github.com/processone/p1_oauth2

BuildArch: noarch

# https://github.com/processone/p1_oauth2.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-proper
BuildRequires: erlang-meck

%description
This library is designed to simplify the implementation of the server side of
OAuth2. It is a fork of erlang-oauth2 by processone, and is needed by ejabberd.

%prep
%setup

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
* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.8-alt1
- Updated to upstream version 0.6.8.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.7-alt1
- Updated to upstream version 0.6.7.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.6-alt1
- Updated to upstream version 0.6.6.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.5-alt1
- Updated to upstream version 0.6.5.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt1
- Updated to upstream version 0.6.4.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.3-alt1
- Updated to upstream version 0.6.3.

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.2-alt1.git5806c87
- Initial build for ALT.

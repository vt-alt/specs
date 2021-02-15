%define _unpackaged_files_terminate_build 1

%global realname p1_acme

Name: erlang-%realname
Version: 1.0.11
Release: alt1
Summary: ACME client library for Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/p1_acme

BuildArch: noarch

# https://github.com/processone/p1_acme.git
Source: %name-%version.tar

%add_erlang_req_modules_skiplist str

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-jiffy
BuildRequires: erlang-yconf
BuildRequires: erlang-idna
BuildRequires: erlang-jose

%description
Erlang ACME client (RFC8555).

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE.txt
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1
- Updated to upstream version 1.0.11.

* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Updated to upstream version 1.0.10.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.8-alt1
- Updated to upstream version 1.0.8.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Initial build for ALT.


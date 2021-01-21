%define _unpackaged_files_terminate_build 1

%define realname stun

Name: erlang-%realname
Version: 1.0.40
Release: alt1
Summary: STUN and TURN library for Erlang / Elixir
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/stun

BuildArch: noarch

# https://github.com/processone/stun.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: erlang-fast_tls

%description
STUN and TURN library for Erlang / Elixir. Both STUN (Session Traversal
Utilities for NAT) and TURN standards are used as techniques to establish media
connection between peers for VoIP (for example using SIP or Jingle) and WebRTC.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc LICENSE.txt
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.40-alt1
- Updated to upstream version 1.0.40.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.37-alt1
- Updated to upstream version 1.0.37.

* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.33-alt1
- Updated to upstream version 1.0.33.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.31-alt1
- Updated to upstream version 1.0.31.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.28-alt1
- Updated to upstream version 1.0.28.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.27-alt1
- Updated to upstream version 1.0.27.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.26-alt1
- Updated to upstream version 1.0.26.

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.21-alt1
- Initial build for ALT.

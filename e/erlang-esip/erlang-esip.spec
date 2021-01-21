%define _unpackaged_files_terminate_build 1

%define realname esip

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.39
Release: alt1
Summary: ProcessOne SIP server component in Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/esip

# https://github.com/processone/esip.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: erlang-stun
BuildRequires: erlang-fast_tls

%description
ProcessOne SIP server component in Erlang.

%prep
%setup

%build
%autoreconf
%configure
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
* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.39-alt1
- Updated to upstream version 1.0.39.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.37-alt1
- Updated to upstream version 1.0.37.

* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.34-alt1
- Updated to upstream version 1.0.34.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.32-alt1
- Updated to upstream version 1.0.32.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.29-alt1
- Updated to upstream version 1.0.29.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.28-alt1
- Updated to upstream version 1.0.28.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.27-alt1
- Updated to upstream version 1.0.27.

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.22-alt1
- Initial build for ALT.

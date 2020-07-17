%define _unpackaged_files_terminate_build 1

%define realname esip

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.34
Release: alt1
Summary: ProcessOne SIP server component in Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/esip

# https://github.com/processone/esip.git
Source: %name-%version.tar

Patch1: erlang-esip-fedora-include_lib.patch

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
%patch1 -p0

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

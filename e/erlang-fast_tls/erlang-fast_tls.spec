%define _unpackaged_files_terminate_build 1

%global realname fast_tls

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.1.6
Release: alt1
Summary: TLS / SSL OpenSSL-based native driver for Erlang / Elixir
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/fast_tls

# https://github.com/processone/fast_tls.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: openssl-devel

%description
Fast TLS is a native TLS / SSL driver for Erlang / Elixir.
It is based on OpenSSL, a proven and efficient TLS implementation.

It is designed for efficiency, speed and compliance.

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
* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.6-alt1
- Updated to upstream version 1.1.6.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.4-alt1
- Updated to upstream version 1.1.4.

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream version 1.1.0.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.26-alt1
- Updated to upstream version 1.0.26.

* Tue Sep 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.21-alt2
- Rebuilt with openssl 1.1.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.21-alt1
- Initial build for ALT.

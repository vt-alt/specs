%define _unpackaged_files_terminate_build 1

%define realname pkix

Name: erlang-%realname
Version: 1.0.7
Release: alt1
Summary: PKIX certificates management for Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/pkix

BuildArch: noarch

# https://github.com/processone/pkix.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%add_findprov_skiplist %_erllibdir/%realname-%version/priv/cacert.pem
%add_findreq_skiplist  %_erllibdir/%realname-%version/priv/cacert.pem

Requires: ca-trust

%description
A library for managing TLS certificates in Erlang.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

# pkix includes a CA bundle in priv/cacert.pem. Let's use a symlink to system CA bundle instead.
install -d -m 0755 %buildroot%_erllibdir/%realname-%version/priv
ln -s $(relative %_sysconfdir/pki/tls/certs/ca-bundle.trust.crt %_erllibdir/%realname-%version/priv/cacert.pem) %buildroot%_erllibdir/%realname-%version/priv/cacert.pem

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt1
- Updated to upstream version 1.0.7.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.6-alt1
- Updated to upstream version 1.0.6.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Updated to upstream version 1.0.5.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Updated to upstream version 1.0.1.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Initial build for ALT.

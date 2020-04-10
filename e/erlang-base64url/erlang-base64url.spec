%define _unpackaged_files_terminate_build 1

%define realname base64url

Name: erlang-%realname
Version: 1.0.1
Release: alt1
Summary: URL safe base64-compatible codec
Group: Development/Erlang
License: MIT
Url: https://github.com/dvv/base64url

BuildArch: noarch

# https://github.com/dvv/base64url.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%description
Standalone URL safe base64-compatible codec.

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
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Updated to upstream version 1.0.1.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2
- NMU: remove %%ubt from release

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

%define realname triq

%add_erlang_req_modules_skiplist triq_rnd

Name: erlang-%realname
Version: 1.3.0
Release: alt1
Summary: A property-based testing library for Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://gitlab.com/triq/triq

BuildArch: noarch

# https://gitlab.com/triq/triq.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%description
A property-based testing library for Erlang.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
export ERL_LIBS=%buildroot%_erllibdir
%rebar_eunit -C rebar.config.script

%files
%doc LICENSE
%doc README.org
%_erllibdir/%realname-%version

%changelog
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt1
- Updated to upstream version 1.3.0.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2
- NMU: remove %%ubt from release

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

%define realname unicode_util_compat

Name: erlang-%realname
Version: 0.4.1
Release: alt1
Summary: unicode_util compatibility library for Erlang < 20
Group: Development/Erlang
License: BSD-3-Clause
Url: https://github.com/benoitc/unicode_util_compat

BuildArch: noarch

# https://github.com/benoitc/unicode_util_compat.git
Source: %name-%version.tar

%add_erlang_req_modules_skiplist str

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%description
Allows the usage of unicode_util and string from Erlang R21 in older erlang >= R18.

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
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt1
- Initial build for ALT.


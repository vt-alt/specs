%define _unpackaged_files_terminate_build 1

%define realname meck

Name: erlang-%realname
Version: 0.8.13
Release: alt2
Summary: A mocking library for Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/eproxus/meck

BuildArch: noarch

# https://github.com/eproxus/meck.git
Source: %name-%version.tar

Patch1: erlang-meck-fedora-workaround-for-Rebar-2.x.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-hamcrest

%description
With meck you can easily mock modules in Erlang. Since meck is intended to be
used in testing, you can also perform some basic validations on the mocked
modules, such as making sure no function is called in a way it should not.

%prep
%setup
%patch1 -p1

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.13-alt2
- Fixed build with rebar2.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.13-alt1
- Updated to upstream version 0.8.13.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.12-alt1
- Updated to upstream version 0.8.12.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.9-alt1
- Initial build for ALT.

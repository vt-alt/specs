%define _unpackaged_files_terminate_build 1

%define realname hamcrest

Name: erlang-%realname
Version: 0.1.0
Release: alt3.git.0766ea0
Summary: A framework for writing matcher objects using declarative rules
Group: Development/Erlang
License: MIT and BSD
Url: https://github.com/hyperthunk/hamcrest-erlang

BuildArch: noarch

# https://github.com/hyperthunk/hamcrest-erlang.git
Source: %name-%version.tar

Patch1: erlang-hamcrest-fedora-remove-the-warnings-cause-by-type-declarations.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-common_test-devel
BuildRequires: erlang-proper

%description
Hamcrest is a framework for writing matcher objects allowing 'match' rules to
be defined declaratively. There are a number of situations where matchers are
invaluable, such as UI validation, or data filtering, but it is in the area of
writing flexible tests that matchers are most commonly used.

%prep
%setup
%patch1 -p1

%build
%rebar_compile

%install
%rebar_install %realname

%check
export ERL_LIBS=%buildroot%_erllibdir
%rebar_eunit -C rebar.test.config

%files
%doc LICENCE
%doc README.markdown
%_erllibdir/%realname-%version

%changelog
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt3.git.0766ea0
- Fixed build with rebar2.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt2.git0766ea0
- Updated to current version.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt1.gita857893
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

%global realname cache_tab

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.27
Release: alt1
Summary: In-memory cache Erlang / Elixir library
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/cache_tab

# https://github.com/processone/cache_tab.git
Source: %name-%version.tar

# Upstream check didn't work for some reason, just revert it
Patch1: %name-alt-erlang-compat.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils

%description
In-memory cache Erlang / Elixir library.

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
%doc LICENSE.txt
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.27-alt1
- Updated to upstream version 1.0.27.

* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.26-alt1
- Updated to upstream version 1.0.26.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.25-alt1
- Updated to upstream version 1.0.25.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.22-alt1
- Updated to upstream version 1.0.22.

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.19-alt1
- Updated to upstream version 1.0.19.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.18-alt1
- Updated to upstream version 1.0.18.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.17-alt1
- Updated to upstream version 1.0.17.

* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.13-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

%global realname ezlib

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.9
Release: alt1
Summary: Native zlib driver for Erlang / Elixir
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/ezlib

# https://github.com/processone/ezlib.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: zlib-devel

%description
Native zlib driver for Erlang / Elixir. This library focuses on compression / decompression of data streams.

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
* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.9-alt1
- Updated to upstream version 1.0.9.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.8-alt1
- Updated to upstream version 1.0.8.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt1
- Updated to upstream version 1.0.7.

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.6-alt1
- Updated to upstream version 1.0.6.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Updated to upstream version 1.0.5.

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt1
- Initial build for ALT.

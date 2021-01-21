%define _unpackaged_files_terminate_build 1

%global realname fast_yaml

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.29
Release: alt1
Summary: Fast YAML native library for Erlang / Elixir
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/fast_yaml

# https://github.com/processone/fast_yaml.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: libyaml-devel

%description
Fast YAML is an Erlang wrapper for libyaml "C" library.

It is designed to be fast and efficient.

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
* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.29-alt1
- Updated to upstream version 1.0.29.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.27-alt1
- Updated to upstream version 1.0.27.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.24-alt1
- Updated to upstream version 1.0.24.

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.19-alt1
- Updated to upstream version 1.0.19.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.18-alt1
- Updated to upstream version 1.0.18.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.17-alt1
- Updated to upstream version 1.0.17.

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.13-alt1
- Initial build for ALT.

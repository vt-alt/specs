%define _unpackaged_files_terminate_build 1

%define realname mqtree

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.12
Release: alt1
Summary: Index tree for MQTT topic filters
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/mqtree

# https://github.com/processone/mqtree.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils

%description
mqtree is an Erlang NIF implementation of N-ary tree to keep MQTT
topic filters for efficient matching.

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
* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.12-alt1
- Updated to upstream version 1.0.12.

* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1
- Updated to upstream version 1.0.11.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Updated to upstream version 1.0.10.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt1
- Updated to upstream version 1.0.7.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.3-alt1
- Updated to upstream version 1.0.3.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Initial build for ALT.

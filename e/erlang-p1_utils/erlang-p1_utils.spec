%define _unpackaged_files_terminate_build 1

%global realname p1_utils

Name: erlang-%realname
Version: 1.0.19
Release: alt1
Summary: Erlang Utility Modules from ProcessOne
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/p1_utils

BuildArch: noarch

# https://github.com/processone/p1_utils.git
Source: %name-%version.tar

%add_erlang_req_modules_skiplist str

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%description
Erlang Utility Modules from ProcessOne.

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
%doc doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.19-alt1
- Updated to upstream version 1.0.19.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.18-alt1
- Updated to upstream version 1.0.18.

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.15-alt1
- Updated to upstream version 1.0.15.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.14-alt1
- Updated to upstream version 1.0.14.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.13-alt1
- Updated to upstream version 1.0.13.

* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

%define realname eimp

%set_verify_elf_method relaxed

# https://github.com/processone/eimp/issues/5
%def_disable check

Name: erlang-%realname
Version: 1.0.19
Release: alt1
Summary: Erlang Image Manipulation Process
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/eimp

# https://github.com/processone/eimp.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: libgd3-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libwebp-devel

%description
eimp is an Erlang/Elixir application for manipulating graphic images
using external C libraries. It supports WebP, JPEG, PNG and GIF.

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
* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.19-alt1
- Updated to upstream version 1.0.19.

* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.18-alt1
- Updated to upstream version 1.0.18.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.17-alt1
- Updated to upstream version 1.0.17.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.14-alt1
- Updated to upstream version 1.0.14.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1
- Updated to upstream version 1.0.11.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Updated to upstream version 1.0.10.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.9-alt1
- Updated to upstream version 1.0.9.

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt1
- Initial build for ALT.

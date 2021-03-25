%define _unpackaged_files_terminate_build 1

Name: kumoworks
Version: 1.0.1
Release: alt2.git.6c50826
Summary: Cloud rendering tool for animation production
Group: Graphics
License: BSD-3-Clause
URL: https://opentoonz.github.io/e/

# https://github.com/opentoonz/kumoworks.git
Source: %name-%version.tar

Patch1: %name-%version-alt-install-path.patch
Patch2: %name-%version-alt-qt-compat.patch

BuildRequires: gcc-c++ cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel

%description
KumoWorks is a cloud rendering tool for animation production.

The software is based on a cloud rendering engine developed by Tomohiro Suzuki.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
pushd sources
%cmake
%cmake_build
popd

%install
pushd sources
%cmakeinstall_std
popd

%files
%doc LICENSE.txt
%doc misc/licenses/LICENSE_ARHOSEK_SKYMODEL.txt
%doc README.md
%_bindir/*

%changelog
* Fri Aug 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2.git.6c50826
- Fixed build with qt-5.15.0.

* Thu Jul 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1.git.6c50826
- Initial build for ALT

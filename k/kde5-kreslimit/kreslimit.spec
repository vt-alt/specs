%define rname kreslimit
Name: kde5-kreslimit
Version: 1.2.2
Release: alt1

%K5init altplace

Group: Graphical desktop/KDE
Summary: Application resource limit configurator
License: GPLv2+

Requires: plasma5-desktop
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: boost-devel extra-cmake-modules gcc-c++
BuildRequires: kf5-ki18n-devel kf5-kcmutils-devel kf5-kio-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kservice-devel

Provides: kreslimit = %EVR
Obsoletes: kreslimit <= %EVR

%description
Resource limit for launched applications

%prep
%setup 

%build
%K5cmake \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DCMAKE_BUILD_TYPE=Debug \

%K5make

%install
%K5install

%find_lang %rname --with-kde --all-name

%files -f %rname.lang
%_K5plug/*.so
%_K5srv/*.desktop


%changelog
* Thu Feb 18 2021 Ivan Razzhivin <underwit@altlinux.org> 1.2.2-alt1
- remove mention from help center
- remove help button

* Wed Sep 09 2020 Ivan Razzhivin <underwit@altlinux.org> 1.2.1-alt1
- the application fills the parent window
- remove multiple items
- set default memory size after adding application

* Fri Aug 07 2020 Ivan Razzhivin <underwit@altlinux.org> 1.2.0-alt1
- select application from list
- add tooltip

* Thu Jun 25 2020 Ivan Razzhivin <underwit@altlinux.org> 1.1.0-alt1
- update translation
- remove unit size column
- remove pidtransit.sh script

* Fri Jun 05 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.3-alt1
- add ability to edit records

* Mon Jun 01 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.2-alt1
- add column for units
- change default values

* Thu Apr 16 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.1-alt1
- change package name
- change units
- set minimum limit size

* Fri Feb 28 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.0-alt1
- init

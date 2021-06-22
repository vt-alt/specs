%define apache2docstartalias alt-docs
%define apache2indexhtmlalias indexhtml
%define apache2documentationalias documentation
%define _indexhtmldir %_defaultdocdir/indexhtml
%define _documentationdir %_defaultdocdir/documentation

Name: alt-docs-apache2
Version: 0.2.2
Release: alt1

Summary: apache2-related config for ALT Linux documentation
License: %gpl3plus
Group: Networking/WWW
URL: http://git.altlinux.org/people/azol/packages/%name.git
Packager: Artem Zolochevskiy <azol@altlinux.org>
Buildarch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-macros-apache2
BuildRequires: cmake
Requires: apache2
Requires: indexhtml

%description
apache2-related config for ALT Linux documentation.

Documentation is accessible by URL:
http://localhost/%apache2docstartalias

%prep
%setup

%build
cmake \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DSYSCONF_DIR=/etc \
  -DAPACHE2_INDEXHTML_ALIAS=%apache2indexhtmlalias \
  -DAPACHE2_INDEXHTML_DIR=%_indexhtmldir \
  -DAPACHE2_DOCUMENTATION_ALIAS=%apache2documentationalias \
  -DAPACHE2_DOCUMENTATION_DIR=%_documentationdir \
  -DAPACHE2_DOCSTART_ALIAS=%apache2docstartalias \

%install
%makeinstall_std

%files
%apache2_extra_available/*
%apache2_extra_start/*
%apache2_mods_start/*

%post
%_sbindir/a2chkconfig > /dev/null
%post_apache2conf

%postun
%_sbindir/a2chkconfig > /dev/null
%post_apache2conf

%changelog
* Tue May 25 2021 Artem Zolochevskiy <azol@altlinux.org> 0.2.2-alt1
- use updated rpm-macros-apache2

* Tue Oct 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- package provides three aliases:
  + alt-docs (default starting point)
  + indexhtml
  + documentation
- add initial CMake build system

* Mon Oct 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- change default documentation dir
  * indexhtml: /usr/share/doc/indexhtml
  * documentation: /usr/share/doc/documentation
- remove %%preun
- add %%postun: a2chkconfig

* Fri Jan 30 2009 Artem Zolochevsky <azol@altlinux.org> 0.1-alt3
- spec modification:
  * add Url:
  * use -p option for install call

* Thu Dec 04 2008 Artem Zolochevsky <azol@altlinux.org> 0.1-alt2
- more descriptive %%description

* Tue Dec 02 2008 Artem Zolochevsky <azol@altlinux.org> 0.1-alt1
- initial build for Sisyphus

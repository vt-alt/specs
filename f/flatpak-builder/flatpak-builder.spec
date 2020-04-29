%define _localstatedir %_var
%define _libexecdir %_prefix/libexec
%define _userunitdir %_prefix/lib/systemd/user

%def_enable docs
%{?_enable_docs:%def_enable docbook_docs}

Name: flatpak-builder
Version: 1.0.10
Release: alt1.1
Epoch:1

Summary: Tool to build flatpaks from source
Group: Development/Other
License: LGPL-2.1
Url: http://flatpak.org/

# VCS: https://github.com/flatpak/flatpak-builder.git
Source: https://github.com/flatpak/flatpak-builder/releases/download/%version/%name-%version.tar.xz

%define glib_ver 2.44
%define ostree_ver 2017.14
%define flatpak_ver 0.99.1

Requires: flatpak >= %flatpak_ver
Requires: libostree >= %ostree_ver
Requires: /usr/bin/bzip2
Requires: /usr/bin/bzr
Requires: /usr/bin/eu-strip
Requires: /usr/bin/git
Requires: /usr/bin/patch
Requires: /usr/bin/rofiles-fuse
Requires: /usr/bin/strip
Requires: /usr/bin/svn
Requires: /bin/tar
Requires: /usr/bin/unzip
Requires: /usr/bin/7z

BuildRequires: flatpak >= %flatpak_ver
BuildRequires: libcap-devel
BuildRequires: libdwarf-devel
BuildRequires: pkgconfig(glib-2.0) >= %glib_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(ostree-1) >= %ostree_ver
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: libcurl-devel
BuildRequires: xsltproc
%{?_enable_docs:BuildRequires: xsltproc docbook-dtds docbook-style-xsl}
%{?_enable_docbook_docs:BuildRequires: xmlto}

%description
Flatpak-builder is a tool for building flatpaks from sources.

See http://flatpak.org/ for more information.

%prep
%setup

%build
%autoreconf
%configure \
    %{?_disable_docs:--disable-documentation --disable-docbook-docs} \
    %{?_enable_docbook_docs:--enable-docbook-docs} \
    --with-dwarf-header=%_includedir/libdwarf
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%{?_enable_docs:%_man1dir/%name.1*
%_man5dir/flatpak-manifest.5*
%{?_enable_docbook_docs:%doc %_docdir/%name}}

%changelog
* Sat Apr 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.10-alt1.1
- improved "docs" knob

* Sat Mar 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.10-alt1
- 1.0.10

* Sun Nov 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.9-alt1
- 1.0.9

* Fri Jun 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.8-alt1
- 1.0.8

* Sat May 11 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.7-alt1
- 1.0.7

* Sun Apr 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.6-alt1
- 1.0.6

* Sun Feb 10 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.5-alt1
- 1.0.5

* Fri Feb 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.4-alt1
- 1.0.4

* Tue Jan 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.3-alt1
- 1.0.3

* Wed Jan 16 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.2-alt1
- 1.0.2

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.1-alt1
- 1.0.1

* Wed Aug 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt1
- 1.0.0

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 1:0.10.10-alt1
- first build for Sisyphus



%define _libexecdir %prefix/libexec
%define sover 2
%define libsignon_glib libsignon-glib%sover

Name: signon-glib
Version: 2.1
Release: alt1

Group: System/Libraries
Summary: Single signon authentication library for GLib applications
Url: https://gitlab.com/accounts-sso/libsignon-glib
License: LGPLv2+

Source: %name-%version.tar
Source10: com.google.code.AccountsSSO.SingleSignOn.AuthService.xml
Source11: com.google.code.AccountsSSO.SingleSignOn.AuthSession.xml
Source12: com.google.code.AccountsSSO.SingleSignOn.Identity.xml


# Automatically added by buildreq on Thu Oct 15 2015 (-bi)
# optimized out: elfutils glib2-devel gnu-config gobject-introspection gtk-doc libgio-devel pkg-config python-base python-devel python-module-google python-modules python-modules-compiler python-modules-encodings python-modules-xml python3 python3-base rpm-build-gir ruby ruby-stdlibs xml-utils
#BuildRequires: dconf glib-networking glibc-devel-static gobject-introspection-devel gtk-doc-mkpdf libGConf rpm-build-python3 rpm-build-ruby rpm-build-vala signon-devel time
#BuildRequires: dconf glib-networking glibc-devel gobject-introspection-devel gtk-doc-mkpdf rpm-build-vala signon-devel
BuildRequires: meson libcheck-devel /usr/bin/vapigen
BuildRequires: rpm-build-python3 python3(gi)
BuildRequires: glibc-devel gobject-introspection-devel gtk-doc-mkpdf rpm-build-vala signon-devel

%description
This project is a library for managing single signon credentilas which can be
used from GLib applications. It is effectively a GLib binding for the D-Bus API
provided by signond. It is part of the accounts-sso project.

%package -n %libsignon_glib
Group: System/Libraries
Summary: %name library
#Requires: %name-common = %version-%release
%description -n %libsignon_glib
%summary.

%package -n python3-module-signon-overrides
Summary: Python bindings for %name
Group: Development/Python
%description -n python3-module-signon-overrides
Python bindings for %name

%package devel
Group: Development/Other
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

for x in %SOURCE10 %SOURCE11 %SOURCE12 ; do
    install -m 0644 $x libsignon-glib/interfaces/
done


%build
%meson
%meson_build

%install
%meson_install

%files -n %libsignon_glib
%doc README* NEWS
%_libdir/libsignon-glib.so.%sover
%_libdir/libsignon-glib.so.*

%files -n python3-module-signon-overrides
%python3_sitelibdir/gi/overrides/Signon.py*
%python3_sitelibdir/gi/overrides/__pycache__/Signon.*

%files devel
%_includedir/libsignon-glib/
%_libdir/lib*.so
%_pkgconfigdir/libsignon-glib.pc
%_datadir/vala/vapi/libsignon-glib.deps
%_datadir/vala/vapi/libsignon-glib.vapi
%_typelibdir/Signon-2.0.typelib
%_girdir/Signon-2.0.gir

%changelog
* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 2.1-alt1
- new version

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.14-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.14-alt2
- NMU: remove ubt from release

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 1.14-alt1
- new version

* Fri Jan 22 2016 Sergey V Turchin <zerg@altlinux.org> 1.13-alt1
- new version

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 1.12-alt2
- redefine libexecdir

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 1.12-alt1
- initial build

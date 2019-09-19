# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtkdocize intltool
# END SourceDeps(oneline)
BuildRequires: /usr/bin/db2html
%define _libexecdir %_prefix/libexec
%define oldname caja-actions
%define fedora 25
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	Caja extension for customizing the context menu
Name:		mate-file-manager-actions
Version:	1.8.3
Release:	alt3_2
Group:		Graphical desktop/MATE
License:	GPLv2+ and LGPLv2+

URL:		https://github.com/raveit65/%{oldname}
Source0:	https://github.com/raveit65/%{oldname}/releases/download/v%{version}/%{oldname}-%{version}.tar.xz

# only for rhel
Patch1:     caja-actions_0001-Revert-No-version-in-documentation-install-path.patch
Patch2: 1002_cross.patch
Patch10: caja-actions-1.8.3-alt-fix-doc-build-gtk-doc-1.27.patch

BuildRequires:	mate-file-manager-devel
BuildRequires:	libuuid-devel
BuildRequires:	libSM-devel
BuildRequires:	mate-common
BuildRequires:	libxml2-devel
BuildRequires:	yelp-tools
BuildRequires:	libgtop-devel libgtop-gir-devel
BuildRequires:	dblatex

Requires:       mate-file-manager-actions-doc = %{version}-%{release}
Source44: import.info


%description
Caja actions is an extension for Caja, the MATE file manager.
It provides an easy way to configure programs to be launch on files 
selected in Caja interface

%package doc
Summary:	Documentations for %{oldname}
Group:		Documentation
BuildArch:  noarch

%description doc
This package contains the documentation for %{oldname}

%package	devel
Summary:	Development tools for the caja-actions
Group:		Development/Other
BuildArch:  noarch
Requires:	%{name} = %{version}-%{release}

%description	devel
This package contains headers and shared libraries needed for development
with caja-actions.

%prep
%setup -n %{oldname}-%{version} -q

# move doc dir for rhel
%if 0%{?rhel}
%patch1 -p1 -b .0001
NOCONFIGURE=1 ./autogen.sh
%endif
%patch2 -p1
%patch10 -p1

%build
%autoreconf
%configure \
    --enable-gtk-doc \
    --enable-html-manuals \
    --enable-pdf-manuals \
    --enable-deprecate

%make_build 

%install
%{makeinstall_std}

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

# clean docs dirs
%if 0%{?rhel}
rm -f $RPM_BUILD_ROOT%{_docdir}/%{%{oldname}-%{version}}/INSTALL
rm -f $RPM_BUILD_ROOT%{_docdir}/%{%{oldname}-%{version}}/ChangeLog-2008
rm -f $RPM_BUILD_ROOT%{_docdir}/%{%{oldname}-%{version}}/ChangeLog-2009
rm -f $RPM_BUILD_ROOT%{_docdir}/%{%{oldname}-%{version}}/ChangeLog-2010
rm -f $RPM_BUILD_ROOT%{_docdir}/%{%{oldname}-%{version}}/ChangeLog-2011
rm -f $RPM_BUILD_ROOT%{_docdir}/%{%{oldname}-%{version}}/ChangeLog-2012
rm -f $RPM_BUILD_ROOT%{_docdir}/%{%{oldname}-%{version}}/MAINTAINERS
%else
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}/INSTALL
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}/ChangeLog-2008
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}/ChangeLog-2009
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}/ChangeLog-2010
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}/ChangeLog-2011
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}/ChangeLog-2012
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}/MAINTAINERS
%endif

%find_lang %{oldname} --with-gnome --all-name


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/cact.desktop


%files
%doc AUTHORS COPYING COPYING-DOCS ChangeLog NEWS README
%exclude %{_docdir}/caja-actions/AUTHORS
%exclude %{_docdir}/caja-actions/COPYING
%exclude %{_docdir}/caja-actions/COPYING-DOCS
%exclude %{_docdir}/caja-actions/ChangeLog
%exclude %{_docdir}/caja-actions/NEWS
%exclude %{_docdir}/caja-actions/README
%{_bindir}/caja-actions-run
%{_bindir}/caja-actions-config-tool
%{_bindir}/caja-actions-new
%{_bindir}/caja-actions-print
%{_libexecdir}/caja-actions/
%{_libdir}/caja-actions/
%dir %{_libdir}/caja
%dir %{_libdir}/caja/extensions-2.0
%{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so
%{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so
%{_datadir}/caja-actions/
%dir %{_datadir}/icons/hicolor/22x22
%dir %{_datadir}/icons/hicolor/22x22/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/*/apps/caja-actions.*
%{_datadir}/applications/cact.desktop

%files doc -f %{oldname}.lang
%if 0%{?fedora} > 19 || 0%{?rhel} > 7
%dir %{_docdir}/caja-actions
%{_docdir}/caja-actions/html/
%{_docdir}/caja-actions/pdf/
%{_docdir}/caja-actions/objects-hierarchy.odg
%else
%dir %{_docdir}/caja-actions-%{version}
%{_docdir}/caja-actions-%{version}/html/
%{_docdir}/caja-actions-%{version}/pdf/
%{_docdir}/caja-actions-%{version}/objects-hierarchy.odg
%endif
%dir %{_datadir}/help
%dir %{_datadir}/help/C
%dir %{_datadir}/help/de
%dir %{_datadir}/help/el
%dir %{_datadir}/help/es
%dir %{_datadir}/help/fr
%dir %{_datadir}/help/sl

%files devel
%{_includedir}/caja-actions/
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/caja-actions-3/


%changelog
* Tue Sep 17 2019 Leontiy Volodin <lvol@altlinux.org> 1.8.3-alt3_2
- Backport to ALTLinux p9 (ALT #37221).

* Tue Sep 17 2019 Leontiy Volodin <lvol@altlinux.org> 1.8.3-alt3_3
- Fixed cross build.
- Excluded docs in caja-actions.
- Fixed post-install files.

* Sun Mar 11 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.8.3-alt2_3
- Added BR: intltool.
- Fixed build with gtk-doc 1.27.

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.3-alt1_3
- new fc release

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_3
- update to 1.16

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1
- new version

* Wed Oct 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_2
- new version

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2_1
- rebuild with libgtop

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_1
- new fc release

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_1
- new fc release

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_0
- new fc release

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0101
dropped obsolete mate-conf BR:

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0101
- initial import


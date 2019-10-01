%define _unpackaged_files_terminate_build 1

Name: homebank
Version: 5.2.8
Release: alt1

# Note: _unstable suffix sometimes appears in some versions of the tarball.
%define _version %{version}
#_unstable

Summary: Free easy personal accounting for all!
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://%name.free.fr/index.php

Source: http://%name.free.fr/public/%name-%_version.tar.gz

BuildRequires(pre): rpm-build-licenses

# From configure.ac
BuildPreReq: intltool
BuildPreReq: glib2-devel >= 2.40
BuildPreReq: libgtk+3-devel >= 3.12
BuildPreReq: libsoup-devel >= 2.26
BuildPreReq: libofx-devel

BuildPreReq: perl-XML-Parser shared-mime-info desktop-file-utils libappstream-glib-devel

%description
HomeBank is the free software you have always wanted to manage your
personal accounts at home. The main concept is to be light, simple and
very easy to use.

It brings you many features that allow you to analyze your finances in
a detailed way instantly and dynamically with powerful report tools
based on filtering and graphical charts.

Furthermore HomeBank benefits now for more than 10 years of users
experience and feedback as its development started in 1995 on Amiga
computers. It is now available on Amiga, GNU/Linux, and will probably be
soon available for Microsoft Windows and MacOS X systems, as GTK+ exists
on it.

%package help
Summary: Help files for HomeBank
Group: Graphical desktop/GNOME
Requires: homebank = %version-%release
BuildArch: noarch

%description help
HomeBank is the free software you have always wanted to manage your
personal accounts at home. The main concept is to be light, simple and
very easy to use.

It brings you many features that allow you to analyze your finances in
a detailed way instantly and dynamically with powerful report tools
based on filtering and graphical charts.

This package contains help files for HomeBank. The manual is easy to
read and rather useful for a first time user.

%prep
%setup -n %name-%_version

%build
%configure \
    --with-ofx

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%dir %_datadir/%name
%dir %_datadir/%name/images
%_datadir/%name/images/*
%_datadir/%name/icons/
%_datadir/%name/datas/
%_datadir/mime-info/%name.keys
%_datadir/mime-info/%name.mime
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/appdata/%name.appdata.xml
%doc README ChangeLog

%files help
%dir %_datadir/%name/help
%_datadir/%name/help/*

%exclude %_datadir/application-registry/%name.applications

%changelog
* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.8-alt1
- 5.2.8

* Fri Aug 02 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.7-alt1
- 5.2.7

* Mon May 27 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.6-alt1
- 5.2.6

* Tue May 14 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.5-alt1
- 5.2.5

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt1
- 5.2.4

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.3-alt1
- 5.2.3

* Mon Oct 08 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.2-alt1
- 5.2.2

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.1-alt1
- 5.2.1

* Fri Sep 14 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2-alt1
- 5.2

* Mon Mar 19 2018 Yuri N. Sedunov <aris@altlinux.org> 5.1.8-alt1
- 5.1.8

* Sun Jan 07 2018 Yuri N. Sedunov <aris@altlinux.org> 5.1.7-alt1
- 5.1.7

* Fri Sep 15 2017 Yuri N. Sedunov <aris@altlinux.org> 5.1.6-alt1
- 5.1.6

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 5.1.5-alt1
- 5.1.5

* Sun Feb 19 2017 Yuri N. Sedunov <aris@altlinux.org> 5.1.4-alt1
- 5.1.4

* Tue Jan 24 2017 Yuri N. Sedunov <aris@altlinux.org> 5.1.3-alt1
- 5.1.3

* Thu Dec 08 2016 Yuri N. Sedunov <aris@altlinux.org> 5.1.2-alt1
- 5.1.2

* Sun Nov 06 2016 Yuri N. Sedunov <aris@altlinux.org> 5.1.1-alt1
- 5.1.1

* Mon Oct 17 2016 Yuri N. Sedunov <aris@altlinux.org> 5.1-alt1
- 5.1

* Mon Jul 25 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0.9-alt1
- 5.0.9

* Mon May 30 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0.8-alt1
- 5.0.8

* Thu May 12 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0.7-alt1
- 5.0.7

* Mon Nov 02 2015 Yuri N. Sedunov <aris@altlinux.org> 5.0.6-alt1
- 5.0.6

* Thu Sep 24 2015 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt1
- 5.0.5

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 5.0.4-alt1
- 5.0.4

* Thu Jun 11 2015 Yuri N. Sedunov <aris@altlinux.org> 5.0.3-alt1
- 5.0.3

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 5.0.2-alt1
- 5.0.2

* Tue Apr 07 2015 Yuri N. Sedunov <aris@altlinux.org> 5.0.1-alt1
- 5.0.1

* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 5.0.0-alt1
- 5.0.0

* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 4.6.3-alt1
- 4.6.3

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 4.6.1-alt1
- 4.6.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 4.5.6-alt1
- 4.5.6

* Thu Jan 30 2014 Yuri N. Sedunov <aris@altlinux.org> 4.5.5-alt1
- 4.5.5

* Sat Nov 23 2013 Yuri N. Sedunov <aris@altlinux.org> 4.5.4-alt1
- 4.5.4

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 4.4-alt1
- 4.4
- spec cleanup

* Sat Aug 22 2009 Alexey Rusakov <ktirf@altlinux.org> 4.0.4-alt1
- New version.
- Moved help files to a separate noarch subpackage (addressing a notice
  from repocop).

* Sat Apr 04 2009 Alexey Rusakov <ktirf@altlinux.org> 4.0.2-alt1
- Repocop-reported fixes:
  + removed deprecated post/postun macros;
  + added Packager tag.
- Specfile cleaned up, buildreqs updated.

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for homebank

* Sat Oct 13 2007 Alexey Rusakov <ktirf@altlinux.org> 3.5-alt1
- new version (3.5)
- updated files list

* Sun Jul 01 2007 Alexey Rusakov <ktirf@altlinux.org> 3.4-alt1
- new version (3.4)

* Wed Jun 13 2007 Alexey Rusakov <ktirf@altlinux.org> 3.3-alt1
- Initial Sisyphus version


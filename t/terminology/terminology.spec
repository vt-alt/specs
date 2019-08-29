%def_disable snapshot
%define ver_major 1.5

%def_enable check

Name: terminology
Version: %ver_major.0
Release: alt1

Summary: EFL terminal emulator
License: BSD
Group: Terminals
Url: http://www.enlightenment.org/p.php?p=about/terminology

%if_disabled snapshot
Source: https://download.enlightenment.org/rel/apps/%name/%name-%version.tar.xz
#Source: https://fau.re/terminology/%name-%version.tar.xz
%else
#VCS: https://git.enlightenment.org/apps/terminology.git
Source: %name-%version.tar
%endif
Patch: %name-1.0.0-alt-default_font.patch

Requires: fonts-bitmap-terminus
Provides: xvt

BuildRequires(pre): meson
Conflicts: libelementary < 1.20.0
BuildRequires: efl-libs-devel
BuildRequires: libelementary-devel >= 1.20.0

%description
An EFL terminal emulator with some extra bells and whistles. It's brand
new and was only started near the begining of June 2012, so expecting it
to do everything a mature terminal emulator does is a bit premature, but
considering it's young age, it does a lot.

%prep
%setup
%patch -b .def_font

%build
%meson %{?_enable_check:-Dtests=true}
%meson_build

%install
%meson_install

# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt	%_bindir/%name	30
EOF

%find_lang %name

%check
%meson_test

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/%name/
%_altdir/%name
%_iconsdir/hicolor/*/*/%name.png
%_man1dir/*
%doc AUTHORS ChangeLog COPYING README.md

%changelog
* Sun Jul 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sun Mar 31 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Sat Nov 24 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Tue May 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Apr 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Sep 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Fri Aug 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Jan 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Dec 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt2
- updated to v0.9.1-51-gf731ff6

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.99-alt0.1
- 0.8.99_27179b65

* Mon Feb 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.99-alt1
- 0.6.99_a61c3499

* Thu Sep 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt2
- rebuilt with efl/elementary-1.11.2

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Thu Jul 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Mar 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Sun Dec 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0 for E18

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Wed Jan 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.2
- used Terminus 18 as default font

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.1
- first preview build for Sisyphus


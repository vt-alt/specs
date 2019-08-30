%def_enable snapshot
%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: ufraw
Version: 0.23
Release: alt0.2

Summary: UFRaw is a graphical utility for opening and converting RAW files from digital photo cameras
License: GPLv2+
Group: Graphics
Url: http://ufraw.sourceforge.net/

%if_disabled snapshot
Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
%else
# none-official repo
# VCS: https://github.com/sergiomb2/ufraw.git
Source: %name-%version.tar
%endif

Requires(pre): GConf

%ifnarch %e2k
# lcc-1.23.12: ftbfs on ufraw_developer.c:862
BuildRequires: libgomp-devel
%endif
BuildRequires: gcc-c++
BuildRequires: liblensfun-devel >= 0.2.5
BuildRequires: libexiv2-devel >= 0.20
BuildRequires: liblcms2-devel libgimp-devel libgtkimageview-devel
BuildRequires: libjpeg-devel liblensfun-devel libpng-devel libtiff-devel
BuildRequires: libcfitsio-devel zlib-devel bzlib-devel perl-podlators
BuildRequires: libjasper-devel
BuildRequires: libGConf-devel

%package -n gimp-plugin-ufraw
Summary: GIMP plugin for opening and converting RAW files from digital photo cameras (part of UFRaw project)
Group: Graphics
Conflicts: rawphoto
Requires: gimp
Obsoletes: gimp2-plugin-ufraw

%description
UFRaw is a graphical utility for opening and converting RAW files from digital
photo cameras.

%description -n gimp-plugin-ufraw
GIMP plugin for opening and converting RAW files from digital photo cameras
(part of UFRaw project).

%prep
%setup

%build
%autoreconf
%configure \
	--enable-contrast \
%ifnarch %e2k
	--enable-openmp \
%endif
	--enable-mime \
	--enable-extras
%make_build schemasdir=%_sysconfdir/gconf/schemas

%install
%makeinstall_std schemasdir=%_sysconfdir/gconf/schemas
install -d %buildroot%_datadir/ufraw
install -pD -m644 icons/ufraw.png %buildroot%_liconsdir/ufraw.png

%find_lang ufraw

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f ufraw.lang
%_bindir/*
%exclude  %_bindir/dcraw
%_datadir/%name/
%_man1dir/*
%_desktopdir/*
%_liconsdir/*
%_pixmapsdir/*
%_sysconfdir/gconf/schemas/%name.schemas
%_datadir/appdata/%name.appdata.xml
%doc MANIFEST README

%files -n gimp-plugin-ufraw
%gimpplugindir/plug-ins/*

%changelog
* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt0.2
- updated to ufraw-0-22-74-gc65b423

* Thu Apr 18 2019 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt0.1
- updated to 0-22-71-gac8c746 from new none-official git repo

* Fri Feb 01 2019 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt5
- mike@: E2K: avoid openmp for now (ftbfs)

* Wed Jun 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt4
- rebuilt against libjasper.so.4

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt3
- applied fc patchset
- rebuilt against libexiv2.so.26

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt2
- rebuilt against libcfitsio.so.4

* Fri Feb 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt3
- rebuilt against liblensfun.so.1

* Mon Jun 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt2
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.21-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed May 27 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt1
- 0.21 (usibg gcc4.9)

* Tue Oct 28 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20-alt1
- 0.20
- removed obsolete patches

* Fri Apr 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.19.2-alt2.1
- exclude dcraw extras executable

* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.19.2-alt2
- applied some patches from ufraw bugtracker
- built against liblcms2 (ALT #29942)

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0.19.2-alt1
- 0.19.2
- built against libexiv2.so.13

* Fri Jan 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt4
- rebuilt against libexiv2.so.12
- removed obsolete options for configure
- updated buildreqs (FITS support enabled)

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt3.1
- Rebuilt with libpng15

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt3
- rebuilt against libexiv2.so.11

* Thu Mar 24 2011 Victor Forsiuk <force@altlinux.org> 0.18-alt2
- Fix BuildRequires.
- Fix crash when loading dark frame (patch from Fedora).

* Mon Feb 21 2011 Victor Forsiuk <force@altlinux.org> 0.18-alt1
- 0.18

* Mon Aug 16 2010 Victor Forsiuk <force@altlinux.org> 0.17-alt1
- 0.17

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 0.16-alt3
- Rebuild with libexiv2.so.9.

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 0.16-alt2
- Rebuild with libexiv2.so.6.

* Tue Oct 20 2009 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- 0.16

* Tue Jul 21 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt3
- Rebuild with libexiv2.so.5.

* Tue Jun 09 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt2
- Fix gcc4.4 build.

* Fri Feb 20 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- 0.15
- Build with OpenMP support.

* Mon Oct 20 2008 Victor Forsyuk <force@altlinux.org> 0.14.1-alt1
- 0.14.1

* Thu Oct 16 2008 Victor Forsyuk <force@altlinux.org> 0.14-alt1
- 0.14
- Build with lensfun support.

* Fri Jun 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.13-alt2.1
- Automated rebuild due to libexiv2.so.2 -> libexiv2.so.4 soname change.

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 0.13-alt2
- Rebuild with new libexiv2.

* Tue Nov 13 2007 Victor Forsyuk <force@altlinux.org> 0.13-alt1
- 0.13

* Tue Sep 04 2007 Victor Forsyuk <force@altlinux.org> 0.12.1-alt1
- 0.12.1

* Tue Jul 31 2007 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- 0.12

* Tue Apr 10 2007 Victor Forsyuk <force@altlinux.org> 0.11-alt1
- 0.11

* Thu Nov 23 2006 Victor Forsyuk <force@altlinux.org> 0.10-alt1
- 0.10
- Build with EXIF read support (using exiv2 library).
- Use SMP build.

* Mon Mar 06 2006 Dmitry Marochko <mothlike@altlinux.ru> 0.7-alt1
- New version
  + Much more accurate white balance temperature setting.
  + White balance presets per camera model.
  + Show the channel multipliers in the UI.
  + Apply base curve before gamma curve.
  + Fix a few general bugs.
  + Fix camera specific bugs for Sony F828, Sigma Foveon, Nikon D2H, D1X.
- Patch removed due incompatibility

* Fri Nov 25 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.6-alt1
- New version
  + Enabled AHD (Adaptive Homogeneity-Directed) interpolation.
  + Added base curve, which simulates Nikon tone curve behavior. (The old correction curve is still there.)
  + Automatically apply the embedded custom curve only if the camera was setup to use this curve.
  + Support the D1X rectangular pixels.
  + Fix EXIF support with libtiff 3.7.4.
  + Some bug fixes.
- Patch from Sergei Epiphanov kept back

* Sun Oct 02 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt2
- Patch removed
- Version 0.5
- Read support for Nikon Tone Curve (NTC/NCV) files.
- Added a curve editor.
- Added control on the base curve (see the user guide for more information).
- Support the new DCRaw color matrices for better color rendering.
- More controls can be set from the command-line.
- Preliminary EXIF support.
- New UFRaw ID files contain all the conversion parameters and allow for batch conversion.
- New ufraw-batch replaces ufraw --batch.
- Numerous other changes.
- Notice that the new Adaptive Homogeneity-Directed interpolation is still not enabled.

* Sun Sep 11 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt1.20050906cvs
- New CVS version
- ufraw(1) manual added
- Increased stability
- Build with new dcraw version included
- Enhance curves

* Mon Aug 08 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt1.20050808cvs
- CVS version 0.5
- Major changes from Sergei Epiphanov:
  + Package splitted to binary and GIMP plugin parts
  + Patch to enhance functionality

* Wed Aug 03 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.4-alt1
- Initial Sisyphus build
- Version 0.4

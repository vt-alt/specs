Name: autodownloader
Version: 0.5.0
Release: alt1
Summary: GUI-tool to automate the download of certain files
License: GPLv2+
Group: Networking/File transfer
Url: https://github.com/frenzymadness/AutoDownloader
Source0: %name-%version.tar.gz
BuildArch: noarch

BuildRequires: rpm-build-python3

%description
Some software (usually games) requires certain data files to operate, sometimes
these datafiles can be freely downloaded but may not be redistributed and thus
cannot be put into so called packages as part of a distro.

autodownloader is a tool which can be used as part of a package to automate the
download of the needed files. It will prompt the user explaining to him the
need of the download and asking if it is ok to make an internet connection,
after this it will show the license of the to be downloaded files and last it
will do the actual download and md5 verification off these files. This whole
process can be configured by the packager through a simple configuration file.

Notice that Autodownloader while open source itself, may download files which
are not permitted to be (re)distributed unlike most files in Fedora.

%prep
%setup -q
sed -i 's/env python$/env python3/' AutoDL.py

%build
# nothing to build pure python code only

%install
make install DESTDIR=%buildroot

%files
%doc README* examples
%_bindir/autodl
%_datadir/autodl
%_datadir/icons/hicolor/*/apps/autodl.png

%changelog
* Fri May 07 2021 Fr. Br. George <george@altlinux.ru> 0.5.0-alt1
- Build slightly updeted version from GH fork (python3 now)

* Sat May 30 2020 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.qa1.1.2
- FTBFS: set correct python2 executable in shebang.

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1.qa1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for autodownloader
  * postclean-05-filetriggers for spec file

* Sun Jul 20 2008 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Initial build from FC

* Sun Jun  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.0-1
- New upstream release (all patches merged)
- Includes new icons by Michael Beckwith

* Thu Dec 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-6
- Add 2 more patches from Ivo Manca:
  * Make ask to start configurable
  * Some trailing whitespace cleanups

* Thu Nov 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-5
- Apply patch from Ivo Manca fixing the downloading of files with an
  unknown size, thanks!

* Thu Oct  4 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-4
- Check if files exist (and have the correct md5sum) from a previous download
  and skip downloading them (bz 309381)

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-3
- Update License tag for new Licensing Guidelines compliance

* Wed May 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-2
- Make the timeout for stalled mirror detection larger, this fixes the use of
  autodownloader for those with slow links

* Sun Apr 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-1
- Initial Fedora Extras package

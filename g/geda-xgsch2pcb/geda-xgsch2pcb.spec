Name: geda-xgsch2pcb
Version: 0.1.3
Release: alt2

Summary: xgsch2pcb
License: GPL
Group: Development/Other
Url: http://git.geda-project.org/xgsch2pcb

Packager: barssc <barssc@altlinux.ru>

Source0: %name-%version.tar.gz
Patch0: Makefile.am.patch

BuildArch: noarch

# Automatically added by buildreq on Wed May 22 2019
# optimized out: fontconfig libX11-locales libgdk-pixbuf libgpg-error perl perl-Encode perl-XML-Parser perl-parent python-base python-module-pycairo python-module-pygobject python-modules python-modules-compiler python-modules-distutils python-modules-encodings python-modules-logging python-modules-xml sh4
BuildRequires: desktop-file-utils intltool python-module-dbus python-module-pygtk

%description
Graphic wrapper for gsch2pcb. This is a easy way to forward notation and
syncronization from schematic to pcb.

%description -l ru_RU.UTF-8
Графический враппер для программы gsch2pcb. Облегчает поцесс
синхронизации принципиальной схемы с разводкой печатной платы.

%prep
%setup -q
%patch0 -p1
for f in `grep -rl @pkglibdir@ .`; do sed -i s,@pkglibdir@,%python_sitelibdir_noarch/xgsch2pcb,g $f; done

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot%python_sitelibdir_noarch/xgsch2pcb
mv %buildroot%python_sitelibdir_noarch/*.py %buildroot%python_sitelibdir_noarch/xgsch2pcb/

%files -n %name
%_bindir/*
%python_sitelibdir/xgsch2pcb
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/48x48/apps/geda-xgsch2pcb.png
%_datadir/icons/hicolor/scalable/apps/geda-xgsch2pcb.svg
%_datadir/locale/ru/*

%changelog
* Wed May 22 2019 Fr. Br. George <george@altlinux.ru> 0.1.3-alt2
- Move invalid-placed python module files

* Mon Dec 7 2015 barssc <barssc@altlinux.ru> 0.1.3-alt1
- New version 0.1.3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt1.3.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.3
- Rebuilt with python 2.6

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for geda-xgsch2pcb
 * update_menus for geda-xgsch2pcb

* Wed Feb 20 2008 Alexander Gvozdev <gab@altlinux.ru> 0.1.2-alt1.2
- Remove unneeded file "mimeinfo.cache"

* Sat Jan 12 2008 Alexander Gvozdev <gab@altlinux.ru> 0.1.2-alt1
- New version in upstream

* Sat Jan 5 2008 Alexander Gvozdev <gab@altlinux.ru> 0.1.1-alt1
- Initial build


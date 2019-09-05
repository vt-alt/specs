# prontserve is not yet ready for production
%def_without prontserve

Name:           printrun
Version:        1.6.0
Release:        alt2
Epoch:          1
Summary:        RepRap printer interface and tools

License:        GPLv3+
Group:          Engineering
URL:            https://github.com/kliment/Printrun
Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        %name-%version.tar

BuildRequires:  rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-Cython
BuildRequires:  python-module-Polygon
BuildRequires:  python-module-serial
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       pronterface = %EVR
Requires:       pronsole = %EVR
Requires:       plater = %EVR

%description
Printrun is a set of G-code sending applications for RepRap.
It consists of printcore (dumb G-code sender), pronsole (featured command line
G-code sender), pronterface (featured G-code sender with graphical user
interface), and a small collection of helpful scripts. Together with skeinforge
they form a pretty powerful softwarecombo. This package installs whole Printrun.

%package        common
Group:          Engineering
Summary:        Common files for Printrun

%description    common
Printrun is a set of G-code sending applications for RepRap.
This package contains common files.

%package     -n pronsole
Summary:        CLI interface for RepRap
Group:          Engineering
Requires:       python-module-serial
Requires:       skeinforge
Requires:       %name-common = %EVR
BuildArch:      noarch

%description -n pronsole
Pronsole is a featured command line G-code sender.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

%if_with prontserve
%package     -n prontserve
Summary:        Web interface for RepRap
Group:          Engineering
Requires:       python-module-tornado
Requires:       pronsole = %EVR
BuildArch:      noarch

%description -n prontserve
Pronserve is a featured web G-code sender.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.
%endif

%package     -n pronterface
Summary:        GUI interface for RepRap
Group:          Engineering
Requires:       wxPython
Requires:       python-module-cairosvg
Requires:       python-module-pyglet
Requires:       simarrange
Requires:       pronsole = %EVR
BuildArch:      noarch

%description -n pronterface
Pronterface is a featured G-code sender with graphical user interface.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

%package     -n plater
Summary:        RepRap STL plater
Group:          Engineering
Requires:       wxPython
Requires:       %name-common = %EVR
Requires:       python-module-pyglet
Requires:       simarrange
BuildArch:      noarch

%description -n plater
Plater is a GUI tool to prepare printing plate from STL files for ReRap.
It is a part of Printrun.


%prep
%setup -q
# Remove unsupported module
rm -f printrun/power/osx.py

# use launchers for skeinforge
sed -i 's|python skeinforge/skeinforge_application/skeinforge.py|skeinforge|' %name/pronsole.py
sed -i 's|python skeinforge/skeinforge_application/skeinforge_utilities/skeinforge_craft.py|skeinforge-craft|' %name/pronsole.py

%build
%python_build

# rebuild locales
cd locale
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/plater.po -o $FILE/LC_MESSAGES/plater.mo || :
     msgfmt $FILE/LC_MESSAGES/pronterface.po -o $FILE/LC_MESSAGES/pronterface.mo || :
done
cd ..

%install
%python_install

# Remove .py extension from executable files
cd %buildroot%_bindir
for FILE in *.py; do
  mv -f "$FILE" "${FILE%.py}"
done
cd -

# Remove .py extension in desktop files (ALT #36763)
cd %buildroot%_desktopdir
for file in $(ls) ; do sed -i "s/\(.*\).py/\1/" $file; done
cd -

# locales
mkdir -p %buildroot%_datadir/locale
cp -ar %buildroot%_datadir/pronterface/locale/* %buildroot%_datadir/locale
rm -rf %buildroot%_datadir/pronterface/locale
ln -s -f %_datadir/locale/ %buildroot%_datadir/pronterface/ # the app expects the locale folder in here

%if_without prontserve
rm -f %buildroot%_bindir/prontserve
rm -f %buildroot%python_sitelibdir/%name/prontserve.py
%endif

mv %buildroot%_datadir/{metainfo,appdata}

%find_lang pronterface
%find_lang plater

%files
%doc README* COPYING

%files common
%doc README* COPYING
%python_sitelibdir/%name
%python_sitelibdir/Printrun-*.egg-info
%_bindir/printcore*
%_pixmapsdir/plater.png

%files -n pronsole
%doc README* COPYING
%_bindir/pronsole*
%_pixmapsdir/pronsole.png
%_desktopdir/pronsole.desktop
%_datadir/appdata/pronsole.appdata.xml

%if_with prontserve
%files -n prontserve
%doc README* COPYING
%_bindir/prontserve*
%endif

%files -n pronterface -f pronterface.lang
%doc README* COPYING
%_bindir/pronterface*
%_datadir/pronterface
%_pixmapsdir/pronterface.png
%_desktopdir/pronterface.desktop
%_datadir/appdata/pronterface.appdata.xml

%files -n plater -f plater.lang
%doc README* COPYING
%_bindir/plater*
%_desktopdir/plater.desktop
%_datadir/appdata/plater.appdata.xml

%changelog
* Thu Jun 06 2019 Grigory Ustinov <grenka@altlinux.org> 1:1.6.0-alt2
- Fix desktop files (Closes: #36763).

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.6.0-alt1.qa1
- NMU: applied repocop patch

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.0-alt1
- New version.

* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 20131019-alt1
- Import from Fedora


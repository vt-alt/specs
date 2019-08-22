Name: scratch

%define installdir %_datadir/scratch

Summary: A new programming language
Summary(ru.UTF-8): Программирование для детей на основе Logo

Group: Education
Version: 1.4.0.7
Release: alt6

License: Artistic License
Url: http://scratch.mit.edu/

Source: %name.tar.gz
Source1: %name.png
Source2: ru.po

Patch0: scratch-1.4.0.7-use-fedora-squeak.patch
# Patch1: 002-locale-fix.patch
Patch2: scratch-1.4.0.7-open-from-commandline.patch
Patch4: 005-fix-desktop-file.patch
# deprecated patches, as plugins moved to squeak-vm.
Patch5: 006-unicodeplugin-dirty-rollback.patch
Patch6: 007-fix-scrathplugin-build.patch

Requires: %name-image
Requires: squeak-vm >= 4.10.2.2614-alt3_8
Obsoletes: %name-bin
Provides: scratch-plugins = %version-%release
Obsoletes: scratch-plugins < %version-%release

BuildArch: noarch

# Automatically added by buildreq on Tue Jan 19 2010
BuildRequires: libpango-devel libv4l-devel

%description
Scratch is a new programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

Scratch is designed to help young people (ages 8 and up) develop 21st century
learning skills. As they create Scratch projects, young people learn important
mathematical and computational ideas, while also gaining a deeper understanding
of the process of design.

#Virtual package which provides a complete environment
%package full
Summary: Virtual package which provides a complete environment for %name
Group: Education
Requires: %name %name-image %name-media %name-projects
BuildArch: noarch

%description full
Virtual package which provides a complete environment for %name

%description full -l ru_RU.UTF-8
Виртуальный пакет устанавливающий все файлы для %name

#Scrath image
%package image
Summary: Image file of %name
Group: Education
Requires: %name
BuildArch: noarch
%description image
Image file of %name

%description image -l ru_RU.UTF-8
Файл образа %name

#Scrath help-en
%package help-en
Summary: English help files for %name
Group: Education
Requires: %name
BuildArch: noarch
%description help-en
English help files for %name

%description help-en -l ru_RU.UTF-8
Файлы справки для %name (Английский)

#Scrath Media
%package media
Summary: Media files for %name
Group: Education
Requires: %name-image
BuildArch: noarch
%description media
Media files for %name

%description media -l ru_RU.UTF-8
Медиафайлы для %name

#Scrath Projects
%package projects
Summary: Projects files for %name
Group: Education
Requires: %name
BuildArch: noarch
%description projects
Projects files for %name

%description projects -l ru_RU.UTF-8
Подборка готовых проектов для %name

%prep
%setup -q -n %name

%patch0 -p1
#patch1 -p1
%patch2 -p2
%patch4 -p2
%patch5 -p1
%patch6 -p1

cp -f %SOURCE2 locale/ru.po

%build
# since the Squeak VM version 4.10.2.2593 and greater includes all the
# plugins previously included as part of Scratch, we don't need to build
# anything here.

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/scratch

mkdir -p %buildroot%_iconsdir/hicolor/128x128/apps
mkdir -p %buildroot%_iconsdir/hicolor/48x48/apps
mkdir -p %buildroot%_iconsdir/hicolor/128x128/mimetypes
mkdir -p %buildroot%_iconsdir/hicolor/48x48/mimetypes

install -Dm644 Scratch.image %buildroot%installdir/Scratch.image
install -Dm644 Scratch.ini %buildroot%installdir/Scratch.ini
install -Dm755 src/%name %buildroot%_bindir/%name
install -Dm644 src/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 %SOURCE1 %buildroot%_pixmapsdir/%name.png
install -Dm644 src/icons/48x48/scratch.png %buildroot%_iconsdir/hicolor/48x48/apps/
install -Dm644 src/icons/128x128/scratch.png %buildroot%_iconsdir/hicolor/128x128/apps/
install -Dm644 src/icons/48x48/gnome-mime-application-x-scratch-project.png %buildroot%_iconsdir/hicolor/48x48/mimetypes/
install -Dm644 src/icons/128x128/gnome-mime-application-x-scratch-project.png %buildroot%_iconsdir/hicolor/128x128/mimetypes/

install -m 755 -d %buildroot%_datadir/mime/packages
install -m 644 src/%name.xml %buildroot%_datadir/mime/packages/

install -m 755 -d %buildroot%_man1dir
install -m 644 src/man/scratch.1.gz %buildroot%_man1dir/

mkdir -p %buildroot%installdir

mv Help %buildroot%installdir/
mv locale %buildroot%installdir/
mv Media %buildroot%installdir/
mv Projects %buildroot%installdir/
#%_bindir/scratch is a shell script
%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_man1dir/%name.*

#virtual package which provides a complete environment for Scratch
%files full

#Scrath image
%files image
%doc KNOWN-BUGS ACKNOWLEDGEMENTS LICENSE NOTICE TRADEMARK_POLICY gpl-2.0.txt README
%installdir/Scratch.image
%installdir/locale
%installdir/Scratch.ini
%_iconsdir/hicolor/48x48/*/*
%_iconsdir/hicolor/128x128/*/*
%_datadir/mime/packages/*
#Scrath image
%files help-en
%installdir/Help
#Scrath Media
%files media
%installdir/Media
#Scrath Projects
%files projects
%installdir/Projects

%changelog
* Thu Aug 22 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.0.7-alt6
- Use Fixed font (doubled size, not bold)' for Russian UI.

* Fri Apr 05 2019 Ivan Razzhivin <underwit@altlinux.org> 1.4.0.7-alt5
- Update Russian translation
- Add Russian Comment in desktop file

* Wed Feb 13 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.0.7-alt4
- Fix open Scratch file from command line and file manager.

* Wed May 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.0.7-alt3
- Add Russian GenericName in desktop file

* Thu Sep 05 2013 Andrey Cherepanov <cas@altlinux.org> 1.4.0.7-alt2
- require new squeak-vm because scratch-plugins was moved to squeak-vm
- add provides and obsoletes of old version scratch-plugins
- fix program start (ALT #29296)

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0.7-alt1
- new version

* Tue Aug 16 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.0.1-alt4
- Remove all .svn subdirectories from source
- Cleanup patches

* Mon Aug 15 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.0.1-alt3
- Enable patch to fix Cyrillic letter show in GUI (closes: #26051)

* Thu May 06 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4.0.1-alt2
- spec cleanup

* Tue May 04 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4.0.1-alt1
- totally reworked
- add webcam support (/dev/video0 only)
- some ru.po fix

* Sat Jan 30 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.7
- spec cleanup

* Fri Jan 29 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.6
- some ru.po fix from edmdv

* Thu Jan 28 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.5
- yet another build

* Thu Jan 28 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.4
- switch arch to "noarch"
- spec cleanup

* Wed Jan 27 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.3
- initial build for ALT Linux


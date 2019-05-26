%define java_version 1.8

Name:    projectlibre
Version: 1.9.1
Release: alt1

Summary: ProjectLibre - The open source replacement of Microsoft Project

License: CPAL
Group:   Office
Url:     https://sourceforge.net/projects/projectlibre/
# VCS:   git://git.code.sf.net/p/projectlibre/code

Source:  %name-%version.tar
Source1: %name.watch
Patch1:  %name-1.6.2-mga-l10n-dialogs.patch
Patch2:  %name-1.6.2-alt-fix-path-in-executable.patch

Packager: Danil Mikhailov <danil@altlinux.org>

Requires: java >= 1.6.0

BuildArch: noarch
BuildPreReq: rpm-build-compat
BuildRequires: ant
BuildRequires: java-1.8.0-openjdk-devel

%define projectlibredir %_libexecdir/%name

%description
ProjectLibre is an open source alternative to Microsoft Project.  It is
also the new updated version of OpenProj. We were the developers of
OpenProj A compliment to Apache OpenOffice and LibreOffice.  We have a
community site as well at http://www.projectlibre.org It has been
downloaded over 500,000 times in 200 countries and was just won
InfoWorld "Best of Open Source" award. ProjectLibre is compatible
with Microsoft Project 2003, 2007 and 2010 files. You can simply open
them on Linux, Mac OS or Windows. ProjectLibre has been rewritten and
added key features:

* Compatibility with Microsoft Project 2010
* User Interface improvement
* Printing (does not allow printing)
* Bug fixes

%prep
%setup
#patch2 -p1
#patch1 -p1
# Set Java version
subst 's/\(source\|target\)="[0-9.]\+"/\1="%java_version"/g' `find . -name build.xml`
# Replace hard-coded library path by default JRE path
subst 's|/Library/Java/JavaVirtualMachines/jdk1.7.0_45.jdk/Contents/Home/jre/lib/rt.jar|%_libexecdir/jvm/jre/lib/rt.jar|' projectlibre_contrib/projectlibre_*.conf

%build
#Set the file encoding for source files
export JAVA_TOOL_OPTIONS=-Dfile.encoding=cp1252
cd projectlibre_build/
ant clean
ant

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %buildroot/%projectlibredir/lib
install -Dm0755  projectlibre_build/dist/%name.jar %buildroot/%projectlibredir/
install -Dm0755 projectlibre_contrib/*.jar %buildroot/%projectlibredir/lib

# startscript
cat > %name << EOF
#!/bin/sh
#
echo Starting %name version %version ...
echo with options : \${@}

java -jar %projectlibredir/%name.jar \${@}

EOF

# Install startscript
install -Dm0755 %name %buildroot%_bindir/%name

install -Dm0644 projectlibre_build/resources/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm0644 projectlibre_build/resources/%name.png %buildroot%_pixmapsdir/%name.png

%files
%doc projectlibre_build/license/*
%_bindir/%name
%projectlibredir
%_desktopdir/*
%_pixmapsdir/*

%changelog
* Fri May 24 2019 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1
- New version.

* Tue Nov 14 2017 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt1
- new version 1.7.0

* Tue Oct 04 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.2-alt3
- Remove strict requires on java-1.7.0-openjdk

* Wed Sep 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.2-alt2
- First check Java at default location (/usr/java/latest) (ALT #32386)
- Require java-1.7.0-openjdk because bundled jar is linked with Java 1.7
- Apply l10n patch from Mageia

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.2-alt1
- New version
- Build from upstream Git repository

* Thu Feb 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt4
- Fix path to jar file in startup script

* Fri Nov 07 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt3
- set BuildArch: noarch

* Wed Oct 29 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt2
- Some cleaup

* Wed Oct 15 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt1
- Added right pixmap, and run script
- Change to right version

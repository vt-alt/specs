# 6.2.4.2
%def_without forky
%def_without python
%def_with parallelism
%def_without fetch
%def_without lto

# enable kde5 UI
%def_enable kde5

%ifarch mipsel
%def_without java
%def_disable qt5
%else
%def_with java
%if_enabled kde5
%def_enable qt5
%else
%def_disable qt5
%endif
%endif
%def_disable mergelibs

Name: LibreOffice
%define hversion 6.2
%define urelease 4.2
Version: %hversion.%urelease
%define uversion %version.%urelease
%define lodir %_libdir/%name
%define uname libreoffice
%define conffile %_sysconfdir/sysconfig/%uname
Release: alt1
Summary: LibreOffice Productivity Suite
License: LGPL
Group: Office
URL: http://www.libreoffice.org

Requires: %name-integrated = %EVR
Requires: %name-common = %EVR
Requires: %name-mimetypes = %EVR
Requires: %name-extensions = %EVR

Provides: %name-full = %EVR
Provides: libreoffice = %EVR
Obsoletes: libreoffice < 3.99
Obsoletes: %name-full < %EVR
Obsoletes: LibreOffice4

%define with_lang ru be de fr uk pt-BR es kk tt
#Requires: java xdg-utils hunspell-en hyphen-en mythes-en
#Requires: gst-plugins-bad1.0 gst-plugins-good1.0 gst-plugins-nice1.0 gst-plugins-ugly1.0 gst-plugins-base1.0
Requires: gst-libav

Source:		libreoffice-%version.tar.xz
Source1:	libreoffice-dictionaries-%version.tar.xz
Source2:	libreoffice-help-%version.tar.xz
Source3:	libreoffice-translations-%version.tar.xz

Source10:	libreoffice-ext_sources.%version.tar
Source100:	forky.c
Source200:	key.gpg
Source300:	libreoffice.unused

## FC patches
Patch1: FC-0001-don-t-suppress-crashes.patch
Patch2: FC-0001-Resolves-rhbz-1432468-disable-opencl-by-default.patch
Patch3: FC-0001-rhbz-1690732-basic-font-variation-support.patch
Patch4: FC-0001-rhbz-1699347-__glibcxx_requires_subscript-enabled-in.patch
Patch5: FC-0001-no-home-as-templates.patch
Patch6: FC-0001-Resolves-rhbz-1702810-Prepare-for-upcoming-libebook-.patch
Patch7: FC-0001-Resolves-rhbz-1712823-prefer-help-strings-to-a11y-st.patch
Patch8: FC-0001-Resolves-tdf-125099-round-duration-results-in-interp.patch
Patch9: FC-0001-Resolves-rhbz-1713827-protect-against-null-ViewShell.patch
Patch10: FC-0001-disable-libe-book-support.patch

## Long-term FC patches

## ALT patches
Patch401: alt-001-MOZILLA_CERTIFICATE_FOLDER.patch
Patch402: alt-002-tmpdir.patch
Patch403: alt-003-poppler-compat.patch
Patch404: alt-004-shortint.patch
Patch405: alt-005-mysql8-transition.patch

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*
%add_findreq_skiplist %lodir/sdk/examples/python/toolpanel/toolpanel.py 

# Automatically added by buildreq on Wed Feb 13 2019
# optimized out: ant-lib apache-commons-logging at-spi2-atk bash4 boost-devel boost-devel-headers cppunit dconf fontconfig fontconfig-devel gcc-c++ glib-networking glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gobject-introspection gobject-introspection-devel gstreamer1.0-devel hamcrest-core icu-utils java java-headless javapackages-tools javazi kf5-kconfig-devel kf5-kcoreaddons-devel libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXt-devel libat-spi2-core libatk-devel libatk-gir-devel libboost_numpy3-1.67.0 libboost_python3-1.67.0 libcairo-devel libcairo-gobject libcairo-gobject-devel libclucene-contribs-lib libclucene-core libclucene-shared libcrypt-devel libcurl-devel libe-book libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-gir-devel libgio-devel libglvnd-devel libgpg-error libgpg-error-devel libgraphite2-devel libgst-plugins1.0 libgtk+3-devel libharfbuzz-devel libharfbuzz-icu libicu-devel libltdl7-devel libnspr-devel libnss-devel libpango-devel libpango-gir-devel libpng-devel libpoppler-devel libpq-devel libqt5-core libqt5-gui libqt5-network libqt5-widgets libqt5-x11extras librasqal-devel librevenge-devel libsasl2-3 libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libxcb-devel libxml2-devel libxmlsec1-devel libxmlsec1-nss libxslt-devel pentaho-libxml perl pkg-config python-base python-modules python-modules-compiler python-modules-distutils python3 python3-base python3-module-lxml qt5-base-devel raptor2-devel sac sh4 termutils wayland-devel xml-common xml-utils xorg-proto-devel xz zlib-devel
BuildRequires: boost-filesystem-devel boost-locale-devel boost-signals-devel bsh cppunit-devel doxygen flex fontforge fonts-ttf-liberation git-core gperf graphviz gst-plugins1.0-devel imake libGConf libabw-devel libavahi-devel libbluez-devel libcdr-devel libclucene-core-devel libcmis-devel libcups-devel libdbus-devel libe-book-devel libepoxy-devel libepubgen-devel libetonyek-devel libexpat-devel libexttextcat-devel libfreehand-devel libglm-devel libgpgme-devel libgtk+2-devel libgtk+3-gir-devel libhunspell-devel libhyphen-devel libjpeg-devel liblangtag-devel liblcms2-devel libldap-devel liblpsolve-devel libmspub-devel libmwaw-devel libmysqlclient-devel libmythes-devel libneon-devel libnumbertext-devel libodfgen-devel liborcus-devel libpagemaker-devel libpoppler-cpp-devel libqxp-devel libredland-devel libsane-devel libssl-devel libstaroffice-devel libunixODBC-devel libvisio-devel libwpd10-devel libwpg-devel libwps-devel libxmlsec1-nss-devel libzmf-devel mdds-devel pentaho-reporting-flow-engine postgresql-devel unzip xorg-cf-files xsltproc zip
%if_with java
BuildRequires: java-devel junit ant
%endif

%if_enabled qt5
BuildRequires: qt5-base-devel qt5-x11extras-devel 
%endif

%if_enabled kde5
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kwindowsystem-devel
%endif

%if_without python
BuildRequires: python3-dev
%endif

%description
LibreOffice is a productivity suite that is compatible with other major
office suites.

This package provides maximum possible installation of %name along winth
other office packages, except of language packs and GNOME/KDE bindings.

%package common
Summary: Basic installation of %name
Group: Office
Obsoletes: LibreOffice4-common
AutoReqProv: yes, noshell, nopython
%description common
Common part of %name that does not interfere with other packages

%package integrated
Summary: Binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %EVR
Obsoletes: LibreOffice4-integrated
Requires: %name-common = %EVR
%description integrated
Wrapper scripts, icons and desktop files for running %name

%package gtk2
Summary: GTK2 Extensions for %name
Group:  Office
Requires: %uname = %EVR
Requires: %name-common = %EVR
Provides: %name-gtk = %EVR
Obsoletes: %name-gtk
%description gtk2
GTK2 extensions for %name

%package gtk3
Summary: GTK3 Extensions for %name
Group:  Office
Requires: %uname = %EVR
Requires: %name-common = %EVR
Provides: %name-gnome = %EVR
Obsoletes: %name-gnome
%description gtk3
GTK3 extensions for %name

%if_enabled qt5
%package qt5
Summary: Qt5 Extensions for %name
Group:  Office
Requires: %uname = %EVR
Requires: %name-common = %EVR
Obsoletes: LibreOffice4-kde4 < %EVR
%description qt5
qt5 extensions for %name
%endif

%if_enabled kde5
%package kde5
Summary: KDE5 Extensions for %name
Group:  Office
Requires: %uname = %EVR
Requires: %name-common = %EVR
Provides: LibreOffice-kde = %EVR
%description kde5
KDE5 extensions for %name
%endif

%package -n libreofficekit
Summary: A library providing access to LibreOffice functionality
Group: Graphical desktop/GNOME
License: MPLv2.0
%description -n libreofficekit
LibreOfficeKit can be used to access LibreOffice functionality
through C/C++, without any need to use UNO.

%package -n libreofficekit-devel
Summary: Development files for libreofficekit
Group: Development/GNOME and GTK+
License: MPLv2.0
%description -n libreofficekit-devel
The libreofficekit-devel package contains libraries and header files for
developing applications that use libreofficekit.


%package extensions
Summary: Additional extensions for %name
Group:  Office
Requires: %uname = %EVR
AutoReqProv: yes, noshell, nopython
Obsoletes: LibreOffice4-extensions
%description extensions
Additional extensions for %name.
One can choose either to install this package at once,
or to download and install (possibly newer) extensions manually.

%package mimetypes
Summary: Mimetype keys support for %name
Group: Office
BuildArch: noarch
Obsoletes: LibreOffice4-mimetypes
%description mimetypes
%name is distributed along with some mimetype settings and files.
This package installs them.

%package sdk
Group: Development/Other
Summary: Software Development Kit for LibreOffice

%description sdk
The SDK is a development kit for LibreOffice 5.3, which
eases the development of office components. It provides a set of
libraries, binaries, header, and IDL files which have final API's
and can only be extended with new functionality. This set of libraries
and binaries is the minimum set of functions needed to use system
abstraction for base functionality and for using UNO (Universal
Network Objects) component technology. The UNO component model is the
base of the whole Office API. The SDK provides everything necessary
to use the Office API from external programs (e.g. Java, C++) or to
extend the Office functionality with new components (e.g. new filter
components, CalcAddin functions). It is compatible over several
versions because the API remains unaffected and will only be extended
with new functions.


# TODO redefine %%lang adding corr langpack
# define macro for quick langpack description
%define langpack(l:n:mh) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %name \
Group:  Office \
Requires: %uname = %EVR \
%{-m:Requires: mythes-%lang} \
%{-h:Requires: hyphen-%lang} \
Obsoletes: LibreOffice4-%{pkgname} \
%description %{pkgname} \
Provides additional %{langname} translations and resources for %name. \
\
%files %{pkgname} -f %{lang}.lang \
%{nil}

%prep
%if_with forky
echo Using forky
%else
echo Direct build
%endif
%setup -q -n libreoffice-%version -a10 -b1 -b2 -b3

## FC apply patches
%patch1 -p1
%patch2 -p1
#patch3 -p1
#patch4 -p1
#patch5 -p1
#patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#patch10 -p1

## Long-term FC patches applying

## ALT apply patches
%patch401 -p0
%patch402 -p1
#patch403 -p1
%patch404 -p1
%patch405 -p2

# Hack in proper LibreOffice PATH in libreofficekit
sed -i 's@/libreoffice/@/LibreOffice/@g' libreofficekit/Library_libreofficekitgtk.mk

# Hack hardcoded lsattr path
for f in `grep -rl '/usr/sbin/lsattr' *`; do sed -i 's@/usr/sbin/lsattr@/usr/bin/lsattr@g' $f; done

# Hack in MimeType=application/vnd.ms-visio.drawing.main+xml
fgrep -q "application/vnd.ms-visio.drawing.main+xml" sysui/desktop/menus/draw.desktop || sed -i 's@MimeType=@MimeType=application/vnd.ms-visio.drawing.main+xml;@' sysui/desktop/menus/draw.desktop

# hack hardcoded libodbc version
sed -i 's/libodbc.so.1/libodbc.so.2/g' connectivity/source/drivers/odbc/OFunctions.cxx

rm -fr %name-tnslations/git-hooks

install -D %SOURCE100 forky.c

# create shell wrappers
for n in office writer impress calc base draw math qstart; do
	oname=lo$n
	case "$n" in 
		office) opt=""; oname=libreoffice%hversion;;
		qstart) opt="--quickstart --nologo --nodefault";;
		*) opt="--$n";;
	esac
	cat > $oname.sh <<@@@
#!/bin/sh
exec %lodir/program/soffice $opt "\$@"
@@@
done

# Now create a config file
grep -r getenv * | sed -n 's/.*getenv *( *"\([^"]*\).*/\1/p' | sort -u | egrep 'STAR_|SAL_|OOO_' > %name.config.ENV

sed -n '/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/p' < desktop/scripts/soffice.sh > libreoffice.config
test -n "libreoffice.config"
sed -i '/# STAR_PROFILE_LOCKING_DISABLED/i\
test -r %conffile && . %conffile ||:
/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/d' desktop/scripts/soffice.sh

%build
export CC=%_target_platform-gcc
export CXX=%_target_platform-g++
%ifarch mipsel
export CFLAGS="-Os --param ggc-min-expand=20 --param ggc-min-heapsize=32768 -g0"
export CXXFLAGS="$CFLAGS"
%endif

./autogen.sh \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--disable-lto \
        --with-vendor="ALT Linux Team" \
        %{subst_enable mergelibs} \
        --enable-odk \
	--disable-firebird-sdbc \
	--disable-coinmp \
        --enable-dbus \
        --enable-evolution2 \
        --enable-gio \
	--enable-build-opensymbol \
  	--enable-avahi \
        %{subst_with java} \
        --without-fonts \
        --without-myspell-dicts \
	\
        --with-external-dict-dir=%_datadir/myspell \
        --with-external-hyph-dir=%_datadir/hyphen \
        --with-external-thes-dir=%_datadir/mythes \
        --with-lang="en-US %with_lang" \
        --with-external-tar=`pwd`/ext_sources \
	\
	--enable-ext-nlpsolver \
	--enable-ext-numbertext \
	--enable-ext-wiki-publisher \
	--enable-ext-ct2n \
	--enable-ext-languagetool \
  \
	--enable-release-build \
	--with-help \
  \
	%{subst_enable kde5} \
	%{subst_enable qt5} \
	--enable-gtk \
	--enable-gtk3 \
  	--enable-cipher-openssl-backend \
%if_enabled kde5
	--enable-kde5 \
%endif
	--disable-gstreamer-0-10 \
  \
%if_with lto
  	--enable-lto \
%endif
%if_with parallelism
	--with-parallelism=`nproc` \
%else   
        --without-parallelism \
%endif
%if_with python
	--enable-python=internal \
%endif
%if_with fetch
	--enable-fetch-external
%else
	--with-system-libs \
	--disable-fetch-external
%endif

# TODO  --enable-vlc --enable-eot

%if_with forky
# Make forky
gcc -g -DHAVE_CONFIG_H -shared -O3 -fomit-frame-pointer -fPIC forky.c -oforky.so -ldl
%endif

%make bootstrap

%if_with parallelism
export _JAVA_OPTIONS="-XX:ParallelGCThreads=4 $_JAVA_OPTIONS"
%endif

%if_with forky
# TODO prefect forky_max tune
echo Using forky
export forky_divider=21
export forky_max_procs=`awk '/^Max processes/{print int(5*$3/'$forky_divider')}' < /proc/self/limits`
export forky_max_rss=6400000
export forky_max_vsz=9600000
export forky_verbose=1
echo "max_procs $forky_max_procs / max_vsz $forky_max_vsz / max_rss $forky_max_rss" | tee $HOME/forky.log
export LD_PRELOAD=`pwd`/forky.so

%make build-nocheck || { tail -100 $HOME/forky.log; head -1 $HOME/forky.log; wc $HOME/forky.log; false; }
test -r $HOME/forky.log && echo "Fork() was `wc -l $HOME/forky.log` times delayed" || :
%else
%make verbose=true build-nocheck
%endif

# Generate typelib files
## TODO use stuff generated here
export DESTDIR=../output
export KDEMAINDIR=/usr
export GNOMEDIR=/usr
export GNOME_MIME_THEME=hicolor
export PREFIXDIR=/usr
. ./bin/get_config_variables PRODUCTVERSIONSHORT PRODUCTVERSION SRCDIR WORKDIR PKG_CONFIG INSTDIR
export PRODUCTVERSIONSHORT PRODUCTVERSION SRCDIR WORKDIR PKG_CONFIG INSTDIR
cd $WORKDIR/CustomTarget/sysui/share/libreoffice
./create_tree.sh

%install
%makeinstall DESTDIR=%buildroot INSTALLDIR=%lodir
%if_with python
# Ignore dull /usr/local/bin/python hack
chmod -x %buildroot%lodir/program/python-core*/lib/cgi.py
%endif

# Pick up LOO-generated file lists
for l in %with_lang; do
	ll="`echo "$l" | tr '-' '_'`"
	cat %buildroot/gid_*_$ll | sort -u > $l.lang
done

# Create gnome plugin list
find %buildroot%lodir -name "*_gtk[^3]*"  | sed 's@^%buildroot@@' > files.gtk2

# Create gtk3 plugin list
find %buildroot%lodir -name "*_gtk3*" ! -name "*_kde5*" | sed 's@^%buildroot@@' > files.gtk3

# Create kde plugin list
find %buildroot%lodir -name "*kde4*"  | sed 's@^%buildroot@@' > files.kde4

# Create qt5 plugin list
find %buildroot%lodir -name "*qt5*"   | sed 's@^%buildroot@@' > files.qt5

# Create kde5 plugin list
find %buildroot%lodir -name "*_kde5*" -o -name "libkde5*" | sed 's@^%buildroot@@' > files.kde5

# Generate base filelist by removing files from  separated packages
{ cat %buildroot/gid_* | sort -u ; cat *.lang files.gtk2 files.gtk3 files.kde4 files.kde5 files.qt5; echo %lodir/program/liblibreofficekitgtk.so; } | sort | uniq -u | grep -v '~$' | egrep -v '/share/extensions/.|%lodir/sdk/.' > files.nolang

unset RPM_PYTHON

# Install wrappers
for n in lo*.sh; do install -m755 -D $n %buildroot%_bindir/${n%%.sh}; done
install -m755 -D libreoffice%hversion.sh %buildroot%_bindir/loffice
ln -s loffice %buildroot%_bindir/soffice
install -m755 -D libreoffice%hversion.sh %buildroot%_bindir/libreoffice
install -m755 libreoffice%hversion.sh %buildroot%_bindir/libreoffice%hversion

# install icons
for f in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	d=`dirname "$f"`; n=`basename "$f"`
	install -D sysui/desktop/icons/$f %buildroot%_iconsdir/$d/$n
	ln -sr %buildroot%_iconsdir/$d/$n %buildroot%_iconsdir/$d/libreoffice%hversion-$n
done

# TODO icon-themes/

# Hack out "Education" category from Math
sed -i 's/Education;//' %buildroot%lodir/share/xdg/math.desktop

mkdir -p %buildroot%_desktopdir
for n in writer impress calc base draw math;  do
	ln %buildroot%lodir/share/xdg/$n.desktop %buildroot%_desktopdir/$n.desktop
done

# TODO some other hack with .mime (?)
mkdir -p %buildroot%_datadir/mime-info %buildroot%_datadir/mimelnk/application %buildroot%_datadir/application-registry
install sysui/desktop/mimetypes/*.keys %buildroot%_datadir/mime-info/
install sysui/desktop/mimetypes/*.mime %buildroot%_datadir/mime-info/
install sysui/desktop/mimetypes/*.desktop %buildroot%_datadir/mimelnk/application/
install sysui/desktop/mimetypes/*.applications %buildroot%_datadir/application-registry/

# Config file
install -D libreoffice.config %buildroot%conffile

# Typelib/GIR stuff
install -D workdir/CustomTarget/sysui/share/output/girepository-1.0/LOKDocView-0.1.typelib %buildroot%_typelibdir/LOKDocView-0.1.typelib
install -D workdir/CustomTarget/sysui/share/output/usr/share/gir-1.0/LOKDocView-0.1.gir %buildroot%_girdir/LOKDocView-0.1.gir
mv %buildroot%lodir/program/liblibreofficekitgtk.so %buildroot%_libdir/
mkdir -p %buildroot%_includedir/LibreOfficeKit
install -p include/LibreOfficeKit/* %{buildroot}%{_includedir}/LibreOfficeKit

%files

%files sdk
%lodir/sdk

%files common -f files.nolang
%exclude /gid_Module*
%_bindir/libreoffice%hversion
%config %conffile
%lodir/share/extensions/package.txt
#lodir/share/extensions/presentation-minimizer
%_iconsdir/*/*/apps/libreoffice%{hversion}-*.*g

%files integrated
%_bindir/*
%exclude %_bindir/libreoffice%hversion
%_desktopdir/*
%_iconsdir/*/*/mimetypes/*
%_iconsdir/*/*/apps/*
%exclude %_iconsdir/*/*/apps/libreoffice%{hversion}-*.*g

%files gtk2 -f files.gtk2

%files gtk3 -f files.gtk3

%if_enabled kde4
%files kde4 -f files.kde4
%endif

%if_enabled qt5
%files qt5 -f files.qt5
%endif

%if_enabled kde5
%files kde5 -f files.kde5
%endif

%files extensions
%lodir/share/extensions/*
%exclude %lodir/share/extensions/package.txt

%files mimetypes
%_datadir/mime-info/*
%_datadir/mimelnk/application/*
%_datadir/application-registry/*

%langpack -m -h -l ru -n Russian
%langpack -h -l be -n Belorussian
%langpack -m -h -l de -n German
%langpack -m -h -l fr -n French
%langpack -m -h -l uk -n Ukrainian
%langpack -l pt-BR -n Brazilian Portuguese
%langpack -h -m -l es -n Espanian
%langpack -l kk -n Kazakh
%langpack -h -l tt -n Tatar

%files -n libreofficekit
%_typelibdir/LOKDocView-*.typelib
%_libdir/liblibreofficekitgtk.so

%files -n libreofficekit-devel
%_girdir/LOKDocView-*.gir
%_includedir/LibreOfficeKit

%changelog
* Mon May 27 2019 Fr. Br. George <george@altlinux.ru> 6.2.4.2-alt1
- Verion up (Closes: #36635, #35896)

* Mon Apr 08 2019 Fr. Br. George <george@altlinux.ru> 6.2.2.2-alt1.1
- Build with internal python

* Mon Mar 25 2019 Fr. Br. George <george@altlinux.ru> 6.2.2.2-alt1
- Update to 6.2.2.2

* Sun Mar 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.2.1.1-alt2
- Fix FTBFS against libmysqlclient21

* Mon Feb 18 2019 Fr. Br. George <george@altlinux.ru> 6.2.1.1-alt1
- Update to 6.2.1.1 (Closes: #36107, #35504, #35420, #35292)
- Move KDE-depended library to -kde5 package (Closes: #36100)

* Tue Feb 12 2019 Fr. Br. George <george@altlinux.ru> 6.2.0.3-alt1
- Update to 6.2.0.3
- Build with native kde5 SAL instead of gtk3/kde5

* Wed Nov 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.3.1-alt3
- NMU: fixed build with new poppler.

* Mon Oct 22 2018 Ivan Razzhivin <underwit@altlinux.org> 6.1.3.1-alt2
- build with gtk3/kde5 UI

* Wed Oct 17 2018 Fr. Br. George <george@altlinux.ru> 6.1.3.1-alt1
- Update to 6.1.3.1

* Tue Sep 25 2018 Fr. Br. George <george@altlinux.ru> 6.1.2.1-alt1
- Update to 6.1.2.1

* Mon Sep 17 2018 Fr. Br. George <george@altlinux.ru> 6.1.1.2-alt1
- Update to 6.1.1.2

* Mon Aug 20 2018 Fr. Br. George <george@altlinux.ru> 6.1.0.3-alt1
- Update to 6.1.0.3 (Closes: #35135)
- MIPS port, thanks to iv@ (Closes: #35171)

* Wed Jun 06 2018 Fr. Br. George <george@altlinux.ru> 6.0.5.1-alt1
- Update to 6.0.5.1 (Closes: #34765)
- Introduce Qt5 chooser (Closes: #33136)
- Provide libreoffice binary (Closes: #34825)
- Add application/vnd.ms-visio.drawing.main+xml to mimetypes (Closes: #32699)

* Wed May 23 2018 Fr. Br. George <george@altlinux.ru> 6.0.4.2-alt1
- Update to 6.0.4.2

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.1.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Feb 14 2018 Fr. Br. George <george@altlinux.ru> 6.0.1.1-alt1
- Update to 6.0.1.1

* Thu Nov 30 2017 Fr. Br. George <george@altlinux.ru> 5.4.3.2-alt1
- Update to 5.4.3.2

* Mon Nov 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4.2.2-alt2
- Rebuilt with libCoinMP-1.8.3.

* Thu Oct 05 2017 Fr. Br. George <george@altlinux.ru> 5.4.2.2-alt1
- Update to 5.4.2.2

* Tue Sep 12 2017 Fr. Br. George <george@altlinux.ru> 5.4.1.2-alt1
- Update to 5.4.1.2

* Mon Jul 31 2017 Fr. Br. George <george@altlinux.ru> 5.4.0.3-alt1
- Update to 5.4.0.3

* Wed Jun 07 2017 Fr. Br. George <george@altlinux.ru> 5.3.3.2-alt2
- Enable languagetool extension

* Wed May 17 2017 Fr. Br. George <george@altlinux.ru> 5.3.3.2-alt1
- Update to 5.3.3.2
- Build SDK

* Wed Apr 12 2017 Fr. Br. George <george@altlinux.ru> 5.3.2.2-alt1
- Update to 5.3.2.2

* Thu Feb 09 2017 Fr. Br. George <george@altlinux.ru> 5.3.0.3-alt1
- Update to 5.3.0.3
- Change versioning scheme

* Mon Oct 17 2016 Fr. Br. George <george@altlinux.ru> 5.2-alt4
- Update to 5.2.3.1

* Wed Aug 24 2016 Fr. Br. George <george@altlinux.ru> 5.2-alt3
- Update to 5.2.1.1

* Tue Jul 19 2016 Fr. Br. George <george@altlinux.ru> 5.2-alt2
- Update to 5.2.0.2
- (closes: #31953)

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 5.2-alt1
- Update to 5.2.0.1

* Thu Jun 02 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt4
- Update to 5.1.3.2
- Fix buildreqs

* Thu Mar 31 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt3
- Update to 5.1.2.1
- Build with system python again

* Thu Mar 10 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt2
- Update to 5.1.1.3
- Build without forky (turns out -XX:ParallelGCThreads=2 fixes OOM)

* Wed Feb 10 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt1
- Update to 5.1.1.1
- Build with internal Python3

* Wed Nov 04 2015 Fr. Br. George <george@altlinux.ru> 5.0-alt2
- Update to 5.0.3.2

* Wed Sep 16 2015 Fr. Br. George <george@altlinux.ru> 5.0-alt1
- Update to 5.0.3.1
- Rename package
- Remove -standalone package

* Tue Feb 24 2015 Fr. Br. George <george@altlinux.ru> 4.4-alt2
- Update to 4.4.1.2

* Thu Feb 05 2015 Fr. Br. George <george@altlinux.ru> 4.4-alt1
- Update to 4.4.0.3
- Turn tt and be langpacks on

* Mon Dec 01 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt3
- Update to 4.3.5.1

* Wed Nov 19 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt2
- Update to 4.3.4.1

* Wed Nov 12 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt1
- Update to 4.3.3.2
- Provide loffice binary (Closes: #30044)
- Reqiure gst-libav (Closes: #30015)

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 4.3-alt0.beta2.buildfix1
- 4.3.0.0.beta2-buildfix1
- update BR:
- switch to librevenge-based import libs

* Wed Apr 30 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt3
- Version up to 4.2.4.1

* Wed Apr 16 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt2
- Version up to 4.2.3.3

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt1
- Version up

* Tue Feb 04 2014 Fr. Br. George <george@altlinux.ru> 4.1-alt9
- Merge -full package into general one
- Buld with help (closes: #29735)
- Require gst1.0 plugins to install (closes: #29782)

* Thu Dec 26 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt8
- Build with --enable-release-build

* Thu Dec 19 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt7
- Version up to officially corporative stable 4.1.4.2
- Disable applied patches

* Mon Nov 25 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt6
- Version up to officially stable 4.1.3.2
- More accurate forky utilization

* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt5
- Version up to 4.1.2.3

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt4
- rebuild against libharfbuzz-icu

* Wed Sep 04 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt3
- Version up to 4.1.1.2
- Refresh FC patchset
- Un-hardcode /tmp usage (Closes: 29267)

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 4.1-alt2
- fixed gnome file list
- fixed kde file list
- drop use gnome-open in gnome-open-url.sh
- build with gstreamer-1.0
- build with system libraries (libodfgen,libcdr,libmspub,libmwaw,libvisio,libcmis,libexttextcat)
- build with system jar files
- changed configure options --with-system-* to --with-system-libs

* Tue Jul 30 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt1
- Version up to 4.1.0.4
- Renew FC patchset (previous ones are pushed to upstream)

*  Wed May 15 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt8
- Version up to 4.0.3.3
- Drop some RH patches accepted by upstream

* Wed Apr 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.0-alt7.1
- NMU: rebuilt with new poppler

* Mon Apr 22 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt7
- Closes: 28883
- Drop some internal libraries build

* Thu Apr 18 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt6
- Version up to 4.0.2.2
- Incoprporate useful RH patches

* Thu Mar 21 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt5
- Introduce Kazakh locale
- Fix common binary displacement

* Tue Mar 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt4
- Fix conflicts with LO3
- Introduce "full" package (without langpacks and GNOME/KDE stuff)

* Wed Mar 06 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt3
- Update to 4.0.2.1
- Introduce extra extensions
- Separate %name-standalone and %name-integrated packages
- Introduce %name-mimetype

* Tue Mar 05 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt2
- Separate KDE4 plugins
- Apply Firefox certificates import patch

* Tue Feb 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt1
Initial test build


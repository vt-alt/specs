Name: netsurf
Version: 3.9
Release: alt1

Summary: Lightweight Web Browser With Good HTML 4 And CSS Support
License: GNU General Public License v2 (GPL v2)
Group: Networking/WWW

Url: http://www.netsurf-browser.org
Source0: netsurf-all.tar.gz
Source1: netsurf.desktop
Source2: netsurf.png
# перевод (дополнительно см. netsurf-all/netsurf/resources/FatMessages)
Source3: netsurf_Messages
Patch: netsurf-3.8-alt-e2k.patch

BuildRequires: gtk2-devel libglade2-devel libjpeg-devel libpng-devel libmng-devel
BuildRequires: libxml2-devel zlib-devel
BuildRequires: libgtk+2-devel
BuildRequires: gcc make glibc-devel perl libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libssl-devel
BuildRequires: gperf flex
%ifarch %e2k
BuildRequires: libmozjs52-devel
%else
BuildRequires: libmozjs60-devel
%endif
BuildRequires: perl-HTML-Parser
BuildRequires: perl-IO-Compress
BuildRequires: xxd

# Версия 3.1 + 
# git clone git://git.netsurf-browser.org/netsurf.git
# git clone git://git.netsurf-browser.org/libcss.git

# Для FRAMEBUFFER версии
# BuildRequires: libxcbutil-keysyms-devel libxcbutil-icccm-devel libxcbutil-devel libxcb-render-util-devel libxcbutil-image-devel libSDL_image-devel libxcb-devel
# make TARGET=framebuffer PREFIX=/usr
# И см. переменную TARGET=Linux в файле netsurf-all-3.1/libnsfb/Makefile 36 "ifeq ($(TARGET),Linux)"
# Для FRAMEBUFFER версии

Group: Networking/WWW

Summary(ru_RU.UTF-8): Легкий кроссплатформенный Web-браузер с поддержкой HTML и CSS.

%description
NetSurf is a lightweight cross-platform Web browser. It supports
the HTML4 and CSS standards and provides a small, fast,
and comprehensive Web browsing solution.

%description -l ru_RU.UTF-8
Легкий кроссплатформенный Web-браузер с хорошей поддержкой HTML и CSS.

%prep
%setup -c %name-%version
%patch -p1

mkdir -p netsurf/!NetSurf/Resources/ru
cp -a %SOURCE3 netsurf/!NetSurf/Resources/ru/Messages

# Скрипт запуска (начало)
cat > netsurf/netsurf << EOF
#!/bin/sh
cd %_libdir/netsurf
./nsgtk \$1
EOF
chmod +x netsurf/netsurf
# Скрипт запуска (конец)

mkdir -p netsurf/gtk/res/ru
pushd netsurf/gtk/res/ru
ln -s ../../../!NetSurf/Resources/ru/Messages Messages
popd

# По дефолту пусть JavaScript включен
# netsurf/desktop/options.h NSOPTION_BOOL(enable_javascript, false)
subst 's/(enable_javascript, false)/(enable_javascript, true)/' netsurf/desktop/options.h

%build
PATH="`pwd`/inst-gtk/bin:$PATH"
echo $PATH
%make_build TARGET=gtk PREFIX=%_usr

%install
%makeinstall_std PREFIX=%_usr

install -pDm755 netsurf/nsgtk %buildroot%_libdir/netsurf/nsgtk
install -pDm755 netsurf/netsurf %buildroot%_bindir/netsurf

mkdir -p %buildroot%_libdir/netsurf/gtk
cp -r --dereference netsurf/gtk/res %buildroot%_libdir/netsurf/gtk
cp -r --dereference netsurf/!NetSurf %buildroot%_libdir/netsurf/

install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pDm644 %SOURCE2 %buildroot%_pixmapsdir/netsurf.png

echo $RPM_FIXUP_METHOD
export RPM_FIXUP_METHOD="binconfig pkgconfig libtool"

%files
%doc netsurf/README
%_bindir/netsurf*
%dir %_datadir/%name
%_datadir/%name/*
%dir %_libdir/netsurf
%_libdir/netsurf/*
%_desktopdir/*
%_datadir/pixmaps/*

%changelog
* Thu Nov 14 2019 Michael Shigorin <mike@altlinux.org> 3.9-alt1
- 3.9 (see also https://bugs.netsurf-browser.org/mantis/view.php?id=2673)
- enable parallel build

* Tue Sep 18 2018 Michael Shigorin <mike@altlinux.org> 3.8-alt2
- E2K: use libmozjs 52, recognize lcc
- proper libdir detection

* Wed Sep 12 2018 Andrey Cherepanov <cas@altlinux.org> 3.8-alt1
- New version.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.7-alt1
- New version.

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5-alt2
- Fixed build with new gperf

* Mon Jun 27 2016 Andrey Cherepanov <cas@altlinux.org> 3.5-alt1
- New version

* Mon Nov 23 2015 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1
- Initial build in Sisyphus (thanks mike@ and YYY for spec)


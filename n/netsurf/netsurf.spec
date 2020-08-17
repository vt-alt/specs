Name: netsurf
Version: 3.10
Release: alt1

Summary: Lightweight Web Browser With Good HTML 4 And CSS Support
License: GNU General Public License v2 (GPL v2)
Group: Networking/WWW

Url: http://www.netsurf-browser.org
Source0: netsurf-all-%version.tar.gz
Source1: netsurf.desktop
Source2: netsurf.png
# перевод (дополнительно см. netsurf-all/netsurf/resources/FatMessages)
Source3: netsurf_Messages

BuildRequires: gtk2-devel libglade2-devel libjpeg-devel libpng-devel libmng-devel
BuildRequires: libxml2-devel zlib-devel
BuildRequires: libgtk+2-devel
BuildRequires: gcc make glibc-devel perl libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libssl-devel
BuildRequires: gperf flex
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

Summary(ru_RU.UTF-8): Легкий кроссплатформенный Web-браузер с поддержкой HTML и CSS.

%description
NetSurf is a lightweight cross-platform Web browser. It supports
the HTML4 and CSS2 standards and provides a small, fast,
and comprehensive Web browsing solution.

%description -l ru_RU.UTF-8
Легкий кроссплатформенный Web-браузер с хорошей поддержкой HTML4 и CSS2.

%prep
%setup -n %name-all-%version

mkdir -p netsurf/!NetSurf/Resources/ru
cp -a %SOURCE3 netsurf/!NetSurf/Resources/ru/Messages

# Скрипт запуска (начало)
cat > netsurf/netsurf.sh << EOF
#!/bin/sh
cd %_libdir/netsurf
./nsgtk2 \$1
EOF
chmod +x netsurf/netsurf.sh
# Скрипт запуска (конец)

mkdir -p netsurf/gtk/res/ru
pushd netsurf/gtk/res/ru
ln -s ../../../!NetSurf/Resources/ru/Messages Messages
popd

# По умолчанию пусть JavaScript будет включен
# netsurf/desktop/options.h NSOPTION_BOOL(enable_javascript, false)
sed -i 's/(enable_javascript, false)/(enable_javascript, true)/' netsurf/desktop/options.h

%build
PATH="`pwd`/inst-gtk/bin:$PATH"
echo $PATH
%make_build TARGET=gtk2 PREFIX=%_usr

%install
%makeinstall_std PREFIX=%_usr

install -pDm755 netsurf/nsgtk2 %buildroot%_libdir/netsurf/nsgtk2
install -pDm755 netsurf/netsurf.sh %buildroot%_bindir/netsurf

mkdir -p %buildroot%_libdir/netsurf/gtk
cp -r --dereference netsurf/gtk/res %buildroot%_libdir/netsurf/gtk
cp -r --dereference netsurf/!NetSurf %buildroot%_libdir/netsurf/

install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pDm644 %SOURCE2 %buildroot%_pixmapsdir/netsurf.png

echo $RPM_FIXUP_METHOD
export RPM_FIXUP_METHOD="binconfig pkgconfig libtool"

%files
%doc netsurf/README*
%_bindir/netsurf*
%dir %_datadir/%name
%_datadir/%name/*
%dir %_libdir/netsurf
%_libdir/netsurf/*
%_desktopdir/*
%_datadir/pixmaps/*

# TODO:
# - gtk2/gtk3/fb builds/subpackages?
# - update/submit translation

%changelog
* Wed May 27 2020 Michael Shigorin <mike@altlinux.org> 3.10-alt1
- 3.10 (gtk2 target)
  + dropped patches (merged upstream)
- spec cleanup

* Wed Dec 11 2019 Ivan A. Melnikov <iv@altlinux.org> 3.9-alt2
- add upstream patch to fix crash on file download (closes: #37596)
- drop BR: libmozjs, it is not used

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


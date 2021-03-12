%define oname PyQtWebEngine

%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
# Note: check QtWebEngine subst below
%define webenginever %(rpm -q --qf '%%{VERSION}' libqt5-webengine | sed -e 's|\\.|_|g')

Name: python3-module-%oname
Version: 5.13.1
Release: alt2

Summary: Python bindings for Qt WebEngine 5

License: GPL
Url: http://www.riverbankcomputing.co.uk/software/pyqtwebengine
Group: Development/Python

# Source0-url: https://www.riverbankcomputing.com/static/Downloads/PyQtWebEngine/%version/PyQtWebEngine_gpl-%version.tar.gz
Source0: %name-%version.tar

Requires: python3-module-PyQt5-sip = %sipver3

BuildRequires(pre): rpm-macros-qt5-webengine

ExclusiveArch: %qt5_qtwebengine_arches
BuildRequires(pre):python3-module-sip-devel
BuildRequires: python3-module-PyQt5-devel >= %version

BuildRequires(pre): rpm-build-python3 >= 0.1.9.2-alt1 python3-module-sip-devel
BuildRequires: gcc-c++ python3-devel python3-module-dbus

BuildRequires: pkgconfig(Qt5WebEngineCore)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)

# makes python3(QtWebEngineCore) only
#add_python3_path %python3_sitelibdir/PyQt5
# but we need
Provides: python3(PyQt5.QtWebEngine)
Provides: python3(PyQt5.QtWebEngineCore)
Provides: python3(PyQt5.QtWebEngineWidgets)

%description
Python bindings for the Qt WebEngine C++ class library.

%package devel
Summary: Sip files for %name
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-PyQt5-devel >= %version
Requires: %name = %EVR

%description devel
Python bindings for the Qt WebEngine C++ class library.

%prep
%setup
%__subst "s|QtWebEngine_5_12_4|QtWebEngine_5_12_4 QtWebEngine_%webenginever|" sip/*/*.sip

subst "s|/lib'$|/%_lib'|g" configure.py
find . -type f -name \*.pro -o -name '*.pro-in' -print0 |while read -r -d '' f; do
cat >> "$f" << 'E_O_F'
QMAKE_CFLAGS += %optflags %optflags_shared
QMAKE_CXXFLAGS += %optflags %optflags_shared
E_O_F
done

%build
export PATH="$PATH":%_qt5_bindir

python3 configure.py \
	--debug --verbose \
	-q %_qt5_qmake \
	-d %python3_sitelibdir/PyQt5 \
	--sip=%_bindir/sip3 \
	--sip-incdir=%__python3_includedir \
	--sipdir=%_datadir/sip3/PyQt5 \
	--pyqt-sipdir=%_datadir/sip3/PyQt5 \
	CFLAGS+="%optflags" CXXFLAGS+="%optflags"
# remove rpath
find ./ -name Makefile -print0 | while read -r -d '' i; do
	sed -i 's|-Wl,-rpath,|-I|g' "$i"
done
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

# There is a file in the package named .DS_Store or .DS_Store.gz,
# the file name used by Mac OS X to store folder attributes.
# Such files are generally useless in packages and were usually accidentally
# included by copying complete directories from the source tarball.
find "$RPM_BUILD_ROOT" \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete


%files
%python3_sitelibdir/PyQt5/QtWebEngine.*
%python3_sitelibdir/PyQt5/QtWebEngineCore.*
%python3_sitelibdir/PyQt5/QtWebEngineWidgets.*
%python3_sitelibdir/PyQtWebEngine-*

%files devel
%_datadir/sip3/PyQt5/QtWebEngine*
%_qt5_datadir/qsci/api/python/*

%changelog
* Thu Jan 23 2020 Vitaly Lipatov <lav@altlinux.ru> 5.13.1-alt2
- rebuild with QtWebEngine 5.12.6 (ALT bug 37911)

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 5.13.1-alt1
- Initial build for ALT Sisyphus


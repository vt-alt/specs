Name: kdevelop-pg-qt
Version: 2.2.1
Release: alt1
Obsoletes: kdevelop-unstable-pg-qt

Group: Development/Other
Summary: KDevelop parser generator
Url: http://techbase.kde.org/Development/KDevelop-PG-Qt_Introduction
License: GPLv2+

Source: v%version.tar.gz
Provides: kdevelop-pg-qt-devel = %EVR
Obsoletes: kdevelop-unstable-pg-qt-devel < %version

# Automatically added by buildreq on Sun Aug 12 2018
# optimized out: cmake cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libqt5-core libqt5-test libstdc++-devel python-base python-modules python3-base sh3
BuildRequires: extra-cmake-modules flex git-core libssl-devel python3 qt5-base-devel
BuildRequires(pre): rpm-build-kf5

%description
KDevelop-PG-Qt is a parser generator written in readable source-code and
generating readable source-code. Its syntax was inspirated by AntLR. It
implements the visitor-pattern and uses the Qt library. That is why it
is ideal to be used in Qt-/KDE-based applications like KDevelop.

%prep
%setup -n kdevelop-pg-qt-%version

%build
%K5build

%install
%K5install

%files
%doc README AUTHORS
%_bindir/kdev-pg-qt
%_includedir/kdevelop-pg-qt
%_libdir/cmake/*

%changelog
* Thu Sep 03 2020 Sergey V Turchin <zerg@altlinux.org> 2.2.1-alt1
- New version

* Mon Aug 13 2018 Fr. Br. George <george@altlinux.ru> 2.1.0-alt2
- Fix provides

* Sun Aug 12 2018 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Autobuild version bump to 2.1.0

* Sun Aug 12 2018 Automated package hasher <george@altlinux.org> 2.0.0-alt1
- New major version (using qt5)
- Join -devel package (see PACKAGING)

* Tue Apr 30 2013 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt4.git
- new post-1.0 git snapshot (97e140477e7247ec8c823cdc54500b5691d9a896)

* Thu Oct 18 2012 Alesey Morozov <morozov@altlinux.org> 1.0.0-alt3.git
- new post-1.0 git snapshot (2d403c527a697e91441d2ecb94a947d04c55bafb)

* Wed Mar 21 2012 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt2
- Dropped -unstable suffix because of the official release

* Sun Jan 29 2012 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt1
- 1.0.0 release

* Fri Jan 27 2012 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt0.1.git
- a new unstable git snapshot (f823d767a1799a14d32fe9152bba3bee35c15178,
  pre-1.0.0)

* Wed Dec 14 2011 Alexey Morozov <morozov@altlinux.org> 0.9.82-alt0.1.git
- a new unstable git snapshot (6570e01287e9eb45f7bdaab2b81b1d7082d2558a,
  0.9.82 aka 1.0 Beta)
- package gained -unstable suffix to peacefully co-exist with the
  version needed for "stable" versions of the KDevelop modules

* Thu Jun 16 2011 Alexey Morozov <morozov@altlinux.org> 0.9.5-alt2.git
- post 0.9.5 git snapshot (ba59270f286c50569de5bbe8eb0261d2280b6913)

* Wed Apr 27 2011 Alexey Morozov <morozov@altlinux.org> 0.9.5-alt1.git
- post 0.9.5 git snapshot (16d67d1082f1f2d69491c4e22131df89a39f32f9)
- buildreqs adjusted

* Wed Mar 16 2011 Alexey Morozov <morozov@altlinux.org> 0.9.0-alt2.git
- build git snapshot (7dff783443)

* Tue Oct 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- initial build


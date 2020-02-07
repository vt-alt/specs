%define rname kde-dev-scripts

%add_findreq_skiplist %_K5bin/kdedoc
%add_findreq_skiplist %_K5bin/package_crystalsvg
%add_findreq_skiplist %_K5bin/kde-systemsettings-tree.py

Name: kde5-dev-scripts
Version: 19.12.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Various development scripts
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

BuildArch: noarch

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Oct 01 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl kf5-kdoctools-devel less libgpg-error libqt5-core libstdc++-devel perl-Encode perl-HTTP-Date perl-HTTP-Message perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage perl-Term-ANSIColor perl-URI perl-XML-Parser perl-XML-RegExp perl-libwww python-base python3 python3-base rpm-build-gir termutils xml-common xml-utils
#BuildRequires: cvs extra-cmake-modules gcc-c++ git-core graphviz kde5-konqueror kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static perl-XML-DOM perl-podlators python-module-google qt5-base-devel rpm-build-python3 ruby ruby-stdlibs subversion
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: graphviz perl-XML-DOM perl-podlators rpm-build-python rpm-build-python3 ruby ruby-stdlibs
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data uncrustify

# fix shebang
sed -i \
  -e "s|^#![[:space:]]*/usr/bin/env python$|#!%{__python3}|g" \
  %buildroot/%_K5bin/*

# fix scripts for strong /usr/lib/rpm/find-requires
pushd %buildroot/%_K5bin
for f in `(file ./* | grep bash; file ./* | grep shell) | awk -F: '{print $1}' | xargs grep -l ^=head`
do
    mv "$f" "$f.tmp"
    awk 'BEGIN{found=0;} /^=head/ {if (found==0){print "cat <<\\__EOF__";found=1;};} {print} END{if (found!=0) print "__EOF__";}' <"$f.tmp" >"$f"
    rm -f "$f.tmp"
    chmod a+x $f
done
popd


%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING* README
%_bindir/*
%_K5bin/*
%_K5data/*/

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt2
- build with python3 only

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Fri Jun 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Thu May 04 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Mon Dec 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- initial build

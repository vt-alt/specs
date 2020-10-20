%define _unpackaged_files_terminate_build 1

Name: freecol
Version: 0.11.6
Release: alt2
Summary: FreeCol is opensource Colonization clone.
Url: http://freecol.org
Group: Games/Strategy
License: GPL-2.0+

BuildArch: noarch

Source: %name-%version.tar
Source1: %name.desktop
Source2: %name.xpm

Patch1: %name-%version-fedora-source-encoding.patch
Patch2: CVE-2018-1000825.patch

BuildRequires: rpm-build-java
BuildRequires: ant ant-nodeps
BuildRequires: subversion
BuildRequires: java-devel junit

Requires: java

%description
FreeCol is a turn-based strategy game based on the old game Colonization and similar to Civilization. 
The objective of the game is to create an independent nation.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
export CLASSPATH=$(build-classpath junit)
%ant

%install
mkdir -p %buildroot%_bindir \
%buildroot%_gamesdatadir/%name/jars/ \
%buildroot%_gamesdatadir/%name/data/{audio,fonts,images,maps,strings} \
%buildroot%_gamesdatadir/%name/data/audio/sfx \
%buildroot%_gamesdatadir/%name/data/images/{bonus,colonies,forest,good,indians,misc,monarch,order-buttons,river,terrain,ui,units} \
%buildroot%_gamesdatadir/%name/data/images/order-buttons/{order-buttons00,order-buttons01,order-buttons02,order-buttons03} \
%buildroot%_gamesdatadir/%name/data/images/terrain/{terrain00,terrain01,terrain02,terrain03,terrain04,terrain05,terrain06,terrain07,terrain08,terrain09,terrain10,terrain11,terrain12,terrain13,terrain14,terrain15} \
%buildroot%_desktopdir \
%buildroot%_niconsdir

install -p FreeCol.jar %buildroot%_gamesdatadir/%name/FreeCol.jar
install -p jars/*.jar %buildroot%_gamesdatadir/%name/jars/
cp -pr data/ %buildroot%_gamesdatadir/%name/

cat > %buildroot%_bindir/%name <<EOF
pushd %_gamesdatadir/%name >/dev/null 2>&1
/usr/bin/java -Xmx256M -jar %_gamesdatadir/%name/FreeCol.jar $1 $2 $3 $4 $5 $6 $7 $8 $9
popd >/dev/null 2>&1
EOF

chmod +x %buildroot%_bindir/%name
install -p %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -p %SOURCE2 %buildroot%_niconsdir/%name.xpm

%files
%_bindir/%name
%_gamesdatadir/%{name}*
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm

%changelog
* Mon Oct 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.6-alt2
- Applied security fix from Debian (Fixes: CVE-2018-1000825).
- Updated license tag.

* Tue Nov 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.6-alt1
- Updated to upstream version 0.11.6.

* Mon Sep 05 2011 Mikhail Pokidko <pma@altlinux.org> 0.10.2-alt1
- v0.10.2 (stable)

* Wed Jul 27 2011 Mikhail Pokidko <pma@altlinux.org> 0.10.1-alt1
- v0.10.1

* Tue Jun 14 2011 Mikhail Pokidko <pma@altlinux.org> 0.10.0-alt1
- v0.10.0

* Fri Oct 15 2010 Mikhail Pokidko <pma@altlinux.org> 0.9.5-alt1
- 0.9.5. Another maintenance release.

* Mon Aug 09 2010 Mikhail Pokidko <pma@altlinux.org> 0.9.4-alt1
- 0.9.4. Bugfixes release.

* Tue Jun 22 2010 Mikhail Pokidko <pma@altlinux.org> 0.9.3-alt1
- v 0.9.3

* Wed Mar 17 2010 Mikhail Pokidko <pma@altlinux.org> 0.9.2-alt1
- 0.9.2 is a bug/feature-fix release.

* Wed Mar 03 2010 Mikhail Pokidko <pma@altlinux.org> 0.9.1-alt1
- 0.9.1 is a bug fix release.

* Wed Jan 13 2010 Mikhail Pokidko <pma@altlinux.org> 0.9.0-alt1
- 0.9.0 + repocop fixes.

* Tue Jun 17 2008 Mikhail Pokidko <pma@altlinux.org> 0.7.4-alt1
- Bugfix release. Prepairing for 0.8.0.

* Thu Apr 03 2008 Mikhail Pokidko <pma@altlinux.org> 0.7.2-alt2
- repocop fix

* Fri Sep 21 2007 Mikhail Pokidko <pma@altlinux.org> 0.7.2-alt1
- Version up
 + Windowed mode added.

* Mon Sep 03 2007 Mikhail Pokidko <pma@altlinux.org> 0.7.1-alt1
- Version up

* Fri Aug 03 2007 Mikhail Pokidko <pma@altlinux.org> 0.7.0-alt1.cvs20070803
- Initial build.
  CVS version with bug fixes

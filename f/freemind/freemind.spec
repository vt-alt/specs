#TODO: check doc, check with removed batik
%define set_system_jar() \
	for p in %* ; do \
		for i in $p $(echo $p/*.jar); do \
			test -f "$i" || continue \
			build-classpath $(basename "$i") 2>/dev/null || continue \
			ln -sf $(build-classpath $(basename "$i")) "$i" \
		done \
	done

%define set_system_namejar() \
	test -f "%2" \
	build-classpath %1 \
	ln -sf $(build-classpath %1) "%2"

# TODO: plugins/svg
# wait for xstream
Name: freemind
Version: 1.0.1
Release: alt2

Summary: A Program for creating and viewing Mindmaps

Group: Text tools
License: GPL
Url: http://freemind.sourceforge.net/wiki/index.php/Main_Page

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://prdownloads.sf.net/%name/freemind-src-0.9.0_Beta_16_icon_butterfly.tar.bz2
Source: http://prdownloads.sf.net/freemind/freemind-src-%version.tar

Source1: %name.desktop
Source2: %name.xml
Requires: java >= 1.5.0

BuildRequires: ant gnu-regexp xerces-j2
#BuildRequires: batik batik-squiggle gnu-regexp groovy jtidy rhino

BuildRequires: java-devel-default

BuildRequires: rpm-build-java

BuildArch: noarch

%description
FreeMind is a premier free mind-mapping software written in Java.

%prep
%setup -n %name
chmod a+x check_for_duplicate_resources.sh
subst "s|�|oe|g" freemind/main/XHTMLWriter.java freemind/main/FixedHTMLWriter.java
# for build
#set_system_jar lib/ lib/jibx/ lib/SimplyHTML/ plugins/svg/ plugins/latex/ plugins/help/ 
#set_system_namejar xerces-j2 plugins/svg/xerces_2_5_0.jar
#set_system_namejar groovy plugins/script/groovy-all-1.5.6.jar

%build
JAVA_HOME=%java_home
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8
sed -i s,./doc/freemind.mm,%_docdir/freemind.mm, freemind.properties
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dfile.encoding=UTF8 dist browser

%install
mkdir -p %buildroot/{%_datadir,%_bindir}
cp -a ../bin/dist %buildroot%_datadir/%name

rm %buildroot%_datadir/%name/{FreeMind.exe,freemind.bat}
rm %buildroot%_datadir/%name/license
chmod 755 %buildroot%_datadir/%name/%name.sh
ln -s ../share/%name/%name.sh %buildroot%_bindir/%name

# for packing
#set_system_jar %buildroot%_datadir/%name/{lib,lib/jibx,lib/SimplyHTML,plugins/svg,plugins/latex,plugins/help}
#set_system_namejar xerces-j2 %buildroot%_datadir/%name/plugins/svg/xerces_2_5_0.jar
#set_system_namejar groovy %buildroot%_datadir/%name/plugins/script/groovy-all-1.5.6.jar
#rm -f %buildroot%_datadir/%name/plugins/svg/batik-*.jar

install -D -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D -m644 images/FreeMindWindowIcon.png %buildroot%_pixmapsdir/%name.png

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/*.png

%changelog
* Mon Oct 28 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- fix desktop file (ALT bug #36809)

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1.1
- NMU: corrected java BuildRequires

* Sat Jan 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Wed Jul 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt5.2
- NMU: dropped dependencies, use pre-bundled jars

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0_9_0-alt5.1
- NMU: dropped incidental depandency on groovy10
- added -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0_9_0-alt5
- NMU: 0.9.0 release; fixed build, cleaned up desktop

* Thu Oct 08 2009 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt4.rc4
- new version (0_9_0 RC4)
- add rpm-build-java buildreq (bug #21825)

* Sun Jan 25 2009 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt4.rc1
- build without some internal jars

* Wed Jan 14 2009 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt3.rc1
- set noarch, update buildreqs
- build with system groovy-all and commons-lang (fix bug #18456)
- move doc to right place

* Fri Jan 02 2009 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt2.rc1
- new version (0_9_0 RC1)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt1.18b1
- new version (0_9_0 beta 18)

* Mon Apr 14 2008 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt1.16b1
- fix build process (use ant)
- add desktop file (thanks, PLD)
- install icon file
- add update/clean menus

* Thu Mar 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt0.16b1
- new version (0_9_0)

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt0.15b1
- new version (0_9_0 beta15)

* Sat Mar 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt0.10b1
- new version (0_9_0-b10-aki-b1)
- set requires to java >= 1.5.0

* Thu Mar 22 2007 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt0.2b12
- new version, add requires (fix bug #10927)

* Sun Dec 31 2006 Vitaly Lipatov <lav@altlinux.ru> 0_9_0-alt0.1cvs20061229
- beta version (0_9_0)

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0_8_0-alt0.1
- initial build for ALT Linux Sisyphus

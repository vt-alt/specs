%define sun_desktop_version 1.6.0.26-alt4
%define origin default
%def_enable desktop

Name: java-common
Version: 1.6.0
Release: alt1

Summary: Common files for Java runtimes
Group: System/Base
License: GPL
Packager: Igor Vlasenko <viy@altlinux.org>
Requires: jpackage-utils

Source: mime-packages.tar

# merged mime data
%if_enabled desktop
#Provides: java-sun-desktop = %sun_desktop_version
Obsoletes: java-sun-desktop < %sun_desktop_version
Conflicts: java-sun-desktop < %sun_desktop_version
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-java

%description
This package contains the Java profile scripts 
used to select a Java runtime environment available 
in the system to execute Java applications.

%prep
tar xf %{S:0}

%install

# Install profile scripts
# note: they are not needed in jpackage environment
mkdir -p %buildroot%{_sysconfdir}/profile.d/
cat >%buildroot%{_sysconfdir}/profile.d/javahome.sh <<EOF
if test -e %{_prefix}/lib/jvm/java; then
    JAVA_HOME=%{_prefix}/lib/jvm/java
    export JAVA_HOME
elif test -e %{_prefix}/lib/jvm/jre; then
    JAVA_HOME=%{_prefix}/lib/jvm/jre
    export JAVA_HOME
fi
EOF
chmod 755 %buildroot%{_sysconfdir}/profile.d/javahome.sh
cat >%buildroot%{_sysconfdir}/profile.d/javahome.csh <<EOF
if ( -e %{_prefix}/lib/jvm/java ) then
setenv JAVA_HOME %{_prefix}/lib/jvm/java
else if ( -e %{_prefix}/lib/jvm/jre ) then
setenv JAVA_HOME %{_prefix}/lib/jvm/jre
endif
EOF
chmod 755 %buildroot%{_sysconfdir}/profile.d/javahome.csh

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs


%if_enabled desktop
install -d -m 755 $RPM_BUILD_ROOT{%_desktopdir,%_datadir/mime/packages/}
mv mime-packages/* $RPM_BUILD_ROOT%{_datadir}/mime/packages/
cat > %buildroot%_datadir/applications/%origin-java.desktop <<'EOF'
[Desktop Entry]
Name=Java
Comment=Java Virtual Machine
Exec=java -jar %f
Icon=java
Terminal=false
Type=Application
NoDisplay=true
Categories=X-ALTLinux-Java;
MimeType=application/x-java-archive;application/x-jar;
InitialPreference=7
EOF

cat > %buildroot%_datadir/applications/%origin-javaws.desktop <<'EOF'
[Desktop Entry]
Name=Java Web Start (system default)
Comment= Java Application Launcher
Exec=javaws %u
Icon=javaws
Terminal=false
Type=Application
NoDisplay=true
Categories=Settings;Java;X-ALTLinux-Java;
MimeType=application/x-java-jnlp-file;
EOF
%endif

%files
%{_sysconfdir}/profile.d/javahome.*sh
#%dir %{_sysconfdir}/.java/
#%dir %{_sysconfdir}/.java/.systemPrefs
%if_enabled desktop
%{_datadir}/mime/packages/*.xml
%_desktopdir/%{origin}-java.desktop
%_desktopdir/%{origin}-javaws.desktop
%endif

%changelog
* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- dropped /etc/.java/.systemPrefs
- fixed javahome.sh (closes: #36987)

* Wed Feb 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1
- merged desktop support (mime types and mime handlers).

* Mon Feb 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2
- added /etc/.java/.systemPrefs

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- added java-sun-desktop as dependency due to mime types

* Sun Dec 21 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.18-alt1
- spec cleanup

* Tue Dec 09 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.17-alt1
- removed old /usr/bin/java crutch

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.16-alt1
- removed /usr/share/java-common
- TODO: remove /usr/bin/java crutch

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.15-alt1
- reduced /usr/bin/java priority to 200
- simplified /usr/bin/java stub

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1
- restored /usr/bin/java max priority

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt1
- fixes in /usr/bin/java
  TODO: remove /usr/bin/java crutch (required by jdkgcj).

* Sun Nov 23 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.12-alt1
- removed obsolete post/un alternatives calls

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.11-alt1
- removed obsolete java functions

* Thu Oct 30 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.10-alt1
- added %{_sbindir}/update-jre-environment for future use

* Tue Sep 30 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.9-alt1
- java.sh now uses jpackage functions

* Sat Sep 13 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.8-alt2
- really fixed #16868

* Mon Aug 25 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.8-alt1
- fixed #16868

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.7-alt1
- removed filesystem intersections with jpackage-utils

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 1.3.6-alt4
- removed LIBXCB_ALLOW_SLOPPY_LOCK (no more needed)

* Mon Oct 15 2007 Igor Vlasenko <viy@altlinux.ru> 1.3.6-alt3
- fixed test in libxcb workaround

* Tue Sep 25 2007 Igor Vlasenko <viy@altlinux.ru> 1.3.6-alt2
- fixed syntax error

* Mon Sep 24 2007 Igor Vlasenko <viy@altlinux.ru> 1.3.6-alt1
- added JRE_HOME if JDK is not found
- added JVM search in jre

* Fri May 11 2007 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt1
- added LIBXCB_ALLOW_SLOPPY_LOCK=1 to hack around new libX11 w/xcb

* Mon Feb 19 2007 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1
- fixed triggerpostun -- java-common < 1.3 
  ('relative' is for build environment only)

* Sun Feb 18 2007 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1
- new profile scripts for JAVA_HOME (see #9766)
- %_bindir/java is moved to %_datadir/%name/java.sh
- symlink %_bindir/java is provided using alternatives
- raw symlink %_bindir/java is provided to fix upgrade

* Fri Feb 16 2007 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1
- added basic JPackage support 
  (imtermediate version to allow smooth migration)

* Sun Oct 23 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.1-alt1
- Support 64-bit architectures by searching in /usr/lib64 as well (bug #8315)

* Sat Jun 25 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3-alt1
- Incorporated jdkgcj fallback into the FindJVM function
  which also sets JAVA_BIN global variable
- Moved java-functions under /usr/share to be truly arch-independent

* Mon Dec 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2-alt1
- Added FindJVM function to java-functions

* Sun Mar 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1-alt1
- Provided fallback to jdkgcj in case no full-scale JDK is found
- Added a feature to the AddToClasspath function: non-absolute path names
  get prefixed with /usr/share/java

* Sat Oct 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt3
- Added the /usr/share/javadoc directory

* Mon Oct 06 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt2
- Added /usr/bin/java to Provides:

* Mon Nov 18 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt1
- Initial release


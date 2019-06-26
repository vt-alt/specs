Group: Networking/WWW
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install /usr/bin/rustc /usr/bin/xsltproc gcc-c++ rpm-build-java zip
# END SourceDeps(oneline)
%def_enable javaws
%def_enable moz_plugin
BuildRequires(pre): browser-plugins-npapi-devel
BuildRequires: bc

%set_compress_method none
%define oldname icedtea-web
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#can rust have debuginfo? Verify and fix! Likely issue in Makefile of itw.
%global debug_package %{nil}

# Version of java
%define javaver 1.8.0

# Alternatives priority
%define priority 18000
# jnlp prorocol gnome registry keys
%define gurlhandler   /desktop/gnome/url-handlers
%define jnlphandler   %{gurlhandler}/jnlp
%define jnlpshandler  %{gurlhandler}/jnlps

%define javadir     %{_jvmdir}/java-%{javaver}-openjdk
%define jredir      %{_jvmdir}/jre-%{javaver}-openjdk

%define binsuffix      .itweb

%define preffered_java  java-%{javaver}-openjdk

Name:		mozilla-plugin-java-1.8.0-openjdk
Version:	1.8
Release:	alt1_2jpp8
Summary:	Additional Java components for OpenJDK - Java browser plug-in and Web Start implementation

License:    LGPLv2+ and GPLv2 with exceptions
URL:        http://icedtea.classpath.org/wiki/IcedTea-Web
Source0:    http://icedtea.classpath.org/download/source/%{oldname}-%{version}.tar.gz
Patch1:     patchOutDunce.patch

BuildRequires:  javapackages-tools
#for deprecated add_maven_depmap, see https://www.spinics.net/lists/fedora-devel/msg233211.html
BuildRequires:  javapackages-local
BuildRequires:  %{preffered_java}-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:	rust-cargo
BuildRequires:  junit
BuildRequires:  hamcrest
BuildRequires:  libappstream-glib
# new in 1.5 to have  clean up for malformed XMLs
BuildRequires:  tagsoup

# For functionality and the OpenJDK dirs
Requires:      %{preffered_java}
Requires:      javapackages-tools
#maven fragments
Requires(post):      javapackages-tools
Requires(postun):      javapackages-tools

# When itw builds against it, it have to be also in runtime
Requires:      tagsoup

# Post requires alternatives to install tool alternatives.
# jnlp protocols support
Requires(post):   GConf libGConf
# Postun requires alternatives to uninstall tool alternatives.
# jnlp protocols support
Requires(postun):   GConf libGConf

# Standard JPackage plugin provides.
Provides: javaws = 1:%{javaver}
Provides:   %{preffered_java}-javaws = 1:%{version}
Source44: import.info

%define altname java-%{javaver}-openjdk
%define origin openjdk
%define label -itweb
%define javaws_ver      %{javaver}
%define sdkdir          java-%{javaver}-openjdk-%{javaver}.0.%{_arch}
# TODO: move here
#define mozilla_java_plugin_so %{_prefix}/lib/%{sdkdir}/IcedTeaPlugin.so
%define mozilla_java_plugin_so %{_libdir}/IcedTeaPlugin.so

# hack not to forget to rebuild this pkg with every new openjdk
# JAVACANDIDATE in alternatives below is release-dependent :(
%define _alt_javacandidate %(head -2 /etc/alternatives/packages.d/java-%{javaver}-openjdk-java-headless| tail -1 | awk '{print $3}')
%if "%{_alt_javacandidate}" != ""
Requires: %{_alt_javacandidate}
%endif
Provides: icedtea-web = %version-%release
Obsoletes: mozilla-plugin-java-1.7.0-openjdk < 1.5
Patch33: translation-desktop-files.patch
Source45: Messages_ru.properties

#BuildRequires: java-%javaver-%origin-devel

%description
The IcedTea-Web project provides a Java web browser plugin, an implementation
of Java Web Start (originally based on the Netx project) and a settings tool to
manage deployment settings for the aforementioned plugin and Web Start
implementations. 

%if_enabled javaws
%package -n %altname-javaws
Summary: Java Web Start
Group: Networking/Other
Requires: %name = %version-%release
Requires(post,preun): alternatives
# --- jpackage compatibility stuff starts here ---
Provides:       javaws = %{javaws_ver}
Obsoletes:      javaws-menu
# --- jpackage compatibility stuff ends here ---
# due to the build specific
Requires: mozilla-plugin-%altname = %version-%release

%description -n %altname-javaws
Java Web Start is a deployment solution for Java-technology-based
applications. It is the plumbing between the computer and the Internet
that allows the user to launch and manage applications right off the
Web. Java Web Start provides easy, one-click activation of
applications, and guarantees that you are always running the latest
version of the application, eliminating complicated installation or
upgrade procedures.

This package provides the Java Web Start installation that is bundled
with %{name} J2SE Runtime Environment.
%endif # enabled javaws

%package javadoc
Group: Development/Java
Summary:    API documentation for IcedTea-Web
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description javadoc
This package contains Javadocs for the IcedTea-Web project.


%package devel
Group: Development/Java
Summary:    pure sources for debugging IcedTea-Web
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description devel
This package contains ziped sources of the IcedTea-Web project.

%prep
%setup -n %{oldname}-%{version} -q
%patch1 -p1
%patch33 -p2

cp -f %SOURCE45 netx/net/sourceforge/jnlp/resources/Messages_ru.properties
sed -i 's/en_US.UTF-8/en_US.UTF-8 ru_RU.UTF-8/' Makefile.am

# test fails when /tmp files go missing :( aarch64 known mystery bug
%ifarch aarch64
sed -i 's,\$(CARGO) test,echo test,' Makefile.am
%endif

%build
autoreconf -vfi
CXXFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS" \
%configure \
    --with-pkgversion=ALTLinux-%{release}-%{_arch} \
    --docdir=%{_datadir}/javadoc/%{oldname} \
    --with-jdk-home=%{javadir} \
    --with-jre-home=%{jredir} \
    --libdir=%{_libdir} \
    --program-suffix=%{binsuffix} \
    --disable-native-plugin \
    --with-itw-libs=DISTRIBUTION \
    --with-modularjdk-file=%{_sysconfdir}/java/%{oldname}    \
    --prefix=%{_prefix}
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT

# icedteaweb-completion is currently not handled by make nor make install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
mv completion/policyeditor.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
mv completion/javaws.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
mv completion/itweb-settings.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

# Move javaws man page to a more specific name
mv $RPM_BUILD_ROOT/%{_mandir}/man1/javaws.1 $RPM_BUILD_ROOT/%{_mandir}/man1/javaws.itweb.1

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications javaws.desktop
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications itweb-settings.desktop
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications policyeditor.desktop

# install MetaInfo file for firefox
DESTDIR=%{buildroot} appstream-util install metadata/%{oldname}.metainfo.xml
# install MetaInfo file for javaws
DESTDIR=%{buildroot} appstream-util install metadata/%{oldname}-javaws.appdata.xml

# maven fragments generation
mkdir -p $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s ../%{oldname}/javaws.jar %{oldname}.jar
ln -s ../%{oldname}/plugin.jar %{oldname}-plugin.jar
popd
mkdir -p $RPM_BUILD_ROOT/%{_mavenpomdir}
cp  metadata/%{oldname}.pom  $RPM_BUILD_ROOT/%{_mavenpomdir}/%{oldname}.pom
cp metadata/%{oldname}-plugin.pom  $RPM_BUILD_ROOT/%{_mavenpomdir}/%{oldname}-plugin.pom

%add_maven_depmap %{oldname}.pom %{oldname}.jar
%add_maven_depmap %{oldname}-plugin.pom %{oldname}-plugin.jar

cp  netx.build/lib/src.zip  $RPM_BUILD_ROOT%{_datadir}/%{oldname}/javaws.src.zip
cp liveconnect/lib/src.zip  $RPM_BUILD_ROOT%{_datadir}/%{oldname}/plugin.src.zip

%find_lang %{oldname} --all-name --with-man
# multiple -f flags in %files for <main>: merging -f %{oldname}.lang into -f .mfiles
cat %{oldname}.lang >> .mfiles

install -d -m 755 %buildroot/etc/icedtea-web
cat > %buildroot/etc/icedtea-web/javaws.policy << EOF
// Based on Oracle JDK policy file
grant codeBase "file:/usr/share/icedtea-web/netx.jar" {
    permission java.security.AllPermission;
};
EOF
sed -e 's,^JAVA_ARGS=,JAVA_ARGS="-Djava.security.policy=/etc/icedtea-web/javaws.policy",' \
%buildroot%_bindir/javaws.itweb


##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################
%if_enabled moz_plugin
# ControlPanel freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_desktopdir}/%{altname}-control-panel.desktop << EOF
[Desktop Entry]
Name=Java %javaver Plugin Control Panel
Comment=Java Control Panel
Exec=itweb-settings.itweb
Icon=java-%{javaver}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

%if_enabled javaws
# javaws freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_desktopdir}/%{altname}-javaws.desktop << EOF
[Desktop Entry]
Name=Java Web Start (%{javaver})
Comment=Java Application Launcher
MimeType=application/x-java-jnlp-file;
Exec=javaws.itweb %%u
Icon=java-%{javaver}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif


JAVACANDIDATE=`head -2 /etc/alternatives/packages.d/java-%{javaver}-openjdk-java-headless| tail -1 | awk '{print $3}'`
[ -n "JAVACANDIDATE" ] || exit 1

install -d %buildroot%_altdir
%if_enabled moz_plugin
# Mozilla plugin alternative
%__cat <<EOF >%buildroot%_altdir/%altname-plugin
%browser_plugins_path/libjavaplugin_oji.so	%mozilla_java_plugin_so	%priority
EOF
%__cat <<EOF >>%buildroot%_altdir/%altname-plugin
%{_bindir}/ControlPanel	%_bindir/itweb-settings.itweb	$JAVACANDIDATE
%{_bindir}/jcontrol	%_bindir/itweb-settings.itweb	$JAVACANDIDATE
EOF
%endif

%if_enabled javaws
# Java Web Start alternative
cat <<EOF >%buildroot%_altdir/%altname-javaws
%_bindir/javaws	%_bindir/javaws.itweb	$JAVACANDIDATE
%_man1dir/javaws.1.gz	%_man1dir/javaws%label.1.gz	$JAVACANDIDATE
EOF
# ----- JPackage compatibility alternatives ------
%__cat <<EOF >>%buildroot%_altdir/%altname-javaws
%{_datadir}/javaws	%_bindir/javaws.itweb	$JAVACANDIDATE
EOF
# ----- end: JPackage compatibility alternatives ------
%endif	# enabled javaws

# hack (see #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################

%check
make check
appstream-util validate $RPM_BUILD_ROOT/%{_datadir}/appdata/*.xml || :

%files -f .mfiles 
%{_sysconfdir}/bash_completion.d/*
%config(noreplace) %{_sysconfdir}/java/%{oldname}/itw-modularjdk.args
%{_prefix}/bin/*
%{_datadir}/applications/*
%dir %{_datadir}/%{oldname}
%{_datadir}/%{oldname}/*.jar
%{_datadir}/%{oldname}/*.png
%{_datadir}/man/man1/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.xml
%doc NEWS README
%doc --no-dereference COPYING
# alt linux specific
%_altdir/%altname-plugin
%{_desktopdir}/%{altname}-control-panel.desktop
# replace by local variants
%exclude %{_desktopdir}/javaws.desktop
%exclude %{_desktopdir}/itweb-settings.desktop
# separate javaws
%exclude %{_desktopdir}/%{altname}-javaws.desktop
%exclude %{_datadir}/pixmaps/javaws.png
%exclude %{_man1dir}/javaws.itweb.1.gz
%exclude %_bindir/javaws.itweb
# security policy
%dir /etc/icedtea-web
/etc/icedtea-web/javaws.policy

%files javadoc
%{_datadir}/javadoc/%{oldname}
%doc --no-dereference COPYING

%files devel
%{_datadir}/%{oldname}/*.zip
%doc --no-dereference COPYING

%files -n %altname-javaws
#
%_altdir/%altname-javaws
%{_desktopdir}/%{altname}-javaws.desktop
%{_datadir}/pixmaps/javaws.png
%{_man1dir}/javaws.itweb.1.gz
%_bindir/javaws.itweb


%changelog
* Tue Jun 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2jpp8
- restored Ivan Razzhivin patches

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_1jpp8
- new version

* Wed Jan 09 2019 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt5_6jpp8
- fix russian translation

* Fri Dec 07 2018 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt4_6jpp8
- add russian translation to desktop files

* Thu Nov 15 2018 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt3_6jpp8
- add russian translation

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2_6jpp8
- fixed alternatives

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_6jpp8
- fixed icons in desktop files

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_5jpp8
- new version

* Sat Apr 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt3_1jpp8
- removed fedora-based alternative (closes: #32043)

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_1jpp8
- fixed requires

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1jpp8
- new version


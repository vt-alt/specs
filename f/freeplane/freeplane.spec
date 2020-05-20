# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%define product_distribution Mageia
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# This two are not defined in Mageia
%define _desktopdir	%{_datadir}/applications
%define _iconsscaldir	%{_datadir}/icons/hicolor/scalable/apps
# include jar-files not yet available as separate packages for Mageia
%define __fp_github	https://github.com/freeplane/freeplane/tree/master

Name:		freeplane
Version:	1.3.15
Release:	alt1_7jpp8
Summary:	Mind mapping, knowledge management and project management tool
Group:		Office
License:	GPLv2+
#https://github.com/htgoebel/freeplane-mageia
URL:		http://freeplane.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}%%20stable/%{name}_srcpure-%{version}.tar.gz
Source2:	freeplane.desktop
Source3:	freeplane.sh
Source10:	README.Mageia
# man-page from http://anonscm.debian.org/gitweb/?p=pkg-java/freeplane.git;a=blob_plain;f=debian/freeplane.1.xml;hb=HEAD
Source80:	freeplane.1.xml
# as of freeplane 1.3.5, knopflerfish 2.3.3 is used (see framework.jar:release)
Source90:	%{__fp_github}/freeplane_framework/lib/knopflerfish/framework.jar
Source91:	%{__fp_github}/freeplane/lib/idw-gpl.jar
Source92:	%{__fp_github}/freeplane_plugin_script/lib/jsyntaxpane.jar
# 3rd-party .jars still kept in the package:
# freeplane: knopflerfish, idw-gpl
# freeplane_plugin_script: jsyntaxpane (see Source.. above)
Patch15:	15_libraries_manifest.patch
# port to JMapViewer >= 1.11
Patch16:	16_port_to_JMapViewer1.11.patch
# remove automatic updates
Patch70:	70_skip_bugreport.patch
Patch80:	80_no_update_check.patch
Patch81:	81_remove_update_and_bugreport_prefs.patch
Patch82:	82_remove_browser_command_prefs_for_other_oses.patch
Patch93:	93_jgoodies1.6.patch
Patch95:	95_run_jflex.patch
Patch97:	97_fix_CVE-2018-1000069.patch

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	jflex
BuildRequires:	antlr-tool >= 2.7.7
BuildRequires:	apache-commons-cli >= 1.2
BuildRequires:	apache-commons-codec >= 1.7
BuildRequires:	apache-commons-io >= 2.4
BuildRequires:	apache-commons-lang >= 2.0
BuildRequires:	batik
BuildRequires:	felix-osgi-core
BuildRequires:	fop
BuildRequires:	gnu-regexp >= 1.1.4
BuildRequires:	groovy18 >= 1.8
BuildRequires:	jgoodies-common >= 1.6
BuildRequires:	jgoodies-forms >= 1.2
BuildRequires:	jlatexmath >= 1.0.2
BuildRequires:	jmapviewer >= 1.03
#BuildRequires:	knopflerfish
BuildRequires:	objectweb-asm3 >= 3.3.1
BuildRequires:	rhino
BuildRequires:	SimplyHTML >= 0.16.7
BuildRequires:	xerces-j2
BuildRequires:	xml-commons-apis >= 1.4

# for building the man-page
BuildRequires:	xsltproc
BuildRequires:	docbook-xsl

Requires:	javapackages-tools
# Freeplane uses xdg-open for opening URLs
Requires:	xdg-utils
Requires:	antlr-tool >= 2.7.7
Requires:	apache-commons-cli >= 1.2
Requires:	apache-commons-codec >= 1.7
Requires:	apache-commons-io >= 2.4
Requires:	apache-commons-lang >= 2.0
Requires:	batik
Requires:	felix-osgi-core
Requires:	fop
Requires:	gnu-regexp >= 1.1.4
Requires:	groovy18 >= 1.8
Requires:	jgoodies-common >= 1.6
Requires:	jgoodies-forms >= 1.2
Requires:	jlatexmath >= 1.0.2
Requires:	jmapviewer >= 1.03
#Requires:	knopflerfish
Requires:	objectweb-asm3 >= 3.3.1
Requires:	rhino
Requires:	SimplyHTML >= 0.16.7
Requires:	xerces-j2
Requires:	xml-commons-apis >= 1.4
Source44: import.info

%description
Freeplane is a premier free and open source software application that
supports thinking, sharing information and getting things done at
work, in school and at home. The core of the software is tools for
mind mapping (also known as concept mapping or information mapping)
and using mapped information.

Freeplane is a Freemind fork. FreePlane fully supports the FreeMind
file format, but adds features and tags not supported by FreeMind
which are ignored on loading.

New features of Freeplane include:
* Export to PNG, JPEG, SVG (in addition to HTML / XHTML and PDF)
* Find / Replace in all open maps
* Paste HTML as node structure
* Outline mode
* Scripting via Groovy
* Spell Checker

%prep
%setup -q

# Clean up prebuild artefacts
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.zip' -delete

# Put the jars to be included at the place where they are expected.
# This they will be put into the freeplane_bin-${version}.zip.
# - knopflerfish
mkdir -p freeplane_framework/lib/knopflerfish
cp -a %{SOURCE90} freeplane_framework/lib/knopflerfish
# - infonode docking window (idw-gpl)
mkdir -p freeplane/lib/
cp -a %{SOURCE91} freeplane/lib/
# - jsyntaxpane
mkdir -p freeplane_plugin_script/lib/
cp -a %{SOURCE92} freeplane_plugin_script/lib/

%patch15 -p1
#%%patch16 -p1
%patch70 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch93 -p1
%patch95 -p1
%patch97 -p1

# set default lookandfeel to be gtk.
sed -i 's/lookandfeel = default/lookandfeel = com.sun.java.swing.plaf.gtk.GTKLookAndFeel/' \
	freeplane/viewer-resources/freeplane.properties

%build
CLASSPATH=
for cp in \
    avalon-framework-api \
    objectweb-asm3/asm-distroshaded \
    jgoodies-forms \
    commons-lang \
    commons-io \
    commons-codec \
    SimplyHTML/SimplyHTML \
    felix/org.osgi.core \
    jlatexmath \
    JMapViewer \
    batik-all \
    groovy-1.8 \
    js \
    pdf-transcoder \
    xerces \
    xml-commons-apis-ext \
    xml-commons-apis \
    fop
do
    CLASSPATH=$CLASSPATH:%{_javadir}/$cp.jar
done

export CLASSPATH
%ant build

pushd freeplane_framework/build/plugins
    rm org.freeplane.plugin.script/lib/groovy-all-LICENSE.txt
popd

find -name gitinfo.\* -delete

xsltproc \
	--nonet \
	--param make.year.ranges 1 \
	--param make.single.year.ranges 1 \
	--param man.charmap.use.subset 0 \
	http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl \
	%{SOURCE80}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_javadir}/%{name}

cp -ap -t %{buildroot}%{_datadir}/%{name} \
	freeplane_framework/build/resources \
	freeplane_framework/build/scripts

# main application and plugins
cp -ap -t %{buildroot}%{_javadir}/%{name} \
	freeplane_framework/build/core/* \
	freeplane_framework/build/plugins/* \
	freeplane_framework/build/framework.jar

cp -ap -t %{buildroot}%{_javadir}/%{name}/org.freeplane.core/lib/ \
	freeplane/lib/jortho.jar

# freeplane hard-coded searches for plugins in <resourcedir>/plugins,
# so we need to put a link there
ln -s ../java/%{name} %{buildroot}%{_datadir}/%{name}/plugins

# Freeplane is searching for docs in <resourcedir>/doc, so add a
# link
ln -s ../doc/freeplane-%version %{buildroot}%{_datadir}/%{name}/doc

# cleaning documentation sources:
rm -f freeplane/dist/doc/*odt ./freeplane/dist/doc/*docx
cp -pr %{SOURCE10} README.%{product_distribution}

# launcher script
install -pm  0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}

# set up the osgi shell:
cp -pr freeplane_framework/script/props.xargs %{buildroot}%{_datadir}/%{name}

# add antialiasing settings
cat > %{buildroot}%{_datadir}/%{name}/init.xargs <<EOF
-istart freeplane/org.freeplane.core
-Dawt.useSystemAAFontSettings=on
EOF

# desktop file
mkdir -p %{buildroot}%{_desktopdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_desktopdir}/

# icon
install -m 0644 -D freeplane_framework/script/freeplane.svg %{buildroot}%{_iconsscaldir}/%{name}.svg

# man-page
install -m 0644 -D freeplane.1 %{buildroot}%{_mandir}/man1/%{name}.1

# fix wrong-file-end-of-line-encoding
pushd freeplane/dist/doc
    sed -i 's/\r$//' history_en.txt freeplaneTutorial*.mmfilter
popd

%files
%doc README.%{product_distribution}
%doc freeplane/dist/doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_javadir}/%{name}/
%{_desktopdir}/%{name}.desktop
%{_iconsscaldir}/%{name}.svg
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.15-alt1_7jpp8
- sisyphus build


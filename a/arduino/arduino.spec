Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/desktop-file-validate gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		arduino
Epoch:		1
Version:	1.8.5
Release:	alt2_8jpp8
Summary:	An IDE for Arduino-compatible electronics prototyping platforms
License:	GPLv2+ and LGPLv2+ and CC-BY-SA
URL:		http://www.arduino.cc/

# There are a lot of binaries in the "source" tarball.
# These binaries are removed in the prep section of the SPEC file.
Source0:	https://github.com/arduino/Arduino/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# additional files needed for packaging
Source1:    http://downloads.arduino.cc/packages/package_index.json.gz
Source2:    http://downloads.arduino.cc/packages/package_index.json.sig
Source3:    http://downloads.arduino.cc/libraries/library_index.json.gz

Source4:    https://github.com/arduino-libraries/Firmata/archive/2.5.6.zip#/Firmata-2.5.6.zip
Source5:    https://github.com/arduino-libraries/Bridge/archive/1.6.3.zip#/Bridge-1.6.3.zip
Source6:    https://github.com/arduino-libraries/Robot_Control/archive/1.0.4.zip#/Robot_Control-1.0.4.zip
Source7:    https://github.com/arduino-libraries/Robot_Motor/archive/1.0.3.zip#/Robot_Motor-1.0.3.zip
Source8:    https://github.com/arduino-libraries/RobotIRremote/archive/2.0.0.zip#/RobotIRremote-2.0.0.zip
Source9:    https://github.com/arduino-libraries/SpacebrewYun/archive/1.0.1.zip#/SpacebrewYun-1.0.1.zip
Source10:   https://github.com/temboo/Temboo/archive/1.2.1.zip#/Temboo-1.2.1.zip
Source11:   https://github.com/arduino-libraries/Esplora/archive/1.0.4.zip#/Esplora-1.0.4.zip
Source12:   https://github.com/arduino-libraries/Mouse/archive/1.0.1.zip#/Mouse-1.0.1.zip
Source13:   https://github.com/arduino-libraries/Keyboard/archive/1.0.1.zip#/Keyboard-1.0.1.zip
Source14:   https://github.com/arduino-libraries/SD/archive/1.1.1.zip#/SD-1.1.1.zip
Source15:   https://github.com/arduino-libraries/Servo/archive/1.1.2.zip#/Servo-1.1.2.zip
Source16:   https://github.com/arduino-libraries/LiquidCrystal/archive/1.0.7.zip#/LiquidCrystal-1.0.7.zip
Source17:   https://github.com/adafruit/Adafruit_CircuitPlayground/archive/1.6.8.zip#/Adafruit_CircuitPlayground-1.6.8.zip
Source18:   https://github.com/arduino-libraries/WiFi101-FirmwareUpdater-Plugin/releases/download/v0.9.1/WiFi101-Updater-ArduinoIDE-Plugin-0.9.1.zip

BuildArch:	noarch

BuildRequires:	jpackage-utils ant ant-apache-regexp desktop-file-utils ecj jna
BuildRequires:	jmdns jsemver apache-commons-net apache-commons-codec git
BuildRequires:	apache-commons-compress apache-commons-exec apache-commons-lang3
BuildRequires:	apache-commons-logging jsch guava jackson-annotations jssc
BuildRequires:	bouncycastle-pg jackson-databind jackson-module-mrbean
BuildRequires:	apache-commons-httpclient objectweb-asm
BuildRequires:	rsyntaxtextarea batik xml-commons-apis xmlgraphics-commons
BuildRequires:  libappstream-glib
Requires:	java = 1.8.0
Requires:	fonts-type1-xorg ecj jna zenity polkit ecj jna
Requires:	jmdns jsemver apache-commons-net apache-commons-codec git
Requires:	apache-commons-compress apache-commons-exec apache-commons-lang3
Requires:	apache-commons-logging jsch guava jackson-annotations jssc
Requires:	bouncycastle-pg jackson-databind jackson-module-mrbean
Requires:	apache-commons-httpclient objectweb-asm astyle libastyle libserialport
Requires:	rsyntaxtextarea batik xml-commons-apis xmlgraphics-commons
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:   arduino-listSerialPortsC

# require arduino-builder, which is a go project and won't exist outside these arches
Requires:	arduino-builder >= 1.3.25


# This patch skips the init process for OSX platforms.
Patch0:		arduino-1.8.5-macosx.patch
# Redirects Arduino to system avr-gcc and avrdude utilities
Patch2:		arduino-1.8.3-use-system-avrdude.patch
Patch3:		arduino-add-to-groups.patch
Patch4:		arduino-1.8.3-script.patch
# Redirects Arduino to system astyle libraries
Patch5:		arduino-1.8.3-use-system-astyle.patch
# Allows Arduino to build on non-intel systems
Patch6:		arduino-1.8.3-armbuild.patch
# Do not download listSerialPortsC bits (they are in arduino-listSerialPortsC)
Patch7:		arduino-1.8.3-use-system-libserialport.patch
Source44: import.info
Patch33: arduino-1.8.5-use-system-listSerialsj.patch

%description
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains an IDE that can be used to develop and upload code
to the micro-controller.

%package -n %{name}-core
Group: Development/Java
Summary:	Files required for compiling code for Arduino-compatible micro-controllers
Requires:	avr-gcc avr-gcc-c++ avr-libc avrdude


%description -n %{name}-core
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains the core files required to compile and upload
Arduino code.


%package -n %{name}-doc
Group: Development/Java
Summary:	Documentation for the Arduino micro-controller platform
Requires:	avr-gcc avr-gcc-c++ avr-libc avrdude
BuildArch: noarch


%description -n %{name}-doc
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains reference documentation.


%prep
%setup -q -n Arduino-%{version}
# Add downloaded files from arduino.cc
cp -p %SOURCE1 .
gunzip package_index.json.gz
cp -p %SOURCE2 .
cp -p %SOURCE3 .
gunzip library_index.json.gz

# Add libraries
cp -p %SOURCE4 ./build
cp -p %SOURCE5 ./build
cp -p %SOURCE6 ./build
cp -p %SOURCE7 ./build
cp -p %SOURCE8 ./build
cp -p %SOURCE9 ./build
cp -p %SOURCE10 ./build
cp -p %SOURCE11 ./build
cp -p %SOURCE12 ./build
cp -p %SOURCE13 ./build
cp -p %SOURCE14 ./build
cp -p %SOURCE15 ./build
cp -p %SOURCE16 ./build
cp -p %SOURCE17 ./build
cp -p %SOURCE18 ./build/shared

%patch0 -p1 -b .macosx
%patch2 -p1 -b .avrdude
%patch3 -p1 -b .groups
%patch4 -p1 -b .scripts
%patch5 -p1 -b .system-astyle
%patch6 -p1 -b .armbuild
%patch7 -p1 -b .system-libserialport

# Remove Windows and OSX specific code
find -type d \( -name macosx -o -name windows \) -print0 | xargs -0 rm -rf
# As mentioned earlier, binary forms are removed here.
find -name '*.elf' -delete
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.so' -delete

echo -e "\n# By default, don't notify the user of a new upstream version." \
		"\n# https://bugzilla.redhat.com/show_bug.cgi?id=773519" \
	    "\nupdate.check=false" \
    >> build/shared/lib/preferences.txt

build-jar-repository -p -s arduino-core/lib/ apache-commons-codec \
apache-commons-compress apache-commons-exec apache-commons-lang3 \
apache-commons-logging apache-commons-net bcpg bcprov jackson-core \
jackson-databind jackson-modules-base jmdns jsch jsemver jssc guava \
objectweb-asm jackson-annotations rsyntaxtextarea batik xml-commons-apis-ext xmlgraphics-commons

build-jar-repository -p -s app/lib/ guava apache-commons-logging \
jakarta-commons-httpclient jsch apache-commons-lang3 jssc jsemver \
apache-commons-compress apache-commons-codec rsyntaxtextarea batik xml-commons-apis-ext xmlgraphics-commons

touch app/test/cc/arduino/packages/contributions/library_index.json
%patch33 -p1

%build
%global antflags -Dno_docs=true -Dno_arduino_builder=true -Dsystem_avr=true -Dlight_bundle=true

pushd build
ant -verbose %{antflags}
echo %{version} | ant dist %{antflags}
mv linux/%{name}*.tar.xz linux/%{name}-%{version}.tar.xz
tar -xf linux/%{name}-%{version}.tar.xz
popd

%install
%global appstream_id cc.arduino.arduinoide

cd build/%{name}-%{version}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -a arduino $RPM_BUILD_ROOT%{_bindir}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a hardware lib examples $RPM_BUILD_ROOT/%{_datadir}/%{name}/
mkdir $RPM_BUILD_ROOT/%{_datadir}/%{name}/dist
mkdir $RPM_BUILD_ROOT/%{_datadir}/%{name}/tools-builder
cp -a ../../*.json* $RPM_BUILD_ROOT/%{_datadir}/%{name}/dist/
cp -a ../../libraries $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -a ../../hardware/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/hardware/

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/*.jar
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/tools

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -a ../../license.txt ../../README.md $RPM_BUILD_ROOT/%{_docdir}/%{name}/

# Requested upstream in http://github.com/arduino/Arduino/pull/4:
find $RPM_BUILD_ROOT -type f -iname *.jpg -or -iname *.java -or -iname *.pde -or -iname *.h -or -iname *.cpp -or -iname *.c -or -iname *.txt -or -iname makefile -or -iname key*.txt -or -iname pref*.txt | xargs chmod -x;

cp -a lib/arduino-core.jar lib/pde.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/%{name}/avr/boards.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/%{name}/avr/programmers.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/preferences.txt \
   $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
ln -s %{_sysconfdir}/%{name}/boards.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/%{name}/avr/boards.txt
ln -s %{_sysconfdir}/%{name}/programmers.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/hardware/%{name}/avr/programmers.txt
ln -s %{_sysconfdir}/%{name}/preferences.txt \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/preferences.txt

ln -s %{_bindir}/arduino-builder $RPM_BUILD_ROOT%{_datadir}/%{name}/arduino-builder

cp -p ../linux/dist/desktop.template ../linux/dist/%{appstream_id}.desktop
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications --set-icon=%{appstream_id} --set-key=Exec --set-value=%{name} ../linux/dist/%{appstream_id}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages
cp -a ../linux/dist/mime.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages/%{appstream_id}.xml

for dir in ../shared/icons/*; do
    if [ -d $dir ]
    then
	    size=`basename $dir`
	    mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
	    cp $dir/apps/%{name}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps/%{appstream_id}.png
    fi
done

install -D ../linux/dist/%{name}-add-groups $RPM_BUILD_ROOT%{_libexecdir}/%{name}-add-groups

mkdir -p $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions
cp -a ../linux/dist/cc.arduino.add-groups.policy $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions

mkdir -p $RPM_BUILD_ROOT%{_datadir}/metainfo
cp -a ../linux/dist/appdata.xml $RPM_BUILD_ROOT%{_datadir}/metainfo/%{appstream_id}.appdata.xml
# unFedorize; ALTize
if grep 'dialout lock' %buildroot/%_bindir/arduino; then
   sed -i -e 's,dialout lock,uucp,' %buildroot/%_bindir/arduino
else
   echo "ALT-specific group hack is deprecated"
   exit 2
fi


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/*.appdata.xml

# TODO
#pushd build
#ant test
#popd


%files
%{_bindir}/*
%{_datadir}/%{name}/*.jar
%{_datadir}/%{name}/lib/*
%exclude %{_datadir}/%{name}/lib/version.txt
%{_datadir}/applications/%{appstream_id}.desktop
%{_datadir}/mime/packages/%{appstream_id}.xml
%{_datadir}/icons/hicolor/*/apps/%{appstream_id}.png
%{_datadir}/polkit-1/actions/cc.arduino.add-groups.policy
%{_libexecdir}/%{name}-add-groups
%{_datadir}/metainfo/%{appstream_id}.appdata.xml

%files -n %{name}-doc
%{_docdir}/%{name}/

%files -n %{name}-core
%doc --no-dereference license.txt
%doc README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/boards.txt
%config(noreplace) %{_sysconfdir}/%{name}/programmers.txt
%config(noreplace) %{_sysconfdir}/%{name}/preferences.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/hardware/
%{_datadir}/%{name}/libraries/
%{_datadir}/%{name}/dist/
%dir %{_datadir}/%{name}/lib
%dir %{_datadir}/%{name}/tools-builder
%{_datadir}/%{name}/lib/version.txt
%{_datadir}/%{name}/arduino-builder

%changelog
* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_8jpp8
- fixed avrdude path (closes: #37154)

* Fri Jul 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_7jpp8
- fc update & java 8 build

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_4jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_3jpp8
- java update

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2_1jpp8
- fixed load of liblistSerialsj

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt1_1jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.6.6-alt1_1jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_8jpp8
- new fc release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_6jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.6-alt1_3jpp8
- new version

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.0.6-alt1_3jpp7
- update to new release by jppimport

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.5-alt1_7jpp7
- update to new release by jppimport

* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.5-alt1_6jpp7
- update

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.5-alt1_4jpp7
- update to new release by jppimport

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 1:1.0.1-alt2_4jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for arduino-core

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_4jpp7
- fc update

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_3jpp7
- update to new release by jppimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_1jpp7
- applied repocop patches

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_1jpp7
- new version

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_5jpp6
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_4jpp6
- update to new release by jppimport

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 0022-alt1_3jpp6
- import by jppimport


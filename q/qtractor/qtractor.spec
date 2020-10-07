# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libX11-devel libXext-devel pkgconfig(aubio) pkgconfig(lv2) pkgconfig(ogg) pkgconfig(samplerate) pkgconfig(xcb) pkgconfig(zlib)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		qtractor
Version:	0.9.17
Release:	alt1_1
Summary:	An Audio/MIDI multi-track sequencer
License:	GPLv2+
Group:		Sound
URL:		http://qtractor.sourceforge.io/
Source0:	http://www.rncbc.org/archive/%{name}-%{version}.tar.gz
Patch0:		qtractor-0.9.6-mga-qmake-strip.patch

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(rubberband)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(lilv-0)
BuildRequires:	pkgconfig(dssi)
BuildRequires:	pkgconfig(suil-0)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	ladspa_sdk
BuildRequires:	qt5-designer qt5-tools

Requires:	dssi dssi-examples
Requires:	ladspa_sdk
Source44: import.info

%description
Qtractor is an Audio/MIDI multi-track sequencer application
written in C++ around the Qt4 or Qt5 toolkit using Qt Designer.

The initial target platform will be Linux, where the Jack Audio
Connection Kit (JACK) for audio, and the Advanced Linux Sound
Architecture (ALSA) for MIDI, are the main infrastructures to
evolve as a fairly-featured Linux Desktop Audio Workstation GUI,
specially dedicated to the personal home-studio.

%prep
%setup -q
%patch0 -p1


%build
%configure

%make_build

%install
%makeinstall_std

desktop-file-install \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--set-key=Exec --set-value="%{name}" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog README TODO TRANSLATORS
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/mimetypes/*.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-%{name}-*.svg
%{_mandir}/man1/%{name}*.1*
%lang(fr) %{_mandir}/fr/man1/%{name}*.1*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%lang(cs) %{_datadir}/%{name}/translations/%{name}_cs.qm
%lang(de) %{_datadir}/%{name}/translations/%{name}_de.qm
%lang(es) %{_datadir}/%{name}/translations/%{name}_es.qm
%lang(fr) %{_datadir}/%{name}/translations/%{name}_fr.qm
%lang(it) %{_datadir}/%{name}/translations/%{name}_it.qm
%lang(ja) %{_datadir}/%{name}/translations/%{name}_ja.qm
%lang(pt) %{_datadir}/%{name}/translations/%{name}_pt.qm
%lang(ru) %{_datadir}/%{name}/translations/%{name}_ru.qm


%changelog
* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.17-alt1_1
- new version

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_1
- update to new release by fcimport

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1_1
- new version

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_2
- update to new release by fcimport

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_1
- new version

* Thu Jun 20 2013 Andrey Cherepanov <cas@altlinux.org> 0.5.8-alt1.1
- Rebuild with new version liblo

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1
- manual update to 0.5.8

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_2
- update from fc import

* Mon Sep 12 2011 Egor Glukhov <kaman@altlinux.org> 0.5.0.44-alt1
- fixed build
- 0.5.0.44

* Mon May 30 2011 Egor Glukhov <kaman@altlinux.org> 0.4.9-alt1
- 0.4.9

* Sun Feb 13 2011 Egor Glukhov <kaman@altlinux.org> 0.4.8.18-alt1
- 0.4.8.18

* Thu Jul 15 2010 Egor Glukhov <kaman@altlinux.org> 0.4.6-alt1
- initial build for Sisyphus

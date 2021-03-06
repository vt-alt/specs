%define voice rablpc16k
%define voicepath english/rab_diphone
%define version	1.95
%define release	alt3

Name:		festvox_%{voice}
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	MIT
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: British English RP male speaker (16KHz sampling)
Requires:	festival, festlex_POSLEX, festlex_OALD
Provides:	festvox
BuildArch:	noarch
# useless and too slow on large data files
AutoReqProv:	no

Source0:	http://www.cstr.ed.ac.uk/downloads/festival/2.5/festvox_%{voice}.tar.bz2

%description
British English RP male speaker using residual excited LPC diphone database
at 16KHz sampling.

%prep
%setup -q -c

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

install -d $VOICE_DIR/%{voicepath}/festvox
install -d $VOICE_DIR/%{voicepath}/group
install -m 644 festival/lib/voices/%{voicepath}/festvox/* $VOICE_DIR/%{voicepath}/festvox
install -m 644 festival/lib/voices/%{voicepath}/group/* $VOICE_DIR/%{voicepath}/group

%files
%doc festival/lib/voices/%{voicepath}/COPYING
%{_datadir}/festival/*

%changelog
* Sat Sep 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.95-alt3
- fixed license

* Wed Oct 18 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt2
- fixed dependency on OALD

* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- initial release for Sisyphus

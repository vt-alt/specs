Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           boswars
Version:        2.7
Release:        alt1_24.svn160110
Summary:        Bos Wars is a futuristic real-time strategy game
License:        GPLv2
URL:            http://www.boswars.org/
Source0:        ftp://ftp.nluug.nl/pub/os/Linux/distr/debian/pool/main/b/boswars/boswars_2.7+svn160110.orig.tar.xz
Source1:        %{name}.desktop
Source2:        %{name}-48.png
Source3:        %{name}-128.png
Source4:        %{name}.appdata.xml
Source5:        %{name}.6
Patch0:         boswars-2.4.1-SConstruct.patch
# incomplete patch to port boswars to the system guichan-0.6 instead of
# using the included guichan-0.4. Incomplete, NOT finished and NOT working!
#Patch1:         boswars-2.4.1-guichan26.patch
# Incomplete Lua 5.2 patch, this fixes the C-code but not the actual lua scripts
#Patch2:         boswars-2.6.1-lua-5.2.patch
# Use compat-lua51 for now
Patch3:         boswars-2.7-compat-lua-5.1.patch
Patch4:         boswars-2.7-sconstruct-py3.patch
BuildRequires:  gcc gcc-c++
BuildRequires:  libtheora-devel libvorbis-devel libSDL-devel libGL-devel
BuildRequires:  libtolua++-lua5.1-devel libpng-devel scons
BuildRequires:  libappstream-glib desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Bos Wars is a futuristic real-time strategy game. It is possible to play
against human opponents over LAN, internet, or against the computer.
Bos Wars aims to create a completly original and fun open source RTS game.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch3 -p1
%patch4 -p1

iconv -f ISO-8859-1 -t UTF8 doc/guichan-copyright.txt > guichan-copyright.txt
find campaigns engine maps -type f -executable -exec chmod -x {} ';'
# we want to use the system version of these
rm engine/tolua/*.h engine/tolua/tolua_*.cpp


%build
scons-3 %{?_smp_mflags} opengl=1 CC="gcc $RPM_OPT_FLAGS" CXX="g++ $RPM_OPT_FLAGS" LIBPATH=%{_libdir}


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/languages
install -m 755 build/boswars-release $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 644 languages/*.po languages/*.pot \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/languages
cp -a campaigns graphics intro maps scripts sounds units patches \
  $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man6


%files
%doc README.txt CHANGELOG doc/*.html
%doc --no-dereference COPYRIGHT.txt LICENSE.txt guichan-copyright.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_24.svn160110
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_22.svn160110
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_21.svn160110
- update to new release by fcimport

* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_19.svn160110
- fixed build

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_14.svn160110
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_13.svn160110
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_11.svn160110
- update to new release by fcimport

* Fri Feb 10 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_10.svn160110
- new version

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.6.1-alt1.1.qa1
- NMU: rebuilt for updated dependencies.

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1.1
- Rebuilt with libpng15

* Wed Jun 23 2010 Egor Glukhov <kaman@altlinux.org> 2.6.1-alt1
- 2.6.1 (specfile based on Fedora's)

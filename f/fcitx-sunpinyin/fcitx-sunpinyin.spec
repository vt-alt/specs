Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:			fcitx-sunpinyin
Version:		0.4.2
Release:		alt1_12
Summary:		Sunpinyin Wrapper for Fcitx
License:		GPLv2+
URL:			http://fcitx-im.org/wiki/Fcitx
Source0:		http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	gcc-c++
BuildRequires:	ctest cmake
BuildRequires:	fcitx-devel
BuildRequires:	gettext gettext-tools
BuildRequires:	intltool
BuildRequires:	sunpinyin-devel
BuildRequires:	libdbus-devel
BuildRequires:	libtool
BuildRequires:	sunpinyin
BuildRequires:	fcitx
Requires:		fcitx
Requires:		fcitx-data
Requires:		sunpinyin-data
Source44: import.info

%description
Fcitx-sunpinyin is a Sunpinyin Wrapper for Fcitx.

SunPinyin is an SLM (Statistical Language Model) based input method
engine. To model the Chinese language, it use a backoff bigram and
trigram language model.

%prep
%setup -q -n %{name}-%{version}


%build
%{fedora_v2_cmake}
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README
%doc --no-dereference COPYING
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/sunpinyin.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/fcitx/skin/classic/sunpinyin.png
%{_datadir}/fcitx/skin/dark/sunpinyin.png
%{_datadir}/fcitx/skin/default/sunpinyin.png
%{_datadir}/fcitx/imicon/sunpinyin.png


%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 0.4.2-alt1_12
- new version

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.4.1-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_3
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_2
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_1
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- initial fc import


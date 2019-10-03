%def_disable palemoon   # Only compatible versions

%define cid     \{73a6fe31-595d-460b-a920-fcc0f8843232\}

%if_enabled palemoon
%define cid_dir        %palemoon_noarch_extensionsdir/%cid
%endif

%define cidf_dir       %firefox_noarch_extensionsdir/%cid

Summary: NoScript extension for Firefox and Pale Moon (for firefox-esr)
Summary (ru_RU.utf8): Дополнение NoScript для  Firefox и Pale Moon
Name: firefox-esr-noscript
Version: 5.1.8.4
Release: alt2
Source: noscript-%version.xpi
License: GPL
Group: Networking/WWW
Url: http://noscript.net
Packager: Alexey Gladkov <legion@altlinux.ru>
BuildArch: noarch
Conflicts: firefox-noscript

BuildRequires(pre): rpm-build-firefox
#BuildRequires(pre): rpm-build-palemoon
BuildRequires: unzip

%if_enabled palemoon
%package -n palemoon-noscript
Group: System/Libraries
Summary: Plugin NoScript for Pale Moon
Requires: palemoon
%endif

%description
Extra protection for your Firefox: NoScript allows JavaScript,
Java (and other plugins) only for trusted domains of your
choice (e.g. your home-banking web site). This whitelist
based pre-emptive blocking approach  prevents exploitation
of security vulnerabilities (known and even unknown!) with
no loss of functionality.

%description -l ru_RU.utf8
Расширение для вашего браузер:  NoScript позволяет выполнять
скрипты JavaScript, Java (и другие расширения ) только с доверенных
доменов выбранных вами (например: с сайта банковского обслуживания).
Список доверенных сайтов основанн на принципе упреждающей блокировки
угроз, и позволяет предотвращать использование уязвимостей
(как известных, так и ещё неизвестных) без потери функциональности.

%if_enabled palemoon
%description -n palemoon-noscript
Extra protection for your Pale Moon: NoScript allows JavaScript,
Java (and other plugins) only for trusted domains of your
choice (e.g. your home-banking web site). This whitelist
based pre-emptive blocking approach  prevents exploitation
of security vulnerabilities (known and even unknown!) with
no loss of functionality.

%description -l ru_RU.utf8 -n palemoon-noscript
Расширение для вашего браузер:  NoScript позволяет выполнять
скрипты JavaScript, Java (и другие расширения ) только с доверенных
доменов выбранных вами (например: с сайта банковского обслуживания).
Список доверенных сайтов основанн на принципе упреждающей блокировки
угроз, и позволяет предотвращать использование уязвимостей 
(как известных, так и ещё неизвестных) без потери функциональности.
%endif

%prep
%setup -n noscript

%install
%if_enabled palemoon
mkdir -p %buildroot/%cid_dir
cp -r * %buildroot/%cid_dir
%endif

mkdir -p %buildroot/%cidf_dir
cp -r * %buildroot/%cidf_dir

%if_enabled palemoon
%files -n palemoon-noscript
%cid_dir
%endif

%files
%cidf_dir

%postun
if [ "$1" = 0 ]; then
%if_enabled palemoon
	[ ! -d "%cid_dir" ] || rm -rf "%cid_dir"
%endif
	[ ! -d "%cidf_dir" ] || rm -rf "%cidf_dir"
fi

%changelog
* Wed Oct 02 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.1.8.4-alt2
- Fixed build without rpm-build-palemoon.

* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.8.4-alt1
- New version for firefox-esr with name firefox-esr-noscript.

* Mon May 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.0.11-alt1
- New version (supports Firefox <= 48.0)

* Sun Mar 20 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2.9.0.7-alt2
- Fix errors in spec

* Sun Mar 20 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2.9.0.7-alt1
- Version 2.9.0.7

* Sat Jun 06 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.9.26-alt1
- New version

* Wed Oct 30 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.8.4-alt1
- New version

* Wed Dec 19 2012 Andrey Cherepanov <cas@altlinux.org> 2.6.4.1-alt1
- New version 2.6.4.1

* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 2.2.6-alt1
- New version (2.2.6).

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 2.1.2.5-alt1
- New version (2.1.2.5).

* Fri Apr 08 2011 Alexey Gladkov <legion@altlinux.ru> 2.1.0.1-alt1
- New version (2.1.0.1)

* Sun Jan 24 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.9.39-alt1
- New version (1.9.9.39)

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.3.3-alt1
- New version (1.9.3.3)

* Mon Jul 07 2008 Alexey Gladkov <legion@altlinux.ru> 1.7.6-alt1
- first build for ALT Linux.

%define xsane_verel 0.999-alt6
Name: xsane-doc-ru
Version: 0.999
Release: alt1

Summary: XSane russian documentation
Summary(ru_RU.UTF-8): Документация на русском языке для XSane

License: GPL
Group: Graphics
Url: http://www.xsane.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: xsane-doc >= %xsane_verel

Requires: xsane-doc >= %xsane_verel

%description
XSane russian documentation.

%description -l ru_RU.UTF-8
Документация на русском языке для XSane

%prep
%setup

%install
mkdir -p %buildroot/%_docdir/xsane/ru/
cp -f %_docdir/xsane/*.jpg %buildroot/%_docdir/xsane/ru/
cp -f *.html %buildroot/%_docdir/xsane/ru/

%files
%_docdir/xsane/ru/

%changelog
* Thu Sep 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.999-alt1
- initial build for ALT Sisyphus (ALT bug 35345)

Name: fonts-cascadia-code
Version: 21909.16
Release: alt1

Summary: A fun, new monospaced font that includes programming ligatures
License: OFL
Group: System/Fonts/True type
Url: https://devblogs.microsoft.com/commandline/cascadia-code/
Source: Cascadia.ttf

BuildArch: noarch
Requires(pre,postun): fontconfig

BuildRequires: rpm-build-fonts

%description
This is a fun, new monospaced font that includes programming ligatures and is designed to enhance the modern look and feel of the Windows Terminal. 

%prep
cp %SOURCE0 .

%build

%install
%ttf_fonts_install Cascadia

%files -f Cascadia.files

%changelog
* Thu Sep 19 2019 Fr. Br. George <george@altlinux.ru> 21909.16-alt1
- Initial build for ALT


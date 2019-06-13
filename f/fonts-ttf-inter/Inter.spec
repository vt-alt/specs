Name: fonts-ttf-inter
Version: 3.6
Release: alt1
Summary: The Inter typeface family carefully crafted & designed for computer screens
License: OFL
Group: System/Fonts/True type
Url: https://rsms.me/inter/
Source: Inter-%version.zip
BuildArch: noarch

BuildRequires: rpm-build-fonts

# Automatically added by buildreq on Mon Nov 19 2012
BuildRequires: unzip

%description
Inter features a tall x-height to aid in readability of mixed-case and
lower-case text. Several OpenType features are provided as well, like
contextual alternates that adjusts punctuation depending on the shape of
surrounding glyphs, slashed zero for when you need to disambiguate "0"
from "o", tabular numbers, etc.

%prep
%setup -c

%build
%install
cd 'Inter (TTF)' && %ttf_fonts_install inter
ln -s 'Inter (TTF)'/inter.files ../inter.files

%files -f inter.files
%doc *.txt

%changelog
* Tue May 28 2019 Fr. Br. George <george@altlinux.ru> 3.6-alt1
- Autobuild version bump to 3.6

* Tue May 28 2019 Fr. Br. George <george@altlinux.ru> 3.5-alt1
- Initial build for ALT


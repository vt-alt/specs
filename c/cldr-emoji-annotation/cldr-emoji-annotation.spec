Name: cldr-emoji-annotation
Version: 35.12.14971_0
Release: alt1

# Annotation files are in Unicode license
Summary: Emoji annotation files in CLDR
Group: Development/Other
License: LGPLv2+ and Unicode
Url: https://github.com/fujiwarat/cldr-emoji-annotation

Source: %url/releases/download/%version/%name-%version.tar.gz

BuildArch: noarch

%description
This package provides the emoji annotation files by language in CLDR.
See http://cldr.unicode.org/translation/short-names-and-keywords

%package devel
Summary: Files for development using cldr-annotations
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package contains the pkg-config files for development
when building programs that use cldr-annotations.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_datadir/unicode/cldr/*
%doc AUTHORS NEWS README unicode-license.txt

%files devel
%_datadir/pkgconfig/*.pc


%changelog
* Thu Aug 22 2019 Yuri N. Sedunov <aris@altlinux.org> 35.12.14971_0-alt1
- first build for Sisyphus


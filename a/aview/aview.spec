%define _unpackaged_files_terminate_build 1

Name: aview
Version: 1.3.0
Release: alt3.rc1

Summary: High quality ascii-art image (pnm) browser and animation (fli/flc) player
License: GPL
Group: Graphics
Url: http://aa-project.sourceforge.net/aview/

Source: %name-%{version}rc1.tar

# Patches from Debian
Patch1: 00_misc_fixes.patch
Patch2: 01_manpages.patch
Patch3: 02_tmp_creation.patch
Patch4: 03_missing_library.patch

# ALT patches
Patch100: alt-no-implicit-function-declarations.patch

# Automatically added by buildreq on Fri Jun 15 2007
BuildRequires: aalib-devel libgpm-devel libslang-devel libX11-devel

%description
High quality ascii-art image(pnm) browser and animation(fli/flc) player.
Features:
- High quality ascii art rendering 
- Portable 
- Save into many formats (html, text, ansi, more/less etc...) 
- Contrast, Bright, Gamma control 
- Image zooming/unzooming 
- Three dithering modes 
- Hidden "bonus" features :) 
- Inversion 
- Support for bright, dim, inverse attributes/extended character set

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch100 -p2

%build
%add_optflags -Werror=implicit-function-declaration
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc ANNOUNCE AUTHORS ChangeLog INSTALL README README.flip NEWS TODO
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt3.rc1
- Switched to CVE-2008-4935 fix from Debian.
- Added -Werror=implicit-function-declaration compiler flag.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.0-alt2.rc1.qa1
- NMU: rebuilt for debuginfo.

* Fri Oct 24 2008 Sergey Kurakin <kurakin@altlinux.org> 1.3.0-alt2.rc1
- fixed unsafe tmp usage in scripts

* Fri Jun 15 2007 Sergey Kurakin <kurakin@altlinux.ru> 1.3.0-alt1.rc1
- initial build for Sisyphus


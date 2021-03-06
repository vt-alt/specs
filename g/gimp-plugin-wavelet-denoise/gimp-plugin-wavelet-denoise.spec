%def_enable snapshot
%define _name wavelet-denoise
%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-%_name
Version: 0.3.1
Release: alt3

Summary: GIMP tool for reducing sensor noise in an image
License: GPLv2+
Group: Graphics
Url: http://registry.gimp.org/node/4235/

%if_disabled snapshot
# the gimp registry is dead
Source: http://registry.gimp.org/files/%_name-%version.tar.gz
%else
Vcs: https://github.com/gimp-plugins-justice/wavelet-denoise.git
Source: %_name-%version.tar
%endif
Patch: %_name-0.3.1-alt-makefile.patch
# fc
Patch1: gimp-wavelet-denoise-plugin-fno-common-fix.patch

Requires: gimp >= 2.6
BuildRequires: libgimp-devel

%description
The wavelet denoise plugin is a tool to selectively reduce noise in individual
channels of an image with optional RGB<->YCbCr conversion. It has a user
inteface to adjust the amount of denoising applied. The wavelet nature of the
algorithm makes the processing quite fast.

%prep
%setup -n %_name-%version
%patch -p1
%patch1 -p1

%build
%make

%install
%makeinstall_std -C po
install -pD -m755 src/%_name %buildroot%gimpplugindir/plug-ins/%_name
%find_lang --output=%_name.lang gimp20-%_name-plug-in

%files -f %_name.lang
%gimpplugindir/plug-ins/*
%doc AUTHORS ChangeLog README

%changelog
* Sat Dec 05 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt3
fixed build with gcc10/-fno-common (fc patch)

* Tue Sep 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt2
- fixed build

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 0.3.1-alt1
- 0.3.1

* Thu Aug 28 2008 Victor Forsyuk <force@altlinux.org> 0.2-alt1
- Initial build.

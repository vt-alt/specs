%define oversion 0.9.6

Name: screenruler
Version: 0.96
Release: alt1

Summary: GNOME screen ruler - measure objects on screen with a variety of metrics

License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://launchpad.net/screenruler/

# Source-url: http://launchpad.net/screenruler/trunk/%oversion/+download/%name-%oversion.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Source1: %name.desktop
Source2: %name.appdata.xml

Patch: screenruler-ruby19.patch
# %_datadir/screenruler/utils/addons_ruby.rb:62:in `loop': wrong number of arguments (given 0, expected 2..3) (ArgumentError)
Patch1: screenruler-ruby25-loop.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-ruby
BuildRequires: desktop-file-utils

Requires: ruby
Requires: gem-gtk2 gem-cairo gem-gettext

Provides: gruler = %version-%release
Obsoletes: gruler

%description
Screenruler is a small GNOME based utility that allows you to measure objects
on your desktop. It can be used to take both horizontal and vertical
measurement in 6 different metrics: pixels, centimeters, inches, picas, points,
and as a percentage of the ruler's length.

%prep
%setup
%patch0 -p0 -b ruby19
%patch1 -p1 -b .ruby25

%install
mkdir -p %buildroot
cat << EOF > screenruler
#!/bin/bash

cd %_datadir/%name
ruby ./screenruler.rb
EOF

chmod 0755 screenruler

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name/
mkdir -p %buildroot%_pixmapsdir/
cp -p screenruler %buildroot%_bindir/
cp -p screenruler-icon*.png %buildroot%_pixmapsdir/
cp -pr utils *.rb screenruler*.* *.glade %buildroot%_datadir/%name/
ln -s screenruler-icon-32x32.png %buildroot%_pixmapsdir/screenruler-icon.png

desktop-file-install --dir=%buildroot%_desktopdir %SOURCE1

# Add AppStream metadata
install -Dm 0644 -p %SOURCE2 %buildroot%_datadir/appdata/%name.appdata.xml

%files
%doc AUTHORS
%_bindir/screenruler
%_datadir/screenruler/
%_desktopdir/screenruler.desktop
%_pixmapsdir/screenruler*.png
%_datadir/appdata/%name.appdata.xml

%changelog
* Wed Nov 18 2020 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt1
- new version (0.96) with rpmgs script
- sync spec with Fedora

* Thu Dec 25 2008 Sir Raorn <raorn@altlinux.ru> 0.85-alt1
- Built for Sisyphus


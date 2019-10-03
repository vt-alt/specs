Name: openarena
Version: 0.8.8
Release: alt3

Summary: Open source first person shooter
Group: Games/Arcade
License: GPLv2
URL: http://openarena.ws/

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: openarena-0.8.8.zip
Source1: %name.sh
Source2: %name.png
Source3: %name.desktop

AutoReq: yes, noshell

# We need 1.36-11 or newer for the new standalone game and protocol cvars
#Requires: quake3 >= 1.36-11
Requires: quake3
Requires: opengl-games-utils

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 27 2012
BuildRequires: dos2unix unzip

%description
OpenArena is an open-source content package for Quake III Arena licensed under
the GPL, effectively creating a free stand-alone game.

%prep
%setup -q
dos2unix CHANGES CREDITS LINUXNOTES README WENEED readme_085.txt

%install
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/pixmaps
mkdir -p %buildroot%_bindir/

cp -pr baseoa missionpack %buildroot%_datadir/%name
install -p -m755 %SOURCE1 %buildroot%_bindir/%name
ln -s %name %buildroot%_bindir/%{name}_ded
cp -p %SOURCE2 %buildroot%_datadir/pixmaps

install -pD -m644 %SOURCE3 %buildroot%_datadir/applications/%name.desktop

%files
%doc CHANGES CREDITS LINUXNOTES README WENEED readme_085.txt readme_088.txt
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%changelog
* Thu Oct 03 2019 Anton Midyukov <antohami@altlinux.org> 0.8.8-alt3
- Fix path for quake3 binary for aarch64

* Mon Dec 31 2012 Igor Zubkov <icesik@altlinux.org> 0.8.8-alt2
- Fix path for quake3 binary

* Tue Nov 27 2012 Igor Zubkov <icesik@altlinux.org> 0.8.8-alt1
- 0.8.5 -> 0.8.8

* Sun Nov 04 2012 Igor Zubkov <icesik@altlinux.org> 0.8.5-alt1
- build for Sisyphus

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 28 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.5-3
- Update launcher script to work with newer quake3 package + require this

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 12 2010 Hans de Goede <hdegoede@redhat.com> - 0.8.5-2
- Fix compability with network play with official openarena servers (#565763)
- Various specfile cleanups

* Tue Apr 27 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5 via patch
- Update spec to match the latest Fedora packaging guidelines

* Tue Jul 28 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.1-1
- Catching up to a new release in a long time
- new maps, guns, models, textures 
- http://openarena.ws/svn/CHANGES

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 06 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.7-2
- Fix permissions...

* Wed Jun 04 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.7-1
- Add patch
- Get rid of macros from Sources

* Wed Apr 23 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.6-1
- New release
- Fix desktop file a bit

* Sun Jan 13 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.1-5
- Fix wrapper to include master server adress

* Sat Jan 05 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.1-4
- Use quake3 package from repo instead of own engine
- No -data subpackage since the main package now contains data
- Now the spec simple creates wrapper and just copy data to proper dir

* Fri Oct 05 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.1-3
- Add support for opengl-games-utils

* Fri Aug 24 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.1-2
- BuildID rebuild
- License tag fix

* Mon Aug 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.7.1-1
- Added 0.7.1 patch. 
- Uses 0.7.0 .zip, took version macro out of URL and setup to accommodate.

* Fri Jul 13 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.0-3
- NO_VM_COMPILED flag on ppc64

* Fri Jul 13 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.0-2
- Add libvorbis-devel BR

* Wed Jul 11 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jan 12 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.6.0-4
- Get rid of -maltivec flag

* Wed Jan 10 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.6.0-3
- Do some ppc fixes

* Wed Jan 03 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.6.0-2
- Add COPYING to data subpackage
- Remove LINUXNOTES from %%doc

* Mon Jan 01 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.6.0-1
- Initial new year release


%define _libexecdir /usr/libexec

Name: virt-manager
Version: 2.2.1
Release: alt2
Summary: Virtual Machine Manager

Group: Emulators
License: GPLv2+
Url: https://virt-manager.org/
BuildArch: noarch
AutoReqProv: nopython

# https://github.com/virt-manager/virt-manager
Source: %name-%version.tar
# Patch: %name-%version-%release.patch

Requires: virt-manager-common = %EVR
Requires: libvirt-client
Requires: virt-install = %EVR
Requires: python3-module-pygobject3 >= 3.22
Requires: python3-module-libxml2
Requires: vte3
Requires: dconf
Requires: libosinfo >= 0.2.10
Requires: librsvg
Requires: genisoimage

# define version of requires based on "from gi.repository import foo"
Requires: typelib(Gtk) = 3.0
Requires: typelib(GtkVnc) = 2.0
Requires: typelib(GtkSource) = 4
Requires: typelib(SpiceClientGtk) = 3.0
Requires: typelib(Vte) = 2.91

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel python3-module-argcomplete
BuildRequires: libgio
BuildRequires: intltool
BuildRequires: /usr/bin/pod2man
BuildRequires: bash-completion

%add_python3_lib_path %_datadir/%name
%allow_python3_import_path %_datadir/%name
# libaptindicator is not package in ALT Linux
%add_typelib_req_skiplist typelib(AppIndicator3)

%description
Virtual Machine Manager provides a graphical tool for administering
virtual machines for KVM, Xen, and QEmu. Start, stop, add or remove
virtual devices, connect to a graphical or serial console, and see
resource usage statistics for existing VMs on local or remote machines.
Uses libvirt as the backend management API.

%package common
Summary: Common files used by the different Virtual Machine Manager interfaces
Group: Emulators
AutoReqProv: nopython

%description common
Common files used by the different virt-manager interfaces, as well as
virt-install related tools.

%package -n virt-install
Summary: Utilities for installing virtual machines
Group: Emulators
AutoReqProv: nopython

Requires: virt-manager-common = %EVR

Provides: virt-clone
Provides: virt-convert
Provides: virt-xml

%description -n virt-install
Package includes several command line utilities, including virt-install
(build and install new VMs) and virt-clone (clone an existing virtual
machine).

%prep
%setup
#%%patch -p1

%build
python3 setup.py configure

#%%python_build

%install
#%%python_install
python3 setup.py \
	--no-update-icon-cache --no-compile-schemas \
	install --root=%buildroot

%find_lang --with-gnome %name

# Replace '#!/usr/bin/env python3' with '#!/usr/bin/python3'
# The format is ideal for upstream, but not a distro. See:
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
for f in $(find %buildroot -type f -executable -print); do
    sed -i "1 s|^#!/usr/bin/env python3|#!/usr/bin/python3|" $f || :
done

%files
%_bindir/%name
%_datadir/%name/ui/*.ui
%_datadir/%name/virt-manager
%_datadir/%name/virtManager
%_datadir/%name/icons
%_desktopdir/%name.desktop
%_datadir/appdata/%name.appdata.xml
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/glib-2.0/schemas/*.gschema.xml

%_man1dir/%name.1*
%doc README.md COPYING NEWS.md

%files common -f %name.lang
%dir %_datadir/%name
%_datadir/%name/virtconv
%_datadir/%name/virtinst

%files -n virt-install
%_bindir/virt-install
%_bindir/virt-clone
%_bindir/virt-convert
%_bindir/virt-xml
%_datadir/%name/virt-install
%_datadir/%name/virt-clone
%_datadir/%name/virt-convert
%_datadir/%name/virt-xml
%_datadir/bash-completion/completions/virt-install
%_datadir/bash-completion/completions/virt-clone
%_datadir/bash-completion/completions/virt-convert
%_datadir/bash-completion/completions/virt-xml
%_man1dir/virt-install.1*
%_man1dir/virt-clone.1*
%_man1dir/virt-convert.1*
%_man1dir/virt-xml.1*

%changelog
* Mon Dec 02 2019 Alexey Shabalin <shaba@altlinux.org> 2.2.1-alt2
- fixed requires(added gir packages)

* Thu Jul 04 2019 Alexey Shabalin <shaba@altlinux.org> 2.2.1-alt1
- 2.2.1 (Fixes: CVE-2019-10183)

* Mon Feb 04 2019 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- new version 2.1.0
- add bash completions

* Thu Oct 18 2018 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt2
- allow python3 provides non-standart path

* Tue Oct 16 2018 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1.git2549e6%ubt
- upstream master snapshot

* Fri Jul 27 2018 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt0.git4484f473%ubt
- pre release 1.6.0
- migrate to python3

* Tue Mar 06 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1%ubt
- 1.5.1

* Wed Feb 07 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1%ubt
- 1.5.0

* Tue Sep 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt1%ubt
- 1.4.3

* Wed Aug 09 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Mar 09 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Jun 21 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu May 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt2
- upstream master snapshot

* Fri Mar 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Thu Dec 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt2
- update requires (ALT #31635)

* Tue Dec 08 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon Jun 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- git snapshot

* Wed May 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt2
- backport patches from upstream master:
  + domain: Fix memory stats for shutoff VM (#1215453)
  + sshtunnels: fix exception when the address is not an IP (RH#1218958 ALT#31020)
  + pollhelpers: Fix VM polling on old libvirt (RH#1219443)
  + storage: do not throw exception if the volume or the pool don't exist (RH#219427)
  + interface: read the start mode from the inactive conf XML (RH#1154480)

* Tue May 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0
- update Requires (#30809)

* Thu Sep 11 2014 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Wed Apr 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1
- updare Requires (#29396, #22760)

* Wed Mar 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1.git.7dfdbb
- upstream snapshot 7dfdbb3f352817a61fa7c06f463500807840348d

* Thu Aug 08 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt2
- add ALT Linux support

* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0
- add subpackages virt-install and virt-manager-common

* Wed Apr 10 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Wed Jan 23 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.4-alt1.git0ca8c
- upstream git snapshot 0ca8cf6d4316d1b3f55226c3782a3ac92eb34967

* Tue Jul 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Mon Apr 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt2.git.9d2119
- git snapshot

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Tue Mar 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt3.hg20110224
- snapshot 20110224

* Thu Feb 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt3.hg20110215
- snapshot 20110215

* Fri Feb 11 2011 Anton Protopopov <aspsk@altlinux.org> 0.8.6-alt2
- Don't always launch consoles for running domains (ALT #25073)

* Tue Jan 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Tue Jan 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1.hg20110107
- snapshot 20110107
- build as noarch

* Thu Dec 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1.hg20101220
- snapshot 20101220 (with spice support)
- define _libexecdir as /usr/libexec (fix dbus service)

* Tue Dec 07 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt3
- Add perl-Pod-Parser to build requires

* Tue Dec 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt2
- Merge with gears/

* Tue Dec 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2.

* Wed Dec 09 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.1-alt1
- Updated to 0.8.1.

* Tue Dec 01 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt2
- Add Packager field

* Thu Oct 08 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Thu Jul 02 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6.0-alt1
- new version
- remove post scripts

* Tue Apr 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.4-alt2
- fix #15493, #15494

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.4-alt1
- First build for ALTLinux


Name: pve-docs
Summary: PVE Documentation
Version: 6.0.4
Release: alt1
License: GPLv3
Group: Documentation
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64
BuildArch: noarch
BuildRequires: asciidoc-a2x source-highlight xmlto librsvg-utils mailcap pve-common
BuildRequires: perl(MediaWiki/API.pm) perl(JSON.pm)

%description
PVE Documentation files

%package -n pve-doc-generator
Summary: Proxmox VE Documentation helpers
Group: Documentation
Requires: asciidoc-a2x source-highlight xmlto

%description -n pve-doc-generator
Tool to auto-generate various Proxmox VE Documentation files

%add_findreq_skiplist %_datadir/pve-doc-generator/*.pl

%prep
%setup -q -n %name-%version
grep 'proxmox.com' * -rl | while read f; do
	sed -i 's|proxmox.com|basealt.ru|' $f
done

rm -f getting-help.adoc howto-improve-pve-docs.adoc pve-package-repos.adoc pve-faq.adoc pve-installation.adoc pve-system-requirements.adoc translation.adoc

%build
%make

%install
mkdir -p %buildroot%_datadir/pve-doc-generator/asciidoc
cp *.adoc *.pl *.mk *.xml %buildroot%_datadir/pve-doc-generator/
cp asciidoc/*pve*.conf %buildroot%_datadir/pve-doc-generator/asciidoc/
install -pD -m755 asciidoc-pve %buildroot%_bindir/asciidoc-pve

mkdir -p %buildroot%_datadir/%name/{api-viewer,images/screenshot}
install -m644 *.html %buildroot%_datadir/%name/
install -m644 api-viewer/apidoc.js %buildroot%_datadir/%name/api-viewer/
install -m644 api-viewer/index.html %buildroot%_datadir/%name/api-viewer/
install -m644 images/*.svg %buildroot%_datadir/%name/images/
install -m644 images/screenshot/*.png %buildroot%_datadir/%name/images/screenshot/

%files
%_datadir/%name

%files -n pve-doc-generator
%_bindir/asciidoc-pve
%_datadir/pve-doc-generator

%changelog
* Tue Jul 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.4-alt1
- 6.0-4

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.4.2-alt1
- 5.4-2

* Wed Dec 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.3.1-alt1
- 5.3-1

* Mon Nov 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.10-alt1
- 5.2-10

* Wed Jul 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt1
- 5.2-3

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt1
- 5.0-12

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.10-alt1
- 5.0-10

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.9-alt0.M80C.1
- backport to c8 branch

* Thu Jul 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.9-alt1
- 5.0-9

* Mon Dec 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt1
- 4.4-1

* Fri Dec 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.19-alt2
- remove pve-admin-guide.pdf

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.19-alt1
- 4.3-19

* Fri Dec 02 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.18-alt1
- 4.3-18

* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.16-alt1
- 4.3-16

* Fri Oct 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.12-alt1
- 4.3-12

* Sun Oct 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.5-alt2
- pve-doc-generator: fixed build man pages

* Fri Oct 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.5-alt1
- 4.3-5

* Tue Oct 04 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.2-alt1
- 4.3-2

* Mon Sep 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.11-alt1
- 4.2-11

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.10-alt1
- 4.2-10

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.8-alt1
- 4.2-8

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.5-alt1
- 4.2-5

* Sat May 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2-alt1
- initial release


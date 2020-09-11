%def_enable daemon
%def_disable appliance
%def_enable fuse
%def_enable ocaml
%def_enable perl
%def_enable python
%def_disable ruby
%def_disable haskell
%def_disable php
%def_disable erlang
%def_disable lua
%def_disable golang
%def_enable introspection
%def_enable vala
%def_disable rust
%def_disable static
%def_enable bash_completion

Summary: Tools for accessing and modifying virtual machine disk images
Name: libguestfs
Version: 1.42.0
Release: alt2
License: LGPLv2+
Group: System/Libraries
Url: http://libguestfs.org/

Source: %name-%version.tar
Source2: gnulib-%name-%version.tar
Source3: libguestfs-common-%version.tar
Patch1: %name-%version-alt-fixes.patch
Patch2: %name-%version-alt-fixes-common.patch

# libguestfs live service
#%%Source2: guestfsd.service
#%%Source3: 99-guestfsd.rules

BuildRequires: /proc
BuildRequires: gcc gcc-c++ flex
BuildRequires: glibc-utils libselinux-devel libaugeas-devel
BuildRequires: libgio-devel libgtk+3-devel
BuildRequires: gtk-doc
BuildRequires: gettext-tools
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgjs-devel}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala}
%{?_enable_vala:BuildRequires: vala-tools}
BuildRequires: cpio gperf genisoimage xml-utils db4-utils zip unzip
# po4a 
BuildRequires: qemu-kvm qemu-system >= 1.3.0
BuildRequires: libncurses-devel libtinfo-devel libreadline-devel
BuildRequires: libpcre-devel libmagic-devel libvirt-devel libxml2-devel libconfig-devel hivex-devel
BuildRequires: libacl-devel libcap-devel
BuildRequires: netpbm
BuildRequires: libyajl-devel >= 2.0.4
BuildRequires: libjansson-devel
BuildRequires: libsystemd-journal-devel >= 196
BuildRequires: liblzma-devel
BuildRequires: libdbus-devel
BuildRequires: libtirpc-devel
#BuildRequires: libtsk-devel
# BuildRequires: supermin >= 5.1.0
%{?_enable_fuse:BuildRequires: libfuse-devel}
%{?_enable_ocaml:BuildRequires(pre): rpm-build-ocaml}
%{?_enable_ocaml:BuildRequires: ocaml ocaml-findlib ocaml-gettext-devel ocaml-ounit-devel ocaml-ocamldoc ocaml-ocamlbuild ocaml-hivex-devel}
%{?_enable_python:BuildRequires(pre): rpm-build-python3}
%{?_enable_python:BuildRequires: python3-devel python3-module-libvirt}
%{?_enable_ruby:BuildRequires: ruby rpm-build-ruby ruby-rake ruby-mkrf libruby-devel rubygems}
BuildRequires: java-devel-default jpackage-utils
%{?_enable_haskell:BuildRequires: ghc}
%{?_enable_php:BuildRequires: php7-devel}
%{?_enable_erlang:BuildRequires: erlang-devel}
%{?_enable_perl:BuildRequires: perl-Pod-Parser perl-Sys-Virt perl-libintl perl-hivex perl-Module-Build perl-ExtUtils-CBuilder perl-devel}
%{?_enable_golang:BuildRequires(pre): rpm-macros-golang}
%{?_enable_rust:BuildRequires: rust rust-cargo}
%{?_enable_bash_completion:BuildRequires: bash-completion >= 2.0}

%description
libguestfs is a set of tools for accessing and modifying virtual
machine (VM) disk images. You can use this for viewing and editing
files inside guests, scripting changes to VMs, monitoring disk
used/free statistics, P2V, V2V, performing partial backups, cloning
VMs, and much else besides.

%package -n guestfsd
Summary: Provides guestfsd for the appliance
Group: File tools

%description -n guestfsd
guestfsd runs within the appliance. It receives commands from the host
and performs the requested action by calling the helper binaries.
This package is only required for building the appliance.

%package devel
Summary: Header files for libguestfs library
Group: Development/Other
Requires: %name = %EVR
Requires: %name-gobject = %EVR
Requires: %name-gir = %EVR
Provides: %name-gobject-devel = %EVR
Obsoletes: %name-gobject-devel < %EVR
Provides: %name-gir-devel = %EVR
Obsoletes: %name-gir-devel < %EVR

%description devel
Header files for libguestfs library.

%package gobject
Summary: GObject'ified version of libguestfs API
Group: System/Libraries
Requires: %name = %EVR

%description gobject
GObject'ified version of libguestfs API

%package gir
Summary: GObject introspection data for the libguestf library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the libguestfs library

%package -n golang-guestfs
Summary: Golang bindings for %name
Group: Development/Other
Requires: %name = %EVR
Requires: golang

%description -n golang-guestfs
golang-%name contains Go language bindings for %name.

%package -n guestfs-tools
Summary: System administration tools for virtual machines
Group: File tools
License: GPLv2+
Requires: %name = %EVR
Provides: %name-tools = %EVR
Obsoletes: %name-tools < %EVR
%if_enabled bash_completion
Provides: bash-completion-libguestfs = %EVR
Obsoletes: bash-completion-libguestfs < %EVR
%endif
%ifarch %ix86 x86_64 aarch64
Requires: guestfs-data
%endif

Requires: libosinfo

# for virt-make-fs:
Requires: qemu-img >= 1.3.0
Requires: libvirt-daemon-driver-qemu >= 0.10.2

# for virt-sysprep:
Requires: %_bindir/fusermount
Requires: %_bindir/getopt
# for virt-df and other tools, who is working via libvirtd
Requires: /lib/systemd/systemd-machined

%description -n guestfs-tools
This package contains miscellaneous system administrator command line
tools for virtual machines.

%package -n ocaml-%name
Summary: OCaml bindings for %name
Group: Development/Other
Requires: %name = %EVR
Provides: ocaml4-%name = %EVR
Obsoletes: ocaml4-%name < %EVR

%description -n ocaml-%name
ocaml-%name contains OCaml bindings for %name.

This is for toplevel and scripting access only.  To compile OCaml
programs which use %name you will also need ocaml-%name-devel.

%package -n ocaml-%name-devel
Summary: OCaml bindings for %name
Group: Development/Other
Requires: ocaml-%name = %EVR
Provides: ocaml4-%name-devel = %EVR
Obsoletes: ocaml4-%name-devel < %EVR

%description -n ocaml-%name-devel
ocaml-%name-devel contains development libraries
required to use the OCaml bindings for %name.

%package -n perl-Sys-Guestfs
Summary: Perl bindings for %name (Sys::Guestfs)
Group: Development/Other
Requires: %name = %EVR
Provides: perl-%name = %EVR

%description -n perl-Sys-Guestfs
perl-Sys-Guestfs contains Perl bindings for %name (Sys::Guestfs).

%package -n python3-module-%name
Summary: Python3 bindings for %name
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%name
python3-module-%name contains Python3 bindings for %name.

%package -n ruby-%name
Summary: Ruby bindings for %name
Group: Development/Other
Requires: %name = %EVR

%description -n ruby-%name
ruby-%name contains Ruby bindings for %name.

%package java
Summary: Java bindings for %name
Group: Development/Other
Requires: %name = %EVR
Requires: jpackage-utils

%description java
%name-java contains Java bindings for %name.

If you want to develop software in Java which uses %name, then
you will also need %name-java-devel.

%package java-devel
Summary: Java development package for %name
Group: Development/Other
Requires: %name = %EVR
Requires: %name-java = %EVR

%description java-devel
%name-java-devel contains the tools for developing Java software
using %name.

See also %name-javadoc.

%package javadoc
Summary: Java documentation for %name
Group: Development/Other
Requires: %name = %EVR
Requires: %name-java = %EVR
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%name-javadoc contains the Java documentation for %name.

%package -n php7-%name
Summary: PHP bindings for %name
Group: Development/Other
Requires: %name = %EVR

%description -n php7-%name
php-%name contains PHP bindings for %name.

%package -n erlang-%name
Summary: Erlang bindings for %name
Group: Development/Other
Requires: %name = %EVR

%description -n erlang-%name
erlang-%name contains Erlang bindings for %name.

%package -n virt-dib
Summary: Safe and secure diskimage-builder replacement
Group: Development/Other
License: GPLv2+
Requires: %name = %EVR

%description -n virt-dib
Virt-dib is a safe and secure alternative to the OpenStack
diskimage-builder command.  It is compatible with most
diskimage-builder elements.

%prep
%setup -a2
tar -xf %SOURCE3 -C common

%patch1 -p1
pushd common
%patch2 -p1
popd

%build
export PYTHON=%__python3
%define localconfigure \
    %configure \\\
	vmchannel_test=no \\\
	%{subst_enable daemon} \\\
	--enable-install-daemon \\\
	%{subst_enable appliance} \\\
	%{subst_enable fuse} \\\
	%{subst_enable ocaml} \\\
	%{subst_enable perl} \\\
	%{subst_enable python} \\\
	%{subst_enable ruby} \\\
	%{subst_enable haskell} \\\
	%{subst_enable php} \\\
	%{subst_enable erlang} \\\
	%{subst_enable lua} \\\
	%{subst_enable goolang} \\\
	%{subst_enable introspection} \\\
	%{subst_enable vala} \\\
	%{subst_enable rust} \\\
	%{subst_enable static} \\\
	--with-default-backend=libvirt \\\
	--with-distro=ALT \\\
	--with-extra="ALTLinux,release=%version-%release,libvirt" \\\
	--with-qemu="qemu-kvm qemu-system-%_build_arch qemu" \\\
	--disable-silent-rules \\\
	--disable-probes \\\
	--disable-rpath

./bootstrap --gnulib-srcdir=gnulib-%name-%version

%localconfigure
%make INSTALLDIRS=vendor

%install
%make install INSTALLDIRS=vendor DESTDIR=%buildroot

# Delete static libraries, libtool files.
rm -f %buildroot%_libdir/libguestfs.{la,a}

find %buildroot -name perllocal.pod -delete
find %buildroot -name .packlist -delete
find %buildroot -name '*.bs' -delete
find %buildroot -name 'bindtests.pl' -delete

# Remove static-linked Java bindings.
rm %buildroot%_libdir/libguestfs_jni.la

# Move installed documentation back to the source directory so
# we can install it using a %%doc rule.
mv %buildroot%_docdir/libguestfs installed-docs

# Remove Japanese manpages, since these are not translated fully at
# the moment.  When these are translated properly we intend to add
# them back.
rm -rf %buildroot%_mandir/ja/man{1,3}/

# For the libguestfs-live-service subpackage install the systemd
# service and udev rules.
#mkdir -p %buildroot%systemd_unitdir
#mkdir -p %buildroot%_sysconfdir/udev/rules.d
#install -m 0644 %%SOURCE2 %buildroot%systemd_unitdir
#install -m 0644 %%SOURCE3 %buildroot%_sysconfdir/udev/rules.d

# delete unneeded
rm -f %buildroot%_man1dir/guestfs-release-notes*

%find_lang %name

%files -f %name.lang
%doc COPYING README
%_bindir/libguestfs-test-tool
%_libdir/libguestfs.so.*
%_man1dir/guestfs-testing.1*
%_man1dir/libguestfs-test-tool.1*

%files -n guestfsd
%_sbindir/guestfsd
%_man8dir/guestfsd.*

%files devel
%doc AUTHORS BUGS HACKING TODO README
%doc examples/*.c
%doc installed-docs/*
%_libdir/libguestfs.so
#%_sbindir/libguestfs-make-fixed-appliance
#%_man1dir/libguestfs-make-fixed-appliance.1*
%_man1dir/guestfs-building.1*
%_man1dir/guestfs-recipes.1*
%_man3dir/guestfs.3*
%_man3dir/guestfs-examples.3*
%_man3dir/libguestfs.3*
%_includedir/guestfs.h
%_pkgconfigdir/libguestfs.pc

%if_enabled introspection
%_libdir/libguestfs-gobject-*.so
%_includedir/guestfs-gobject
%_includedir/guestfs-gobject.h
%_pkgconfigdir/libguestfs-gobject-1.0.pc
%_man3dir/guestfs-gobject.3.*

%_girdir/*.gir

%if_enabled vala
%_datadir/vala/vapi/libguestfs-gobject-1.0.*
%endif
%endif #introspection

%if_enabled introspection
%files gobject
%_libdir/libguestfs-gobject-*.so.*

%files gir
%_typelibdir/*.typelib
%endif

%if_enabled golang
%files -n golang-guestfs
%doc golang/examples/*.go
%doc golang/examples/LICENSE
%_libdir/golang/src/libguestfs.org
%_man3dir/guestfs-golang.3*
%endif

%files -n guestfs-tools
%doc README
%config(noreplace) %_sysconfdir/libguestfs-tools.conf
%_man5dir/libguestfs-tools.conf.5*
%_sysconfdir/virt-builder
%dir %_sysconfdir/xdg/virt-builder
%dir %_sysconfdir/xdg/virt-builder/repos.d
%config %_sysconfdir/xdg/virt-builder/repos.d/libguestfs.conf
%config %_sysconfdir/xdg/virt-builder/repos.d/libguestfs.gpg
%config %_sysconfdir/xdg/virt-builder/repos.d/opensuse.conf
%config %_sysconfdir/xdg/virt-builder/repos.d/opensuse.gpg
%_bindir/guestfish
%_man1dir/guestfish.1*
%_bindir/guestmount
%_man1dir/guestmount.1*
%_bindir/guestunmount
%_man1dir/guestunmount.1*
%_bindir/virt-alignment-scan
%_man1dir/virt-alignment-scan.1*
%_bindir/virt-builder
%_man1dir/virt-builder.1*
%_bindir/virt-builder-repository
%_man1dir/virt-builder-repository.1*
%_bindir/virt-cat
%_man1dir/virt-cat.1*
%_bindir/virt-copy-in
%_man1dir/virt-copy-in.1*
%_bindir/virt-copy-out
%_man1dir/virt-copy-out.1*
%_bindir/virt-customize
%_man1dir/virt-customize.1*
%_bindir/virt-df
%_man1dir/virt-df.1*
%_bindir/virt-diff
%_man1dir/virt-diff.1*
%_bindir/virt-edit
%_man1dir/virt-edit.1*
%_bindir/virt-filesystems
%_man1dir/virt-filesystems.1*
%_bindir/virt-format
%_man1dir/virt-format.1*
%_bindir/virt-get-kernel
%_man1dir/virt-get-kernel.1*
%_bindir/virt-index-validate
%_man1dir/virt-index-validate.1*
%_bindir/virt-inspector
%_man1dir/virt-inspector.1*
%_bindir/virt-log
%_man1dir/virt-log.1*
%_bindir/virt-ls
%_man1dir/virt-ls.1*
%_bindir/virt-rescue
%_man1dir/virt-rescue.1*
%_bindir/virt-resize
%_man1dir/virt-resize.1*
%_bindir/virt-sparsify
%_man1dir/virt-sparsify.1*
%_bindir/virt-tar-in
%_man1dir/virt-tar-in.1*
%_bindir/virt-tail
%_man1dir/virt-tail.1*
%_bindir/virt-tar-out
%_man1dir/virt-tar-out.1*
%_bindir/virt-list-filesystems
%_man1dir/virt-list-filesystems.1*
%_bindir/virt-list-partitions
%_man1dir/virt-list-partitions.1*
%_bindir/virt-make-fs
%_man1dir/virt-make-fs.1*
%_bindir/virt-sysprep
%_man1dir/virt-sysprep.1*
%_bindir/virt-tar
%_man1dir/virt-tar.1*
%_bindir/virt-win-reg
%_man1dir/virt-win-reg.1*
%_man1dir/guestfs-faq.1*
%_man1dir/guestfs-hacking.1*
%_man1dir/guestfs-internals.1*
%_man1dir/guestfs-performance.1*
%_man1dir/guestfs-security.1*
%if_enabled bash_completion
%_datadir/bash-completion/completions/*
%endif

%files -n virt-dib
%_bindir/virt-dib
%_man1dir/virt-dib.1*

#%files live-service
#%doc COPYING README
#%_sbindir/guestfsd
#%_unitdir/guestfsd.service
#/lib/udev/rules.d/99-guestfs-serial.rules
#/lib/udev/rules.d/99-guestfsd.rules

%if_enabled ocaml
%files -n ocaml-%name
%_libdir/ocaml/guestfs
%exclude %_libdir/ocaml/guestfs/*.a
%exclude %_libdir/ocaml/guestfs/*.cmxa
%exclude %_libdir/ocaml/guestfs/*.cmx
%exclude %_libdir/ocaml/guestfs/*.mli
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner

%files -n ocaml-%name-devel
%doc ocaml/examples/*.ml
%_libdir/ocaml/guestfs/*.a
%_libdir/ocaml/guestfs/*.cmxa
%_libdir/ocaml/guestfs/*.cmx
%_libdir/ocaml/guestfs/*.mli
%_man3dir/guestfs-ocaml.3*
%endif #ocaml

%if_enabled perl
%files -n perl-Sys-Guestfs
%doc perl/examples
%perl_vendor_archlib/*
#%_man3dir/Sys::Guestfs.3pm*
#%_man3dir/Sys::Guestfs::Lib.3pm*
%_man3dir/guestfs-perl.3*
%endif #perl

%if_enabled python
%files -n python3-module-%name
%doc python/examples/*.py
%python3_sitelibdir/*
%_man3dir/guestfs-python.3*
%endif #python

%if_enabled ruby
%files -n ruby-%name
%doc ruby/examples/*.rb
%doc ruby/doc/site/*
%ruby_sitelibdir/guestfs.rb
%ruby_sitearchdir/_guestfs.so
%_man3dir/guestfs-ruby.3*
%endif #ruby

%files java
%_libdir/libguestfs_jni*.so.*
%_datadir/java/*.jar

%files java-devel
%_libdir/libguestfs_jni*.so
%_man3dir/guestfs-java.3*

%files javadoc
%_datadir/javadoc/%name

%if_enabled php
%files -n php7-%name
%doc php/README-PHP
%dir %_sysconfdir/php.d
%_sysconfdir/php.d/guestfs_php.ini
%_libdir/php/modules/guestfs_php.so
%endif #php

%if_enabled erlang
%files -n erlang-%name
%doc erlang/README
%doc erlang/examples/*.erl
%doc erlang/examples/LICENSE
%_bindir/erl-guestfs
%_libdir/erlang/lib/%name-%version
%_man3dir/guestfs-erlang.3*
%endif #erlang

%changelog
* Tue Jun 30 2020 Alexey Shabalin <shaba@altlinux.org> 1.42.0-alt2
- Set default guestfs appliance path to $libdir/guestfs

* Fri Apr 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.42.0-alt1
- 1.42.0
- build with vala support
- drop virt-p2v and virt-v2v

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.40.2-alt3
- removed python-2 support
- fixed build with python-3.8 by patch from upstream

* Thu Jul 18 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.40.2-alt2
- %%build: changed to always pass distro name to configure script in case
  /etc/os-release file is missing.
- %name: added R: guestfs-data on aarch64.

* Wed Apr 03 2019 Alexey Shabalin <shaba@altlinux.org> 1.40.2-alt1
- 1.40.2

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.38.6-alt3.1
- rebuild with new perl 5.28.1

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.38.6-alt3
- build python3 package
- build bash-completion package

* Sat Oct 20 2018 Anton Farygin <rider@altlinux.ru> 1.38.6-alt2
- rebuilt with ocaml-4.07.1

* Thu Oct 18 2018 Alexey Shabalin <shaba@altlinux.org> 1.38.6-alt1
- 1.38.6

* Tue Oct 09 2018 Alexey Shabalin <shaba@altlinux.org> 1.36.15-alt1
- 1.36.15

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.36.9-alt2
- rebuilt with ocaml 4.07

* Mon May 21 2018 Anton Farygin <rider@altlinux.ru> 1.36.9-alt1
- rebuilt for ocaml 4.06.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.36.5-alt1.1
- rebuild with new perl 5.26.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.36.5-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.36.3-alt3
- rebuild with ocaml 4.04.1

* Thu Apr 27 2017 Anton Farygin <rider@altlinux.ru> 1.36.3-alt2
- using /var/tmp for tmppath in virt-* tools instead of TMPDIR
- added ubt tag
- added /lib/systemd/systemd-machined  requires to guestfs-tools 

* Mon Apr 03 2017 Anton Farygin <rider@altlinux.ru> 1.36.3-alt2
- rebuild with ocaml-4
- ocaml modules renamed back to ocaml-*

* Tue Mar 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.36.3-alt1
- 1.36.3

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.33.38-alt1.1
- rebuild with new perl 5.24.1

* Wed Jun 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.33.38-alt1
- 1.33.38

* Thu May 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1.32.4-alt1
- 1.32.4

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.32.0-alt1
- 1.32.0

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.31.17-alt1.1
- rebuild with new perl 5.22.0

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.31.17-alt1
- 1.31.17

* Thu Sep 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.31.6-alt1
- 1.31.6

* Thu Jul 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.29.6-alt2
- vkni@: Rebuild with new rpm-build-ocaml4. Renamed ocaml packages to ocaml4-.

* Thu Feb 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.29.6-alt1
- 1.29.6

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.29.2-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.29.2-alt1
- 1.29.2

* Tue Sep 03 2013 Vladimir Lettiev <crux@altlinux.ru> 1.23.19-alt2
- built for perl 5.18

* Fri Aug 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.23.19-alt1
- 1.23.19

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.19.66-alt1
- 1.19.66

* Thu Sep 06 2012 Vladimir Lettiev <crux@altlinux.ru> 1.19.38-alt2
- rebuilt for perl-5.16

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 1.19.38-alt1
- 1.19.38

* Thu Jan 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.15.16-alt1
- initial build


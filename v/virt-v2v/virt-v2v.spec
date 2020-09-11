# The source directory.
%global source_directory 1.42-stable

Name: virt-v2v
Version: 1.43.1
Release: alt2
Summary: Convert a virtual machine to run on KVM
Group: Development/Other
License: GPLv2+
Url: https://github.com/libguestfs/virt-v2v

Source0: http://download.libguestfs.org/virt-v2v/%source_directory/%name-%version.tar.gz
Patch1: 0001-fix-fatal-error-pcreh-No-such-file-or-directory.patch
Patch2: add-alt-support.patch

BuildRequires(pre): rpm-build-ocaml
BuildRequires: /usr/bin/pod2man
BuildRequires: gcc
BuildRequires: ocaml >= 4.01 ocaml-findlib ocaml-ocamlbuild
BuildRequires: ocaml-libguestfs-devel
BuildRequires: ocaml-gettext-devel
BuildRequires: ocaml-fileutils-devel
BuildRequires: ocaml-ounit-devel
BuildRequires: libguestfs-devel
BuildRequires: libaugeas-devel
BuildRequires: bash-completion
BuildRequires: gettext-tools
BuildRequires: libjansson-devel
BuildRequires: libosinfo-devel
BuildRequires: libvirt-devel
BuildRequires: libvirt-kvm
BuildRequires: libxml2-devel
BuildRequires: libpcre-devel
BuildRequires: perl-Sys-Guestfs
BuildRequires: /usr/bin/virsh
BuildRequires: genisoimage zip unzip db4-utils
#BuildRequires: nbdkit-python-plugin


Requires: guestfs-tools
Requires: gawk
Requires: gzip
Requires: unzip
Requires: curl
Requires: /usr/bin/virsh

%description
Virt-v2v converts a single guest from a foreign hypervisor to run on
KVM.  It can read Linux and Windows guests running on VMware, Xen,
Hyper-V and some other hypervisors, and convert them to KVM managed by
libvirt, OpenStack, oVirt, Red Hat Virtualisation (RHV) or several
other targets.  It can modify the guest to make it bootable on KVM and
install virtio drivers so it will run quickly.


%prep
%setup
%patch2 -p1
pushd common
%patch1 -p1
popd

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# Delete libtool crap.
find %buildroot -name '*.la' -delete

# Delete the v2v test harness (except for the man page).
rm -r %buildroot%_libdir/ocaml/v2v_test_harness
rm -r %buildroot%_libdir/ocaml/stublibs/dllv2v_test_harness*

# Find locale files.
%find_lang %name

%files -f %name.lang
%doc COPYING README
%_bindir/virt-v2v*
%_man1dir/virt-v2v*
#%%_datadir/virt-tools
%_datadir/bash-completion/completions/virt-v2v*

%changelog
* Thu Sep 03 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.43.1-alt2
- Refactor (after discussions with upstream) ALT support

* Mon Aug 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.43.1-alt1
- update to 1.43.1
- Add ALT support

* Sun May 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.42.0-alt1
- Initial release of separate virt-v2v program, was part of libguestfs.

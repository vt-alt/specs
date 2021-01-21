Name: shim-signed
Version: 15
Release: alt2

Summary: UEFI RestrictedBoot shim signed by Microsoft
License: BSD
Group: System/Kernel and hardware

Url: https://github.com/rhboot/shim
Source: %name-%version.tar

BuildRequires: rpm-macros-uefi
ExclusiveArch: x86_64

%description
This package contains shim binaries signed by "Microsoft
Windows UEFI Driver Publisher" key for both EFI x64 and EFI ia32
architectures. MokManager (as mm*.efi) and fallback (as fb*.efi)
utilities signed by "ALT UEFI SB Signer 2013" are provided as well.

See https://github.com/rhboot/shim-review/issues/47 for details.

%prep
%setup

%install
mkdir -p %buildroot%_efi_bindir %buildroot%_libexecdir/shim
install -p *.efi %buildroot%_efi_bindir/
install -p BOOT*.CSV %buildroot%_libexecdir/shim/
# both should end up within /usr
for pefile in $(ls %buildroot%_efi_bindir/*.efi | rev | cut -d/ -f1 | rev);
  do
	ln %buildroot%_efi_bindir/$pefile \
		%buildroot%_libexecdir/shim/$pefile.signed
  done

%files
%attr(0644,root,root) %_efi_bindir/*.efi
%attr(0644,root,root) %_libexecdir/shim/*.efi.signed
%attr(0644,root,root) %_libexecdir/shim/BOOT*.CSV

%changelog
* Mon Dec 21 2020 Nikolai Kostrigin <nickel@altlinux.org> 15-alt2
- add BOOT<efi_arch>.CSV files for fallback boot variable creation

* Mon Mar 18 2019 Nikolai Kostrigin <nickel@altlinux.org> 15-alt1
- new shim version
  + add EFI ia32 binaries as well
  + MokManager and fallback are now renamed to mm<efi_arch>.efi and
    fb<efi_arch>.efi respectively
- adjust spec accordingly to new upstream

* Fri Jun 09 2017 Michael Shigorin <mike@altlinux.org> 0.4-alt6
- built for sisyphus

* Wed Jun 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt5
- made shim binaries accessible also by debian'ish paths

* Sat Apr 01 2017 Michael Shigorin <mike@altlinux.org> 0.4-alt4
- removed ALT signature (closes: #33314)

* Tue Dec 10 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt3
- added ALT signature

* Fri Nov 22 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt2
- added fallback.efi
- signed supplementary binaries with ALT key for versatility

* Tue Nov 19 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- ALT build

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- only makes sense for x86_64

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- initial release

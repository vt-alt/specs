Name: atf-sunxi
Version: 2.4
Release: alt1

Summary: ARM Trusted Firmware
License: BSD
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including Exception Level 3 (EL3) software.
This release provides support for the Allwinner A64/H5/H6 SoC families.

%prep
%setup

%build
for plat in sun50i_a64 sun50i_h6; do
	make PLAT=$plat bl31
	install -pm0644 -D build/$plat/release/bl31.bin out/$plat/bl31.bin
	make distclean
done

%install
mkdir -p %buildroot%_datadir/atf
cp -a out/* %buildroot%_datadir/atf/

%files
%_datadir/atf/*

%changelog
* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- 2.4 released

* Thu Jul 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3-alt1
- 2.3 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Mon Apr 15 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Fri Jan 25 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- 2.0-686-ga1d1d24b

* Mon Oct 02 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- initial

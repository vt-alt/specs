%def_disable static

Name: libksba
Version: 1.3.6
Release: alt14

Group: System/Libraries
Summary: X.509 library
URL: http://www.gnupg.org/
License: LGPLv3 / GPLv2

Source0: %name-%version.tar
Patch1:		%{name}-info.patch

# GOST patch
%define gostversion 2.0.0
Patch2: %name-%version-derutil.patch
Patch3: %name-%version-gost-cms.patch
Patch4: %name-%version-pkcs7-gost.patch
#Patch5: %name-%version-pkcs8.patch
Provides: %name(gost) = %gostversion

# Automatically added by buildreq on Tue Apr 06 2004 (-bi)
#BuildRequires: gcc-c++ gcc-g77 libgcrypt-devel libgpg-error-devel libstdc++-devel
BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ libgcrypt-devel libstdc++-devel
BuildRequires: libgpg-error-devel >= 0.6
BuildRequires: texinfo

%description
KSBA is a library designed to build software based
on the X.509 and CMS protocols.

%package -n %name-devel
Summary: Development files for the %name package
Group: Development/Other
Requires: %name = %version-%release
%description -n %name-devel
Development files for the %name package

%package -n %name-devel-static
Summary: Static libraries for the %name-devel package
Group: Development/Other
Requires: %name-devel = %version-%release
Requires: glibc-devel-static
%description -n %name-devel-static
Static libraries for the %name-devel package

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1

%build
#__aclocal
#__autoconf
#__automake
./autogen.sh
%configure \
    %{subst_enable static} \
    --enable-ld-version-script
%make_build

%install
%makeinstall
#rm -fv %buildroot/usr/share/info/dir

%check
%make_build check

%files
%doc AUTHORS NEWS README 
%_libdir/*.so.8
%_libdir/*.so.*

%files -n %name-devel
%doc TODO ChangeLog
%_bindir/*
%prefix/share/aclocal/*
%prefix/include/*.h
#%_libdir/*.la
%_libdir/*.so
%_infodir/*.info*

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif

%changelog
* Sun Nov 08 2020 Michael Shigorin <mike@altlinux.org> 1.3.6-alt14
- srpm_cleanup related ftbfs fixup

* Tue Oct 22 2019 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt13
- Maintenance release.

* Wed Oct 16 2019 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt12
- Fix the PKCS#7 parser: by '*' skip only the first bit/octet string.

* Tue Oct 15 2019 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt11
- Postpone PKCS#8 (private key) modifications.

* Tue Oct 15 2019 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt10
- Switch the autotests on.

* Tue Oct 15 2019 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt9
- Reworked ASN.1 PKCS#7 parser / builder with GOST support.
- Support of GOST-R.3410-2012 and the appropriate cipher S-box.
- Make read_values() not to skip leading zeros of a value.
- Fixed read_values(): handle the default case with no parameters.
- Try to support the headless RSA private key format.

* Wed Dec 19 2018 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt8
- Fixed writing the algorithm capabilities.
- Fixed read_values() for an unspecified (RSA) value.

* Tue Dec 18 2018 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt7
- Parse and save the data encryption S-Box OID.
- Implement AlgorithmIdentifier parameters parser and use it to parse
  the ContentEncryptionAlgorithmIdentifier properly getting the IV.
- Flip the ECC key coords prior to write them to the CMS structure.
- Fixed writing of an uncompressed point to CMS.
- Fixed public key DER -> SEXP parsing.
- Specify the Verba-0 digest.
- Write down the symmetric cipher parameters (CMS).
- Make _ksba_der_write_algorithm_identifier() more flexible related
  to paramter types and count.
- Fixed ephemeral public key encoding + missing UKM.
- Encode GOST key transport (compiles).
- Encode GOST key transport (draft).
- Store curve and digest parameters in the GOST key transfer
  structure.
- Added some structures from TK26CMS.1.1.
- Use "--km-b--p-CD-Qu" parsing formula for GOST CMS encrypted data.
- Added GOST 2012 to the encryption algos table.

* Wed Nov 07 2018 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt6
- Fixed/restored parsing of bit strings.

* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt5
- Include GOST patches into the main package version.
- Set the GOST CMS signature value.
- Added GOST patch (thx Dmitry Eremin-Solenikov).

* Tue Oct 02 2018 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt4.gost
- Set the GOST CMS signature value.
- Restore build-generated files and revert the corresponding changes
  in the spec.

* Fri Sep 07 2018 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt3.gost
- GOST patch version 1.0.0 providing the virtual package.

* Thu Sep 06 2018 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt2.gost
- Added GOST patch (thx Dmitry Eremin-Solenikov).
- Remove unused patches (source package).
- Remove build-generated files (source package).
- Use autoreconf for setup.

* Tue Aug 07 2018 Paul Wolneykien <manowar@altlinux.org> 1.3.6-alt1
- New version 1.3.6 (development).

* Mon Sep 18 2017 Sergey V Turchin <zerg@altlinux.org> 1.3.5-alt1
- new version

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 1.3.3-alt2
- fix build requires

* Tue Jun 23 2015 Sergey V Turchin <zerg@altlinux.org> 1.3.3-alt1
- new version

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt0.M70P.1
- built for M70P

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt1
- new version

* Thu Sep 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.8-alt0.M51.1
- built for M51

* Wed Jul 21 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.8-alt1
- new version

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 1.0.5-alt1
- new version
- remove deprecated macroses from specfile

* Tue Sep 23 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.4-alt1
- new version

* Thu Feb 14 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt1
- new version

* Tue Jul 10 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.2-alt1
- new version

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- new version

* Fri Sep 01 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Fri Jan 20 2006 Sergey V Turchin <zerg at altlinux dot org> 0.9.13-alt1
- new version

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 0.9.11-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9.9-alt1
- new version

* Fri Apr 16 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9.5-alt1
- new version

* Mon Apr 05 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9.4-alt1
- new version
- sync patches with PLD

* Fri Nov 28 2003 Sergey V Turchin <zerg at altlinux dot org> 0.4.7-alt2
- remove *.la files

* Wed Sep 03 2003 Sergey V Turchin <zerg at altlinux dot org> 0.4.7-alt1
- new version

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.4.6-alt2
- fix requires

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.4.6-alt1
- build for ALT

* Wed Dec 11 2002 Fabrice MARIE <fabrice-marie-sec@ifrance.com> 0.4.6-1mdk
- update to version 0.4.6

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.5-1mdk
- First package


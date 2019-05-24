%def_enable doc

Summary:          Library to support IDNA2008 internationalized domain names
Name:             libidn2
Version:          2.2.0
Release:          alt1
License:          (GPLv2+ or LGPLv3+) and GPLv3+
Group:            System/Libraries
URL:              https://www.gnu.org/software/libidn/#libidn2
Source0:          %name-%version.tar
BuildRequires:    libunistring-devel
# Needed for autoreconf
BuildRequires: /usr/bin/gtkdocize
%{?_enable_doc:BuildRequires: texinfo ronn groff-base}

Requires: libunistring2 >= 0.9.8-alt1

%define _unpackaged_files_terminate_build 1

%description
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892, 5893 and TR46 for internationalized domain names
(IDN). It is a standalone library, without any dependency on libidn.

%package devel
Summary:          Development files for libidn2
Group:            Development/Other
Requires:         %name = %version-%release

%description devel
The libidn2-devel package contains libraries and header files for
developing applications that use libidn2.

%package -n idn2
Summary:          Libidn2 Internationalized Domain Names conversion tool
Group:            Networking/DNS

%description -n idn2
idn2 tool converts DNS domains from UTF-8 to ASCII compatibile encoding (ACE)
form, as used in the DNS protocol. The encoding format is the Internationalized
Domain Name (IDNA2008/TR46) format.

%prep
%setup
# Workaround for generating idn2.1
rm doc/idn2.1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-silent-rules \
	%{subst_enable doc}

%make_build

%install
%makeinstall_std

# Clean-up examples for documentation
%make_build -C examples distclean
rm -f examples/Makefile*

# Relocate shared libraries from %%_libdir/ to /%%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink -v "$f")
	ln -fnrs %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%find_lang %name

%check
%make_build -C tests check

%files -f %name.lang
%doc COPYING COPYING.LESSERv3 COPYING.unicode COPYINGv2
%doc AUTHORS NEWS README.md
/%_lib/%name.so.*

%files devel
%doc doc/%name.html examples
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_includedir/*.h
%if_enabled doc
%_man3dir/*
%_datadir/gtk-doc/
%_infodir/%name.info*
%endif

%files -n idn2
%_bindir/idn2
%{?_enable_doc:%_man1dir/idn2.1*}

%changelog
* Thu May 23 2019 Mikhail Efremov <sem@altlinux.org> 2.2.0-alt1
- 2.1.1 -> 2.2.0.
- Drop libidn2.so.4 symlink and provides.

* Mon Feb 11 2019 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1
- Drop obsoleted patch.
- 2.1.0 -> 2.1.1.

* Tue Jan 22 2019 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt2
- Add symlink libidn2.so.4 -> libidn2.so.0.
- Change soname back to 0.

* Fri Jan 11 2019 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1
- Add symlink libidn2.so.0 -> libidn2.so.4.
- Workaround for generating idn2.1 man page.
- Add enable/disable documentation knob.
- 2.0.5 -> 2.1.0.

* Mon May 21 2018 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt1
- Package translations.
- 2.0.4 -> 2.0.5.

* Wed Jan 31 2018 Alexey Shabalin <shaba@altlinux.ru> 2.0.4-alt4
- Add R: libunistring2 >= 0.9.8-alt1 (library in /%_lib)

* Mon Jan 22 2018 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt3
- Use _unpackaged_files_terminate_build.
- Move library %_libdir -> /%_lib (closes: #34449).
- Move info to devel subpackage.

* Fri Jan 19 2018 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt2
- Disable silent rules.
- Split idn2 tool to separate subpackage.
- Drop rpath.patch and use autoreconf.
- Spec cleanup.
- Don't compress tarball.
- Drop unused libidn2-2.0.4.tar.gz.sig.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3.1
- NMU: added BR: texinfo

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_4
- update to new release by fcimport

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- initial import by fcimport


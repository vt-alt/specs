Name: adns
Version: 1.5.2
Release: alt1

Summary: GNU adns, an asynchronous DNS resolver
License: GPLv2+
Group: Networking/Other
URL: http://www.gnu.org/software/adns/

Source: adns-%version.tar
Patch0: %name-%version-alt.patch

Requires: lib%name = %version-%release

%package -n lib%name
Summary: GNU adns, an asynchronous DNS resolver (shared library)
Group: System/Libraries

%package -n lib%name-devel
Summary: GNU adns, an asynchronous DNS resolver (header files)
Group: Development/C
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: GNU adns, an asynchronous DNS resolver (static library)
Group: Development/C
Requires: lib%name-devel = %version-%release

%description
adns is a resolver library for C (and C++) programs,
and a collection of useful DNS resolver utilities.

This package contains %name utilities.

%description -n lib%name
adns is a resolver library for C (and C++) programs,
and a collection of useful DNS resolver utilities.

This package contains %name runtime library.

%description -n lib%name-devel
adns is a resolver library for C (and C++) programs,
and a collection of useful DNS resolver utilities.

This package contains developement library and include file
required for development of %name-based software.

%description -n lib%name-devel-static
adns is a resolver library for C (and C++) programs,
and a collection of useful DNS resolver utilities.

This package contains static library required for
development of statically linked %name-based software.

%prep
%setup
%patch0 -p1

%build
%configure
%make_build srcdir=$PWD/src

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir}
%makeinstall

%files
%_bindir/%{name}*
%doc GPL-vs-LGPL README TODO changelog

%files -n lib%name
%_libdir/lib%name.so.?*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so

%files -n lib%name-devel-static
%_libdir/lib%name.a

%changelog
* Sun Jun 14 2020 Anton Farygin <rider@altlinux.ru> 1.5.2-alt1
- 1.5.2 (Fixes: CVE-2017-9103 CVE-2017-9104 CVE-2017-9105 CVE-2017-9109, 
	CVE-2017-9106, CVE-2017-9107, CVE-2017-9108)

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2
- NMU: remove %ubt from release

* Thu May 11 2017 Anton Farygin <rider@altlinux.ru> 1.5.1-alt1
- new version

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.qa2
- Rebuilt for debuginfo

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Fri Feb 20 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt2
- Removed obsolete post_ldconfig/postun_ldconfig calls.
- Updated package descriptions.

* Fri Apr 13 2007 Alexey Tourbin <at@altlinux.ru> 1.4-alt1
- 1.3 -> 1.4

* Fri Sep 01 2006 Alexey Tourbin <at@altlinux.ru> 1.3-alt2
- resotred source compatility with earlier adns releases by providing
  adns__rrt_typemask constant (with the same value as adns_rrt_typemask);
  this should fix adns-python 1.1.0
- restricted symbols exported from the shared library

* Sat Jul 08 2006 Alexey Tourbin <at@altlinux.ru> 1.3-alt1
- 1.1 -> 1.3

* Sun Aug 15 2004 Alexey Tourbin <at@altlinux.ru> 1.1-alt1
- 1.0 -> 1.1
- use strict (%%release-dependent) rules between subpackages
- applied upstream patches:
  * Fix error in prototype in definition of adns__parse_domain.
  * Allow `;'-comments in resolv.conf (report from Colin Charles).
- packaged GPL-vs-LGPL, an indelicate GPL advocacy
- updated descriptions

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 1.0-ipl4mdk
- Split lib%name-devel to lib%name-devel-static

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.0-ipl3mdk
- rebuild

* Mon Jan 15 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl2mdk
- Split into %name, lib%name and lib%name-devel.

* Wed Nov 15 2000 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1mdk
- RE adaptions.

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0-1mdk
- new and shiny release.

* Fri Jul 21 2000 Warly <warly@mandrakesoft.com> 0.8-1mdk
- new release

* Tue May 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.7-4mdk
- Definitively remove the make check (stupid).

* Sun May 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.7-3mdk
- Work around for i486
- Fix prefix
- Use %%_tmppath for BuildRoot

* Thu Mar 23 2000 Florent Villard <warly@mandrakesoft.com> 0.7-2mdk
- rebuild

* Fri Mar  3 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.7-1mdk
- 0.7.
- clean spec and split in 2 packages.

* Mon Feb 07 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used srpm provided by Vincent Danen <vdanen@linux-mandrake.com>

* Sun Jan 30 2000 Vincent Danen <vdanen@linux-mandrake.com>
- initial specfile
- bzip sources

Epoch: 1
Packager: Vitaly Lipatov <lav@altlinux.ru>
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dvipdfm /usr/bin/makeindex gcc-c++ texlive-latex-base texlive-dist
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           gnucap
Version:        0.35
Release:        alt124
Summary:        The Gnu Circuit Analysis Package
Group:          Engineering
License:        GPLv2+
URL:            http://www.gnu.org/software/gnucap/
Source0:        http://www.gnucap.org/devel/gnucap-%{version}.tar.gz
Patch0:         gnucap-0.34-debian.patch
Patch1:         gnucap-0.35-gcc43.patch
Patch2:         gnucap-0.35-gcc6.patch
BuildRequires:  readline-devel
Source44: import.info

%ifnarch %e2k
BuildRequires: /usr/bin/hacha /usr/bin/hevea
%endif

%description
The primary component is a general purpose circuit simulator. It performs
nonlinear dc and transient analyses, fourier analysis, and ac analysis. Spice
compatible models for the MOSFET (level 1-7), BJT, and diode are included in
this release. Gnucap is not based on Spice, but some of the models have been
derived from the Berkeley models. Unlike Spice, the engine is designed to do
true mixed-mode simulation. Most of the code is in place for future support of
event driven analog simulation, and true multi-rate simulation.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# use ncurses instead of termcap (bz 226771)
sed -i 's/-ltermcap/-lncurses/g' configure


%build
%configure
%make_build


%install
%makeinstall_std

# for %%doc
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}
mv doc/acs-tutorial doc/gnucap-tutorial
rm examples/Makefile*


%files
%doc doc/history doc/relnotes.* doc/gnucap-tutorial doc/whatisit
%doc man/gnucap-man.pdf examples
%doc doc/COPYING
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Feb 09 2020 Vitaly Lipatov <lav@altlinux.ru> 1:0.35-alt124
- add BR: texlive-dist (fix missed dehypht.tex)

* Thu May 30 2019 Michael Shigorin <mike@altlinux.org> 1:0.35-alt123.2
- dropped self-BR:
- E2K: avoid hevea (not built yet)

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1:0.35-alt123.1
- autorebuild with libreadline7

* Mon Dec 04 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.35-alt1_23
- new version (closes: #34274)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20090822-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Aug 27 2009 Vitaly Lipatov <lav@altlinux.ru> 20090822-alt1
- new version 20090822 (with rpmrb script)

* Tue Jul 28 2009 Vitaly Lipatov <lav@altlinux.ru> 20090202-alt1
- new version 20090202 (with rpmrb script)

* Fri Nov 28 2008 Vitaly Lipatov <lav@altlinux.ru> 20080527-alt1
- new version (20080527)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 20070329-alt0.1
- new version (20070329)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 20060830-alt0.1
- new version (20060830)
- rewrite spec, update buildreq

* Wed Sep 14 2005 Vitaly Lipatov <lav@altlinux.ru> 20050610-alt0.1
- initial build for ALT Linux Sisyphus


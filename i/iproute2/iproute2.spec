%def_with libatm
%def_with selinux

Name: iproute2
Version: 5.3.0
Release: alt1

Summary: Advanced IP routing and network devices configuration tools
License: GPLv2+
Group: Networking/Other
Url: http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2
# git://git.altlinux.org/gears/i/%name.git
Source: %name-%version-%release.tar

Requires: libnetlink = %version-%release
Provides: iproute = %version-%release
Obsoletes: iproute < %version

# Automatically added by buildreq on Mon Jan 07 2019
BuildRequires: flex libcap-devel libdb4-devel libelf-devel libiptables-devel libmnl-devel
%{?_with_libatm:BuildRequires: libatm-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}

%description
The iproute package contains networking utilities (ip and rtmon, for
example) which are designed to use the advanced networking capabilities
of the Linux 2.4.x and 2.6.x kernel.

%package doc
Summary: Documentation for Advanced IP routing and network device configuration tools
Group: Networking/Other
BuildArch: noarch

%description doc
Documentation for iproute2.

%package -n arpd
Summary: The arpd daemon
Group: Networking/Other
Requires: %name = %version-%release

%description -n arpd
arpd is a daemon collecting gratuitous ARP information, saving it on
local disk and feeding it to kernel on demand to avoid redundant
broadcasting due to limited size of kernel ARP cache.

%package -n libnetlink
Summary: Netlink socket library
Group: System/Libraries

%description -n libnetlink
This package contains libnetlink dynamic library.

%package -n libnetlink-devel
Summary: Netlink socket library headers
Group: System/Libraries
Requires: libnetlink = %version-%release

%description -n libnetlink-devel
This package contains libnetlink dynamic library headers.

%prep
%setup -n %name-%version-%release

%build
%make_build DBM_INCLUDE=%_includedir/db4 LIBDIR=%_libdir CCOPTS='%optflags' V=1

%install
%makeinstall_std LIBDIR=%_libdir
cp -a doc/actions README* %buildroot%_docdir/%name/
mkdir -p %buildroot{%_bindir,%_sbindir,%_localstatedir/arpd}
pushd %buildroot/sbin
rm rtpr
mv arpd bridge ctstat genl ifstat lnstat nstat routef routel rtacct rtstat ss tipc \
	%buildroot%_sbindir/
popd

# libnetlink
mkdir -p %buildroot{%_includedir,%_libdir,%_man3dir,/%_lib}
install -p -m644 lib/libnetlink.so %buildroot/%_lib
install -p -m644 include/{libnetlink.h,ll_map.h} %buildroot%_includedir
install -p -m644 man/man3/libnetlink.3 %buildroot%_man3dir/
ln -rs %buildroot/%_lib/libnetlink.so %buildroot%_libdir/

# symlinks for unprivileged users
for prg in ip rtmon tc; do
	ln -rs %buildroot/sbin/$prg %buildroot%_bindir/
done
for prg in lnstat nstat routel ss; do
	ln -rs %buildroot%_sbindir/$prg %buildroot%_bindir/
done

%define _unpackaged_files_terminate_build 1

%files
/sbin/*
%_sbindir/*
%_bindir/*
%_libdir/tc/
%exclude %_sbindir/arpd
%config(noreplace) %_sysconfdir/%name
%_man7dir/*
%_man8dir/*
%_datadir/bash-completion/completions/tc

%files doc
%_docdir/%name/

%files -n arpd
%_sbindir/arpd
%attr(700,root,root) %dir %_localstatedir/arpd

%files -n libnetlink
/%_lib/libnetlink.so

%files -n libnetlink-devel
%_includedir/*
%_libdir/libnetlink.so
%_man3dir/*

%changelog
* Tue Sep 24 2019 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt1
- 5.2.0 -> 5.3.0.

* Mon Jul 08 2019 Dmitry V. Levin <ldv@altlinux.org> 5.2.0-alt1
- 5.1.0 -> 5.2.0.

* Fri May 10 2019 Dmitry V. Levin <ldv@altlinux.org> 5.1.0-alt1
- 5.0.0 -> 5.1.0.

* Tue Mar 19 2019 Dmitry V. Levin <ldv@altlinux.org> 5.0.0-alt1
- 4.20.0 -> 5.0.0.

* Mon Jan 07 2019 Dmitry V. Levin <ldv@altlinux.org> 4.20.0-alt1
- 4.18.0 -> 4.20.0.
- ip: enabled capability drop.

* Mon Aug 13 2018 Dmitry V. Levin <ldv@altlinux.org> 4.18.0-alt1
- 4.17.0 -> 4.18.0.

* Fri Jun 29 2018 Dmitry V. Levin <ldv@altlinux.org> 4.17.0-alt1
- 4.16.0 -> 4.17.0.

* Wed Apr 25 2018 Dmitry V. Levin <ldv@altlinux.org> 4.16.0-alt1
- 4.15.0 -> 4.16.0.

* Wed Apr 25 2018 Michael Shigorin <mike@altlinux.org> 4.15.0-alt2
- added selinux, bootstrap knobs (on by default).

* Mon Jan 29 2018 Dmitry V. Levin <ldv@altlinux.org> 4.15.0-alt1
- 4.14.1 -> 4.15.0.

* Wed Nov 15 2017 Dmitry V. Levin <ldv@altlinux.org> 4.14.1-alt1
- 4.12.0 -> 4.14.1.

* Wed Jul 05 2017 Dmitry V. Levin <ldv@altlinux.org> 4.12.0-alt1
- 4.11.0 -> 4.12.0.

* Mon May 01 2017 Dmitry V. Levin <ldv@altlinux.org> 4.11.0-alt1
- 4.4.0 -> 4.11.0.

* Tue Jan 19 2016 Dmitry V. Levin <ldv@altlinux.org> 4.4.0-alt1
- Updated to 4.4.0.

* Wed Nov 25 2015 Dmitry V. Levin <ldv@altlinux.org> 4.3.0-alt1
- Updated to 4.3.0.
- Packaged tipc(8).
- Enabled eBPF support in tc(8).
- Enabled SELinux support in ss(8).

* Fri Apr 25 2014 Dmitry V. Levin <ldv@altlinux.org> 3.14.0-alt1
- Updated to 3.14.0.

* Mon Nov 25 2013 Dmitry V. Levin <ldv@altlinux.org> 3.12.0-alt1
- Updated to 3.12.0.

* Mon Jul 22 2013 Dmitry V. Levin <ldv@altlinux.org> 3.10.0-alt1
- Updated to 3.10.0.

* Wed Mar 06 2013 Dmitry V. Levin <ldv@altlinux.org> 3.8.0-alt1
- Updated to v3.8.0-8-gae70d96.

* Wed Oct 10 2012 Dmitry V. Levin <ldv@altlinux.org> 3.6.0-alt1
- Updated to 3.6.0.
- Reviewed patches.

* Fri May 25 2012 Dmitry V. Levin <ldv@altlinux.org> 3.4.0-alt1
- Updated to 3.4.0.
- Built with libxtables.so.7.

* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 3.3.0-alt1
- 3.3.0
- Update source URL.

* Fri Jan 06 2012 Victor Forsiuk <force@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 3.1.0-alt1
- 3.1.0
- lnstat fix: dump to stdout instead of stderr.

* Fri Jul 01 2011 Victor Forsiuk <force@altlinux.org> 2.6.39-alt1
- 2.6.39

* Fri Apr 08 2011 Victor Forsiuk <force@altlinux.org> 2.6.38-alt2
- Fix FTBFS by refreshing BuildRequires.

* Fri Mar 25 2011 Victor Forsiuk <force@altlinux.org> 2.6.38-alt1
- 2.6.38

* Mon Jan 10 2011 Victor Forsiuk <force@altlinux.org> 2.6.37-alt1
- 2.6.37

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.35-alt2.1
- Rebuilt for soname set-versions.

* Thu Aug 12 2010 Victor Forsiuk <force@altlinux.org> 2.6.35-alt2
- Fix bug with 'ip route get' (Closes: #23872).

* Thu Aug 05 2010 Victor Forsiuk <force@altlinux.org> 2.6.35-alt1
- 2.6.35

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 2.6.34-alt1
- 2.6.34

* Tue Mar 02 2010 Victor Forsiuk <force@altlinux.org> 2.6.33-alt1
- 2.6.33

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 2.6.31-alt2
- Provide symlinks in /usr/bin to all utilities usable by unpriviledge users (closes: #22887).
- Rebuild against libxtables.so.4.

* Fri Jan 15 2010 Victor Forsyuk <force@altlinux.org> 2.6.31-alt1
- 2.6.31

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 2.6.29-alt1
- 2.6.29

* Fri Jan 16 2009 Victor Forsyuk <force@altlinux.org> 2.6.28-alt1
- 2.6.28

* Mon Dec 01 2008 Victor Forsyuk <force@altlinux.org> 2.6.26-alt1
- 2.6.26

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.6.25-alt1.1
- Automated rebuild with libdb-4.7.so.

* Thu May 22 2008 Victor Forsyuk <force@altlinux.org> 2.6.25-alt1
- 2.6.25
- Fix #15409 (segfault with tc qdisc).

* Fri Mar 14 2008 Victor Forsyuk <force@altlinux.org> 2.6.23-alt2
- Fix to restore backward compatibility with pre 2.6.22 kernels.

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 2.6.23-alt1
- 2.6.23

* Mon Apr 02 2007 Victor Forsyuk <force@altlinux.org> 2.6.20.20070313-alt1
- 20070313 snapshot.
- Add versioned dependency on libnetlink package (fix ALT#10845). Thanks to ldv@.

* Tue Feb 06 2007 Victor Forsyuk <force@altlinux.org> 2.6.19.20061214-alt1
- 20061214 snapshot.
- Fix ALT#6277.

* Thu Oct 12 2006 Victor Forsyuk <force@altlinux.org> 2.6.18.20061002-alt1
- Updated to 20061002 snapshot.
- Really fixed path to iptables libdir (also for 64-bit arch build).
- Package shared libnetlink library.
- Add LOWER_UP and DORMANT flags (RH#202199).
- Fix ip.8 man page: add initcwnd option description (RH).

* Wed Apr 26 2006 Victor Forsyuk <force@altlinux.ru> 2.6.16.20060323-alt1
- Updated to 20060323 snapshot.
- Don't hardcode /usr/lib in tc (important for 64-bit arch).
- Own %%_libdir/tc.
- Manpages now included into the original package.

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.6.15.20060110-alt1.1
- Rebuilt with libdb4.4.

* Thu Jan 19 2006 Victor Forsyuk <force@altlinux.ru> 2.6.15.20060110-alt1
- Updated to 20060110 snapshot.
- Package routel and routef scripts.
- Add Fedora patches.
- Move big postsript docs to separate package.
- Correct path to iptables libdir (fixes iptables based targets support).

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.7.20020116-alt5.1
- Rebuilt with libdb4.3.

* Sat May 01 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt5
- Fixed the potential buffer overflow in nstat discovered by Steve Grubb,
  and a number of other related potential issues in nstat (Owl).
- Fixed default rtnetlink table (patch from pilot@, #3707).
- Implemented ipsectun support (patch from pilot@, #3708).
- Fixed "ss -f" mode.
- Added tc-cbq-details(8) manpage.

* Fri Feb 13 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt4
- Packaged arpd to separate subpackage.
- Rebuilt with libdb-4.2.so.

* Wed Nov 12 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt3
- Fixed netlink issue (CAN-2003-0856).
- Moved CBQ and HTB init scripts to separate packages (#3095).

* Thu Oct 16 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt2
- /sbin/ifcfg: fixed potential syntax errors (#2422).

* Wed Oct 15 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt1
- Build with TC_CONFIG_DIFFSERV enabled.

* Mon Oct 13 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7-alt6.ss020116
- Updated to ss020116.
- Packaged new tools: arpd, ifstat, nstat, rtstat, ss.
- Removed obsolete patches:
  rh-config
  pld-owl-ll_types_proto
- Patched to use system headers - included ones seem to be broken.
- cbq.init: ignore config files with dots in their names (#3095).
- Added htb startup script.
- Moved Wondershaper to separate package.

* Wed Aug 27 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7-alt5.ss010824
- Updated build dependencies, fixed build.

* Wed Feb 05 2003 Andy Gorev <horror@altlinux.ru> 2.4.7-alt4.ss010824
- Script cbq.init updated from v0.6.2 to v0.7.2
- Patch tc for HTB3 support
- Wondershaper scripts added to doc (lartc.org)
- README-cbq-use fix (added to doc)

* Wed Oct 30 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.7-alt3.ss010824
- Rebuilt in new environment.

* Tue Apr 02 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.7-alt2.ss010824
- Updated code to ss010824.
- Fixed build without kernel-source installed.
- Merged in RH patches:
  + %name-2.4.7-rh-config.patch
  + %name-2.4.7-rh-promisc-allmulti.patch
- Merged in Owl patches:
  + %name-2.4.7-pld-owl-ll_types_proto.patch
  + %name-2.4.7-owl-warnings.patch
- Added manpages from Owl.

* Tue Aug 14 2001 Alexander Bokovoy <ab@altlinux.ru> 2.4.7-alt1
- 2.4.7, cbq.init 0.6.2

* Thu Jan 04 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.4-ipl10mdk
- Removed README.cbq-init, it is %_initdir/cbq now.
- Recompressed postscript documentation with bzip2 since
  our postscript viewer (gv) can show bzipped documents.

* Tue Dec 27 2000 Alexander Bokovoy <ab@avilink.net> 2.2.4-ipl9mdk
- Wrong dependency caused by wrong path (/sbin/arping) in example
  script dhcp-client-script fixed.

* Tue Dec 26 2000 Alexander Bokovoy <ab@avilink.net> 2.2.4-ipl8mdk
- Sally Floyd's papers added as well additional docs about CBQ
- cbq.init script integrated (it really should be in this package)

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 2.2.4-ipl7mdk
- ss001007.
- Merge RH patches.

* Mon Aug 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.2.4-ipl6mdk
- RE adaptions.

* Thu Aug 10 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2.4-6mdk
- fix config files

* Wed Jul 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2.4-5mdk
- BM

* Wed Jul 12 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 2.2.4-4mdk
- removed _sysconfdir
- added %clean

* Wed Jul 12 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2.4-3mdk
- fix a few typo (chrs scks :-) ) and make this spec short-circuit aware :
  *  _sysconfig/_sysconfdir
  *  creation of subdirs while installing
- Christian Zoffoli <czoffoli@linux-mandrake.com> : macroszifications

* Fri Apr 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.4-2mdk
- fix group and files section

* Wed Mar 01 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.4-1mdk
- mandrake build
- used latest release of 2.2.4 series / 000225

* Mon Apr 26 1999 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Added $RPM_OPT_FLAGS

* Fri Apr 23 1999 Damien Miller <damien@ibs.com.au>
- Built RPM

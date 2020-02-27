Name: lsof
Version: 4.93.2
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Lists files open by processes
License: Free
Group: Monitoring

URL: ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof
# This is REPACKAGED upstream source, read README.lsof.maintainer!
#Source: lsof-%version.tar.bz2
# Repackaged file is picked from http://pkgs.fedoraproject.org/repo/pkgs/lsof
Source: %name-%version.tar.xz
Source1: README.lsof.maintainer

%description
Lsof's name stands for LiSt Open Files, and it does just that. It lists
information about files that are open by the processes running on a UNIX
system.

%prep
%setup

%build
%add_optflags -DHASSECURITY -Dlint
#export LSOF_VSTR=2.6.16
./Configure -n linux
%make_build DEBUG="%optflags"

sed -e '/.so .\/00DIALECTS/d' \
    -e 's,.so ./version,.ds VN %version,' \
    Lsof.8 > lsof.8

%install
install -pD lsof %buildroot%_sbindir/lsof
install -pD -m644 lsof.8 %buildroot%_man8dir/lsof.8
mkdir -p %buildroot%_bindir
ln -rs %buildroot%_sbindir/lsof %buildroot%_bindir/

%files
%_sbindir/lsof
%_bindir/lsof
%_man8dir/lsof*
%doc 00*

%changelog
* Mon Dec 09 2019 Ivan A. Melnikov <iv@altlinux.org> 4.93.2-alt1
- Update, taking tarball from RH
- Add lsof symlink to %%_bindir (closes: #37594)

* Thu Aug 18 2016 Fr. Br. George <george@altlinux.ru> 4.89-alt1
- Update, taking tarball from RH

* Thu Aug 18 2016 Fr. Br. George <george@altlinux.ru> 4.88-alt1
- Update, taking tarball from RH

* Mon Oct 18 2010 Victor Forsiuk <force@altlinux.org> 4.84-alt1
- 4.84

* Thu Feb 11 2010 Victor Forsiuk <force@altlinux.org> 4.83-alt1
- 4.83

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 4.82-alt1
- 4.82

* Mon Jun 09 2008 Victor Forsyuk <force@altlinux.org> 4.80-alt1
- 4.80

* Tue May 08 2007 Victor Forsyuk <force@altlinux.org> 4.78-alt1
- 4.78

* Fri Oct 20 2006 Victor Forsyuk <force@altlinux.org> 4.77-alt1
- 4.77

* Thu Sep 29 2005 Victor Forsyuk <force@altlinux.ru> 4.76-alt1
- 4.76

* Wed May 18 2005 Victor Forsyuk <force@altlinux.ru> 4.74-alt1
- 4.74
- Fix "lsof -b" hangs if a process is stuck in disk-wait/NFS (RH#131712).

* Wed Mar 10 2004 Stanislav Ievlev <inger@altlinux.org> 4.70-alt1
- 4.70

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 4.65-alt1
- 4.65
- Build with "-DHASSECURITY -Dlint".

* Thu Jul 18 2002 Dmitry V. Levin <ldv@altlinux.org> 4.64-alt1
- 4.64

* Mon Feb 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 4.60-alt1
- 4.60

* Thu Jul 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.57-alt1
- 4.57

* Mon May 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.56-alt1
- 4.56

* Sat Feb 17 2001 Dmitry V. Levin <ldv@fandra.org> 4.55-ipl1mdk
- 4.55

* Mon Jan 22 2001 Dmitry V. Levin <ldv@fandra.org> 4.54-ipl1mdk
- 4.54

* Fri Dec 08 2000 Dmitry V. Levin <ldv@fandra.org> 4.53-ipl1mdk
- RE adaptions.

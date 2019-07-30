Name: parallel
Version: 20190622
Release: alt1

Summary: A shell tool for executing jobs in parallel
License: GPLv3
Group: File tools

Url: http://www.gnu.org/software/parallel
Source: http://ftp.gnu.org/gnu/parallel/%name-%version.tar.bz2
Source100: parallel.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Apr 16 2013
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators
BuildRequires: perl-Pod-Parser perl-devel

BuildArch: noarch

%set_findreq_skiplist %_bindir/env_parallel.*

%description
GNU parallel is a shell tool for executing jobs in parallel
locally or using remote machines. A job is typically a single
command or a small script that has to be run for each of the
lines in the input. The typical input is a list of files, a list
of hosts, a list of users, a list of URLs, or a list of tables.

%prep
%setup

%build
%configure
%make

%install
%makeinstall_std
rm -r %buildroot%_defaultdocdir/%name/

# *sigh*
ln -sf parallel %buildroot%_bindir/sem

%files
%doc README NEWS src/*.html
%_bindir/*
%_man1dir/*
%_man7dir/*

%changelog
* Sat Jun 22 2019 Michael Shigorin <mike@altlinux.org> 20190622-alt1
- new version (watch file uupdate)

* Thu May 23 2019 Michael Shigorin <mike@altlinux.org> 20190522-alt1
- new version (watch file uupdate)

* Mon Apr 22 2019 Michael Shigorin <mike@altlinux.org> 20190422-alt1
- new version (watch file uupdate)

* Fri Mar 22 2019 Michael Shigorin <mike@altlinux.org> 20190322-alt1
- new version (watch file uupdate)

* Sun Feb 24 2019 Michael Shigorin <mike@altlinux.org> 20190222-alt1
- new version (watch file uupdate)

* Tue Jan 22 2019 Michael Shigorin <mike@altlinux.org> 20190122-alt1
- new version (watch file uupdate)

* Sat Dec 22 2018 Michael Shigorin <mike@altlinux.org> 20181222-alt1
- new version (watch file uupdate)

* Sat Nov 24 2018 Michael Shigorin <mike@altlinux.org> 20181122-alt1
- new version (watch file uupdate)

* Tue Oct 23 2018 Michael Shigorin <mike@altlinux.org> 20181022-alt1
- new version (watch file uupdate)

* Mon Sep 24 2018 Michael Shigorin <mike@altlinux.org> 20180922-alt1
- new version (watch file uupdate)

* Sat Aug 25 2018 Michael Shigorin <mike@altlinux.org> 20180822-alt1
- new version (watch file uupdate)

* Mon Jul 23 2018 Michael Shigorin <mike@altlinux.org> 20180722-alt1
- new version (watch file uupdate)

* Thu Jun 21 2018 Michael Shigorin <mike@altlinux.org> 20180622-alt1
- new version (watch file uupdate)

* Wed May 23 2018 Michael Shigorin <mike@altlinux.org> 20180522-alt1
- new version (watch file uupdate)

* Fri Apr 27 2018 Michael Shigorin <mike@altlinux.org> 20180422-alt1
- new version (watch file uupdate)

* Fri Mar 23 2018 Michael Shigorin <mike@altlinux.org> 20180322-alt1
- new version (watch file uupdate)

* Fri Feb 23 2018 Michael Shigorin <mike@altlinux.org> 20180222-alt1
- new version (watch file uupdate)

* Mon Jan 22 2018 Michael Shigorin <mike@altlinux.org> 20180122-alt1
- new version (watch file uupdate)

* Mon Dec 25 2017 Michael Shigorin <mike@altlinux.org> 20171222-alt1
- new version (watch file uupdate)

* Fri Nov 24 2017 Michael Shigorin <mike@altlinux.org> 20171122-alt1
- new version (watch file uupdate)

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 20171022-alt1
- new version (watch file uupdate)

* Sat Sep 23 2017 Michael Shigorin <mike@altlinux.org> 20170922-alt1
- new version (watch file uupdate)

* Tue Aug 22 2017 Michael Shigorin <mike@altlinux.org> 20170822-alt1
- new version (watch file uupdate)

* Tue Jul 25 2017 Michael Shigorin <mike@altlinux.org> 20170722-alt1
- new version (watch file uupdate)

* Mon Jun 26 2017 Michael Shigorin <mike@altlinux.org> 20170622-alt1
- new version (watch file uupdate)

* Mon May 22 2017 Michael Shigorin <mike@altlinux.org> 20170522-alt1
- new version (watch file uupdate)

* Tue May 09 2017 Michael Shigorin <mike@altlinux.org> 20170422-alt1
- new version (watch file uupdate)

* Sat Mar 25 2017 Michael Shigorin <mike@altlinux.org> 20170322-alt1
- new version (watch file uupdate)

* Thu Feb 23 2017 Michael Shigorin <mike@altlinux.org> 20170222-alt1
- new version (watch file uupdate)

* Mon Jan 23 2017 Michael Shigorin <mike@altlinux.org> 20170122-alt1
- new version (watch file uupdate)

* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 20161222-alt1
- new version (watch file uupdate)

* Sun Dec 04 2016 Michael Shigorin <mike@altlinux.org> 20161122-alt1
- new version (watch file uupdate)

* Sat Oct 22 2016 Michael Shigorin <mike@altlinux.org> 20161022-alt1
- new version (watch file uupdate)

* Sat Sep 24 2016 Michael Shigorin <mike@altlinux.org> 20160922-alt1
- new version (watch file uupdate)

* Mon Aug 22 2016 Michael Shigorin <mike@altlinux.org> 20160822-alt1
- new version (watch file uupdate)

* Tue Jul 26 2016 Michael Shigorin <mike@altlinux.org> 20160722-alt1
- new version (watch file uupdate)

* Mon Jun 20 2016 Michael Shigorin <mike@altlinux.org> 20160622-alt1
- new version (watch file uupdate)

* Mon May 23 2016 Michael Shigorin <mike@altlinux.org> 20160522-alt1
- new version (watch file uupdate)

* Sat Apr 23 2016 Michael Shigorin <mike@altlinux.org> 20160422-alt2
- suppress extra requires (closes: #32016)

* Fri Apr 22 2016 Michael Shigorin <mike@altlinux.org> 20160422-alt1
- new version (watch file uupdate)

* Wed Mar 23 2016 Michael Shigorin <mike@altlinux.org> 20160322-alt1
- new version (watch file uupdate)

* Mon Feb 22 2016 Michael Shigorin <mike@altlinux.org> 20160222-alt1
- new version (watch file uupdate)

* Sat Jan 23 2016 Michael Shigorin <mike@altlinux.org> 20160122-alt1
- new version (watch file uupdate)

* Tue Dec 22 2015 Michael Shigorin <mike@altlinux.org> 20151222-alt1
- new version (watch file uupdate)

* Mon Nov 23 2015 Michael Shigorin <mike@altlinux.org> 20151122-alt1
- new version (watch file uupdate)

* Thu Oct 22 2015 Michael Shigorin <mike@altlinux.org> 20151022-alt1
- new version (watch file uupdate)

* Tue Sep 22 2015 Michael Shigorin <mike@altlinux.org> 20150922-alt1
- new version (watch file uupdate)

* Sat Aug 22 2015 Michael Shigorin <mike@altlinux.org> 20150822-alt1
- new version (watch file uupdate)

* Wed Jul 22 2015 Michael Shigorin <mike@altlinux.org> 20150722-alt1
- new version (watch file uupdate)

* Mon Jun 22 2015 Michael Shigorin <mike@altlinux.org> 20150622-alt1
- new version (watch file uupdate)

* Fri May 22 2015 Michael Shigorin <mike@altlinux.org> 20150522-alt1
- new version (watch file uupdate)
- security fixes, see
  http://lists.gnu.org/archive/html/parallel/2015-04/msg00045.html

* Thu Apr 23 2015 Michael Shigorin <mike@altlinux.org> 20150422-alt1
- new version (watch file uupdate)

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 20150322-alt1
- new version (watch file uupdate)

* Sun Feb 22 2015 Michael Shigorin <mike@altlinux.org> 20150222-alt1
- new version (watch file uupdate)

* Thu Jan 22 2015 Michael Shigorin <mike@altlinux.org> 20150122-alt1
- new version (watch file uupdate)

* Sun Nov 23 2014 Michael Shigorin <mike@altlinux.org> 20141122-alt1
- new version (watch file uupdate)

* Thu Oct 23 2014 Michael Shigorin <mike@altlinux.org> 20141022-alt1
- new version (watch file uupdate)
  + NB: --env adjusted to deal with bash fix of 'shellshock' vulnerability

* Mon Sep 22 2014 Michael Shigorin <mike@altlinux.org> 20140922-alt1
- new version (watch file uupdate)

* Mon Aug 25 2014 Michael Shigorin <mike@altlinux.org> 20140822-alt1
- new version (watch file uupdate)

* Tue Jul 22 2014 Michael Shigorin <mike@altlinux.org> 20140722-alt1
- new version (watch file uupdate)

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 20140622-alt1
- new version (watch file uupdate)

* Thu May 22 2014 Michael Shigorin <mike@altlinux.org> 20140522-alt1
- new version (watch file uupdate)

* Tue Apr 22 2014 Michael Shigorin <mike@altlinux.org> 20140422-alt1
- new version (watch file uupdate)

* Sat Mar 22 2014 Michael Shigorin <mike@altlinux.org> 20140322-alt1
- new version (watch file uupdate)

* Wed Jan 22 2014 Michael Shigorin <mike@altlinux.org> 20140122-alt1
- new version (watch file uupdate)

* Sun Dec 22 2013 Michael Shigorin <mike@altlinux.org> 20131222-alt1
- new version (watch file uupdate)
- NB: "this release is alpha quality"

* Sat Nov 23 2013 Michael Shigorin <mike@altlinux.org> 20131122-alt1
- new version (watch file uupdate)

* Tue Oct 22 2013 Michael Shigorin <mike@altlinux.org> 20131022-alt1
- new version (watch file uupdate)

* Sat Sep 21 2013 Michael Shigorin <mike@altlinux.org> 20130922-alt1
- new version (watch file uupdate)

* Thu Aug 22 2013 Michael Shigorin <mike@altlinux.org> 20130822-alt1
- new version (watch file uupdate)

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 20130722-alt1
- new version (watch file uupdate)

* Sat Jun 22 2013 Michael Shigorin <mike@altlinux.org> 20130622-alt1
- new version (watch file uupdate)

* Wed May 22 2013 Michael Shigorin <mike@altlinux.org> 20130522-alt1
- new version (watch file uupdate)

* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 20130422-alt1
- new version (watch file uupdate)

* Tue Apr 16 2013 Michael Shigorin <mike@altlinux.org> 20130222-alt2
- buildreq (thus cleaned up extremely weird BRs from 2011)

* Fri Feb 22 2013 Michael Shigorin <mike@altlinux.org> 20130222-alt1
- new version (watch file uupdate)
- dropped bzr from BR

* Tue Jan 22 2013 Michael Shigorin <mike@altlinux.org> 20130122-alt1
- new version (watch file uupdate)

* Sun Dec 23 2012 Michael Shigorin <mike@altlinux.org> 20121222-alt1
- new version (watch file uupdate)

* Thu Nov 22 2012 Michael Shigorin <mike@altlinux.org> 20121122-alt1
- new version (watch file uupdate)

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 20121022-alt1
- new version (watch file uupdate)

* Thu Aug 23 2012 Michael Shigorin <mike@altlinux.org> 20120822-alt1
- new version (watch file uupdate)

* Sat Jun 23 2012 Michael Shigorin <mike@altlinux.org> 20120622-alt1
- new version (watch file uupdate)

* Tue May 22 2012 Michael Shigorin <mike@altlinux.org> 20120522-alt1
- new version (watch file uupdate)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 20120422-alt2
- added watch file

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 20120422-alt1
- 20120422

* Fri Mar 23 2012 Michael Shigorin <mike@altlinux.org> 20120322-alt1
- 20120322 (bugfixes only, no new features)

* Tue Feb 28 2012 Michael Shigorin <mike@altlinux.org> 20120222-alt1
- 20120222

* Sun Jan 22 2012 Michael Shigorin <mike@altlinux.org> 20120122-alt1
- 20120122

* Thu Dec 22 2011 Michael Shigorin <mike@altlinux.org> 20111222-alt1
- 20111222

* Wed Nov 23 2011 Michael Shigorin <mike@altlinux.org> 20111122-alt1
- 20111122

* Sun Oct 23 2011 Michael Shigorin <mike@altlinux.org> 20111022-alt1
- 20111022

* Mon Aug 22 2011 Michael Shigorin <mike@altlinux.org> 20110822-alt1
- 20110822

* Fri Jul 22 2011 Michael Shigorin <mike@altlinux.org> 20110722-alt1
- 20110722

* Wed Jun 22 2011 Michael Shigorin <mike@altlinux.org> 20110622-alt1
- 20110622

* Sun May 22 2011 Michael Shigorin <mike@altlinux.org> 20110522-alt1
- 20110522

* Fri Apr 22 2011 Michael Shigorin <mike@altlinux.org> 20110422-alt1
- 20110422

* Tue Mar 22 2011 Michael Shigorin <mike@altlinux.org> 20110322-alt1
- 20110322

* Tue Feb 08 2011 Michael Shigorin <mike@altlinux.org> 20110205-alt1
- 20110205

* Sun Jan 23 2011 Michael Shigorin <mike@altlinux.org> 20110122-alt1
- 20110122

* Wed Dec 22 2010 Michael Shigorin <mike@altlinux.org> 20101222-alt1
- 20101222

* Sat Dec 04 2010 Michael Shigorin <mike@altlinux.org> 20101202-alt1
- 20101202

* Thu Nov 18 2010 Michael Shigorin <mike@altlinux.org> 20101113-alt1
- 20101113

* Thu Sep 23 2010 Michael Shigorin <mike@altlinux.org> 20100922-alt1
- 20100922

* Tue Sep 07 2010 Michael Shigorin <mike@altlinux.org> 20100906-alt1
- 20100906
  + added sem(1) and sql(1)

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 20100722-alt1
- built for ALT Linux (based on cooker spec)
- include HTML documentation
- noarch

* Thu Jul 29 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100722-3mdv2011.0
+ Revision: 563194
- fix summary with "shell tool", recommended by upstream.
- fix summary (thanks Samuel Verschelde)

* Sat Jul 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100722-1mdv2011.0
+ Revision: 557949
- fix description (it's a perl tool!)
- update to 20100722

  + Jani Välimaa <wally@mandriva.org>
    - split one-liner description to a multiple lines
    - fix one file appearing twice in file list

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100620-2mdv2011.0
+ Revision: 554151
- Add Require

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100620-1mdv2011.0
+ Revision: 554150
- import parallel


Name: gear-cronbuild
Version: 1.41
Release: alt1

Summary: gear repository automated build utility
License: GPLv2+
Group: Development/Other
Packager: Igor Vlasenko <viy@altlinux.org>
Url: http://www.altlinux.org/Gear/cronbuild
BuildArch: noarch

Source: %name-%version.tar

# TODO use /usr/bin/gear-rules-print-specfile
BuildRequires: perl-RPM-Source-Editor perl-devel /usr/bin/pod2man /usr/bin/gear-rules-print-specfile /usr/bin/gear-remotes-restore
Requires: gear rpm-uscan > 0.15 gear-uupdate > 0.16

%description
%summary

%prep
%setup

%build
#make_build
rm gear-cronbuild.spec

%install
#make_install install DESTDIR=%buildroot
install -D -m755 gear-cronbuild %buildroot%_bindir/gear-cronbuild
install -D -m755 gear-cronbuild-update-spec-timestamp %buildroot%_bindir/gear-cronbuild-update-spec-timestamp
install -D -m755 gear-cronbuild-apply-hooks %buildroot%_bindir/gear-cronbuild-apply-hooks
install -D -m755 gear-cronbuild-apply-hooks-in-hsh-chroot %buildroot%_bindir/gear-cronbuild-apply-hooks-in-hsh-chroot

for i in gear-cronbuild-apply-hooks gear-cronbuild-apply-hooks-in-hsh-chroot; do
    pod2man  --name $i --center 'gear-cronbuild' --section 1 --release %version $i > $i.1
done

mkdir -p %buildroot%_man1dir
install -m 644 *.1 %buildroot%_man1dir/


%files
%_bindir/*
%_mandir/man?/*

%changelog
* Fri Jan 10 2020 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1
- bugfix release

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- new version

* Wed Nov 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- new version

* Thu Jan 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- bugfix release (thanks to lakostis@)

* Tue Jan 23 2018 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- new version (closes: #34476)

* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- new version

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- new version (perl-RPM dependencies removed)

* Sun Aug 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- new version

* Wed Mar 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- new version

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- new version

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- new version

* Thu Nov 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2
- bugfixes for --exclude thanks to mithraen@

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- exclude pattern support

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- specgen support

* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- use perl-Gear-Rules for gear API

* Fri Jun 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- upodated man pages

* Fri Apr 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- new version

* Mon Jun 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- support for .gear/cronbuild-git-config

* Thu Dec 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- bugfix release

* Tue Dec 13 2011 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- gear-commit is optional (thanks to solo@)

* Mon Nov 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- added help, cleanup

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- support for .watch files

* Wed Oct 12 2011 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- bugfix release

* Wed Oct 12 2011 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- bugfix release

* Wed Oct 12 2011 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- bugfix release

* Sat Oct 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- bugfixes in commit msg, by solo@ (closes: 26428)

* Wed Oct 05 2011 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- update-version, add-changelog hooks are now optional.

* Wed Oct 05 2011 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- added msg shell quoting, by solo@ (closes: 26412)

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- bugfix release

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- new version
- Merged Alexey Avdeev'support for commit msg (closes: 26400)

* Tue Sep 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- bugfix release
- added manuals

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- bugfix release

* Sun Sep 04 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- added gear-cronbuild-apply-hooks-in-hsh-chroot

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- more verbose messages

* Sat Feb 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- bugfix release

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- bugfix release

* Sat Oct 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- no eval in sh script (thanks to raorn@)

* Sat Jul 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- added proper commit diff

* Thu Jul 01 2010 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- added nothing-to-do check

* Wed Jun 30 2010 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- bugfix release

* Tue Jun 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- renamed gear-cronbuild-apply to gear-cronbuild-apply-hooks

* Sat Jun 26 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- added gear-cronbuild-apply

* Thu Jun 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- first release


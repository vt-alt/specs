%ifndef distro
%define distro p9
%endif
%ifndef timestamp
%define timestamp 20190514
%endif
%ifndef dtext
%define dtext %distribution %distro
%endif
%ifndef text_summary
%define text_summary %dtext
%endif
%ifndef text_descr
%define text_descr %dtext
%endif
%ifndef text_file
%define text_file %dtext (Vaccinium)
%endif
%ifndef provide_list
%define provide_list altlinux fedora redhat system
%endif
%ifndef obsolete_list
%define obsolete_list altlinux-4.0 altlinux-release altlinux-release-4.0 altlinux-release-4.1 altlinux-release-5.0 altlinux-release-5.1 altlinux-release-c6 altlinux-release-chainmail altlinux-release-desktop altlinux-release-homeros altlinux-release-hpc altlinux-release-junior altlinux-release-master altlinux-release-office-server altlinux-release-p5 altlinux-release-p6 altlinux-release-p7 altlinux-release-p8 altlinux-release-school-server altlinux-release-server altlinux-release-skif altlinux-release-small_business altlinux-release-t6 altlinux-release-terminal fedora-release redhat-release
%endif
%ifndef conflicts_list
%define conflicts_list altlinux-release-sisyphus
%endif

Name: altlinux-release-p9
Version: %timestamp
Release: alt1

Summary: %text_summary release file
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done)
Obsoletes: %obsolete_list
Conflicts: %conflicts_list

%description
%text_descr release file.

%install
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name
echo "%text_file" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done

%files
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%changelog
* Tue May 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 20190514-alt1
- Updated Obsoletes lists.
- Renamed and updated to altlinux-release-p9.

* Thu Apr 14 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 20160414-alt1
- Updated Obsoletes lists.
- Renamed and updated to altlinux-release-p8.

* Thu Apr 25 2013 Dmitry V. Levin <ldv@altlinux.org> 20130425-alt1
- Updated codename.

* Wed Apr 24 2013 Dmitry V. Levin <ldv@altlinux.org> 20130424-alt1
- Updated Obsoletes lists.
- Renamed and updated to altlinux-release-p7.

* Thu May 05 2011 Dmitry V. Levin <ldv@altlinux.org> 20110505-alt1
- Updated Obsoletes lists.
- Renamed and updated to altlinux-release-p6.

* Tue Oct 27 2009 Dmitry V. Levin <ldv@altlinux.org> 20091027-alt1
- Updated Obsoletes lists.
- Renamed and updated to altlinux-release-p5.

* Tue Oct 27 2009 Dmitry V. Levin <ldv@altlinux.org> 20091027-alt1
- Updated Obsoletes lists.
- Renamed and updated to altlinux-release-5.1.

* Mon Dec 22 2008 Dmitry V. Levin <ldv@altlinux.org> 20081222-alt1
- Updated Obsoletes lists.
- Renamed and updated to altlinux-release-5.0.

* Thu Dec 06 2007 Dmitry V. Levin <ldv@altlinux.org> 20071206-alt1
- Updated Provides/Obsoletes lists and /etc/*-release symlinks.
- Renamed from altlinux-release to altlinux-release-4.0.

* Fri Feb 14 2003 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20030214
- Enhanced %%ifdef logic.

* Tue Dec 31 2002 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20021231
- Implemented %%ifdef logic.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20020814
- Added %_sysconfdir/buildreqs/packages/ignore.d/%name.

* Mon Apr 23 2001 Dmitry V. Levin <ldv@altlinux.ru> Sisyphus-alt20010423
- Renamed to altlinux-release.

* Thu Jan 10 2001 Dmitry V. Levin <ldv@fandra.org> 7.2-ipl0.20010111
- Renamed to %name.
- Implemented autoversioning.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 7.2-ipl0.20001227
- Set 8-digit timestamp number.

* Tue Dec 26 2000 AEN <aen@logic.ru>
- adopted for sisyphus

* Thu Oct  5 2000 Warly <warly@mandrakesoft.com> 7.2-1mdk
- Odyssey

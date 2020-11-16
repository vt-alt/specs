Name: erc
Version: 0.9.4
Release: alt1

Summary: Universal Archive Tool

License: AGPLv3
Group: File tools
Url: https://github.com/Etersoft/erc

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: http://git.etersoft.ru/projects/korinf/erc.git
Source: ftp://updates.etersoft.ru/pub/Korinf/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

# who really does all our work
Requires: patool >= 1.1

%description
Etersoft Universal Archive Tool is the archive manager for any format.
It provides universal command line interface to any archive manager.
Patool is used for real work with archives.

See detailed russian description here: http://wiki.etersoft.ru/ERC

%prep
%setup

%install
# install to datadir and so on
%makeinstall version=%version-%release

#mkdir -p %buildroot%_sysconfdir/bash_completion.d/
#install -m 0644 bash_completion/erc %buildroot%_sysconfdir/bash_completion.d/erc

# shebang.req.files
#chmod a+x %buildroot%_datadir/%name/{erc-}*

%files
%doc README LICENSE TODO
%_bindir/erc
%_bindir/unerc
%_bindir/ercat
%_datadir/%name/
%_man1dir/*
#%_sysconfdir/bash_completion.d/erc

%changelog
* Tue Mar 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- ercat: add check for unpack binary and epm assure
- ercat: add .zst (.zstd) support

* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- add support for pack to zip if one dir arg was received

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- fix get extension: check for tar.* firstly
- allow get type of archive for nonexists files too

* Mon Jul 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- ercat: add lz4 support

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- skip repack for the same input and output file
- erc: add add command
- erc: add tgz format recognize
- pack unerc

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- erc: add -f (--force) for override target, improve test

* Tue Aug 04 2015 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- add zpaq and pax to supported formats
- erc: add options support and implement --quiet
- add unerc command

* Fri Feb 20 2015 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- improve is_target_format to check against supported target formats

* Tue Oct 15 2013 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- erc-archive: fix basename issues
- use bash for all scripts (welcome to debug with dash!)

* Tue Sep 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- ercat: add support for plain text files too
- update README, add man pages

* Fri Jul 26 2013 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- small fixes
- erc: enable search and improve help

* Fri Jul 26 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- erc: unpack archive by default
- erc: add support for target arch to create and repack
- introduce ercat: cat any archive to stdout (like bzcat)

* Thu Jul 25 2013 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

Name: hasher-rich-chroot
Version: 0.05
Release: alt1

Summary: hasher chroot environment for productive work 
License: GPL
Group: Development/Other
Packager: Igor Vlasenko <viy@altlinux.org>
#Url: http://www.altlinux.org/Git.alt/girar-nmu
BuildArch: noarch

Source: %name-%version.tar

Requires: mc less unzip elfutils rpm-utils
# Andrew Savchenko:
#Лично мне приходится на все системы, где я работаю, ставить
#terminfo-extra, т.к. я использую screen-256color-bce-s; даже внутрь
#хешерницы, т.к. иначе hsh-shell не работает нормально.
Requires: terminfo-extra
Requires: vim-console
# vim alternative
Requires: nano

%description
This package contains utilities that configure
hasher chroot for comfortable post mortem work.
They should be installed into chroot.

For user-side utils, see %name-utils


%package user-utils
Summary: User-side utils for hasher-rich-chroot
Group: Development/Other

%description user-utils
User-side utils for hasher-rich-chroot -
hasher chroot environment for productive work

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -m 755 hsh-*  %buildroot%_bindir/

#for i in girar-*; do
#    pod2man  --name $i --center 'girar-nmu utils' --section 1 --release %version $i > $i.1 ||:
#done
#find . -name '*.1' -size 0 -print -delete
#mkdir -p %buildroot%_man1dir
#install -m 644 girar-*.1 %buildroot%_man1dir/

%files
#%doc README
%_bindir/hsh-rich-chroot-create-history
#%_man1dir/*

%files user-utils
%_bindir/hsh-install-rich-chroot

%changelog
* Sun Sep 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated requires in hasher-rich-chroot

* Wed Feb 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added nano as vim-console alternative

* Sat Feb 02 2019 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- fix for broken vim-console installation from p8

* Fri Apr 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added terminfo-extra for screen

* Wed May 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial release


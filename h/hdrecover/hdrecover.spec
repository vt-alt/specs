Name:		hdrecover
Version:	0.5
Release:	alt1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://hdrecover.sourceforge.net/
Packager:	Motsyo Gennadi <drool at altlinux.ru>
Summary:	Tool for recover a hard disk that has bad blocks on it
Summary(ru_RU.UTF-8): Инструмент для восстановления жорсткого диска со сбойными блоками
Summary(uk_UA.UTF-8): Інструмент для відновлення жорсткого диска зі збійними секторами

Source: %name-%version.tar.gz

Patch0: %name-0.5-from_sector.patch

# Automatically added by buildreq on Fri May 01 2020 (-bi)
# optimized out: elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel perl python-base python-modules sh4
BuildRequires: gcc-c++

%description
Tool to encourage hard disks to reallocate bad sectors allowing data recovery
and possible continued use of the hard disk.

%description -l ru_RU.UTF-8
Инструмент для перераспределения сбойных секторов жесткого диска, что позволяет
восстановить данные и, возможно, продлить использование жесткого диска

%description -l uk_UA.UTF-8
Інструмент для перерозподілу збійних секторів жорсткого диска, що дозволяє
відновити дані і, можливо, подовжити використання жорсткого диска

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog README COPYING INSTALL NEWS
%attr(4711, root, root) %_bindir/%name

%changelog
* Fri May 01 2020 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt1
- initial build

%define file_name quick_russian-english

Name: stardict-quick_ru-en
Version: 2.4.2
Release: alt1

Group: Text tools
License: GPL
Url: http://download.huzheng.org/Quick/

Summary: Russian-English dictionary for StarDict
Summary(ru.UTF-8): Русско-английский словарь для StarDict

# http://download.huzheng.org/Quick/stardict-quick_rus-eng-2.4.2.tar.bz2
Source: %name-%version.tar

Requires: stardict >= 2.4.2
BuildArch: noarch

%description
Russian-English translation dictionary for StarDict,
a GUI-based dictionary software.

%description -l ru_RU.UTF-8
Русско-английский словарь для StarDict,
словарь на основе графического интерфейса.

%prep
%setup -q

%install
install -p -m644 -D %file_name.dict.dz %buildroot%_datadir/stardict/dic/%file_name.dict.dz
install -p -m644 -D %file_name.idx %buildroot%_datadir/stardict/dic/%file_name.idx
install -p -m644 -D %file_name.ifo %buildroot%_datadir/stardict/dic/%file_name.ifo

%files
%_datadir/stardict/dic/*

%changelog
* Tue Aug 06 2019 Pavel Moseev <mars@altlinux.org> 2.4.2-alt1
- Initial build

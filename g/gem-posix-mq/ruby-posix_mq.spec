%define        pkgname posix-mq
%define        gemname posix_mq

Name:          gem-%pkgname
Version:       2.4.1
Release:       alt3
Summary:       POSIX Message Queues for Ruby
Group:         Development/Ruby
License:       LGPLv3+ and GPLv2
Url:           http://bogomips.org/ruby_posix_mq/
Vcs:           https://bogomips.org/ruby_posix_mq.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
POSIX message queues allow local processes to exchange data in the form
of messages. This API is distinct from that provided by System V
message queues, but provides similar functionality.


%package       -n posix-mq-rb
Summary:       %summary
Group:         Development/Documentation
BuildArch:     noarch

%description   -n posix-mq-rb
%summary.

Executables files for %gemname gem.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n posix-mq-rb
%_bindir/posix-mq-rb

%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt3
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.1
- Rebuild with Ruby 2.5.0

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Mar 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.0.0-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Thu Dec 06 2012 Led <led@altlinux.ru> 1.0.0-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Aug 15 2011 Anton Gorlov <stalker@altlinux.ru> 1.0.0-alt2
- fix wrong url

* Thu Aug 11 2011 Anton Gorlov <stalker@altlinux.ru> 1.0.0-alt1
- initial build for ALTLinux

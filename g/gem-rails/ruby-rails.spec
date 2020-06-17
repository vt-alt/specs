%define        pkgname rails

Name:          gem-%pkgname
Version:       5.2.4.1
Release:       alt4
Summary:       Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://rubyonrails.org/
Vcs:           https://github.com/rails/rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       railsctl
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR
Requires:      rails = %EVR

%description
Ruby on Rails metapackage gem.

%package       doc
Summary:       Documentation files for %name
Summary(ru_RU.UTF-8): Файлы сведений для %name
Group:         Development/Documentation
BuildArch:     noarch
Provides:      activerecord-gems-doc = %EVR
Obsoletes:     activerecord-gems-doc < %EVR
Provides:      activesupport-gems-doc = %EVR
Obsoletes:     activesupport-gems-doc < %EVR

%description   doc
Documentation files for %{name}.


%package       -n gem-actioncable
Summary:       WebSocket framework for Rails
Group:         Development/Ruby
Provides:      ruby-actioncable
Obsoletes:     ruby-actioncable

%description   -n gem-actioncable
Structure many real-time application concerns into channels over a
single WebSocket connection.


%package       -n gem-actioncable-doc
Summary:       Documentation files for "gem-actioncable" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-actioncable-doc
Obsoletes:     ruby-actioncable-doc

%description   -n gem-actioncable-doc
%summary


%package       -n gem-actionmailer
Summary:       Email composition, delivery, and receiving framework (part of Rails)
Group:         Development/Ruby
Provides:      ruby-actionmailer
Obsoletes:     ruby-actionmailer

%description   -n gem-actionmailer
Email on Rails. Compose, deliver, receive, and test emails using the
familiar controller/view pattern. First-class support for multipart
email and attachments.


%package       -n gem-actionmailer-doc
Summary:       Documentation files for "gem-actionmailer" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-actionmailer-doc
Obsoletes:     ruby-actionmailer-doc

%description   -n gem-actionmailer-doc
%summary


%package       -n gem-actionpack
Summary:       Web-flow and rendering framework putting the VC in MVC (part of Rails)
Group:         Development/Ruby
Provides:      ruby-actionpack
Obsoletes:     ruby-actionpack

%description   -n gem-actionpack
Web apps on Rails. Simple, battle-tested conventions for building and
testing MVC web applications. Works with any Rack-compatible server.


%package       -n gem-actionpack-doc
Summary:       Documentation files for "gem-actionpack" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-actionpack-doc
Obsoletes:     ruby-actionpack-doc

%description   -n gem-actionpack-doc
%summary


%package       -n gem-actionview
Summary:       Rendering framework putting the V in MVC (part of Rails)
Group:         Development/Ruby
Provides:      ruby-actionview
Obsoletes:     ruby-actionview

%description   -n gem-actionview
Simple, battle-tested conventions and helpers for building web pages.


%package       -n gem-actionview-doc
Summary:       Documentation files for "gem-actionview" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-actionview-doc
Obsoletes:     ruby-actionview-doc

%description   -n gem-actionview-doc
%summary


%package       -n gem-activejob
Summary:       Job framework with pluggable queues
Group:         Development/Ruby
Provides:      ruby-activejob
Obsoletes:     ruby-activejob

%description   -n gem-activejob
Declare job classes that can be run by a variety of queueing backends.


%package       -n gem-activejob-doc
Summary:       Documentation files for "gem-activejob" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-activejob-doc
Obsoletes:     ruby-activejob-doc

%description   -n gem-activejob-doc
%summary


%package       -n gem-activemodel
Summary:       A toolkit for building modeling frameworks (part of Rails)
Group:         Development/Ruby
Provides:      ruby-activemodel
Obsoletes:     ruby-activemodel

%description   -n gem-activemodel
A toolkit for building modeling frameworks like Active Record. Rich
support for attributes, callbacks, validations, serialization,
internationalization, and testing.


%package       -n gem-activemodel-doc
Summary:       Documentation files for "gem-activemodel" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-activemodel-doc
Obsoletes:     ruby-activemodel-doc

%description   -n gem-activemodel-doc
%summary


%package       -n gem-activerecord
Summary:       Object-relational mapper framework (part of Rails)
Group:         Development/Ruby
Provides:      activerecord-gems = %EVR
Obsoletes:     activerecord-gems < %EVR
Provides:      ruby-activerecord
Obsoletes:     ruby-activerecord

%description   -n gem-activerecord
Databases on Rails. Build a persistent domain model by mapping database
tables to Ruby classes. Strong conventions for associations,
validations, aggregations, migrations, and testing come baked-in.


%package       -n gem-activerecord-doc
Summary:       Documentation files for "activerecord" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-activerecord-doc
Obsoletes:     ruby-activerecord-doc

%description   -n gem-activerecord-doc
%summary


%package       -n gem-activestorage
Summary:       Local and cloud file storage framework
Group:         Development/Ruby
Provides:      ruby-activestorage
Obsoletes:     ruby-activestorage

%description   -n gem-activestorage
Attach cloud and local files in Rails applications.


%package       -n gem-activestorage-doc
Summary:       Documentation files for "gem-activestorage" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-activestorage-doc
Obsoletes:     ruby-activestorage-doc

%description   -n gem-activestorage-doc
%summary


%package       -n gem-activesupport
Summary:       A toolkit of support libraries and Ruby core extensions extracted from the Rails framework
Group:         Development/Ruby
Provides:      activesupport-gems = %EVR
Obsoletes:     activesupport-gems < %EVR
Provides:      ruby-activesupport
Obsoletes:     ruby-activesupport

%description   -n gem-activesupport
A toolkit of support libraries and Ruby core extensions extracted from
the Rails framework. Rich support for multibyte strings,
internationalization, time zones, and testing.


%package       -n gem-activesupport-doc
Summary:       Documentation files for "gem-activesupport" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-activesupport-doc
Obsoletes:     ruby-activesupport-doc

%description   -n gem-activesupport-doc
%summary


%package       -n gem-railties
Summary:       Tools for creating, working with, and running Rails applications
Group:         Development/Ruby
Provides:      ruby-railties
Obsoletes:     ruby-railties

%description   -n gem-railties
Rails internals: application bootup, plugins, generators, and rake tasks.


%package       -n gem-railties-doc
Summary:       Documentation files for "gem-railties" gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-railties-doc
Obsoletes:     ruby-railties-doc

%description   -n gem-railties-doc
%summary


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -D -m 755 %SOURCE1 %buildroot%_sbindir/railsctl

%check
%ruby_test

%files
%ruby_gemspecdir/rails-%version.gemspec
%ruby_gemslibdir/rails-%version

%files         -n gem-actioncable
%ruby_gemspecdir/actioncable-%version.gemspec
%ruby_gemslibdir/actioncable-%version

%files         -n gem-actioncable-doc
%ruby_gemsdocdir/actioncable-%version

%files         -n gem-actionmailer
%ruby_gemspecdir/actionmailer-%version.gemspec
%ruby_gemslibdir/actionmailer-%version

%files         -n gem-actionmailer-doc
%ruby_gemsdocdir/actionmailer-%version

%files         -n gem-actionpack
%ruby_gemspecdir/actionpack-%version.gemspec
%ruby_gemslibdir/actionpack-%version

%files         -n gem-actionpack-doc
%ruby_gemsdocdir/actionpack-%version

%files         -n gem-actionview
%ruby_gemspecdir/actionview-%version.gemspec
%ruby_gemslibdir/actionview-%version

%files         -n gem-actionview-doc
%ruby_gemsdocdir/actionview-%version

%files         -n gem-activejob
%ruby_gemspecdir/activejob-%version.gemspec
%ruby_gemslibdir/activejob-%version

%files         -n gem-activejob-doc
%ruby_gemsdocdir/activejob-%version

%files         -n gem-activemodel
%ruby_gemspecdir/activemodel-%version.gemspec
%ruby_gemslibdir/activemodel-%version

%files         -n gem-activemodel-doc
%ruby_gemsdocdir/activemodel-%version

%files         -n gem-activerecord
%ruby_gemspecdir/activerecord-%version.gemspec
%ruby_gemslibdir/activerecord-%version

%files         -n gem-activerecord-doc
%ruby_gemsdocdir/activerecord-%version

%files         -n gem-activestorage
%ruby_gemspecdir/activestorage-%version.gemspec
%ruby_gemslibdir/activestorage-%version

%files         -n gem-activestorage-doc
%ruby_gemsdocdir/activestorage-%version

%files         -n gem-activesupport
%ruby_gemspecdir/activesupport-%version.gemspec
%ruby_gemslibdir/activesupport-%version

%files         -n gem-activesupport-doc
%ruby_gemsdocdir/activesupport-%version

%files         -n gem-railties
%ruby_gemspecdir/railties-%version.gemspec
%ruby_gemslibdir/railties-%version
%doc README*

%files         -n gem-railties-doc
%ruby_gemsdocdir/railties-%version

%files         -n %pkgname
%_bindir/*
%_sbindir/*


%changelog
* Tue May 19 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.1-alt4
- * railsctl tmp detection, minor fixes

* Fri May 15 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.1-alt3
- + 'mrproper' procedure to railsctl
- ! railsctl 'setup' procedure

* Fri May 08 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.1-alt2
- ! railsctl

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.1-alt1
- ^ 5.2.3 -> 5.2.4.1
- + railsctl command script to control rails app setup
- ! spec tags

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.3-alt1.1
- fixed (!) spec to fix dependency

* Tue Apr 02 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.3-alt1
- Bump to 5.2.3

* Mon Mar 25 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.2.1-alt2
- Added join lib and bin for railties gem

* Thu Mar 14 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.2.1-alt1
- Bump to 5.2.2.1;
- fix CVE-2019-5418, CVE-2019-5420.

* Sat Mar 09 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.2-alt1
- Bump to 5.2.2;
- Use Ruby Policy 2.0.

* Wed Jan 23 2019 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1.2
- Remove deprecated macros.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- Initial build for Sisyphus

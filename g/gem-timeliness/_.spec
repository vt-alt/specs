# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname timeliness

Name:          gem-%pkgname
Version:       0.4.3
Release:       alt1.1
Summary:       Fast date/time parsing for the control freak
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/adzap/timeliness
%vcs           https://github.com/adzap/timeliness.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Date/time parser for Ruby with the following features:

* Extensible with custom formats and tokens.
* It's pretty fast. Up to 60% faster than Time/Date parse method.
* Control the parser strictness.
* Control behaviour of ambiguous date formats (US vs European e.g. mm/dd/yy,
  dd/mm/yy).
* I18n support (for months), if I18n gem loaded.
* Fewer WTFs than Time/Date parse method.
* Has no dependencies.
* Works with Ruby MRI >= 2.2

Extracted from the validates_timeliness gem, it has been rewritten cleaner and
much faster. It's most suitable for when you need to control the parsing
behaviour. It's faster than the Time/Date class parse methods, so it has
general appeal.


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

%files         doc
%ruby_gemdocdir


%changelog
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1.1
- ! spec according to changelog rules

* Sat Aug 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- + packaged gem with usage Ruby Policy 2.0

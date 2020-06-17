# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname unicode-utils
%define        gemname unicode_utils

Name:          gem-%pkgname
Version:       1.4.0
Release:       alt1.1
Summary:       additional Unicode aware functions for Ruby 1.9
License:       Embedded
Group:         Development/Ruby
Url:           https://github.com/lang/unicode_utils
%vcs           https://github.com/lang/unicode_utils.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

UnicodeUtils implements Unicode algorithms for case conversion, normalization,
text segmentation and more in pure Ruby code.


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
%doc README* LICENSE*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0

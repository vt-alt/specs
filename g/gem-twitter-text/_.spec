%define        pkgname twitter-text

Name:          gem-%pkgname
Version:       3.1.0
Release:       alt1
Summary:       Twitter Text Libraries
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/twitter/twitter-text
Vcs:           https://github.com/twitter/twitter-text.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%gem_replace_version unf ~> 0.1
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %gemname < %EVR
Provides:      %gemname = %EVR

%description
This repo is a collection of libraries and conformance tests to standardize
parsing of Tweet text. It synchronizes development, testing, creating issues,
and pull requests for twitter-text's implementations and specification. These
libraries are responsible for determining the quantity of characters in a Tweet
and identifying and linking any url, @username, #hashtag, or $cashtag.


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
%ruby_build --ignore=conformance #--use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Thu May 14 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 3.0.1 -> 3.1.0
- * recomsotions packages in spec

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

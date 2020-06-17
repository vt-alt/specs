%define        pkgname net-http-pipeline

Name:          gem-%pkgname
Version:       1.0.1
Release:       alt2.1
Summary:       An HTTP/1.1 pipelining implementation atop Net::HTTP
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drbrain/net-http-pipeline
Vcs:           https://github.com/drbrain/net-http-pipeline.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-hoe

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
An HTTP/1.1 pipelining implementation atop Net::HTTP.  A pipelined connection
sends multiple requests to the HTTP server without waiting for the responses.
The server will respond in-order.


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
* Tue May 26 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt2.1
- ! spec tags and syntax

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

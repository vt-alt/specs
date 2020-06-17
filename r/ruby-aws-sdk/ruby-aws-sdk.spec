%define        pkgname aws-sdk

Name: 	       ruby-%pkgname
Version:       2.11.478
Release:       alt1
Summary:       The official AWS SDK for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://aws.amazon.com/ru/sdk-for-ruby/
Vcs:           https://github.com/aws/aws-sdk-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard)
BuildRequires: gem(simplecov)
BuildRequires: gem(kramdown)
BuildRequires: gem(benchmark-ips) >= 2.0
BuildRequires: gem(rake-compiler)
BuildRequires: gem(ruby-ll) >= 2.1
BuildRequires: gem(ast)
BuildRequires: gem(ox)
BuildRequires: gem(nokogiri)
BuildRequires: gem(jmespath)
BuildRequires: ragel
BuildRequires: /usr/bin/ruby-ll

%gem_replace_version nokogiri >= 1.10
%gem_replace_version yard >= 0.9

%description
The official AWS SDK for Ruby. Provides both resource oriented
interfaces and API clients for AWS services.


%package       -n gem-%pkgname
Summary:       AWS SDK for Ruby - Core
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname
The official AWS SDK for Ruby. Provides both resource oriented
interfaces and API clients for AWS services.


%package       -n gem-%pkgname-core
Summary:       AWS SDK for Ruby - Core
Group:         Development/Ruby
BuildArch:     noarch

Obsoletes:     aws-sdk-core
Provides:      aws-sdk-core
Obsoletes:     ruby-aws-sdk-core
Provides:      ruby-aws-sdk-core

%description   -n gem-%pkgname-core
Provides API clients for AWS. This gem is part of the official AWS SDK
for Ruby.


%package       -n gem-%pkgname-resources
Summary:       AWS SDK for Ruby - Resources
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname-resources
Provides resource oriented interfaces and other higher-level
abstractions for many AWS services. This gem is part of the official AWS
SDK for Ruby.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-core-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-core-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-core-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-resources-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-resources-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-resources-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=ruby-aws-sdk --prefixes= \
            --use=aws-sdk --prefixes=gem --version-replace=%version \
            --use=aws-sdk-resources --version-replace=%version \
            --use=aws-sdk-core --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%_libexecdir/%name
%_bindir/aws.rb

%files         -n gem-%pkgname
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-core
%doc README*
%ruby_gemspecdir/%gemname-core-%version.gemspec
%ruby_gemslibdir/%gemname-core-%version

%files         -n gem-%pkgname-core-doc
%ruby_gemsdocdir/%gemname-core-%version

%files         -n gem-%pkgname-resources
%doc README*
%ruby_gemspecdir/%gemname-resources-%version.gemspec
%ruby_gemslibdir/%gemname-resources-%version

%files         -n gem-%pkgname-resources-doc
%ruby_gemsdocdir/%gemname-resources-%version


%changelog
* Mon Mar 30 2020 Pavel Skrylev <majioa@altlinux.org> 2.11.478-alt1
- ^ 2.11.478 -> 2.11.478
- * moving code from %%_libdir -> %%_libexecdir

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 2.11.460-alt1
- updated (^) 2.11.354 -> 2.11.460
- fixed (!) spec

* Tue Sep 17 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.354-alt1
- updated (^) 2.11.351 -> 2.11.354
- added (+) obsoletes/provides on ruby-aws-sdk-code for gem-aws-sdk-code

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.351-alt1
- updated (^) 2.11.345 -> 2.11.351
- fixed (!) spec according to changelog rules

* Tue Sep 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.345-alt1
- updated (^) 2.11.317 -> 2.11.345
- fixed (!) spec
- added (+) obsoletes/provides for aws-sdk-core

* Wed Aug 07 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.317-alt1
- used (^) Ruby Policy 2.0
- updated (^) 2.11.262 -> 2.11.317

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 2.11.262-alt1
- New version.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.188-alt1
- New version.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.185-alt1
- New version.

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.174-alt1
- New version.

* Fri Oct 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.153-alt1
- New version.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.142-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.132-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.130-alt1
- New version.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.83-alt1.1
- Rebuild for new Ruby autorequirements.

* Sat Jul 07 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.83-alt1
- New version.

* Fri Jun 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.78-alt1
- New version.

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.75-alt1
- New version.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.74-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.72-alt1
- New version.

* Sat Jun 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.70-alt1
- New version.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.69-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.68-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.67-alt1
- New version.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.65-alt1
- New version.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.64-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.63-alt1
- New version.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.62-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.61-alt1
- New version.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.58-alt1
- New version.

* Sat May 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.57-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.56-alt1
- New version.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.55-alt1
- New version.

* Tue May 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.54-alt1
- New version.

* Sat May 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.53-alt1
- New version.

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.52-alt1
- New version.

* Thu May 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.51-alt1
- New version.

* Wed May 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.50-alt1
- New version.

* Tue May 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.49-alt1
- New version.

* Fri May 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.48-alt1
- New version.

* Thu May 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.46-alt1
- New version.

* Tue May 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.45-alt1
- New version.

* Tue May 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.44-alt1
- New version.

* Sat May 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.43-alt1
- New version.

* Fri May 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.42-alt1
- New version.

* Thu May 03 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.41-alt1
- New version.

* Tue May 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.40-alt1
- New version.

* Fri Apr 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.39-alt1
- New version.

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.37-alt1
- New version.

* Sun Apr 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.35-alt1
- New version.

* Wed Apr 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.33-alt1
- New version.

* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.32-alt1
- New version.

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.31-alt1
- New version.

* Fri Apr 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.30-alt1
- New version.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.29-alt1
- New version.

* Wed Apr 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.28-alt1
- New version.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.27-alt1
- New version.

* Sun Apr 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.26-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.25-alt1
- New version.

* Thu Mar 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.24-alt1
- New version.

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.23-alt1
- New version.

* Tue Mar 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.22-alt1
- New version.

* Sat Mar 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.21-alt1
- New version.

* Fri Mar 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.20-alt1
- New version.

* Thu Mar 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.19-alt1
- New version.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.18-alt1
- New version.

* Sat Mar 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.17-alt1
- New version.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.16-alt1
- New version.

* Thu Mar 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.15-alt1
- New version.

* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.14-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.13-alt1
- New version.

* Fri Mar 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.12-alt1
- New version.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.10-alt1
- New version.

* Wed Mar 07 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.9-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.8-alt1
- New version.

* Wed Feb 28 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.6-alt1
- New version.

* Tue Feb 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.5-alt1
- New version.

* Sat Feb 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.4-alt1
- New version.

* Fri Feb 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.3-alt1
- New version.

* Thu Feb 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1
- New version.

* Wed Feb 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt1
- New version.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.134-alt1
- New version.

* Fri Feb 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.133-alt1
- New version.

* Thu Feb 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.132-alt1
- New version.

* Wed Feb 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.131-alt1
- New version.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.130-alt1
- New version.

* Mon Feb 12 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.129-alt1
- New version.

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.128-alt1
- New version.

* Thu Feb 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.127-alt1
- New version.

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.126-alt1
- New version.

* Mon Jan 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.125-alt1
- New version.

* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.124-alt1
- New version.

* Wed Jan 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.123-alt1
- New version.

* Sun Jan 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.122-alt1
- New version.

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.121-alt1
- New version.

* Wed Jan 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.119-alt1
- New version.

* Tue Jan 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.118-alt1
- New version.

* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.117-alt1
- New version.

* Thu Jan 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.115-alt1
- New version.

* Tue Jan 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.113-alt1
- New version.

* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.111-alt1
- New version.

* Mon Jan 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.110-alt1
- New version.

* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.109-alt1
- New version.

* Thu Dec 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.107-alt1
- New version.

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.106-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.104-alt1
- New version.

* Fri Dec 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.103-alt1
- New version.

* Wed Dec 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.102-alt1
- New version.

* Sat Dec 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.100-alt1
- New version.

* Fri Dec 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.99-alt1
- New version.

* Thu Dec 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.98-alt1
- New version.

* Wed Dec 06 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.97-alt1
- New version.

* Tue Dec 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.96-alt1
- New version.

* Sat Dec 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.95-alt1
- New version.

* Tue Nov 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.90-alt1
- New version.

* Fri Nov 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.89-alt1
- New version.

* Wed Nov 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.88-alt1
- New version.

* Tue Nov 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.87-alt1
- New version.

* Sun Nov 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.86-alt1
- New version.

* Fri Nov 17 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.85-alt1
- New version.

* Thu Nov 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.84-alt1
- New version.

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.83-alt1
- New version.

* Fri Nov 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.82-alt1
- New version

* Thu Nov 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.81-alt1
- New version

* Wed Nov 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.80-alt1
- New version

* Tue Nov 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.79-alt1
- New version

* Sat Nov 04 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.78-alt1
- New version

* Fri Nov 03 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.77-alt1
- New version

* Thu Nov 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.76-alt1
- New version

* Fri Oct 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.74-alt1
- New version

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.71-alt1
- New version

* Tue Oct 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.70-alt1
- New version

* Sat Oct 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.69-alt1
- New version

* Fri Oct 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.68-alt1
- New version

* Thu Oct 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.67-alt1
- New version

* Wed Oct 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.66-alt1
- New version

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.65-alt1
- New version

* Fri Oct 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.64-alt1
- New version

* Wed Oct 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.62-alt1
- New version

* Sat Oct 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.61-alt1
- New version

* Fri Oct 06 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.59-alt1
- New version

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.58-alt1
- New version

* Wed Oct 04 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.57-alt1
- New version

* Tue Oct 03 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.56-alt1
- New version

* Sat Sep 30 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.55-alt1
- New version

* Thu Sep 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.54-alt1
- New version

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.53-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.52-alt1
- New version

* Thu Sep 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.50-alt1
- New version

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.49-alt1
- New version

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.48-alt1
- New version

* Sat Sep 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.47-alt1
- New version

* Fri Sep 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.46-alt1
- New version

* Thu Sep 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.45-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.44-alt1
- New version

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.40-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.38-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Sep 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.38-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.37-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.21-alt1
- Initial build for Sisyphus

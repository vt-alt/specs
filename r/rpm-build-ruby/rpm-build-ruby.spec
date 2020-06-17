%def_disable check

Name:          rpm-build-ruby
Epoch:         1
Version:       1.0.0
Release:       alt12
Summary:       RPM helper scripts to calculate Ruby dependencies
License:       GPLv2
Group:         Development/Ruby
Source:        %name-%version.tar
BuildArch:     noarch

Requires:      rpm-macros-ruby = %EVR
Requires:      ruby >= 1.9
Conflicts:     rpm-build <= 4.0.4-alt24
AutoReq:       yes,noruby
Requires:      ruby >= 1.9
Requires:      ruby-stdlibs >= 1.9
Requires:      libruby-devel
Requires:      /usr/bin/rdoc
Requires:      /usr/bin/rake
Requires:      /usr/bin/setup.rb
Requires:      /bin/sed
Requires:      gem(bundler)
Requires:      ruby-tool-setup

%{!?_disable_check:BuildRequires: ruby >= 1.9 ruby-stdlibs >= 1.9}

%description
These helper scripts will look at Ruby source files in your package, and will
use this information to generate automatic Requires and Provides tags for the
package.

%package       -n rpm-macros-ruby
Summary: rpm macros for Ruby packages
Group: Development/Ruby

%description   -n rpm-macros-ruby
rpm macros for Ruby packages.

%prep
%setup -q

%install
install -d -m 0755 %buildroot{%_rpmlibdir,%_rpmmacrosdir}
install -p -m 0755 ruby.{req,prov}* %buildroot%_rpmlibdir/
install -p -m 0644 ruby.macros %buildroot%_rpmmacrosdir/ruby
install -p -m 0644 ruby.env %buildroot%_rpmmacrosdir/

%files
%lang(ru) %doc README.ru
%_rpmlibdir/ruby*
%_rpmmacrosdir/ruby.env

%files         -n rpm-macros-ruby
%_rpmmacrosdir/ruby

%changelog
* Wed Apr 08 2020 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt12
- > /usr/bin/setup.rb instead of the gem(setup) requires

* Sun Apr 05 2020 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt11
- + default replacement for ruby's shebang line

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt10
- fixed (!) ruby.macros

* Tue Feb 18 2020 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt9
- Fixed (!) ruby.prov (closes #36506, #37088)
- changed (*) ruby.req output

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt8
- Macros gem- copied to ruby-, old rules ruby-tool-setup is removed

* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt7
- Fix install .so target folder for gems

* Mon Apr 08 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt6
- Avoid multiple cd into source folder (closes: #36506)

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt5
- Use setup gem's dependencies detection

* Thu Mar 21 2019 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.0-alt4
- NMU.
- Removed injection of parasite dependencies (closes: #36325).

* Thu Mar 21 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt3
- Fix #36325

* Mon Mar 11 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt2
- Fixed old macros.

* Tue Jan 29 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.0.0-alt1
- Use macros and prov/req detection code for Ruby Policy 2.0.

* Tue Jan 22 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.7.4-alt1
- Fixed provides output if no gemspec specified.

* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.7.3-alt1
- Added a filter pilling out the non-ASCII chars in input to ruby.prov.

* Fri Jan 18 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.7.2-alt3
- Added template %%ruby_test.

* Thu Jan 17 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.7.2-alt2
- Fix to all ruby packages that use %%ruby_test_unit macro.

* Fri Dec 28 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.7.2-alt1
- Added %%rake-dependent macros for test, spec, and rdoc.
- Find prov is now written in ruby language.

* Mon Dec 24 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.7.1-alt1
- Added provides for ruby gem as "gem(<gem_name>)".

* Wed Sep 26 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.7-alt7
- Fix absent pry gem require.

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.7-alt6
- Fixed provides when no gemspec found.
- Allow "5.x" in requirements defaulting to "5.0"

* Mon Aug 20 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.7-alt5
- Condition "!=" is being converted to ">", ruby version detection for .gemspec
  is rolled back.

* Mon Aug 20 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.7-alt4
- Fixed ruby versions detection in Gemfile, blown out ruby version detection for .gemspec.

* Fri Aug 17 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.7-alt3
- Pass requirements without %%add_ruby_req_skip use.

* Fri Aug 17 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.7-alt2
- Fixed ruby deps detection, now deps in Gemfile and gemspec are separately
  determined, prioritizing for gemspec.

* Tue Jul 10 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.7-alt1
- Competely replace Require/Provides automatic detection based on code parse
  by gemspec specification (thanks majioa@).

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.6-alt1
- Require ruby-tool-setup used in macros.
- ruby-tool-setup requires git-core so remove git requirements from rpm-build-ruby.
- Fix small typo in description.

* Thu Jun 28 2018 Denis Medvedev <nbr@altlinux.org> 1:0.5-alt1
- add git as a requirement fror successful git imported modules build

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.4-alt1
- Add macro %%add_ruby_req_skip module... to exclude ruby(module) from generated requirements.
- Add %%rubygem_specdir macro for Ruby gem specification directory.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.3.1-alt1
- Fix file globbing in testrb.

* Tue May 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1:0.3.0-alt1
- Revert "ruby.req.files: clean ups" (from 0.1.2-alt1) because non-*.rb
  executable scripts were lost.
- ruby.req.files: parse file output case insensitive because now
  file prints Ruby capitalized.

* Mon Mar 13 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.2.4-alt1
- exclude Ruby version from %%ruby_sitearchdir provided pathes
- force newline to Ruby files to prevent output without newline ended

* Tue Feb 07 2017 Denis Medvedev <nbr@altlinux.org> 1:0.2.3-alt2
- filter hash from provides

* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.2.3-alt1
- NMU: added rpm-macros-ruby

* Thu Jan 26 2017 Denis Medvedev <nbr@altlinux.org> 1:0.2.2-alt2
- Skip include in dependencies search

* Thu Jan 26 2017 Denis Medvedev <nbr@altlinux.org> 1:0.2.2-alt1
- Added provides based on "load" in addition to "require"

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.2.1-alt1
- Support requires defined in double quotes in addition to single quotes

* Fri Oct 07 2016 Denis Medvedev <nbr@altlinux.org> 1:0.2.0-alt1
- Requires check changed to bash script instead of ruby

* Fri Oct 07 2016 Denis Medvedev <nbr@altlinux.org> 1:0.1.6-alt1
- Removed dependency to obsolete rubynodes checks

* Thu Oct 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1.5-alt2
- Set to catch any errors and notice them: %%_ruby_req_method strict.

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.1.5-alt1
- Create subpackage ruby-test-unit with only rewritten testrb utility.
  Test::Unit module now is a part of Ruby.

* Wed Sep 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1.4.1-alt1
- Tiny cleanup which is expected to have no noticeable effect:
  + more reliable failing in the shell scripts
    (set -o pipefail; set -eC).
  + .prov: normalize paths before any analysis (and not in the middle).

* Mon Sep 12 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1.4-alt1
- ruby.prov: added a new case: std arch-independent gems
  (those included in the ruby package itself).

* Thu Mar 13 2014 Led <led@altlinux.ru> 1:0.1.3-alt1
- 0.1.3:
  + ruby.macros: fix %%ruby_ri_sitedir macro

* Wed Dec 12 2012 Led <led@altlinux.ru> 1:0.1.2-alt4
- removed temp symlink

* Wed Dec 12 2012 Led <led@altlinux.ru> 1:0.1.2-alt3
- temporarily added symlink for rebuild ruby

* Sun Dec 09 2012 Led <led@altlinux.ru> 1:0.1.2-alt2
- added requires of %%_bindir/testrb and %%_bindir/rake

* Sat Dec 08 2012 Led <led@altlinux.ru> 1:0.1.2-alt1
- 0.1.2:
  + cleaned up
  + dropped ruby 1.8 support
- cleaned up spec
- updated Requires
- added README.ru
- disabled check

* Fri Apr 08 2011 Timur Aitov <timonbl4@altlinux.org> 1:0.1.1-alt1
- Supported both 1.8.7 and 1.9.2 versions of ruby
- Make difference between 1.8 and 1.9

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1:0.1.0-alt2
- Tests moved to %%check section (bootstrap-friendly)

* Mon Jul 06 2009 Alexey I. Froloff <raorn@altlinux.org> 1:0.1.0-alt1
- Updated for ruby 1.9
- Fixed typo in description (closes: #20624)
- Stop processing on syntax error
- Macros moved to %%_rpmmacrosdir

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.4-alt1
- Parser rewritten without recursion (Kirill A. Shutemov)

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.3-alt1
- Strip '.rb' extension from requires/provides to reduce apt
  cache size
- Process "weak provides" for *.so modules too
- Use files.req mechanism for directory requires (needs recent
  libruby)
- New macros:
  + %%update_setup_rb: update setup.rb script from ruby-tool-setup package
  + %%ruby_test_unit: run tests with testrb script

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.2-alt1
- "class << <var>" block support (kas@)

* Fri Mar 28 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.1-alt1
- Initial build, based on rpm-build-perl


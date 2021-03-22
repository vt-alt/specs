%define rel -beta
%global _localstatedir %_var
Name: sphinx
Version: 2.3.2
Release: alt3

Summary: Free open-source SQL full-text search engine

Group: Text tools
License: GPLv2+
Url: http://sphinxsearch.com

# Source0-url: http://sphinxsearch.com/files/%name-%version%rel.tar.gz
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.unit

Patch: sphinx-crash.patch

BuildRequires: gcc-c++ libexpat-devel libmysqlclient-devel libssl-devel libunixODBC-devel postgresql-devel zlib-devel libstemmer-devel

# due /usr/share/man/man1/indexer.1.xz and created by mnogosearch link /usr/bin/indexer
Conflicts: mnogosearch

%description
Sphinx is a full-text search engine, distributed under GPL version 2.
Commercial licensing (eg. for embedded use) is also available upon request.

Generally, it's a standalone search engine, meant to provide fast,
size-efficient and relevant full-text search functions to other applications.
Sphinx was specially designed to integrate well with SQL databases and
scripting languages.

Currently built-in data source drivers support fetching data either via direct
connection to MySQL, or PostgreSQL, or from a pipe in a custom XML format.
Adding new drivers (eg. to natively support some other DBMSes) is designed to
be as easy as possible.

Search API is natively ported to PHP, Python, Perl, Ruby, Java, and also
available as a pluggable MySQL storage engine. API is very lightweight so
porting it to new language is known to take a few hours.

As for the name, Sphinx is an acronym which is officially decoded as SQL Phrase
Index. Yes, I know about CMU's Sphinx project.

%package -n libsphinxclient
Summary: Pure C searchd client API library
Group: System/Libraries

%description -n libsphinxclient
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com

%package -n libsphinxclient-devel
Summary: Development libraries and header files for libsphinxclient
Group: System/Libraries
Requires: libsphinxclient = %version-%release

%description -n libsphinxclient-devel
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com

%package -n libsphinxclient-devel-static
Summary: Development libraries and header files for libsphinxclient
Group: System/Libraries
Requires: libsphinxclient-devel = %version-%release
Conflicts: libsphinxclient-static

%description -n libsphinxclient-devel-static
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com

%prep
%setup
%patch -p2

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r//' api/ruby/spec/sphinx/sphinx_test.sql
sed -i 's/\r//' api/java/mk.cmd
sed -i 's/\r//' api/ruby/spec/fixtures/keywords.php
sed -i 's/\r//' api/ruby/lib/sphinx/response.rb

%build
%configure --sysconfdir=/etc/sphinx --with-mysql --with-pgsql --with-libstemmer

%make_build

# Build libsphinxclient
cd api/libsphinxclient/
%configure
make

%install
make install DESTDIR=%buildroot INSTALL="%__install -p -c"

# Install sphinx initscript
install -p -D -m 0755 %SOURCE1 %buildroot%_initdir/searchd
install -p -D -m 0644 %SOURCE2 %buildroot%_unitdir/searchd.service

# Create /var/log/sphinx
mkdir -p %buildroot%_var/log/sphinx

# Create /var/lib/sphinx
mkdir -p %buildroot%_var/lib/sphinx

# Create sphinx.conf
cp %buildroot%_sysconfdir/sphinx/sphinx-min.conf.dist \
    %buildroot%_sysconfdir/sphinx/sphinx.conf

# Modify sphinx.conf
sed -i 's/\/var\/log\/searchd.log/\/var\/log\/sphinx\/searchd.log/g' \
%buildroot%_sysconfdir/sphinx/sphinx.conf

sed -i 's/\/var\/log\/query.log/\/var\/log\/sphinx\/query.log/g' \
%buildroot%_sysconfdir/sphinx/sphinx.conf

sed -i 's/\/var\/log\/searchd.pid/\/var\/run\/sphinx\/searchd.pid/g' \
%buildroot%_sysconfdir/sphinx/sphinx.conf

sed -i 's|/var/data|/var/lib/sphinx|g' \
%buildroot%_sysconfdir/sphinx/sphinx.conf

# Create /etc/logrotate.d/sphinx
mkdir -p %buildroot%_sysconfdir/logrotate.d
cat > %buildroot%_sysconfdir/logrotate.d/sphinx << EOF
/var/log/sphinx/*.log {
       weekly
       rotate 10
       copytruncate
       delaycompress
       compress
       notifempty
       missingok
       su _sphinx _sphinx
       postrotate
       killall -SIGUSR1 searchd
       endscript
}
EOF

# Create tmpfiles run configuration
mkdir -p %buildroot%_tmpfilesdir
cat > %buildroot%_tmpfilesdir/%name.conf << EOF
d /run/sphinx 755 _sphinx root -
EOF

# Install libsphinxclient
cd api/libsphinxclient/
make install DESTDIR=%buildroot INSTALL="%__install -p -c"

%pre
%_sbindir/groupadd -r -f _sphinx &>/dev/null
%_sbindir/useradd -r -n -g _sphinx -d /var/empty -s /bin/false -c "Sphinx Searchd pseudo user" _sphinx >/dev/null 2>&1 ||:

%post
%post_service searchd

%preun
%preun_service searchd

%files
%doc COPYING doc/sphinx.txt sphinx-min.conf.dist sphinx.conf.dist example.sql
%dir %attr(775,root,_sphinx) %_sysconfdir/sphinx
%config(noreplace) %attr(644,root,_sphinx) %_sysconfdir/sphinx/sphinx.conf
%config(noreplace) %attr(644,root,root) %_tmpfilesdir/%name.conf
%exclude %_sysconfdir/sphinx/*.conf.dist
%exclude %_sysconfdir/sphinx/example.sql
%_initdir/*
%_unitdir/*
%config(noreplace) %_sysconfdir/logrotate.d/sphinx
%_bindir/*
%dir %attr(775,root,_sphinx) %_var/log/sphinx
%dir %attr(775,root,_sphinx) %_var/lib/sphinx
%_man1dir/*

%files -n libsphinxclient
%doc api/java api/ruby api/*.php api/*.py api/libsphinxclient/README
%_libdir/libsphinxclient-0*.so

%files -n libsphinxclient-devel
%_libdir/libsphinxclient.so
%_includedir/*

%files -n libsphinxclient-devel-static
%_libdir/libsphinxclient.a

%changelog
* Thu Mar 18 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt3
- add Conflicts: mnogosearch

* Wed Mar 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt2
- NMU: add hack: immediately exiting due possible hungup

* Thu Apr 02 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- NMU: build 2.3.2-beta

* Sat Mar 16 2019 Anton Farygin <rider@altlinux.ru> 2.2.11-alt7
- removed ubt macros
- rebuilt with libmysqlclient21

* Tue Oct 31 2017 Anton Farygin <rider@altlinux.ru> 2.2.11-alt6
- added config for tmpfilesdir
- send SIGUSR1 to searchd for rotate logs
- systemd unit cleanup
- fixed paths in default config

* Thu Oct 26 2017 Anton Farygin <rider@altlinux.ru> 2.2.11-alt5
- fixed localstatedir location
- fixed typo in systemd unit (closes: #33177)
- rotate logs under unprivileged user (closes: #33634)

* Fri Jun 16 2017 Anton Farygin <rider@altlinux.ru> 2.2.11-alt4
- pidfile location fixed (closes: #33551)

* Thu Jun 15 2017 Anton Farygin <rider@altlinux.ru> 2.2.11-alt3
- fix for searchd process uid (closes: #33551)

* Wed Dec 07 2016 Anton Farygin <rider@altlinux.ru> 2.2.11-alt2
- added %%ubt macros for easy backporting process to stable branches

* Fri Oct 21 2016 Anton Farygin <rider@altlinux.ru> 2.2.11-alt1
- new version

* Thu Jun 06 2013 Igor Zubkov <icesik@altlinux.org> 2.0.8-alt1
- 2.0.7 -> 2.0.8

* Thu Jun 06 2013 Igor Zubkov <icesik@altlinux.org> 2.0.7-alt2
- Rebuilt with new unixODBC 2.3.1-alt1

* Tue Apr 02 2013 Igor Zubkov <icesik@altlinux.org> 2.0.7-alt1
- 2.0.6 -> 2.0.7
- buildreq

* Fri Feb 15 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.0.6-alt2
- Added systemd service
- Fix init

* Mon Nov 05 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.0.6-alt1
- 2.0.6

* Wed Aug 15 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.0.5-alt1
- 2.0.5

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.0.4-alt1
- 2.0.4
- Compiled with libstemmer

* Sat Mar 26 2011 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.9-alt4
- Fix libsphixclient-devel-static package (closes: #24798)

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt3.1
- Rebuilt for soname set-versions

* Sat Aug 28 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.9-alt3
- fix repocop warning to library-pkgnames-static

* Wed Aug 25 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.9-alt2
- Merged with http://git.altlinux.org/people/thresh/packages/sphinx.git

* Wed Aug 25 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.9-alt1
- New version 0.9.9

* Tue Oct 06 2009 Konstantin Pavlov <thresh@altlinux.org> 0.9.8.1-alt1
- First build for ALT Linux.

* Wed Aug 12 2009 Allisson Azevedo <allisson@gmail.com> 0.9.8.1-3
- Fixed macros consistency.
- Modified make install to keep timestamps.
- Added libsphinxclient package.

* Fri Aug  7 2009 Allisson Azevedo <allisson@gmail.com> 0.9.8.1-2
- Added sysv init.
- Added logrotate.d entry.

* Thu Jul 30 2009 Allisson Azevedo <allisson@gmail.com> 0.9.8.1-1
- Initial rpm release.

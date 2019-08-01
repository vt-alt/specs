%define _unpackaged_files_terminate_build 1

Name: slapi-nis
Version: 0.56.3
Release: alt1

Summary: NIS Server and Schema Compatibility plugins for Directory Server
License: GPLv2
Group: System/Base
Url: http://pagure.io/slapi-nis/
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: 389-ds-base-devel
BuildRequires: glibc-utils
BuildRequires: libldap-devel
BuildRequires: libnsl2-devel
BuildRequires: libtirpc-devel
BuildRequires: libnspr-devel
BuildRequires: libnss-devel
BuildRequires: libsss_nss_idmap-devel
BuildRequires: pam-devel

ExcludeArch: %ix86

Requires: 389-ds-base >= 1.3.5.6

%description
This package provides two plugins for Red Hat and 389 Directory Server.

The NIS Server plugin allows the directory server to act as a NIS server
for clients, dynamically generating and updating NIS maps according to
its configuration and the contents of the DIT, and serving the results to
clients using the NIS protocol as if it were an ordinary NIS server.

The Schema Compatibility plugin allows the directory server to provide an
alternate view of entries stored in part of the DIT, optionally adding,
dropping, or renaming attribute values, and optionally retrieving values
for attributes from multiple entries in the tree.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    --disable-static \
    --with-ldap=openldap \
    --with-nsswitch \
    --with-pam \
    --with-pam-service=system-auth \
    --with-tcp-wrappers=no \
    --with-tirpc=yes \
    --enable-be-txns-by-default \
    --with-sss-nss-idmap \
    --with-idviews
sed -i -e 's,%_libdir/dirsrv/plugins/,,g' -e 's,.so$,,g' doc/examples/*.ldif
%make_build

%install
%makeinstall_std

%files
%doc COPYING NEWS README STATUS doc/*.txt doc/examples/*.ldif doc/ipa
%_man1dir/nisserver-plugin-defs.1.*
%_libdir/dirsrv/plugins/nisserver-plugin.so
%_libdir/dirsrv/plugins/schemacompat-plugin.so
%_sbindir/nisserver-plugin-defs
%exclude %_libdir/dirsrv/plugins/*.la

%changelog
* Tue Jun 11 2019 Stanislav Levin <slev@altlinux.org> 0.56.3-alt1
- 0.56.1 -> 0.56.3.
- Built without tcp-wrappers.

* Thu Dec 22 2016 Mikhail Efremov <sem@altlinux.org> 0.56.1-alt1
- Updated spec.
- Fixed url.
- Updated to 0.56.1.

* Mon May 19 2014 Timur Aitov <timonbl4@altlinux.org> 0.53-alt1
- 0.53-alt1

* Tue Apr 22 2014 Nalin Dahyabhai <nalin@redhat.com> - 0.53-1
- correct the default NIS map settings for hosts.byname and hosts.byaddr,
  from report by Rik Megens
- fix several problems when hitting out-of-memory conditions, spotted by
  static analysis

* Mon Jan 20 2014 Nalin Dahyabhai <nalin@redhat.com> - 0.52-3
- remove ExclusiveArch if %%{rhel} is 7 or higher, because 389-ds-base gets
  built for everything now (#1055711)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.52-2
- Mass rebuild 2013-12-27

* Mon Dec 16 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.52-1
- correctly reflect whether or not we're built with transaction support in
  the module's nsslapd-pluginVersion attribute
- fix a couple of should've-used-memmove()-instead-of-memcpy() cases which
  would hit when removing maps or groups of maps (#1043546/#1043638)

* Mon Dec  9 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.51-1
- fix another request argument memory leak in NIS server (#1040159)
- fix miscellaneous items found by static analysis

* Tue Oct  1 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.50-1
- if we get an EPIPE while registering with rpcbind, try to reconnect and
  retransmit before giving up

* Thu Sep 19 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.49-1
- add {nis,schema-compat}-ignore-subtree and -restrict-subtree settings,
  which should let us avoid deadlocks when tasks are modifying data in
  the backend database (#1007451)

* Mon Aug 12 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.48-1
- try to gracefully handle failures obtaining internal locks
- fix locating-by-name of entries with names that require escaping
- add self-tests for nsswitch and PAM functionality
- make nsswitch mode properly handle user and group names with commas in them
- handle attempts to PAM authenticate to compat groups (i.e., with failure)
- drop the "schema-compat-origin" attribute

* Wed Aug  7 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.47.7-1
- fix building against versions of directory server older than 1.3.0, which
  first introduced slapi_escape_filter_value()

* Wed Aug  7 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.47.6-1
- only buildrequire libsss_nss_idmap-devel on releases that included SSSD
  version 1.10 or later, where it first appeared

* Wed Aug  7 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.47.5-1
- merge Alexander Bokovoy's patches to
  - teach the schema compatibility plugin to optionally serve user and group
    information retrieved from libc as part of a set of compat entries
  - handle simple bind requests for those entries by calling out to PAM
  - to rewrite the DN of incoming bind requests to compat entries to point
    at the source entries, instead of returning a referral which most clients
    won't handle
- include IPA-specific docs as docs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.47-1
- fix request argument memory leaks in NIS server
- add a %%sort function

* Thu Apr  4 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.46-1
- when checking if we can skip processing for a given change, pay attention to
  whether or not the changes cause the entry to need to be added or removed
  from a map (#912673)
- check SLAPI_PLUGIN_OPRETURN in post-change hooks, in case the backend failed
  to update things but the server called us anyway

* Tue Mar 19 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.45-1
- fix dispatching for multiple connected clients in the NIS plugin (#923336)

* Tue Feb  5 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.44-3
- work around multilib differences in the example .ldif files (internal
  tooling)

* Tue Nov 20 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.44-2
- set betxn support to be disabled by default on Fedora 17 or EL 5 or older,
  which have versions of IPA < 3.0, per mkosek on freeipa-devel

* Wed Nov 14 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.44-1
- add missing newline to a couple of debug log messages
- note whether or not betxn support is compiled in as part of the
  nsslapd-pluginVersion value we report to the server
- register callbacks in the same order in both plugins, so that
  their log messages are logged in the same order

* Tue Nov 13 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.43-1
- reintroduce support for directory server transactions (nhosoi, IPA#3046)
- control transaction support at run-time, deciding when to do things based
  on the value of the nsslapd-pluginbetxn attribute in the plugin's entry
- NIS: add default settings for shadow.byname and passwd.adjunct.byname maps

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.42-1
- drop support for directory server transactions (richm, #766320)

* Tue May 22 2012 Nalin Dahyabhai <nalin@redhat.com>
- fix a leak due to us assuming that slapi_mods_add_smod() not taking ownership
  of an smod along with its contents, when it just keeps the contents

* Tue Apr 10 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.41-1
- log errors evaluating pad expressions in %%link rather than continuing on
  until we hit an arithmetic exception (#810258)

* Fri Mar 30 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.40-1
- treat padding values passed to the "link" function as expressions to be
  evaluated rather than simply as literal values (part of #767372)

* Wed Mar 28 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.39-1
- add a "default" function for trying to evaluate one expression, then
  another, then another... (part of #767372)
- when creating a compat entry based on a real entry, set an entryUSN based on
  the source entry or the rootDSE (freeipa #864); the "scaffolding" entries
  won't have them

* Tue Mar  6 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.38-1
- properly escape RDN values when building compat entries (#796509, #800625)

* Mon Feb 13 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.37-1
- fix a compile error on systems where LDAP_SCOPE_SUBORDINATE isn't defined
  (reported by Christian Neuhold)
- conditionalize whether we have a build dependency on tcp_wrappers (older
  releases) or tcp_wrappers-devel (newer releases)

* Tue Jan 24 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.36-1
- take steps to avoid making yp_first/yp_next clients loop indefinitely
  when a single LDAP entry produces multiple copies of the same NIS key
  for a given map

* Tue Jan 24 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.35-1
- add mmatch/mregmatch[i]/mregsub[i] formatting functions which work like
  match/regmatch[i]/regsub[i], but which can handle and return lists of
  zero or more results (part of #783274)

* Thu Jan 19 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.34-1
- do entry comparisons ourselves, albeit less throughly, to avoid the worst
  case in pathological cases (more of #771444)

* Tue Jan 17 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.33-1
- get more aggressive about skipping unnecessary calculations (most of
  the problem in #771444, though not the approach described there)

* Mon Jan 16 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.32-1
- add support for directory server transactions (#758830,#766320)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 11 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.31-1
- fix some memory leaks (more of #771493)

* Tue Jan 10 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.30-1
- skip recalculations when the attributes which changed don't factor into
  our calculations (part of #771493)

* Wed Jan  4 2012 Nalin Dahyabhai <nalin@redhat.com> - 0.29-1
- add regmatchi/regsubi formatting functions which work like regmatch/regsub,
  but do matching in a case-insensitive manner
- update NIS map defaults to match {CRYPT} userPassword values in a
  case-insensitive manner so that we also use {crypt} userPassword values
- fix inconsistencies in the NIS service stemming from using not-normalized DNs
  in some places where it should have used normalized DNs

* Mon Dec 19 2011 Nalin Dahyabhai <nalin@redhat.com> - 0.28-1
- when configured with --with-ldap=openldap, link with -lldap_r rather
  than -lldap (rmeggins, #769107)

* Tue Dec  6 2011 Nalin Dahyabhai <nalin@redhat.com> - 0.27-1
- when building for 389-ds, use Slapi_RWLocks if they appear to be available
  (the rest of #730394/#730403)

* Fri Aug 12 2011 Nalin Dahyabhai <nalin@redhat.com> - 0.26-1
- when building for 389-ds, use libpthread's read-write locks instead of
  NSPR's (part of #730394/#730403)

* Wed Jul 27 2011 Nalin Dahyabhai <nalin@redhat.com> - 0.25-1
- speed up building compat entries which reference thousands of other entries
  (more of #692690)
- 389-ds-base is apparently exclusive to x86_64 and %%{ix86} on EL, so we have
  to be, too

* Fri May 13 2011 Nalin Dahyabhai <nalin@redhat.com> - 0.24-1
- carry our own yp.x, so that we don't get bitten if libc doesn't include
  yp client routines
- we need rpcgen at build-time now

* Thu Mar 31 2011 Nalin Dahyabhai <nalin@redhat.com> - 0.23-1
- speed up building compat entries with attributes with thousands of literal
  values (#692690)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Nalin Dahyabhai <nalin@redhat.com> - 0.22-1
- fix a number of scanner-uncovered defects

* Thu Jan  6 2011 Nalin Dahyabhai <nalin@redhat.com> - 0.21-2
- make sure we always pull in nss-devel and nspr-devel, and the right
  ldap toolkit for the Fedora or RHEL version

* Tue Nov 23 2010 Nalin Dahyabhai <nalin@redhat.com> - 0.21-1
- update to 0.21
  - schema-compat: don't look at standalone compat containers for a search,
    since we'll already have looked at the group container

* Tue Nov 23 2010 Nalin Dahyabhai <nalin@redhat.com> - 0.20-1
- update to 0.20
  - add a deref_f function

* Mon Nov 22 2010 Nalin Dahyabhai <nalin@redhat.com> - 0.19-1
- fix a brown-paper-bag crash

* Mon Nov 22 2010 Nalin Dahyabhai <nalin@redhat.com> - 0.18-1
- update to 0.18
  - add a deref_rf function
  - schema-compat: don't respond to search requests for which there's no backend
  - schema-compat: add the ability to do standalone compat containers

* Wed Nov 17 2010 Nalin Dahyabhai <nalin@redhat.com> - 0.17-6
- revert that last change, it's unnecessary

* Thu Nov 11 2010 Nalin Dahyabhai <nalin@redhat.com> - 0.17-5
- build against either 389-ds-base or redhat-ds-base, whichever is probably
  more appropriate here

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.17-3
- change buildreq from fedora-ds-base-devel to 389-ds-base-devel, which
  should avoid multilib conflicts from installing both arches of the new
  package (#511504)

* Tue Jul 14 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.17-2
- fixup changelog entries that resemble possible macro invocations

* Thu May 14 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.17-1
- actually send portmap registrations to the right server

* Thu May 14 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.16-1
- fix NIS server startup problem when no port is explicitly configured and
  we're using portmap instead of rpcbind (#500903)

* Fri May  8 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.15-1
- fix %%deref and %%referred to fail rather than return a valid-but-empty
  result when they fail to evaluate (reported by Rob Crittenden)

* Wed May  6 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.14-1
- correctly handle being loaded but disabled (#499404)

* Thu Apr 30 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.13-1
- update to 0.13, reworking %%link() to correct some bugs (#498432)

* Thu Apr 30 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.12-1
- correct test suite failures that 0.11 started triggering

* Tue Apr 28 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.11-1
- update to 0.11 (#497904)

* Wed Mar  4 2009 Nalin Dahyabhai <nalin@redhat.com> - 0.10-1
- update to 0.10

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  9 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.8.5-2
- make the example nsslapd-pluginpath values the same on 32- and 64-bit
  systems, because we can depend on the directory server "knowing" which
  directory to search for the plugins

* Mon Dec  8 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.8.5-1
- update to 0.8.5 to suppress duplicate values for attributes in the schema
  compatibility plugin

* Thu Dec  4 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.8.4-1
- update to 0.8.4 to fix:
  - problems updating references, particularly those for %%referred() (#474478)
  - inability to notice internal add/modify/modrdn/delete operations (really
    this time) (#474426)

* Wed Dec  3 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.8.3-1
- update to 0.8.3 to also notice and reflect changes caused by internal
  add/modify/modrdn/delete operations

* Wed Nov 19 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.8.2-1
- update to 0.8.2 to remove a redundant read lock in the schema-compat plugin

* Fri Nov  7 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.9-1
- update to 0.9

* Fri Oct  3 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.8.1-1
- update to 0.8.1 to fix a heap corruption (Rich Megginson)

* Wed Aug  6 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.8-1
- update to 0.8

* Wed Aug  6 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.7-1
- update to 0.7

* Wed Jul 23 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.6-1
- rebuild (and make rpmlint happy)

* Wed Jul  9 2008 Nalin Dahyabhai <nalin@redhat.com> - 0.2-1
- initial package

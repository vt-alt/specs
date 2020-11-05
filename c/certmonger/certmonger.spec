%define _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec
%define _localstatedir /var

%def_with check

Name: certmonger
Version: 0.79.11
Release: alt1
Summary: Certificate status monitor and PKI enrollment client

Group: System/Base
License: %gpl3plus
Url: https://pagure.io/certmonger
Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libcurl-devel
BuildRequires: libdbus-devel
BuildRequires: libidn2-devel
BuildRequires: libkrb5-devel
BuildRequires: libldap-devel
BuildRequires: libnss-devel
BuildRequires: libpopt-devel
BuildRequires: libssl-devel
BuildRequires: libtalloc-devel
BuildRequires: libtevent-devel
BuildRequires: libxml2-devel
BuildRequires: libxmlrpc-devel
BuildRequires: libsystemd-devel

%if_with check
BuildRequires: /proc
BuildRequires: dbus-tools-gui
BuildRequires: dos2unix
BuildRequires: nss-utils
BuildRequires: openssl
BuildRequires: python3(dbus)
%endif

Requires: dbus

%description
Certmonger is a service which is primarily concerned with getting your
system enrolled with a certificate authority (CA) and keeping it enrolled.

%prep
%setup
%patch -p1
# writerand option is introduced in openssl 1.1.1
grep -qs 'openssl rand -writerand $$HOME/\.rnd;' tests/Makefile.am || exit 1
sed -i 's/openssl rand -writerand $$HOME\/\.rnd;/openssl rand -out $$HOME\/\.rnd 1024;/g' tests/Makefile.am

%build
%autoreconf
%configure \
        --disable-rpath \
	--enable-systemd \
	--enable-tmpfiles \
	--with-homedir=/run/certmonger \
	--with-tmpdir=/run/certmonger \
        --enable-pie \
        --enable-now

%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sharedstatedir/%name/{cas,requests}
mkdir -p %buildroot%_tmpfilesdir
mv %buildroot/usr%_tmpfilesdir/%name.conf %buildroot%_tmpfilesdir/%name.conf
%find_lang %name

%check
%make check

%post
%post_service %name

%preun
%preun_service %name

%triggerpostun -- certmonger <= 0.79.7-alt1
# update certmonger helper paths for existing installations
# /usr/lib/certmonger/ => /usr/libexec/certmonger/
set -o errexit
set -o nounset
set -o pipefail

export LC_ALL=C

help () {
    printf -- 'Please, check and update certmonger CAs helpers manually\n' >&2
    exit 0
}

getcert refresh-ca -a >/dev/null 2>&1 || help
cas_list="$(getcert list-cas | grep -o "^CA '.*':" | cut -d\' -f2 | \
              tr '\n' ' ')" || \
         help

old_path=" /usr/lib/certmonger/"
new_path=" /usr/libexec/certmonger/"
helper=
modified_helper=
for ca in $cas_list; do
    # helper could be empty
    helper="$(getcert list-cas -c "$ca" | grep 'helper-location:' | \
                cut -d':' -f2)" || \
           continue
    if [ -z "$helper" -o -n "${helper##*$old_path*}" ]; then
        continue
    fi
    modified_helper="${helper//$old_path/$new_path}"
    # remove leading whitespace
    modified_helper="$(sed 's/^[[:space:]]*//' <<<"$modified_helper")"
    getcert modify-ca -c "$ca" -e "$modified_helper" || help
done
getcert refresh-ca -a >/dev/null 2>&1 || help

%files -f %name.lang
%doc README.md LICENSE STATUS doc/*.txt
%config(noreplace) %_sysconfdir/dbus-1/system.d/certmonger.conf
%config(noreplace) %_sysconfdir/certmonger/certmonger.conf
%attr(0644,root,root) %config(noreplace) %_tmpfilesdir/certmonger.conf
%_datadir/dbus-1/services/certmonger.service
%_datadir/dbus-1/system-services/org.fedorahosted.certmonger.service
%_unitdir/certmonger.service
%dir %_sysconfdir/certmonger
%_bindir/certmaster-getcert
%_bindir/getcert
%_bindir/ipa-getcert
%_bindir/local-getcert
%_bindir/selfsign-getcert
%_sbindir/certmonger
%dir %_libexecdir/certmonger
%_libexecdir/certmonger/certmaster-submit
%_libexecdir/certmonger/certmonger-session
%_libexecdir/certmonger/dogtag-ipa-renew-agent-submit
%_libexecdir/certmonger/dogtag-submit
%_libexecdir/certmonger/ipa-submit
%_libexecdir/certmonger/local-submit
%_libexecdir/certmonger/scep-submit
%dir %_sharedstatedir/certmonger
%_sharedstatedir/certmonger/cas/
%_sharedstatedir/certmonger/local/
%_sharedstatedir/certmonger/requests/
%_man1dir/certmaster-getcert.1.*
%_man1dir/getcert-*.1.*
%_man1dir/getcert.1.*
%_man1dir/ipa-getcert.1.*
%_man1dir/local-getcert.1.*
%_man1dir/selfsign-getcert.1.*
%_man5dir/certmonger.conf.5.*
%_man8dir/certmonger-*.8.*
%_man8dir/certmonger.8.*

%changelog
* Mon Sep 28 2020 Stanislav Levin <slev@altlinux.org> 0.79.11-alt1
- 0.79.9 -> 0.79.11.

* Mon Apr 20 2020 Stanislav Levin <slev@altlinux.org> 0.79.9-alt1
- 0.79.8 -> 0.79.9.

* Wed Nov 06 2019 Stanislav Levin <slev@altlinux.org> 0.79.8-alt2
- Added workaround for half-migrated NSS db (NSS_INIT_NOMODDB).
- Migrated tests to Python3.

* Wed Aug 14 2019 Stanislav Levin <slev@altlinux.org> 0.79.8-alt1
- 0.79.7 -> 0.79.8.

* Tue Apr 23 2019 Stanislav Levin <slev@altlinux.org> 0.79.7-alt2
- Fixed upgrade 0.78->0.79.

* Tue Mar 26 2019 Stanislav Levin <slev@altlinux.org> 0.79.7-alt1
- 0.79.6 -> 0.79.7.

* Wed Jan 16 2019 Stanislav Levin <slev@altlinux.org> 0.79.6-alt3.gitba4c5049
- Applied upstream fixes.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 0.79.6-alt2
- Fix build with new openssl1.1.

* Fri May 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.79.6-alt1
- Updated to upstream version 0.79.6.

* Thu Mar 15 2018 Stanislav Levin <slev@altlinux.org> 0.79.5-alt2
- Keep LC_*, LANG, set default LC_CTYPE

* Wed Dec 20 2017 Stanislav Levin <slev@altlinux.org> 0.79.5-alt1
- 0.78.6 -> 0.79.5

* Fri Aug 11 2017 Mikhail Efremov <sem@altlinux.org> 0.78.6-alt2
- Use _unpackaged_files_terminate_build.
- Use post_service/preun_service.
- Package dbus-1/system-services/*.service.
- Patch from upstream (fix build):
  + Fix conversions of bit lengths to byte lengths.
- Change dogtag port.

* Fri Nov 11 2016 Mikhail Efremov <sem@altlinux.org> 0.78.6-alt1
- certsave: Fix double free.
- Updated to 0.78.6.

* Wed Oct 12 2016 Mikhail Efremov <sem@altlinux.org> 0.78-alt1
- Fix XMLRPC_LIBS value.
- Updated to 0.78.

* Tue Apr 29 2014 Timur Aitov <timonbl4@altlinux.org> 0.74-alt1
- first build for ALT

* Thu Apr  3 2014 Nalin Dahyabhai <nalin@redhat.com> 0.74-1
- also save state when we exit due to SIGHUP
- don't get tripped up when enrollment helpers hand us certificates which
  include CRLF line terminators (ticket #25)
- be tolerant of certificate issuer names, subject names, DNS, email, and
  Kerberos principal namem subjectAltNames, and crl distribution point URLs
  that contain newlines
- read and cache the certificate template extension in certificates
- enforce different minimum key sizes depending on the type of key we're
  trying to generate
- store DER versions of subject, issuer and template subject, if we have
  them (Jan Cholasta, ticket #26)
- when generating signing requests with subject names that don't quite parse
  as subject names, encode what we're given as PrintableString rather than
  as a UTF8String
- always chdir() to a known location at startup, even if we're not becoming
  a daemon
- fix a couple of memory leaks (static analysis)
- add missing buildrequires: on which

* Thu Feb 20 2014 Nalin Dahyabhai <nalin@redhat.com> 0.73-1
- updates to 0.73
  - getcert no longer claims to be stuck when a CA is unreachable,
    because the daemon isn't actually stuck

* Mon Feb 17 2014 Nalin Dahyabhai <nalin@redhat.com>
- updates to 0.73
  - also pass the key type to enrollment helpers in the environment as
    a the value of "CERTMONGER_KEY_TYPE"

* Mon Feb 10 2014 Nalin Dahyabhai <nalin@redhat.com>
- move the tmpfiles.d file from /etc/tmpfiles.d to %%{_tmpfilesdir},
  where it belongs

* Mon Feb 10 2014 Nalin Dahyabhai <nalin@redhat.com>
- updates for 0.73
  - set the flag to encode EC public key parameters using named curves
    instead of the default of all-the-details when using OpenSSL
  - don't break when NSS supports secp521r1 but OpenSSL doesn't
  - also pass the CA nickname to enrollment helpers in the environment as
    a text value in "CERTMONGER_CA_NICKNAME", so they can use that value
    when reading configuration settings
  - also pass the SPKAC value to enrollment helpers in the environment as
    a base64 value in "CERTMONGER_SPKAC"
  - also pass the request's SubjectPublicKeyInfo value to enrollment helpers
    in the environment as a base64 value in "CERTMONGER_SPKI"
  - when generating signing requests using NSS, be more accommodating of
    requested subject names that don't parse properly

* Mon Feb  3 2014 Nalin Dahyabhai <nalin@redhat.com> 0.72-1
- update to 0.72
  - support generating DSA parameters and keys on sufficiently-new OpenSSL
    and NSS
  - support generating EC keys when OpenSSL and NSS support it, using key
    size to select the curve to use from among secp256r1, secp384r1,
    secp521r1 (which are the ones that are usually available, though
    secp521r1 isn't always, even if the other two are)
  - stop trying to cache public key parameters at all and instead cache public
    key info properly
  - encode the friendlyName attribute in signing requests as a BMPString,
    not as a PrintableString
  - catch more filesystem permissions problems earlier (more of #996581)

* Mon Jan 27 2014 Nalin Dahyabhai <nalin@redhat.com> 0.71-1
- check for cases where we fail to allocate memory while reading a request
  or CA entry from disk (John Haxby)
- only handle one watch at a time, which should avoid abort() during
  attempts to reconnect to the message bus after losing our connection
  to it (#1055521)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.70-2
- Mass rebuild 2014-01-24

* Thu Jan  2 2014 Nalin Dahyabhai <nalin@redhat.com> 0.70-1
- add a --with-homedir option to configure, and use it, since subprocesses
  which we run and which use NSS may attempt to write to $HOME/.pki, and
  0.69's strategy of setting that to "/" was rightly hitting SELinux policy
  denials (#1047798)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.69-2
- Mass rebuild 2013-12-27

* Mon Dec  9 2013 Nalin Dahyabhai <nalin@redhat.com> 0.69-1
- tweak how we decide whether we're on the master or a minion when we're
  told to use certmaster as a CA
- clean up one of the tests so that it doesn't have to work around internal
  logging producing duplicate messages
- when logging errors while setting up to contact xmlrpc servers, explicitly
  note that the error is client-side
- don't abort() due to incorrect locking when an attempt to save an issued
  certificate to the designated location fails (part of #1032760/#1033333,
  ticket #22)
- when reading an issued certificate from an enrollment helper, ignore
  noise before or after the certificate itself (more of #1032760/1033333,
  ticket #22)
- run subprocesses in a cleaned-up environment (more of #1032760/1033333,
  ticket #22)
- clear the ca-error that we saved when we had an error talking to the CA if we
  subsequently succeed in talking to the CA
- various other static-analysis fixes

* Thu Aug 29 2013 Nalin Dahyabhai <nalin@redhat.com> 0.68-1
- notice when the OpenSSL RNG isn't seeded
- notice when saving certificates or keys fails due to filesystem-related
  permission denial (#996581)

* Tue Aug  6 2013 Nalin Dahyabhai <nalin@redhat.com> 0.67-3
- pull up a patch from master to adapt self-tests to certutil's diagnostic
  output having changed (#992050)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Nalin Dahyabhai <nalin@redhat.com> 0.67-1
- when saving certificates to NSS databases, try to preserve the trust
  value assigned to a previously-present certificate with the same nickname
  and subject, if one is found
- when saving certificates to NSS databases, also prune certificates from
  the database which have both the same nickname and subject as the one
  we're adding, to avoid tripping up tools that only fetch one certificate
  by nickname

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Nalin Dahyabhai <nalin@redhat.com> 0.66-1
- build as position-independent executables with early binding (#883966)
- also don't tag the unit file as a configuration file (internal tooling)

* Wed Jan 23 2013 Nalin Dahyabhai <nalin@redhat.com> 0.65-2
- don't tag the D-Bus session .service file as a configuration file (internal
  tooling)

* Tue Jan  8 2013 Nalin Dahyabhai <nalin@redhat.com> 0.65-1
- fix a crash in the self-tests

* Tue Jan  8 2013 Nalin Dahyabhai <nalin@redhat.com> 0.64-1
- at startup, if we resume the state machine for a given certificate to a state
  which expects to have the newly-added lock already acquired, acquire it
  before moving on with the certificate's work (still aimed at fixing #883484)

* Tue Dec 18 2012 Nalin Dahyabhai <nalin@redhat.com> 0.63-1
- serialize access to NSS databases and the running of pre- and post-save
  commands which might also access them (possibly fixing part of #883484)

* Thu Nov 29 2012 Nalin Dahyabhai <nalin@redhat.com> 0.62-1
- add a -u flag to getcert to enable requesting a keyUsage extension value
- request subjectKeyIdentifier extensions from CAs, and include them in
  self-signed certificates
- request basicConstraints from CAs, defaulting to requests for end-entity
  certificates
- when requesting CA certificates, also request authorityKeyIdentifier
- add support for requesting CRL distribution point and authorityInfoAccess
  extensions that specify OCSP responder locations
- don't crash when OpenSSL can't build a template certificate from a request
  when we're in FIPS mode
- put NSS in FIPS mode, when the system booted that way, except when we're
  trying to write certificates to a database
- fix CSR generation and self-signing in FIPS mode with NSS
- fix self-signing in FIPS mode with OpenSSL
- new languages from the translation team: mai, ml, nn, ga

* Tue Nov 27 2012 Nalin Dahyabhai <nalin@redhat.com> 0.61-3
- backport change from git to not choke if X509_REQ_to_X509() fails when we're
  self-signing using OpenSSL
- backport another change from git to represent this as a CA-rejected error

* Mon Sep 24 2012 Nalin Dahyabhai <nalin@redhat.com> 0.61-1
- fix a regression in reading old request tracking files where the
  request was in state NEED_TO_NOTIFY or NOTIFYING

* Wed Sep  5 2012 Nalin Dahyabhai <nalin@redhat.com> 0.60-1
- adjust internals of logic for talking to dogtag to at least have a
  concept of non-agent cases
- when talking to an IPA server's internal Dogtag instance, infer which
  ports the CA is listening on from the "dogtag_version" setting in the
  IPA configuration (Ade Lee)
- send a notification (or log a message, whatever) when we save a new
  certificate (#766167)

* Mon Jul 30 2012 Nalin Dahyabhai <nalin@redhat.com>
- fix a bad %%preun scriptlet

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Nalin Dahyabhai <nalin@redhat.com> 0.59-1
- mostly documentation updates

* Fri Jun 29 2012 Nalin Dahyabhai <nalin@redhat.com> 0.58-1
- add a "dogtag-ipa-renew-agent" CA so that we can renew certificates using
  an IPA server's internal Dogtag instance
- export the requested profile and old certificate to enrollment helpers
- make libxml and libcurl into hard build-time requirements
- serialize all pre/save/post sequences to make sure that stop/save/start
  doesn't become stop1/save1/stop2/start1/save2/start2 when we're stopping
  a service while we muck with more than one of its certificates

* Fri Jun 15 2012 Nalin Dahyabhai <nalin@redhat.com>
- add a command option (-T) to getcert for specifying which enrollment
  profile to tell a CA that we're using, in case it cares (#10)

* Thu Jun 14 2012 Nalin Dahyabhai <nalin@redhat.com> 0.57-1
- clarify that the command passed to getcert -C is a "post"-save command
- add a "pre"-save command option to getcert, specified with the -B flag (#9)
- after we notify of an impending not-valid-after approaching, don't do it
  again immediately

* Sat Mar  3 2012 Nalin Dahyabhai <nalin@redhat.com> 0.56-1
- when a caller sets the is-default flag on a CA, and another CA is no longer
  the default, emit the PropertiesChanged signal on the CA which is not the
  default, instead on the new default a second time
- drop some dead code from the D-Bus message handlers (static analysis,
  #796813)
- cache public keys when we read private keys
- go back to printing an error indicating that we're missing a required
  argument when we're missing a required argument, not that the option is
  invalid (broken since 0.51, #796542)

* Wed Feb 15 2012 Nalin Dahyabhai <nalin@redhat.com> 0.55-1
- allow root to use our implementation of org.freedesktop.DBus.Properties
- take more care to not emit useless PropertiesChanged signals

* Wed Feb 15 2012 Nalin Dahyabhai <nalin@redhat.com> 0.54-1
- fix setting the group ID when spawning the post-save command

* Tue Feb 14 2012 Nalin Dahyabhai <nalin@redhat.com> 0.53-1
- large changes to the D-Bus glue, exposing a lot of data which we were
  providing via D-Bus getter methods as properties, and providing more
  accurate introspection data
- emit a signal when the daemon saves a certificate to the destination
  location, and provide an option to have the daemon spawn an arbitrary
  command at that point, too (#766167)
- enable starting the service by default on RHEL (#765600)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Nalin Dahyabhai <nalin@redhat.com> 0.52-1
- note that SELinux usually confines us to writing only to cert_t in
  doc/getting-started.txt (#765599)
- fix crashes when we add a request during our first run when we're
  populating the hard-coded CA list
- properly deal with cases where a path is passed to us is "./XXX"
- in session mode, create our data directories as we go

* Tue Dec  6 2011 Nalin Dahyabhai <nalin@redhat.com> 0.51-1
- api: lift restrictions on characters used in request and CA nicknames by
  making their object names not incorporate their nicknames
- api: add find_request_by_nickname and find_ca_by_nickname
- certmonger-ipa-submit.8: list -k, -K, -t in the summary, document -K
- getcert: print "invalid option" error messages ourselves (#756291)
- ipa-submit: supply a Referer: header when submitting requests to IPA
  (#750617, needed for #747710)

* Fri Oct 14 2011 Nalin Dahyabhai <nalin@redhat.com> 0.50-1
- really fix these this time:
 - getcert: error out when "list -c" finds no matching CA (#743488)
 - getcert: error out when "list -i" finds no matching request (#743485)

* Wed Oct 12 2011 Nalin Dahyabhai <nalin@redhat.com> 0.49-1
- when using an NSS database, skip loading the module database (#743042)
- when using an NSS database, skip loading root certs
- generate SPKAC values when generating CSRs, though we don't do anything
  with SPKAC values yet
- internally maintain and use challenge passwords, if we have them
- behave better when certificates have shorter lifetimes
- add/recognize/handle notification type "none"
- getcert: error out when "list -c" finds no matching CA (#743488)
- getcert: error out when "list -i" finds no matching request (#743485)

* Thu Sep 29 2011 Nalin Dahyabhai <nalin@redhat.com> 0.48-1
- don't incorrectly assume that CERT_ImportCerts() returns a NULL-terminated
  array (#742348)

* Tue Sep 27 2011 Nalin Dahyabhai <nalin@redhat.com> 0.47-1
- getcert: distinguish between {stat() succeeds but isn't a directory} and
  {stat() failed} when printing an error message (#739903)
- getcert resubmit/start-tracking: when we're looking for an existing request
  by ID, and we don't find one, note that specifically (#741262)

* Mon Aug 29 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.46-1.1
- Rebuild against fixed libtevent version

* Mon Aug 15 2011 Nalin Dahyabhai <nalin@redhat.com> 0.46-1
- treat the ability to access keys in an NSS database without using a PIN,
  when we've been told we need one, as an error (#692766, really this time)

* Thu Aug 11 2011 Nalin Dahyabhai <nalin@redhat.com> 0.45-1
- modify the systemd .service file to be a proper 'dbus' service (more
  of #718172)

* Thu Aug 11 2011 Nalin Dahyabhai <nalin@redhat.com> 0.44-1
- check specifically for cases where a specified token that we need to
  use just isn't present for whatever reason (#697058)

* Wed Aug 10 2011 Nalin Dahyabhai <nalin@redhat.com> 0.43-1
- add a -K option to ipa-submit, to use the current ccache, which makes
  it easier to test

* Fri Aug  5 2011 Nalin Dahyabhai <nalin@redhat.com>
- if xmlrpc-c's struct xmlrpc_curl_xportparms has a gss_delegate field, set
  it to TRUE when we're doing Negotiate auth (#727864, #727863, #727866)

* Wed Jul 13 2011 Nalin Dahyabhai <nalin@redhat.com>
- treat the ability to access keys in an NSS database without using a PIN,
  when we've been told we need one, as an error (#692766)
- when handling "getcert resubmit" requests, if we don't have a key yet,
  make sure we go all the way back to generating one (#694184)
- getcert: try to clean up tests for NSS and PEM file locations (#699059)
- don't try to set reconnect-on-exit policy unless we managed to connect
  to the bus (#712500)
- handle cases where we specify a token but the storage token isn't
  known (#699552)
- getcert: recognize -i and storage options to narrow down which requests
  the user wants to know about (#698772)
- output hints when the daemon has startup problems, too (#712075)
- add flags to specify whether we're bus-activated or not, so that we can
  exit if we have nothing to do after handling a request received over
  the bus if some specified amount of time has passed
- explicitly disallow non-root access in the D-Bus configuration (#712072)
- migrate to systemd on releases newer than Fedora 15 or RHEL 6 (#718172)
- fix a couple of incorrect calls to talloc_asprintf() (#721392)

* Wed Apr 13 2011 Nalin Dahyabhai <nalin@redhat.com> 0.42-1
- getcert: fix a buffer overrun preparing a request for the daemon when
  there are more parameters to encode than space in the array (#696185)
- updated translations: de, es, id, pl, ru, uk

* Mon Apr 11 2011 Nalin Dahyabhai <nalin@redhat.com> 0.41-1
- read information about the keys we've just generated before proceeding
  to generating a CSR (part of #694184, part of #695675)
- when processing a "resubmit" request from getcert, go back to key
  generation if we don't have keys yet, else go back to CSR generation as
  before (#694184, #695675)
- configure with --with-tmpdir=/var/run/certmonger and own /var/run/certmonger
  (#687899), and add a systemd tmpfiles.d control file for creating
  /var/run/certmonger on Fedora 15 and later
- let session instances exit when they get disconnected from the bus
- use a lock file to make sure there's only one session instance messing
  around with the user's files at a time
- fix errors saving certificates to NSS databases when there's already a
  certificate there with the same nickname (#695672)
- make key and certificate location output from 'getcert list' more properly
  translatable (#7)

* Mon Mar 28 2011 Nalin Dahyabhai <nalin@redhat.com> 0.40-1
- update to 0.40
  - fix validation check on EKU OIDs in getcert (#691351)
  - get session bus mode sorted
  - add a list of recognized EKU values to the getcert-request man page

* Fri Mar 25 2011 Nalin Dahyabhai <nalin@redhat.com> 0.39-1
- update to 0.39
  - fix use of an uninitialized variable in the xmlrpc-based submission
    helpers (#690886)

* Thu Mar 24 2011 Nalin Dahyabhai <nalin@redhat.com> 0.38-1
- update to 0.38
  - catch cases where we can't read a PIN file, but we never have to log
    in to the token to access the private key (more of #688229)

* Tue Mar 22 2011 Nalin Dahyabhai <nalin@redhat.com> 0.37-1
- update to 0.37
  - be more careful about checking if we can read a PIN file successfully
    before we even call an API that might need us to try (#688229)
  - fix strict aliasing warnings

* Tue Mar 22 2011 Nalin Dahyabhai <nalin@redhat.com> 0.36-1
- update to 0.36
  - fix some use-after-free bugs in the daemon (#689776)
  - fix a copy/paste error in certmonger-ipa-submit(8)
  - getcert now suppresses error details when not given its new -v option
    (#683926, more of #681641/#652047)
  - updated translations
    - de, es, pl, ru, uk
    - indonesian translation is now for "id" rather than "in"

* Wed Mar  2 2011 Nalin Dahyabhai <nalin@redhat.com> 0.35.1-1
- fix a self-test that broke because one-year-from-now is now a day's worth
  of seconds further out than it was a few days ago

* Mon Feb 14 2011 Nalin Dahyabhai <nalin@redhat.com> 0.35-1
- update to 0.35
  - self-test fixes to rebuild properly in mock (#670322)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Nalin Dahyabhai <nalin@redhat.com> 0.34-1
- update to 0.34
  - explicitly note the number of requests we're tracking in the output of
    "getcert list" (#652049)
  - try to offer some suggestions when we get certain specific errors back
    in "getcert" (#652047)
  - updated translations
    - es

* Thu Dec 23 2010 Nalin Dahyabhai <nalin@redhat.com> 0.33-1
- update to 0.33
  - new translations
    - id by Okta Purnama Rahadian!
  - updated translations
    - pl, uk
  - roll up assorted fixes for defects

* Fri Nov 12 2010 Nalin Dahyabhai <nalin@redhat.com> 0.32-2
- depend on the e2fsprogs libuuid on Fedora and RHEL releases where it's
  not part of util-linux-ng

* Wed Oct 13 2010 Nalin Dahyabhai <nalin@redhat.com> 0.32-1
- oops, rfc5280 says we shouldn't be populating unique identifiers, so
  make it a configuration option and default the behavior to off

* Tue Oct 12 2010 Nalin Dahyabhai <nalin@redhat.com> 0.31-1
- start populating the optional unique identifier fields in self-signed
  certificates

* Thu Sep 30 2010 Nalin Dahyabhai <nalin@redhat.com> 0.30-4
- explicitly require "dbus" to try to ensure we have a running system bus
  when we get started (#639126)

* Wed Sep 29 2010 jkeating - 0.30-3
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Nalin Dahyabhai <nalin@redhat.com> 0.30-2
- try to SIGHUP the messagebus daemon at first install so that it'll
  let us claim our service name if it isn't restarted before we are
  first started (#636876)

* Wed Aug 25 2010 Nalin Dahyabhai <nalin@redhat.com> 0.30-1
- update to 0.30
  - fix errors computing the time at the end of an interval that were
    caught by self-tests

* Mon Aug 23 2010 Nalin Dahyabhai <nalin@redhat.com> 0.29-1
- update to 0.29
  - fix 64-bit cleanliness issue using libdbus
  - actually include the full set of tests in tarballs

* Tue Aug 17 2010 Nalin Dahyabhai <nalin@redhat.com> 0.28-1
- update to 0.28
  - fix self-signing certificate notBefore and notAfter values on 32-bit
    machines

* Tue Aug 17 2010 Nalin Dahyabhai <nalin@redhat.com> 0.27-1
- update to 0.27
  - portability and test fixes

* Fri Aug 13 2010 Nalin Dahyabhai <nalin@redhat.com> 0.26-1
- update to 0.26
  - when canceling a submission request that's being handled by a helper,
    reap the child process's status after killing it (#624120)

* Fri Aug 13 2010 Nalin Dahyabhai <nalin@redhat.com> 0.25-1
- update to 0.25
  - new translations
    - in by Okta Purnama Rahadian!
  - fix detection of cases where we can't access a private key in an NSS
    database because we don't have the PIN
  - teach '*getcert start-tracking' about the -p and -P options which the
    '*getcert request' commands already understand (#621670), and also
    the -U, -K, -E, and -D flags
  - double-check that the nicknames of keys we get back from
    PK11_ListPrivKeysInSlot() match the desired nickname before accepting
    them as matches, so that our tests won't all blow up on EL5
  - fix dynamic addition and removal of CAs implemented through helpers

* Mon Jun 28 2010 Nalin Dahyabhai <nalin@redhat.com> 0.24-4
- init script: ensure that the subsys lock is created whenever we're called to
  "start" when we're already running (even more of #596719)

* Tue Jun 15 2010 Nalin Dahyabhai <nalin@redhat.com> 0.24-3
- more gracefully handle manual daemon startups and cleaning up of unexpected
  crashes (still more of #596719)

* Thu Jun 10 2010 Nalin Dahyabhai <nalin@redhat.com> 0.24-2
- don't create the daemon pidfile until after we've connected to the D-Bus
  (still more of #596719)

* Tue Jun  8 2010 Nalin Dahyabhai <nalin@redhat.com> 0.24-1
- update to 0.24
  - keep the lock on the pid file, if we have one, when we fork, and cancel
    daemon startup if we can't gain ownership of the lock (the rest of #596719)
  - make the man pages note which external configuration files we consult when
    submitting requests to certmaster and ipa CAs

* Thu May 27 2010 Nalin Dahyabhai <nalin@redhat.com> 0.23-1
- update to 0.23
  - new translations
    - pl by Piotr Drąg!
  - cancel daemon startup if we can't gain ownership of our well-known
    service name on the DBus (#596719)

* Fri May 14 2010 Nalin Dahyabhai <nalin@redhat.com> 0.22-1
- update to 0.22
  - new translations
    - de by Fabian Affolter!
  - certmaster-submit: don't fall over when we can't find a certmaster.conf
    or a minion.conf (i.e., certmaster isn't installed) (#588932)
  - when reading extension values from certificates, prune out duplicate
    principal names, email addresses, and hostnames

* Tue May  4 2010 Nalin Dahyabhai <nalin@redhat.com> 0.21-1
- update to 0.21
  - getcert/*-getcert: relay the desired CA to the local service, whether
    specified on the command line (in getcert) or as a built-in hard-wired
    default (in *-getcert) (#584983)
  - flesh out the default certmonger.conf so that people can get a feel for
    the expected formatting (Jenny Galipeau)

* Wed Apr 21 2010 Nalin Dahyabhai <nalin@redhat.com> 0.20-1
- update to 0.20
  - correctly parse certificate validity periods given in years (spotted by
    Stephen Gallagher)
  - setup for translation
    - es by Héctor Daniel Cabrera!
    - ru by Yulia Poyarkova!
    - uk by Yuri Chornoivan!
  - fix unpreprocessed defaults in certmonger.conf's man page
  - tweak the IPA-specific message that indicates a principal name also needs
    to be specified if we're not using the default subject name (#579542)
  - make the validity period of self-signed certificates into a configuration
    setting and not a piece of the state information we track about the signer
  - init script: exit with status 2 instead of 1 when invoked with an
    unrecognized argument (#584517)

* Tue Mar 23 2010 Nalin Dahyabhai <nalin@redhat.com> 0.19-1
- update to 0.19
  - correctly initialize NSS databases that need to be using a PIN
  - add certmonger.conf, for customizing notification timings and settings,
    and use of digests other than the previously-hard-coded SHA256, and
    drop those settings from individual requests
  - up the default self-sign validity interval from 30 days to 365 days
  - drop the first default notification interval from 30 days to 28 days
    (these two combined to create a fun always-reissuing loop earlier)
  - record the token which contains the key or certificate when we're
    storing them in an NSS database, and report it
  - improve handling of cases where we're supposed to use a PIN but we
    either don't have one or we have the wrong one
  - teach getcert to accept a PIN file's name or a PIN value when adding
    a new entry
  - update the IPA submission helper to use the new 'request_cert' signature
    that's landing soon
  - more tests

* Fri Feb 12 2010 Nalin Dahyabhai <nalin@redhat.com> 0.18-1
- update to 0.18
  - add support for using encrypted storage for keys, using PIN values
    supplied directly or read from files whose names are supplied
  - don't choke on NSS database locations that use the "sql:" or "dbm:"
    prefix

* Mon Jan 25 2010 Nalin Dahyabhai <nalin@redhat.com> 0.17-2
- make the D-Bus configuration file (noreplace) (#541072)
- make the %%check section and the deps we have just for it conditional on
  the same macro (#541072)

* Wed Jan  6 2010 Nalin Dahyabhai <nalin@redhat.com> 0.17-1
- update to 0.17
  - fix a hang in the daemon (Rob Crittenden)
  - documentation updates
  - fix parsing of submission results from IPA (Rob Crittenden)

* Fri Dec 11 2009 Nalin Dahyabhai <nalin@redhat.com> 0.16-1
- update to 0.16
  - set a umask at startup (Dan Walsh)

* Tue Dec  8 2009 Nalin Dahyabhai <nalin@redhat.com> 0.15-1
- update to 0.15
  - notice that a directory with a trailing '/' is the same location as the
    directory without it
  - fix handling of the pid file when we write one (by actually giving it
    contents)

* Wed Nov 25 2009 Nalin Dahyabhai <nalin@redhat.com> 0.14-1
- update to 0.14
  - check key and certificate location at add-time to make sure they're
    absolute paths to files or directories, as appropriate
  - IPA: dig into the 'result' item if the named result value we're looking
    for isn't in the result struct

* Tue Nov 24 2009 Nalin Dahyabhai <nalin@redhat.com> 0.13-1
- update to 0.13
  - change the default so that we default to trying to auto-refresh
    certificates unless told otherwise
  - preemptively enforce limitations on request nicknames so that they
    make valid D-Bus object path components

* Tue Nov 24 2009 Nalin Dahyabhai <nalin@redhat.com> 0.12-1
- update to 0.12
  - add a crucial bit of error reporting when CAs reject our requests
  - count the number of configured CAs correctly

* Mon Nov 23 2009 Nalin Dahyabhai <nalin@redhat.com> 0.11-1
- update to 0.11
  - add XML-RPC submission for certmaster and IPA
  - prune entries with duplicate names from the data store

* Fri Nov 13 2009 Nalin Dahyabhai <nalin@redhat.com> 0.10-1
- update to 0.10
  - add some compiler warnings and then fix them

* Fri Nov 13 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9-1
- update to 0.9
  - run external submission helpers correctly
  - fix signing of signing requests generated for keys stored in files
  - only care about new interface and route notifications from netlink,
    and ignore notifications that don't come from pid 0
  - fix logic for determining expiration status
  - correct the version number in self-signed certificates

* Tue Nov 10 2009 Nalin Dahyabhai <nalin@redhat.com> 0.8-1
- update to 0.8
  - encode windows UPN values in requests correctly
  - watch for netlink routing changes and restart stalled submission requests
  - 'getcert resubmit' can force a regeneration of the CSR and submission

* Fri Nov  6 2009 Nalin Dahyabhai <nalin@redhat.com> 0.7-1
- update to 0.7
  - first cut at a getting-started document
  - refactor some internal key handling with NSS
  - check for duplicate request nicknames at add-time

* Tue Nov  3 2009 Nalin Dahyabhai <nalin@redhat.com> 0.6-1
- update to 0.6
  - man pages
  - 'getcert stop-tracking' actually makes the server forget now
  - 'getcert request -e' was redundant, dropped the -e option
  - 'getcert request -i' now sets the request nickname
  - 'getcert start-tracking -i' now sets the request nickname

* Mon Nov  2 2009 Nalin Dahyabhai <nalin@redhat.com> 0.5-1
- update to 0.5
  - packaging fixes
  - add a selfsign-getcert client
  - self-signed certs now get basic constraints and their own serial numbers
  - accept id-ms-kp-sc-logon as a named EKU value in a request

* Thu Oct 29 2009 Nalin Dahyabhai <nalin@redhat.com> 0.4-1
- update to 0.4

* Thu Oct 22 2009 Nalin Dahyabhai <nalin@redhat.com> 0.1-1
- update to 0.1

* Sun Oct 18 2009 Nalin Dahyabhai <nalin@redhat.com> 0.0-1
- initial package

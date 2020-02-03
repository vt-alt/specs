Name: ca-certificates
Version: 2020.01.23
Release: alt1

Summary: Common CA Certificates
License: MPL-2.0
Group: System/Base
BuildArch: noarch

Source0: mozilla.tar
Source1: ca-bundle.trust.p11-kit

BuildRequires: openssl
BuildRequires: python3(base64)
BuildRequires: python3(os)
BuildRequires: python3(re)
BuildRequires: python3(textwrap)
BuildRequires: python3(urllib)
BuildRequires: python3(subprocess)

Requires: ca-trust

%description
This package contains a bundle of X.509 certificates of public
Certificate Authorities (CA).  This is useful for any applications to
verify SSL/TLS connection.

Note that certificate authorities whose certificates are included in
this package are not in any way audited for trustworthiness and RFC3647
compliance, and that full responsibility to assess them rests with the
user.

%prep
%setup -c

%build
export TZ=UTC
pushd mozilla
	python3 ./certdata2pem.py >c2p.log 2>c2p.err
popd
cat %SOURCE1 mozilla/*.tmp-p11-kit > ca-bundle.trust.p11-kit

%install
install -pD -m 644 ca-bundle.trust.p11-kit \
	%buildroot%_datadir/pki/ca-trust-source/ca-bundle.trust.p11-kit

%files
%_datadir/pki/ca-trust-source/ca-bundle.trust.p11-kit

%changelog
* Thu Jan 23 2020 Alexey Gladkov <legion@altlinux.ru> 2020.01.23-alt1
- mozilla: sync with nss-3.49.1.

* Mon Oct 28 2019 Alexey Gladkov <legion@altlinux.ru> 2019.10.28-alt1
- mozilla: sync with nss-3.47.
- update license tag.
- port certdata2pem.py to python3.

* Tue Sep 10 2019 Alexey Gladkov <legion@altlinux.ru> 2019.09.10-alt1
- mozilla: sync with nss-3.46.

* Thu Jul 11 2019 Alexey Gladkov <legion@altlinux.ru> 2019.07.11-alt1
- mozilla: sync with nss-3.45.

* Sun Mar 31 2019 Alexey Gladkov <legion@altlinux.ru> 2019.03.31-alt1
- mozilla: sync with nss-3.43.

* Fri Feb 01 2019 Alexey Gladkov <legion@altlinux.ru> 2019.02.01-alt1
- mozilla: sync with nss-3.42.1.

* Mon Nov 12 2018 Alexey Gladkov <legion@altlinux.ru> 2018.11.12-alt1
- mozilla: sync with nss-3.40.

* Sun Sep 09 2018 Alexey Gladkov <legion@altlinux.ru> 2018.09.09-alt1
- mozilla: sync with nss-3.39.

* Thu Dec 28 2017 Mikhail Efremov <sem@altlinux.org> 2017.11.22-alt3
- Split all but CA bundle itself to separate ca-trust package.
- Use p11-kit for certificates bundle.

* Thu Dec 21 2017 L.A. Kostis <lakostis@altlinux.ru> 2017.11.22-alt2
- Remove expired ALT CA cert: nobody cares.

* Thu Dec 14 2017 L.A. Kostis <lakostis@altlinux.ru> 2017.11.22-alt1
- mozilla:
    + updated to October 2017 batch of root CA changes.
      (#bmo 1408080).
    + added Certum CA Root certificate back (#bmo 1418678).
- mozilla/mk-ca-bundle.pl: updated to v1.27.
- update BR: added perl-Encode to handle utf8 cert data.

* Mon May 22 2017 L.A. Kostis <lakostis@altlinux.ru> 2017.04.04-alt1
- mozilla: updated to March 2017 batch of root CA changes.
  (#bmo 1350859).

* Fri Sep 30 2016 L.A. Kostis <lakostis@altlinux.ru> 2016.09.28-alt1
- mozilla: updated to September 2016 CA batch root changes.
  (#bmo 1296689).

* Fri Jun 24 2016 L.A. Kostis <lakostis@altlinux.ru> 2016.05.25-alt1
- mozilla: updated to May 2016 CA batch root changes.
  (#bmo 1275533).

* Wed May 04 2016 L.A. Kostis <lakostis@altlinux.ru> 2016.02.25-alt1
- mozilla: updated to February 2016 batch root CA changes.
  (#bmo 1247990).

* Sun Feb 14 2016 L.A. Kostis <lakostis@altlinux.ru> 2015.10.29-alt1
- mozilla: updated to October 2015 batch root CA changes
  (#bmo 1214729).
- added /etc/pki/tls/certs dir (closes: #31213).

* Fri Aug 28 2015 L.A. Kostis <lakostis@altlinux.ru> 2015.08.04-alt1
- mozilla/certdata.txt: updated ca-certificates to v2.5.
- mozilla/mk-ca-bundle.pl:
  + updated to v1.25.
  + use SHA256 for fingerprint.
  + remove MD5 from valid cert signature list.
- remove cacert (untrusted signature).

* Wed Feb 08 2012 Dmitry V. Levin <ldv@altlinux.org> 2012.01.17-alt1
- mozilla/certdata.txt: updated to revision 1.81.
- Filtered out untrusted certs from mozilla bundle (closes: #26904).

* Thu Nov 10 2011 Dmitry V. Levin <ldv@altlinux.org> 2011.11.03-alt1
- mozilla/certdata.txt: updated to revision 1.80.

* Fri Sep 02 2011 Dmitry V. Levin <ldv@altlinux.org> 2011.09.02-alt1
- mozilla/certdata.txt: updated to revision 1.78.

* Thu Sep 30 2010 Dmitry V. Levin <ldv@altlinux.org> 2010.08.27-alt1
- mozilla/certdata.txt: Updated to revision 1.65.

* Sun Apr 05 2009 Dmitry V. Levin <ldv@altlinux.org> 2009.01.15-alt1
- cacert.org: Added http://www.cacert.org/certs/root.crt (closes: #14119).
- mozilla/certdata.txt: Updated to revision 1.51 (closes: #19484).

* Tue Feb 06 2007 Dmitry V. Levin <ldv@altlinux.org> 2007.02.06-alt1
- Imported a bundle of X.509 certificates of public Certificate
  Authorities (CA) from openssl package to this package.
- Updated Mozilla's root CA list.
- Added ALT Root CA.
- Added cacert.org Root CA.

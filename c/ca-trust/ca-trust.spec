%define pkidir %_sysconfdir/pki
%define catrustdir %pkidir/ca-trust
%define classic_tls_bundle ca-bundle.crt
%define openssl_format_trust_bundle ca-bundle.trust.crt
%define java_bundle java/cacerts
%define hooks_dir %_prefix/libexec/ca-trust/update.d

Name: ca-trust
Version: 0.1.2
Release: alt1

Summary: CA certificates and associated trust infrastructure
License: %gpl2plus
Group: System/Base
BuildArch: noarch

Source0: docs.tar
Source1: update-ca-trust
Source2: ca-trust.filetrigger
Source3: extract-openssl.hook
Source4: extract-pem.hook
Source5: extract-java.hook

BuildRequires(pre): rpm-build-licenses
BuildRequires: asciidoc asciidoc-a2x

Requires: p11-kit-trust
Requires: %_datadir/pki/ca-trust-source/ca-bundle.trust.p11-kit

%description
This package contains update-ca-trust utility, files and directories
used to manage a consolidated and dynamic configuration
feature of Certificate Authority (CA) certificates and associated trust.

The feature is available for new applications that read the
consolidated configuration files found in the /etc/pki/ca-trust/extracted
directory or that load the PKCS#11 module p11-kit-trust.so.

In order to enable legacy applications, that read the classic files or
access the classic module, to make use of the new consolidated and dynamic
configuration feature, the classic filenames have been changed to symbolic
links. The symbolic links refer to dynamically created and consolidated
output stored below the /etc/pki/ca-trust/extracted directory hierarchy.

%package java
Summary: update-ca-trust hook for Java
Group: System/Base
Requires: %name = %version-%release
Provides: ca-certificates-java = %version-%release
Obsoletes: ca-certificates-java < %version-%release

%description java
This package contains a hook for update-ca-trust which extracts
CA Certificates in java caserts format.

%prep
%setup -c

%build
pushd docs
# update-ca-trust manpage
asciidoc -v -d manpage -b docbook update-ca-trust.8.txt
xsltproc --nonet -o update-ca-trust.8 \
         /etc/asciidoc/docbook-xsl/manpage.xsl \
         update-ca-trust.8.xml
popd

%install
mkdir -p -m 755 %buildroot%pkidir/java
mkdir -p -m 755 %buildroot%pkidir/tls/certs
mkdir -p -m 755 %buildroot%catrustdir/source/{anchors,blacklist}
mkdir -p -m 755 %buildroot%catrustdir/extracted/{pem,openssl,java}
mkdir -p -m 755 %buildroot%_datadir/pki/ca-trust-source/{anchors,blacklist}
mkdir -p -m 755 %buildroot%_datadir/ca-certificates
mkdir -p -m 755 %buildroot%hooks_dir
mkdir -p -m 755 %buildroot%_bindir
mkdir -p -m 755 %buildroot%_man8dir

install -p -m 644 docs/update-ca-trust.8 %buildroot%_man8dir
install -p -m 644 docs/README.usr %buildroot%_datadir/pki/ca-trust-source/README
install -p -m 644 docs/README.etc %buildroot%catrustdir/README
install -p -m 644 docs/README.extr %buildroot%catrustdir/extracted/README
install -p -m 644 docs/README.java %buildroot%catrustdir/extracted/java/README
install -p -m 644 docs/README.openssl %buildroot%catrustdir/extracted/openssl/README
install -p -m 644 docs/README.pem %buildroot%catrustdir/extracted/pem/README
install -p -m 644 docs/README.src %buildroot%catrustdir/source/README

install -p -m 755 %SOURCE1 %buildroot%_bindir/update-ca-trust

install -pD -m 755 %SOURCE2 %buildroot%_rpmlibdir/ca-trust.filetrigger

install -p -m 755 %SOURCE3 %buildroot%hooks_dir/10-extract-openssl.hook
install -p -m 755 %SOURCE4 %buildroot%hooks_dir/20-extract-pem.hook
install -p -m 755 %SOURCE5 %buildroot%hooks_dir/30-extract-java.hook

# touch ghosted files that will be extracted dynamically
touch %buildroot%catrustdir/extracted/pem/tls-ca-bundle.pem
touch %buildroot%catrustdir/extracted/pem/email-ca-bundle.pem
touch %buildroot%catrustdir/extracted/pem/objsign-ca-bundle.pem
touch %buildroot%catrustdir/extracted/openssl/%openssl_format_trust_bundle
touch %buildroot%catrustdir/extracted/%java_bundle

# legacy filenames
ln -rs %buildroot%catrustdir/extracted/pem/tls-ca-bundle.pem \
    %buildroot%pkidir/tls/cert.pem
ln -rs %buildroot%catrustdir/extracted/pem/tls-ca-bundle.pem \
    %buildroot%pkidir/tls/certs/%classic_tls_bundle
ln -rs %buildroot%catrustdir/extracted/pem/tls-ca-bundle.pem \
    %buildroot%_datadir/ca-certificates/%classic_tls_bundle
ln -rs %buildroot%catrustdir/extracted/openssl/%openssl_format_trust_bundle \
    %buildroot%pkidir/tls/certs/%openssl_format_trust_bundle
ln -rs %buildroot%catrustdir/extracted/%java_bundle \
    %buildroot%pkidir/%java_bundle

%files
%pkidir/*
%_bindir/update-ca-trust
%_prefix/libexec/ca-trust/
%_datadir/pki/ca-trust-source/
%_datadir/ca-certificates/
%_man8dir/update-ca-trust.*
%_rpmlibdir/*.filetrigger
%ghost %catrustdir/extracted/pem/tls-ca-bundle.pem
%ghost %catrustdir/extracted/pem/email-ca-bundle.pem
%ghost %catrustdir/extracted/pem/objsign-ca-bundle.pem
%ghost %catrustdir/extracted/openssl/%openssl_format_trust_bundle

%exclude %pkidir/java
%exclude %catrustdir/extracted/java
%exclude %hooks_dir/30-extract-java.hook

%files java
%hooks_dir/30-extract-java.hook
%pkidir/java
%catrustdir/extracted/java
%ghost %catrustdir/extracted/%java_bundle

%changelog
* Thu Jun 27 2019 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- filetrigger: Add hooks directory to activation paths.

* Wed Jan 10 2018 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt2
- Package ca-bundle.crt symlink.

* Tue Jan 09 2018 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Package java/README file.
- Require p11-kit bundle instead of ca-certificates.
- Simplify update-ca-trust a bit.
- Fix README files.

* Thu Dec 28 2017 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build (closes: #25027).

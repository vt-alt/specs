%define _unpackaged_files_terminate_build 1

%define realname idna

Name: erlang-%realname
Version: 6.0.0
Release: alt1
Summary: Erlang IDNA lib
Group: Development/Erlang
License: MIT
Url: https://github.com/benoitc/erlang-idna

BuildArch: noarch

# https://github.com/benoitc/erlang-idna.git
Source: %name-%version.tar

%add_erlang_req_modules_skiplist str

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-unicode_util_compat

%description
A pure Erlang IDNA implementation that folllow the RFC5891.

- support IDNA 2008 and IDNA 2003.
- label validation:
  * check NFC: Label must be in Normalization Form C
  * check hyphen: The Unicode string MUST NOT contain "--" (two consecutive hyphens)
    in the third and fourth character positions and MUST NOT start or end with a "-" (hyphen).
  * Leading Combining Marks: The Unicode string MUST NOT begin with a combining mark
    or combining character (see The Unicode Standard, Section 2.11 Unicode for an exact definition).
  * Contextual Rules: The Unicode string MUST NOT contain any characters whose validity
    is context-dependent, unless the validity is positively confirmed by a contextual rule.
    To check this, each code point identified as CONTEXTJ or CONTEXTO in the Tables document RFC5892
    MUST have a non-null rule. If such a code point is missing a rule, the label is invalid.
    If the rule exists but the result of applying the rule is negative or inconclusive,
    the proposed label is invalid.
  * check BIDI: label contains any characters from scripts that are written
    from right to left, it MUST meet the Bidi criteria rfc5893

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt1
- Initial build for ALT.

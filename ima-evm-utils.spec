
Summary: IMA/EVM support utilities
Name: ima-evm-utils
Version: 1.1
Release: 3%{?dist}
License: GPLv2
Url:  http://linux-ima.sourceforge.net/
Source: http://sourceforge.net/projects/linux-ima/files/ima-evm-utils/%{name}-%{version}.tar.gz
BuildRequires: autoconf automake libtool m4 asciidoc libxslt
BuildRequires: openssl-devel libattr-devel keyutils-libs-devel
Patch1: docbook-xsl-path.patch
Patch2: libimaevm-keydesc-import.patch

%description
The Trusted Computing Group(TCG) run-time Integrity Measurement Architecture
(IMA) maintains a list of hash values of executables and other sensitive
system files, as they are read or executed. These are stored in the file
systems extended attributes. The Extended Verification Module (EVM) prevents
unauthorized changes to these extended attributes on the file system.
ima-evm-utils is used to prepare the file system for these extended attributes.

%package devel
Summary: Development files for %{name}
Requires: ima-evm-utils = %{version}-%{release}

%description devel
This package provides the header files for %{name}

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
mkdir -p m4
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -type f -name "*.la" -print -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%{_docdir}/%{name}/*.sh
%{_includedir}/*
%{_libdir}/libimaevm.so

%files
%doc ChangeLog README AUTHORS
%license COPYING
%{_bindir}/*
%{_libdir}/libimaevm.so.*
%{_mandir}/man1/*

%changelog
* Fri Mar 01 2019 Bruno E. O. Meneguele <bmeneg@redhat.com> - 1.1-3
- Add patch to correctly handle key description on keyring during importation

* Mon Feb 26 2018 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.1-2
- Add Requires for -devel subpackage

* Mon Feb 26 2018 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.1-1
- New upstream release
- Adjusted docbook xsl path to match the correct stylesheet
- Remove only *.la files, considering there aren't any *.a files

* Tue Sep 05 2017 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.0-1
- New upstream release
- Remove libtool files
- Run ldconfig after un/installation to update *.so files
- Add -devel subpackage to handle include files and examples

* Thu May 11 2017 Laura Abbott <labbott@redhat.com> - 0.9-6
- Use explicit version of _pkgdocdir for non-versioning

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.9-3
- Fix FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 31 2014 Avesh Agarwal <avagarwa@redhat.com> - 0.9-1
- New upstream release
- Applied a patch to fix man page issues.
- Updated spec file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 Vivek Goyal <vgoyal@redhat.com> - 0.6-1
- Initial package

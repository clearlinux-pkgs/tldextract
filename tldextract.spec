#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tldextract
Version  : 2.2.3
Release  : 8
URL      : https://files.pythonhosted.org/packages/45/90/827138ee22b7635e8c71373530e5fabccd89ec636ba6ecedd442b3ecbf5a/tldextract-2.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/90/827138ee22b7635e8c71373530e5fabccd89ec636ba6ecedd442b3ecbf5a/tldextract-2.2.3.tar.gz
Summary  : Accurately separate the TLD from the registered domain and subdomains of a URL, using the Public Suffix List. By default, this includes the public ICANN TLDs and their exceptions. You can optionally support the Public Suffix List's private domains as well.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: tldextract-bin = %{version}-%{release}
Requires: tldextract-license = %{version}-%{release}
Requires: tldextract-python = %{version}-%{release}
Requires: tldextract-python3 = %{version}-%{release}
Requires: idna
Requires: requests
Requires: requests-file
BuildRequires : buildreq-distutils3
BuildRequires : idna
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : requests
BuildRequires : requests-file
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
top-level domain) from the registered domain and subdomains of a URL.
        
            >>> import tldextract

%package bin
Summary: bin components for the tldextract package.
Group: Binaries
Requires: tldextract-license = %{version}-%{release}

%description bin
bin components for the tldextract package.


%package license
Summary: license components for the tldextract package.
Group: Default

%description license
license components for the tldextract package.


%package python
Summary: python components for the tldextract package.
Group: Default
Requires: tldextract-python3 = %{version}-%{release}

%description python
python components for the tldextract package.


%package python3
Summary: python3 components for the tldextract package.
Group: Default
Requires: python3-core
Provides: pypi(tldextract)
Requires: pypi(idna)
Requires: pypi(requests)
Requires: pypi(requests_file)

%description python3
python3 components for the tldextract package.


%prep
%setup -q -n tldextract-2.2.3
cd %{_builddir}/tldextract-2.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597083118
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tldextract
cp %{_builddir}/tldextract-2.2.3/LICENSE %{buildroot}/usr/share/package-licenses/tldextract/b8641358e21254308b9a6258fc93eed20c9f7960
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tldextract

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tldextract/b8641358e21254308b9a6258fc93eed20c9f7960

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

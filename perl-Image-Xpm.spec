#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Image-Xpm
Version  : 1.13
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Image-Xpm-1.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Image-Xpm-1.13.tar.gz
Summary  : 'Load, create, manipulate and save xpm image files.'
Group    : Development/Tools
License  : LGPL-2.0
Requires: perl-Image-Xpm-perl = %{version}-%{release}
Requires: perl(Image::Base)
BuildRequires : buildreq-cpan
BuildRequires : perl(Image::Base)

%description
Image::Xpm
==========
Image::Xpm is a Perl module for loading, creating, manipulating and
saving xpm image files.

%package dev
Summary: dev components for the perl-Image-Xpm package.
Group: Development
Provides: perl-Image-Xpm-devel = %{version}-%{release}
Requires: perl-Image-Xpm = %{version}-%{release}

%description dev
dev components for the perl-Image-Xpm package.


%package perl
Summary: perl components for the perl-Image-Xpm package.
Group: Default
Requires: perl-Image-Xpm = %{version}-%{release}

%description perl
perl components for the perl-Image-Xpm package.


%prep
%setup -q -n Image-Xpm-1.13
cd %{_builddir}/Image-Xpm-1.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Image::Xpm.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

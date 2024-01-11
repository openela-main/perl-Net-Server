Name:           perl-Net-Server
Version:        2.009
Release:        3%{?dist}
Summary:        Extensible, general Perl server engine
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-Server/
Source0:        http://www.cpan.org/modules/by-module/Net/Net-Server-%{version}.tar.gz
# Adapt tests to security level 2 system-wide crypt policy, bug #1611737,
# CPAN RT#126923
Patch0:         Net-Server-2.009-Generate-2048-bit-keys-for-tests.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# BuildRequires:  perl(CGI)
# BuildRequires:  perl(CGI::Compile)
# BuildRequires:  perl(CGI::PSGI)
# BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
# BuildRequires:  perl(HTTP::Parser::XS)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Multiplex) >= 1.05
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
# BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(IO::Socket::SSL) >= 1.31
BuildRequires:  perl(IO::Socket::UNIX)
# BuildRequires:  perl(IPC::Open3)
# BuildRequires:  perl(IPC::Semaphore)
# BuildRequires:  perl(IPC::SysV)
# BuildRequires:  perl(Log::Log4perl)
# BuildRequires:  perl(Net::CIDR)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6)
# BuildRequires:  perl(Symbol)
# BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Time::HiRes)
# BuildRequires:  perl(Unix::Syslog)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(threads)
BuildRequires:  perl(Test::More)
 
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# IO::Multiplex support is optional, but not including it causes build problems in some packages...
Requires:       perl(IO::Multiplex) >= 1.05
#  RHBZ#1395714: Optional dependency, including it so that the build matches runtime
Requires:       perl(IO::Socket::INET6)

%description
An extensible, class oriented module written in perl and intended to
be the back end layer of internet protocol servers.

%prep
%setup -q -n Net-Server-%{version}
%patch0 -p1

# Do not want to pull in any packaging deps here.
chmod -c 644 examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%license LICENSE
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/net-server
%{_mandir}/man1/net-server.1*

%changelog
* Wed Aug 22 2018 Petr Pisar <ppisar@redhat.com> - 2.009-3
- Enable tests (bug #1611737)
- Adapt tests to security level 2 system-wide crypt policy (bug #1611737)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.009-1
- 2.009 bump
- Modernize spec file

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.008-9
- Perl 5.26 rebuild

* Wed May 24 2017 Petr Pisar <ppisar@redhat.com> - 2.008-8
- Restore compatibility with Perl 5.26.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 "D. Johnson" <fenris02@fedoraproject.org> - 2.008-6
- Bug 1395714 - perl-Net-Server should depend on perl-IO-Socket-INET6

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.008-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.008-2
- Perl 5.22 rebuild

* Wed May 27 2015 Kevin Fenzi <kevin@scrye.com> 2.008-1
- Update to 2.008. Fixes bug #1225064

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.007-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2.007-2
- Perl 5.18 rebuild

* Wed Jul 24 2013 Paul Howarth <paul@city-fan.org> - 2.007-1
- Update to 2.007
- BR: perl(Test::More) and perl(Time::HiRes)
- Add various other buildreqs for additional test coverage
- Don't use macros for commands
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.006-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Kevin Fenzi <kevin@scrye.com> 2.006-1
- Update to 2.006 upstream release
- Redo spec with current guidelines. 

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.97-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.97-12
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.97-10
- Rebuild to fix problems with vendorarch/lib (#661697)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.97-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.97-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 11 2008 <nicolas.mailhot at laposte.net>
- 0.97-5
⌖ Fedora 10 alpha general package cleanup

* Mon Jun 02 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.97-3
⋰ remove old %%check Dag leftover rpmbuild does not like anymore

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com>
- 0.97-2
Rebuild for new perl

* Sun Aug 12 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
⍟ 0.97-1

* Fri May 18 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
⍟ 0.96-2
- more build checks
⍟ 0.96-1
- trim changelog

* Tue Mar 20 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.95-1 

* Sat Sep 02 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.94-2
- FE6 Rebuild

* Sun Jul 30 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.94-1

* Sun Apr 23 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.93-1

* Mon Feb 13 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.90-2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Jan 8 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.90-1
- Updated to 0.90
- add IO::Multiplex dep

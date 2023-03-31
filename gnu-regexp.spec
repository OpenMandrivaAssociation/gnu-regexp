# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           gnu-regexp
Version:        1.1.4
Release:        19.5
Summary:        Java NFA regular expression engine implementation
Group:		Development/Java
# GPLv2+: gnu/regexp/util/Egrep.java
#         gnu/regexp/util/Grep.java
#         gnu/regexp/util/REApplet.java
# Public Domain: gnu/regexp/util/RETest.java
#                gnu/regexp/util/Tests.java
# Rest is LGPLv2+
# Note files under GPLv2+ and Public Domain are included in -demo subpackage
License:        LGPLv2+
Source0:        http://ftp.frugalware.org/pub/other/sources/gnu.regexp/gnu.regexp-1.1.4.tar.gz
Source1:        %{name}.build.xml
BuildRequires:  ant
BuildRequires:  gnu-getopt
URL:            http://savannah.gnu.org/projects/gnu-regexp
BuildArch:      noarch
Provides:       gnu.regexp = %{version}-%{release}
Obsoletes:      gnu.regexp < %{version}-%{release}

%description
The gnu.regexp package is a pure-Java implementation of a traditional
(non-POSIX) NFA regular expression engine. Its syntax can emulate many
popular development tools, including awk, sed, emacs, perl and grep. For
a relatively complete list of supported and non-supported syntax, refer
to the syntax and usage notes.

%package demo
Summary:        Demo for %{name}
License:        LGPLv2+ and GPLv2+ and Public Domain
Requires:       %{name} = %{version}-%{release}
Requires:       gnu-getopt
Provides:       gnu.regexp-demo = %{version}-%{release}
Obsoletes:      gnu.regexp-demo < %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
License:        LGPLv2+ and GPLv2+ and Public Domain
Provides:       gnu.regexp-javadoc = %{version}-%{release}
Obsoletes:      gnu.regexp-javadoc < %{version}-%{release}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n gnu.regexp-%{version}
cp %{SOURCE1} build.xml

%build
export CLASSPATH=$(build-classpath gnu-getopt)
ant jar javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 build/lib/gnu.regexp.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/gnu.regexp.jar

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}/gnu/regexp/util
install -p -m 644 build/classes/gnu/regexp/util/*.class \
  %{buildroot}%{_datadir}/%{name}/gnu/regexp/util

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc COPYING COPYING.LIB README TODO docs/*.html
%{_javadir}/*

%files demo
%{_datadir}/%{name}

%files javadoc
%doc COPYING COPYING.LIB
%doc %{_javadocdir}/%{name}

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Michal Srb <msrb@redhat.com> - 1.1.4-18
- Fix license tag
- Fix URLs
- Adapt to current guidelines
- Install license files with javadoc subpackage
- Drop version from JAR name
- Drop group tag
- Fix R

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.4-11
- drop repotag
- fix license tag

* Wed Oct 17 2007 Deepak Bhole <dbhole@redhat.com> 1.1.4-10jpp.3
- Resolve bz# 245270: Fixed URL

* Sun Jun 03 2007 Florian La Roche <laroche@redhat.com> - 1.1.4-10jpp.2
- remove Distribution: tag from .spec file

* Mon Feb 12 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.4-10jpp.1
- Update per Fedora review process
- Resolves rhbz#227057

* Thu May 04 2006 Ralph Apel <r.apel at r-apel.de> 0:1.1.4-10jpp
- First JPP-1.7 release
- Change name to gnu-regexp, Provide/Obsolete gnu.regexp
- Still provide gnu.regexp.jar as symlink

* Wed Feb 16 2005 Ralph Apel <r.apel at r-apel.de> 0:1.1.4-9jpp
- Build with javac 1.4.2

* Sun Feb 06 2005 David Walluck <david@jpackage.org> 0:1.1.4-8jpp
- add non-versioned javadoc link
- modernize spec

* Mon Aug 23 2004 Ralph Apel <r.apel at r-apel.de> 0:1.1.4-7jpp
- Build with ant-1.6.2

* Sun Sep 28 2003 David Walluck <david@anti-microsoft.org> 0:1.1.4-6jpp
- add Distribution and Vendor tags

* Thu Mar 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.1.4-5jpp
- Adapted for JPackage 1.5.

* Sat Feb 01 2003 David Walluck <david@anti-microsoft.org> 1.1.4-4jpp
- remove vendor tag

* Sat Feb 01 2003 David Walluck <david@anti-microsoft.org> 1.1.4-3jpp
- move gnu.regexp.util classes to demo package in order to remove the
  gnu.getopt dependency from the main package
- remove bzip2 compression on build script

* Sat Jan 19 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.1.4-2jpp
- versioned dir for javadoc
- no dependencies for javadoc package
- additional sources in individual archives
- section macro

* Sat Dec 8 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.1.4-1jpp
- first JPackage release


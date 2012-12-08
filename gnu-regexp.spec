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

%define gcj_support 0
%define section free

Name:           gnu-regexp
Version:        1.1.4
# 10jpp, but need 17 to obsolete old mdv package
Release:        %mkrel 17.0.6
Epoch:          0
Summary:        Java NFA regular expression engine implementation
License:        LGPL
Source0:        ftp://ftp.tralfamadore.com/pub/java/gnu.regexp-1.1.4.tar.gz
Source1:        %{name}.build.xml
BuildRequires:  ant
BuildRequires:  gnu-getopt
BuildRequires:  java-rpmbuild >= 0:1.6
URL:            http://www.cacas.org/java/gnu/regexp/
Group:          Development/Java
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:        gnu.regexp = %{epoch}:%{version}-%{release}
Obsoletes:        gnu.regexp < %{epoch}:%{version}-%{release}

%description
The gnu.regexp package is a pure-Java implementation of a traditional
(non-POSIX) NFA regular expression engine. Its syntax can emulate many
popular development tools, including awk, sed, emacs, perl and grep. For
a relatively complete list of supported and non-supported syntax, refer
to the syntax and usage notes.

%package demo
Summary:        Demo for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       gnu.getopt
Group:          Development/Java
Provides:        gnu.regexp-demo = %{epoch}:%{version}-%{release}
Obsoletes:        gnu.regexp-demo < %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Provides:        gnu.regexp-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:        gnu.regexp-javadoc < %{epoch}:%{version}-%{release}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n gnu.regexp-%{version}
%__cp -a %{SOURCE1} build.xml
%remove_java_binaries

%build
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath gnu.getopt)
%{ant} jar javadoc

%install
%__rm -rf %{buildroot}

# jars
%__mkdir_p %{buildroot}%{_javadir}
%__cp -a build/lib/gnu.regexp.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %__ln_s ${jar} `echo $jar| sed "s|-%{version}||g"`; done
%__ln_s %{name}.jar gnu.regexp.jar)

# demo
%__mkdir_p %{buildroot}%{_datadir}/%{name}/gnu/regexp/util
%__cp -a build/classes/gnu/regexp/util/*.class \
  %{buildroot}%{_datadir}/%{name}/gnu/regexp/util

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -a build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && %__ln_s %{name}-%{version} %{name})

%{gcj_compile}

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING COPYING.LIB README TODO docs/*.html
%{_javadir}/*
%{gcj_files}

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%files javadoc
%defattr(0644,root,root,0755)
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%dir %{_javadocdir}/%{name}



%changelog
* Fri Apr 15 2011 Antoine Ginies <aginies@mandriva.com> 0:1.1.4-17.0.4mdv2011.0
+ Revision: 653148
- bump the release

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0:1.1.4-17.0.3mdv2010.1
+ Revision: 502285
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0:1.1.4-17.0.2mdv2010.0
+ Revision: 429283
- rebuild

* Wed Jun 18 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:1.1.4-17.0.1mdv2009.0
+ Revision: 224986
- bump release to obsolete gnu.regexp, disable gcj_compile

* Sat Dec 29 2007 David Walluck <walluck@mandriva.org> 0:1.1.4-15.0.1mdv2008.1
+ Revision: 139082
- update release

* Sat Dec 29 2007 David Walluck <walluck@mandriva.org> 0:1.1.4-10.0.1mdv2008.1
+ Revision: 139010
- import gnu-regexp


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

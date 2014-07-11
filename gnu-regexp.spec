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

Summary:	Java NFA regular expression engine implementation
Name:		gnu-regexp
Epoch:	0
Version:	1.1.4
# 10jpp, but need 17 to obsolete old mdv package
Release:	17.0.13
License:	LGPL
Group:		Development/Java
Url:		http://www.cacas.org/java/gnu/regexp/
Source0:	ftp://ftp.tralfamadore.com/pub/java/gnu.regexp-1.1.4.tar.gz
Source1:	%{name}.build.xml
BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	gnu-getopt
BuildRequires:	java-rpmbuild >= 0:1.6
%if %{gcj_support}
BuildRequires:	java-gcj-compat-devel
%else
%endif
Provides:	gnu.regexp = %{epoch}:%{version}-%{release}

%description
The gnu.regexp package is a pure-Java implementation of a traditional
(non-POSIX) NFA regular expression engine. Its syntax can emulate many
popular development tools, including awk, sed, emacs, perl and grep. For
a relatively complete list of supported and non-supported syntax, refer
to the syntax and usage notes.

%package demo
Summary:	Demo for %{name}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnu.getopt
Group:		Development/Java
Provides:	gnu.regexp-demo = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Provides:	gnu.regexp-javadoc = %{epoch}:%{version}-%{release}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n gnu.regexp-%{version}
cp -a %{SOURCE1} build.xml
%remove_java_binaries

%build
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath gnu.getopt)
%{ant} jar javadoc

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -a build/lib/gnu.regexp.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed "s|-%{version}||g"`; done
ln -s %{name}.jar gnu.regexp.jar)

# demo
mkdir -p %{buildroot}%{_datadir}/%{name}/gnu/regexp/util
cp -a build/classes/gnu/regexp/util/*.class \
  %{buildroot}%{_datadir}/%{name}/gnu/regexp/util

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -a build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -s %{name}-%{version} %{name})

%{gcj_compile}

%files
%doc COPYING COPYING.LIB README TODO docs/*.html
%{_javadir}/*
%{gcj_files}

%files demo
%{_datadir}/%{name}

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%dir %{_javadocdir}/%{name}


%define format	sgml-hu
%define format2	SGML/hu

%define version 2006
%define release %mkrel 5

Summary:	HOWTO documents (sgml format) from the Linux Documentation Project
Name:		howto-%{format}
Version: 	%version
Release: 	%release
Group:		Books/Howtos
Source0:	howto-%{format}.tar.bz2
Url:		http://www.kde.hu/mlp/hogyanok/
License:	GPL
BuildRoot:	%{_tmppath}/howto-%{format}-root
BuildArchitectures: noarch
Requires:   locales-hu howto-utils
BuildRequires:  howto-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

Install the howto package if you'd like to be able to access the Linux
HOWTO documentation from your own system.

%prep 
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
cd $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
bzcat %{SOURCE0} | tar xv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}



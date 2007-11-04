%define name	libopensync-plugin-irmc
%define version	0.34
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	IRMC plugin for opensync synchronization tool
License:	GPLv2+
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libopensync-plugin-irmc-0.34-find-libxml2.patch
BuildRequires:	opensync-devel >= %{version}
BuildRequires:	openobex-devel
BuildRequires:	cmake
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
Sony Ericsson phones.

%prep
%setup -q
%patch0 -p0

%build
%cmake
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*

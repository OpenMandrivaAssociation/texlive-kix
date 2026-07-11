%global tl_name kix
%global tl_revision 21606

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset KIX codes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kix
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kix.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Implements KIX codes as used by the Dutch PTT for bulk mail addressing.
(Royal Mail 4 State Code.) KIX is a registered trade mark of PTT Post
Holdings B. V.


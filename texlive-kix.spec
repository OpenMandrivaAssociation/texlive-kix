Name:		texlive-kix
Version:	20180303
Release:	1
Summary:	Typeset KIX codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kix
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kix.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Implements KIX codes as used by the Dutch PTT for bulk mail
addressing. (Royal Mail 4 State Code.) KIX is a registered
trade mark of PTT Post Holdings B. V.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kix
%doc %{_texmfdistdir}/doc/latex/kix

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

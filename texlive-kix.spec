# revision 21606
# category Package
# catalog-ctan /macros/latex/contrib/kix
# catalog-date 2011-03-04 11:12:16 +0100
# catalog-license lppl1
# catalog-version undef
Name:		texlive-kix
Version:	20110304
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Implements KIX codes as used by the Dutch PTT for bulk mail
addressing. (Royal Mail 4 State Code.) KIX is a registered
trade mark of PTT Post Holdings B. V.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kix/kix.sty
%doc %{_texmfdistdir}/doc/latex/kix/kix.pdf
%doc %{_texmfdistdir}/doc/latex/kix/kix.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

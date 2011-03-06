""" General settings
set nocompatible    " Use vim defaults not vi defaults
set smartindent     " Auto indentation
set nohidden        " Close buffers when file is closed
set ignorecase      " ignore case for search
set ts=4            " Width of a tab (tab stop)
set sw=4            " Width for >> and << commands
set sts=4           " Tabs spacing (soft tab stop)
set tw=79           " Max line width
set smarttab        " Alignment for tab in front of line
set expandtab       " Convert tabs to Spaces
syntax on           " Syntax highlighting
set go+=a           " support for systemp clipboard
filetype on 
filetype plugin on

""" Key mappings
 " Tab for next tab
nnoremap <Tab> :tabn<CR>        
 " Shift+Tab for previous tab
nnoremap <S-Tab> :tabp<CR> 


""" UI Options
set guioptions-=T               " Remove toolbar for gvim

set guifont=Courier\ New\ 9 "   " Set font

if has("gui_running")
    set lines=50 columns=80     " gvim size
endif


""" C/C++ 
 " Doxygen style comments
"autocmd Filetype c,cpp lollerz
au Filetype c,cpp set comments-=://
au Filetype c,cpp set comments+=:///
au Filetype c,cpp set comments+=://

""" Python 
 " auto complete
let g:pydiction_location = '/home/hrishi/.vim/pydict/complete-dict'


""" Json view
autocmd BufRead *.json set filetype=json
au! Syntax json source ~/.vim/json.vim

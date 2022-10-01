""" Options
set background=dark
set clipboard=unnamedplus
set completeopt=noinsert,menuone,noselect
set cursorline
set hidden
set inccommand=split
set mouse=a
set number
set relativenumber
set splitbelow splitright
set title
set ttimeoutlen=0
set wildmenu

let mapleader = " "

""" Tabs size
set expandtab
set shiftwidth=2
set tabstop=2

filetype plugin indent on
syntax on

" set t_Co=256
""" True color if available
let term_program=$TERM_PROGRAM

""" Check for conflicts with Apple Terminal app
if term_program !=? 'Apple_Terminal'
"     set termguicolors
else
    if $TERM !=? 'xterm-256color'
"        set termguicolors
    endif
endif

""" Italics
let &t_ZH="\e[3m"
let &t_ZR="\e[23m"

""" File browser
let g:netrw_banner=0
let g:netrw_liststyle=0
let g:netrw_browse_split=4
let g:netrw_altv=1
let g:netrw_winsize=25
let g:netrw_keepdir=0
let g:netrw_localcopydircmd='cp -r'

""" Normal mode remappings
nnoremap <C-q> :q!<CR>
nnoremap <F4> :bd<CR>
nnoremap <F5> :NERDTreeToggle<CR>
nnoremap <F6> :sp<CR>:terminal<CR>

""" Tabs
nnoremap <S-Tab> gT
nnoremap <Tab> t
nnoremap <silent> <S-t> :tabnew<CR>

call plug#begin('~/.vim/plugged')
"   Plug 'dense-analysis/ale'
    " Plug 'preservim/nerdtree'
    Plug 'arcticicestudio/nord-vim'
    Plug 'easymotion/vim-easymotion'
"   Plug 'vim-airline/vim-airline'
"   Plug 'vim-airline/vim-airline-themes'
    Plug 'tpope/vim-commentary'
    " Plug 'ap/vim-css-color'
    Plug 'tpope/vim-surround'
    Plug 'wellle/targets.vim'
call plug#end()

""" Airline
let g:airline#extensions#searchcount#enabled = 0
let g:airline_extensions = []
let g:airline_theme='deus'
let g:airline_powerline_fonts = 1

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

""" unicode symbols
let g:airline_left_sep = '»'
let g:airline_left_sep = '▶'
let g:airline_right_sep = '«'
let g:airline_right_sep = '◀'
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'
""" airline symbols
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ''

""" easymotion
let g:EasyMotion_do_mapping = 0 " Disable default mappings
let g:EasyMotion_smartcase = 1 " Turn on case-insensitive feature

""" map key
nmap s <Plug>(easymotion-overwin-f2)
map  / <Plug>(easymotion-sn)
omap / <Plug>(easymotion-tn)
map  n <Plug>(easymotion-next)
map  N <Plug>(easymotion-prev)
map <Leader>j <Plug>(easymotion-j)
map <Leader>k <Plug>(easymotion-k)
map H ^
map L $

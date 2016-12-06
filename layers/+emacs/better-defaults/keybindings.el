;;; keybindings.el --- Better Emacs Defaults Layer key bindings File
;;
;; Copyright (c) 2012-2016 Sylvain Benner & Contributors
;;
;; Author: Sylvain Benner <sylvain.benner@gmail.com>
;; URL: https://github.com/syl20bnr/spacemacs
;;
;; This file is not part of GNU Emacs.
;;
;;; License: GPLv3

;; emacs state bindings
(define-key evil-emacs-state-map (kbd "C-o") 'evil-execute-in-normal-state)
(add-hook 'dired-mode-hook (lambda ()
                             (local-set-key (kbd "M-o") 'dired-display-file)))
(evil-leader/set-key
  "mj" 'org-clock-jump-to-current-clock
  ;; *s*ymbol
  "ms" 'prelude-goto-symbol
  )
(global-set-key (kbd "C-w") 'spacemacs/backward-kill-word-or-region)
(global-set-key [remap fill-paragraph] #'spacemacs/fill-or-unfill)

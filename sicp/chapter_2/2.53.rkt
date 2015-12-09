(define (display-list list)
  (display list)
  (newline))

; testing

(display-list (list 'a 'b 'c))            ;; (a b c)

(display-list (list (list 'george)))      ;; ((george))

(display-list (cdr '((x1 x2) (y1 y2))))   ;; ((y1 y2))

(display-list (cadr '((x1 x2) (y1 y2))))  ;; (y1 y2)

(display (pair? (car '(a short list))))   ;; false

(memq 'red '((red shoes) (blue socks)))   ;; false

(memq 'red '(red shoes blue socks))       ;; (red shoes blue socks)
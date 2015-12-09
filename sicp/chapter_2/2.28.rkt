(define (fringe tree)
  (define nil '())
  (define (iter items result)
    (cond ((null? items) result)
          ((not (pair? items))
           (cons items result))
          (else (iter (cdr items) (append result (iter (car items) nil))))))
  (iter tree nil))

; testing
(define (display-list items)
  (display items)
  (newline))

(define x (list (list 1 2) (list 3 4)))
(define y (list 1 2 (list 3 (list 4 5 6) 7 8) (list 9 10))) 

(display-list (fringe x))
(display-list (fringe y))
(display-list (fringe (list x x)))
(define (make-mobile left right)
  (list left right))

(define (make-branch length structure)
  (list length structure))

; a)
(define (left-branch mobile) (car mobile))
(define (right-branch mobile) (car (cdr mobile)))

; testing
(define mobile (make-mobile (make-branch 1 4) (make-branch 2 2)))
(display (left-branch mobile))
(newline)
(display (right-branch mobile))

; b)
(define (total-weight mobile)
  (define 
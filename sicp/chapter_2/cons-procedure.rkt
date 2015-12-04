(define (cons-def x y)
  (define (dispatch m)
    (cond ((= m 0) x)
          ((= m 1) y)
          (else (error "Argument not 0 or 1 -- CONS" m))))
  dispatch)

(define (car-def z) (z 0))
(define (cdr-def z) (z 1))

; testing
(define str-seq (cons-def "a" "b"))
(car-def str-seq)
(cdr-def str-seq)
(define (double func)
  (lambda (x) (func (func x))))

; testing
(define (inc x) (+ x 1))

((double inc) 5)                   ; 2
((double (double inc)) 5)          ; 2 * 2
((double (double (double inc))) 5) ; 2 * 2 * 2
(((double double) inc) 5)          ; 2 ^ 2
(((double (double double)) inc) 5) ; (2 ^ 2) ^ 2
(((double (double (double double))) inc) 5) ; ((2 ^ 2) ^ 2) ^ 2
(define (fast-mul a b)
  (define (double x) (+ x x))
  (define (halve x) (/ x 2))
  (cond ((< b 0) (- (fast-mul a (- b))))
        ((= b 0) 0)
        ((= b 1) a)
        ((even? b) (fast-mul (double a) (halve b)))
        (else (+ a (fast-mul a (- b 1))))))

; test
(fast-mul 2 10)
(fast-mul 2 -1)
(fast-mul 2 0)
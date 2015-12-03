(define (mul-i a b)
  (define (iter accumulator a b)
    (cond ((< b 0) (- (iter accumulator a (- b))))
          ((= b 0) accumulator)
          ((even? b) (iter accumulator (double a) (halve b)))
          (else (iter (+ accumulator a) a (- b 1)))))
  (define (double x) (+ x x))
  (define (halve b) (/ b 2))
  (iter 0 a b))

; testing
(mul-i 2 0)
(mul-i 2 4)
(mul-i 2 -5)
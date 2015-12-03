; iterative version
(define (fast-expt-i b n)
  (define (fast-expt-iter count product)
    (cond ((= count 0) product)
          ((even? count) (fast-expt-iter (/ count 2) (square product)))
          (else (fast-expt-iter (- count 1) (* b product)))))
  (define (square x) (* x x))
  (fast-expt-iter n 1))

; test
(fast-expt-i 9 0)
(fast-expt-i 3 9)
(fast-expt-i 111 999)
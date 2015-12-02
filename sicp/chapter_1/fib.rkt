; recursive version
(define (fib-r n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib-r (- n 1))
                 (fib-r (- n 2))))))

; iterative version
(define (fib-i n)
  (define (fib-iter a b count)
    (if (= count 0)
        b
        (fib-iter (+ a b) a (- count 1))))
  (fib-iter 1 0 n))

; test
(fib-r 0)
(fib-r 1)
(fib-r 2)
(fib-r 5)

(fib-i 0)
(fib-i 1)
(fib-i 2)
(fib-i 5)
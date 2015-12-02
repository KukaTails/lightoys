;; simple algorithm

; recursive version
(define (expt-r b n)
  (if (= n 0)
      1
      (* b (expt-r b (- n 1)))))

; iterative version
(define (expt-i b n)
  (define (expt-iter count product)
    (if (= count 0)
        product
        (expt-iter (- count 1) (* b product))))
  (expt-iter n 1))

; test
(expt-r 9 0)
(expt-r 3 9)
(expt-r 111 999)

(expt-i 9 0)
(expt-i 3 9)
(expt-r 111 999)


;; another algorithm

; recursive version
(define (fast-expt-r b n)
  (define (square x) (* x x))
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt-r b (/ n 2))))
        (else (* b (fast-expt-r b (- n 1))))))


; iterative version
(define (fast-expt-i b n)
  (define (fast-expt-iter count product)
    (cond ((= count 0) product)
          ((even? count) (fast-expt-iter (/ count 2) (square product)))
          (else (fast-expt-iter (- count 1) (* b product)))))
  (define (square x) (* x x))
  (fast-expt-iter n 1))

; test
(fast-expt-r 9 0)
(fast-expt-r 3 9)
(fast-expt-r 111 999)

(fast-expt-i 9 0)
(fast-expt-i 3 9)
(fast-expt-i 111 999)
; recursion version
(define (f-r n)
  (if (< n 3)
      n
      (+ (f-r (- n 1))
         (+ (* 2 (f-r (- n 2)))
            (* 3 (f-r (- n 3)))))))

; iterator version
(define (f-i n)
  (define (f-iter a b c count)
    (if (= count 0)
        a
        (f-iter b c (+ c (+ (* 2 b) (* 3 a))) (- count 1))))
  (f-iter 0 1 2 n))

; recursive test
(f-r 0)
(f-r 1)
(f-r 2)
(f-r 3)
(f-r 4)
(f-r 10)

; iterative test
(f-i 0)
(f-i 1)
(f-i 2)
(f-i 3)
(f-i 4)
(f-i 10)
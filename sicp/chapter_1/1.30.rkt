(define (sum term a next b)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (+ result (term a)))))
  (iter a 0))

; testing
(define (sum-integer a b)
  (define (inc n) (+ n 1))
  (sum identity a inc b))

(sum-integer 0 10)
(sum-integer 5 15)
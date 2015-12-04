; accumulate(recursive-version)
(define (accumulate-r combiner null-value term a next b)
  (if (> a b)
      null-value
      (combiner (term a) (accumulate-r combiner null-value term (next a) next b))))

; accumulate(iterative-version)
(define (accumulate-i combiner null-value term a next b)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (combiner result (term a)))))
  (iter a null-value))

; sum-accumulate
(define (sum-accumulate-r term a next b)
  (accumulate-r + 0 term a next b))

(define (sum-accumulate-i term a next b)
  (accumulate-i + 0 term a next b))

; product-accumulate
(define (product-accumulate-r term a next b)
  (accumulate-r * 1 term a next b))

(define (product-accumulate-i term a next b)
  (accumulate-r * 1 term a next b))

; testing for sum-integer
(define (sum-integer-r a b)
  (define (inc n) (+ n 1))
  (sum-accumulate-r identity a inc b))

(define (sum-integer-i a b)
  (define (inc n) (+ n 1))
  (sum-accumulate-i identity a inc b))

(sum-integer-r 1 10)
(sum-integer-r -10 10)

(sum-integer-i 1 10)
(sum-integer-i -10 10)

; testing for product-integer
(define (product-integer-r a b)
  (define (inc n) (+ n 1))
  (product-accumulate-r identity a inc b))

(define (product-integer-i a b)
  (define (inc n) (+ n 1))
  (product-accumulate-i identity a inc b))

(product-integer-r 1 10)
(product-integer-r -10 -1)

(product-integer-i 1 10)
(product-integer-i -10 -1)
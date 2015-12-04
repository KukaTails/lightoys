; product function(recursive version)
(define (product-r term a next b)
  (if (> a b)
      1
      (* (term a) (product-r term (next a) next b))))

; product function(iterative version)
(define (product-i term a next b)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (* result (term a)))))
  (iter a 1))

; factorial function
(define (factorial-r n)
  (define (inc n) (+ n 1))
  (product-r identity 1 inc n))

(define (factorial-i n)
  (define (inc n) (+ n 1))
  (product-i identity 1 inc n))

; pi-product
(define (pi-product-r n)
  (define (pi-term n)
    (if (even? n)
        (/ (+ n 2) (+ n 1))
        (/ (+ n 1) (+ n 2))))
  (define (inc n) (+ n 1))
  (* 4 (product-r pi-term 1 inc n)))

(define (pi-product-i n)
  (define (pi-term n)
    (if (even? n)
        (/ (+ n 2) (+ n 1))
        (/ (+ n 1) (+ n 2))))
  (define (inc n) (+ n 1))
  (* 4 (product-i pi-term 1 inc n)))

; testing
(define (product-integer-r a b)
  (define (inc n) (+ n 1))
  (product-r identity a inc b))

(define (product-integer-i a b)
  (define (inc n) (+ n 1))
  (product-i identity a inc b))

(product-integer-r 1 10)
(product-integer-r -9 -1)
(product-integer-r -100 10)

(product-integer-i 1 10)
(product-integer-i -9 -1)
(product-integer-i -100 10)

(factorial-r 10)
(factorial-r 5)

(factorial-i 10)
(factorial-i 5)

(pi-product-r 100)
(pi-product-i 100)
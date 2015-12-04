; general function
(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))

;; sum-cubes
(define (inc n) (+ n 1))

(define (sum-cubes a b)
  (define (cube x) (* x (* x x)))
  (sum cube a inc b))

; testing for sum-cubes
(sum-cubes 1 100)
(sum-cubes 10 10)
(sum-cubes 10 9)

;; sum-integers
(define (sum-integers a b)
  (sum identity a inc b))

; testing for sum-integers
(sum-integers 0 10)
(sum-integers 1 1)
(sum-integers 1 0)

;; pi-sum
(define (pi-sum a b)
  (define (pi-term x)
    (/ 1.0 (* x (+ x 2))))
  (define (pi-next x)
    (+ x 4))
  (sum pi-term a pi-next b))

; testing for pi-sum
(* 8 (pi-sum 1 1000))
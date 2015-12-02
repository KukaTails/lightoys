(define (cube-root-iter guess old-guess x)
  (if (good-enough? guess old-guess x)
      guess
      (cube-root-iter (improve guess x) guess x)))

(define (func-x x y)
  (/ (+ (/ x (* y y))
        (* 2 y))
     3))

(define (good-enough? guess old-guess x)
  (> 0.00001 (/ (abs (- guess old-guess))
             x)))

(define (improve guess x)
  (func-x x guess))

(define (cube-root x)
  (cube-root-iter (improve 1.0 x) 1.0 x))

; test
(require racket/trace)
(trace cube-root)
(cube-root 27.0)
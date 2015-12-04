(define (fixed-point f first-guess)
  (define tolerance 0.00001)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) tolerance))
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next)
          next
          (try next))))
  (try first-guess))

; sqrt algorithm
(define (average-damp f)
  (define (average x y) (/ (+ x y) 2))
  (lambda (x) (average x (f x))))

(define (sqrt-def x)
  (fixed-point (average-damp (lambda (y) (/ x y)))
               1.0))

(define (cube-root x)
  (define (square x) (* x x))
  (fixed-point (average-damp (lambda (y) (/ x (square y))))
               1.0))

; testing
(sqrt-def 2.0)

(cube-root 8.0)
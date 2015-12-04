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

; testing
(fixed-point cos 1.0)

(fixed-point (lambda (y) (+ (sin y) (cos y)))
           1.0)

; sqrt algorithm
(define (sqrt-def x)
  (define (average x y) (/ (+ x y) 2))
  (fixed-point (lambda (y) (average y (/ x y)))
           1.0))

(sqrt-def 2.0)

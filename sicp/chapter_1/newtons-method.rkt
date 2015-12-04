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

(define (deriv g)
  (define dx 0.00001)
  (lambda (x)
    (/ (- (g (+ x dx)) (g x))
       dx)))

(define (newtons-transform g)
  (lambda (x)
    (- x (/ (g x) ((deriv g) x)))))

(define (newtons-method g guess)
  (fixed-point (newtons-transform g) guess))

(define (sqrt-def x)
  (define (square x) (* x x))
  (newtons-method (lambda (y) (- (square y) x))
                  1.0))

; testing

(sqrt-def 4.0)
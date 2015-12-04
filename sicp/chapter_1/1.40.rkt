(define (newtons-method g guess)
  (define (deriv g)
    (define dx 0.00001)
    (lambda (x)
      (/ (- (g (+ x dx)) (g x))
         dx)))
  
  (define (newtons-transform g)
    (lambda (x)
      (- x (/ (g x) ((deriv g) x)))))
  
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
  
  (fixed-point (newtons-transform g) guess))

(define (cubic a b c)
  (define (square x) (* x x))
  (define (cube x) (* x x x))
  (lambda (x)
    (+ (cube x) (* a (square x)) (* b x) c)))

; testing
(newtons-method (cubic 1 1 1) 1)
(newtons-method (cubic 1 5 2) 1)
(newtons-method (cubic 0 0 8) 0)
(define (make-rat n d)
  (let ((g (gcd n d)))
    (let ((x (/ n g))
          (y (/ d g)))
      (if (< (* x y) 0)
          (cons (- (abs x)) (abs y))
          (cons (abs x) (abs y))))))

(define (numer x) (car x))

(define (denom x) (cdr x))

(define (add-rat x y)
  (make-rat (+ (* (numer x) (denom x))
               (* (numer y) (denom y)))
            (* (denom x) (denom y))))

(define (sub-rat x y)
  (make-rat (- (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))

(define (mul-rat x y)
  (make-rat (* (numer x) (numer y))
            (* (denom x) (denom y))))

(define (div-rat x y)
  (make-rat (* (numer x) (denom y))
            (* (denom x) (numer y))))

(define (equal-rat? x y)
  (= (* (numer x) (denom x))
     (* (numer y) (denom y))))

(define (print-rat x)
  (newline)
  (display (numer x))
  (display "/")
  (display (denom x)))

; testing
(print-rat (make-rat 4 2))
(print-rat (make-rat -4 -2))
(print-rat (make-rat 4 -2))
(print-rat (make-rat 3 -12))
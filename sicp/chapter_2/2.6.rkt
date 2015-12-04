;; the definition of one

;(add-1 zero)
;(lambda (f) (lambda (x) (f ((zero f) x))))
;(lambda (f) (lambda (x) (f ((lambda (f) (lambda (x) x)) f) x)))
;(lambda (f) (lambda (x) (f ((lambda (x) x) x))))
;(lambda (f) (lambda (x) (f x)))

;; the definition of two

;(add-1 one)
;(lambda (f) (lambda (x) (f ((one f) x))))
;(lambda (f) (lambda (x) (f ((lambda (f) (lambda (x) (f x))) f) x)))
;(lambda (f) (lambda (x) (f ((lambda (x) (f x)) x))))
;(lambda (f) (lambda (x) (f (f x))))

;; the definition of add operator
(define (+ m n)
  (lambda (f)
    (lambda (x) ((m f) ((n f) x)))))

; let n = 1, define add-1 from the definition of add operator
(define (add-1 m)
  (+ one n))

;(+ one n)
;(lambda (f) (lambda (x) ((one f) ((n f) x))))
;(lambda (f) (lambda (x) (((lambda (f) (lambda (x) (f x))) f) ((n f) x))))
;(lambda (f) (lambda (x) ((lambda (x) (f x)) ((n f) x))))
;(lambda (f) (lambda (x) ((f ((n f) x)))))
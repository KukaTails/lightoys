(define (compose-def f g)
  (lambda (x)
    (f (g x))))

; testing

(define (square x) (* x x))
(define (inc x) (+ x 1))
((compose-def square inc) 6)
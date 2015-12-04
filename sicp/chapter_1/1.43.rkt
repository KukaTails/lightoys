(define (compose-def f g)
  (lambda (x)
    (f (g x))))

(define (repeated func n)
  (if (= n 1)
      func
      (compose-def func (repeated func (- n 1)))))

; testing
(define (inc x) (+ x 1))
((repeated inc 10) 1)

(define (square x) (* x x))
((repeated square 10) 100)
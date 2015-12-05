(define (power a n)
  (cond ((= n 0) 1)
        ((even? n) (power (* a a) (/ n 2)))
        (else (* a (power a (- n 1))))))

(define (cons-def a b)
  (* (power 2 a)
     (power 3 b)))

(define (modulo-k n k)
  (if (= 0 (modulo n k))
      (+ 1 (modulo-k (/ n k) k))
      0))

(define (car-def seq)
  (modulo-k seq 2))

(define (cdr-def seq)
  (modulo-k seq 3))

; testing
(define test-seq (cons-def 2 5))
(car-def test-seq)
(cdr-def test-seq)

(define test-seq (cons-def 4 5))
(car-def test-seq)
(cdr-def test-seq)
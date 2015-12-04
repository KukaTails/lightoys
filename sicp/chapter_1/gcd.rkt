(define (gcd-def a b)
  (if (= b 0)
      a
      (gcd-def b (remainder a b))))

; testing
(gcd 206 40)
(gcd-def 206 40)